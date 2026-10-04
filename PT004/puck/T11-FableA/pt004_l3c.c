/*
 * TOGETHER - PROOF TABLE 004 - Round 3 - Turn 11 - item L3-C (prime gate p = 83)
 * Seat: Fable-A (testing seat).
 *
 * NEW code, written from the definitions in arXiv:2609.02604v2 (Allikvere),
 * Section 2 (Definition 2.1, c-lifts, the sets F_l(r)) and Section 4 (the cover
 * formulation of level one, binary lifting, the level-14 step).
 * The author's code was not read, run or copied.
 *
 * Definitions used (k speeds, prime p, level l; all arithmetic is exact integer):
 *
 *   Z_{p,l}  = residues mod p*l that are not divisible by p.
 *   A vector v in Z_{p,l}^k is (k,p,l)-PROPER if
 *     (a) for some i, gcd(l, v_1, .., v_i omitted, .., v_k) > 1, or
 *     (b) for some t = j/(l*p), j an integer, ||t*v_i|| >= 1/(k+1) for every i.
 *   It is IMPROPER otherwise; I(k,p,l) is the set of improper vectors.
 *   With d(x) = distance from x to the nearest multiple of l*p,
 *     ||j*v_i/(l*p)|| >= 1/(k+1)   <=>   (k+1) * d(j*v_i) >= l*p.
 *   Coordinate i "blocks" the time j when (k+1) * d(j*v_i) < l*p.
 *   So (b) fails exactly when every time j is blocked by some coordinate.
 *
 *   Level one.  Signs are folded: speed classes and time classes are 1..n, n=(p-1)/2.
 *   Class v covers time a when (k+1)*d_p(a*v) < p.  I(k,p,1) = the k-multisets of
 *   classes whose cover sets together contain every time class (gcd(1,..) = 1, so
 *   alternative (a) never applies at level one).
 *   Units u of Z_p act by v -> fold(u*v); a "unit orbit" is an orbit of this action
 *   on k-multisets.  MY NORMALISATION: the representative of an orbit is the
 *   lexicographically smallest sorted k-tuple of classes in the orbit.
 *
 *   Lifts.  For c >= 2 the c-lifts of w (level l) are w_i + a_i*l*p, a_i in 0..c-1,
 *   taken mod c*l*p.  F_l(r) = improper level-l vectors congruent to r mod p.
 *   F_{c*l}(r) = the improper c-lifts of the members of F_l(r).
 *
 * Modes:
 *   level1  P K OUT          enumerate all unit orbits of I(K,P,1), write them to OUT
 *   cascade P K ORBITS OUT   for every orbit: |F_2|,|F_4|,..,|F_32|; for an orbit that
 *                            is still alive at level 32, the level-(K+1) step from F_2
 *   tiny    P K c1,c2,..     totals of improper ordered vectors along a lift route
 *                            (used by the test driver against a brute-force oracle)
 *
 * Build:  cc -O2 -std=c11 -o pt004_l3c pt004_l3c.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef uint64_t u64;
typedef unsigned __int128 u128;

#define MAXK 16
#define MAXN 64
#define MAXC 16
#define MAXT 4096
#define MAXW (MAXT / 64)

static int P, K, N, M;
static u64 FULL1;                      /* all time classes (also: all speed classes) */
static u64 cover1[MAXN + 1];           /* cover1[v]: bit a-1 set if class v covers time a */
static u64 covby[MAXN + 1];            /* covby[a]:  bit v-1 set if class v covers time a */
static unsigned char mulf[MAXN + 1][MAXN + 1];   /* mulf[u][x] = fold(u*x) */
static unsigned char invf[MAXN + 1];             /* fold-inverse of a class */

static void die(const char *msg) { fprintf(stderr, "ERROR: %s\n", msg); exit(2); }
static inline int popc(u64 x) { return __builtin_popcountll(x); }
static inline int lowbit(u64 x) { return __builtin_ctzll(x); }

static int fold(long x)
{
    long r = x % P;
    if (r < 0) r += P;
    return (int)(r <= P - r ? r : P - r);
}

static void print_u128(u128 x)
{
    char buf[48]; int i = 47; buf[i] = 0;
    if (x == 0) buf[--i] = '0';
    while (x > 0) { buf[--i] = (char)('0' + (int)(x % 10)); x /= 10; }
    fputs(buf + i, stdout);
}

static void setup(int p, int k)
{
    if (p < 3 || p % 2 == 0) die("p must be an odd prime");
    for (int q = 3; q * q <= p; q += 2) if (p % q == 0) die("p must be prime");
    P = p; K = k; N = (p - 1) / 2;
    if (N > MAXN) die("p too large for this build (n = (p-1)/2 must be <= 64)");
    if (K < 1 || K > MAXK) die("k out of range");
    FULL1 = (N == 64) ? ~(u64)0 : (((u64)1 << N) - 1);
    memset(cover1, 0, sizeof cover1); memset(covby, 0, sizeof covby);
    for (int v = 1; v <= N; v++)
        for (int a = 1; a <= N; a++)
            if ((long)(K + 1) * fold((long)a * v) < P) {
                cover1[v] |= (u64)1 << (a - 1);
                covby[a] |= (u64)1 << (v - 1);
            }
    M = popc(cover1[1]);
    for (int u = 1; u <= N; u++)
        for (int x = 1; x <= N; x++) {
            mulf[u][x] = (unsigned char)fold((long)u * x);
            if (mulf[u][x] == 1) invf[u] = (unsigned char)x;
        }
}

/* ------------------------------------------------------------------------- */
/* Level one: all unit orbits of covering K-multisets                         */
/* ------------------------------------------------------------------------- */

typedef struct { unsigned char c[MAXK]; } Row;

static Row *rows = NULL; static size_t nrows = 0, caprows = 0;
static long long nodes1 = 0, sets_with1 = 0;
static long long sets_by_size[MAXK + 1], canon_by_size[MAXK + 1];
/* two extra counters, reported only (sets that contain class 1) */
static long long irr_K_with1 = 0;      /* irredundant covers on K distinct classes */
static long long cov_K1_with1 = 0;     /* covers on K-1 distinct classes */

static void push_row(const unsigned char *c)
{
    if (nrows == caprows) {
        caprows = caprows ? caprows * 2 : 1 << 16;
        rows = realloc(rows, caprows * sizeof(Row));
        if (!rows) die("out of memory");
    }
    memset(rows[nrows].c, 0, MAXK);
    memcpy(rows[nrows].c, c, (size_t)K);
    nrows++;
}

static void sort_small(unsigned char *t, int len)
{
    for (int i = 1; i < len; i++) {
        unsigned char x = t[i]; int j = i - 1;
        while (j >= 0 && t[j] > x) { t[j + 1] = t[j]; j--; }
        t[j + 1] = x;
    }
}

/* lexicographically smallest sorted tuple in the unit orbit of the multiset m.
   The minimum starts with class 1, so only the units inverse to a member matter. */
static void canon_multiset(const unsigned char *m, unsigned char *best)
{
    unsigned char t[MAXK];
    memcpy(best, m, (size_t)K);
    sort_small(best, K);
    for (int i = 0; i < K; i++) {
        if (i > 0 && m[i] == m[i - 1]) continue;
        int u = invf[m[i]];
        for (int j = 0; j < K; j++) t[j] = mulf[u][m[j]];
        sort_small(t, K);
        if (memcmp(t, best, (size_t)K) < 0) memcpy(best, t, (size_t)K);
    }
}

/* number of units u with u*m = m (as multisets); the orbit has N / this many members */
static int stabilizer_size(const unsigned char *m)
{
    unsigned char t[MAXK]; int s = 0;
    for (int u = 1; u <= N; u++) {
        for (int j = 0; j < K; j++) t[j] = mulf[u][m[j]];
        sort_small(t, K);
        if (memcmp(t, m, (size_t)K) == 0) s++;
    }
    return s;
}

static u64 image_set(u64 S, int u)
{
    u64 T = 0;
    while (S) { int x = lowbit(S) + 1; S &= S - 1; T |= (u64)1 << (mulf[u][x] - 1); }
    return T;
}

/* all ways to give the s classes of S multiplicities >= 1 with total K */
static void compositions(const int *cls, int s, int idx, int left, unsigned char *buf, int filled)
{
    if (idx == s - 1) {
        for (int j = 0; j < left; j++) buf[filled + j] = (unsigned char)cls[idx];
        unsigned char best[MAXK];
        canon_multiset(buf, best);
        push_row(best);
        return;
    }
    int remaining_classes = s - idx - 1;
    for (int mlt = 1; mlt <= left - remaining_classes; mlt++) {
        for (int j = 0; j < mlt; j++) buf[filled + j] = (unsigned char)cls[idx];
        compositions(cls, s, idx + 1, left - mlt, buf, filled + mlt);
    }
}

/* S is a covering set of distinct classes, contains class 1, |S| <= K */
static void process_set(u64 S)
{
    int s = popc(S);
    sets_with1++; sets_by_size[s]++;

    if (s == K - 1) cov_K1_with1++;
    if (s == K) {                          /* irredundant: every class covers some time alone */
        u64 once = 0, twice = 0, T = S;
        while (T) { int c = lowbit(T) + 1; T &= T - 1; twice |= once & cover1[c]; once |= cover1[c]; }
        u64 priv = once & ~twice;
        int irredundant = 1; T = S;
        while (T) { int c = lowbit(T) + 1; T &= T - 1; if (!(cover1[c] & priv)) irredundant = 0; }
        if (irredundant) irr_K_with1++;
    }

    /* keep S only if it is the lexicographic minimum of its unit orbit.  For two sets of
       equal size, the smaller one owns the smallest class of the symmetric difference. */
    u64 T = S & ~(u64)1;
    while (T) {
        int c = lowbit(T) + 1; T &= T - 1;
        u64 img = image_set(S, invf[c]);
        u64 d = img ^ S;
        if (d && (img & (d & (~d + 1)))) return;
    }
    canon_by_size[s]++;
    int cls[MAXK], n = 0; T = S;
    while (T) { cls[n++] = lowbit(T) + 1; T &= T - 1; }
    unsigned char buf[MAXK];
    compositions(cls, s, 0, K, buf, 0);
}

/* add any further classes (not excluded, larger index order) up to the size limit */
static void extend_free(u64 S, u64 allowed, int from, int slots)
{
    process_set(S);
    if (slots == 0) return;
    for (int c = from; c <= N; c++)
        if ((allowed >> (c - 1)) & 1)
            extend_free(S | ((u64)1 << (c - 1)), allowed, c + 1, slots - 1);
}

/* Enumerates every covering set S with 1 in S and |S| <= K exactly once.
   State: chosen (a partial cover containing class 1), excl (classes that S must avoid).
   At an uncovered time a, S must contain a class covering a; branch on the first such
   class of S in a fixed order and exclude the earlier ones.  When chosen covers every
   time, S = chosen + any non-excluded extra classes.                                  */
static void dfs_sets(int depth, u64 covered, u64 excl, u64 chosen)
{
    nodes1++;
    if (covered == FULL1) { extend_free(chosen, FULL1 & ~excl & ~chosen, 1, K - depth); return; }
    if (depth == K) return;
    u64 unc = FULL1 & ~covered;
    if ((K - depth) * M < popc(unc)) return;     /* too few classes left to cover the rest */
    int best_a = 0, best_cnt = 1 << 30;
    for (u64 t = unc; t; t &= t - 1) {
        int a = lowbit(t) + 1;
        int cnt = popc(covby[a] & ~excl);
        if (cnt < best_cnt) { best_cnt = cnt; best_a = a; }
    }
    if (best_cnt == 0) return;
    u64 cand = covby[best_a] & ~excl, e = excl;
    while (cand) {
        int c = lowbit(cand) + 1; cand &= cand - 1;
        dfs_sets(depth + 1, covered | cover1[c], e, chosen | ((u64)1 << (c - 1)));
        e |= (u64)1 << (c - 1);
    }
}

static int cmp_row(const void *a, const void *b) { return memcmp(a, b, MAXK); }

static void level_one(void)
{
    nrows = 0; nodes1 = 0; sets_with1 = 0; irr_K_with1 = 0; cov_K1_with1 = 0;
    memset(sets_by_size, 0, sizeof sets_by_size); memset(canon_by_size, 0, sizeof canon_by_size);
    if (M > 0) dfs_sets(1, cover1[1], 0, 1);
    qsort(rows, nrows, sizeof(Row), cmp_row);
    size_t w = 0;
    for (size_t i = 0; i < nrows; i++)
        if (w == 0 || memcmp(rows[i].c, rows[w - 1].c, MAXK) != 0) rows[w++] = rows[i];
    nrows = w;
}

static u128 perm_count(const unsigned char *m)   /* K! / prod(multiplicity!) */
{
    u128 r = 1; int run = 0;
    for (int i = 0; i < K; i++) {
        r *= (u128)(i + 1);
        run = (i > 0 && m[i] == m[i - 1]) ? run + 1 : 1;
        r /= (u128)run;
    }
    return r;
}

/* ------------------------------------------------------------------------- */
/* Lifts                                                                       */
/* ------------------------------------------------------------------------- */

typedef struct { int w[MAXK]; } Tup;
typedef struct { Tup *t; size_t n, cap; } TupList;

static void tl_push(TupList *L, const Tup *x)
{
    if (L->n == L->cap) {
        L->cap = L->cap ? L->cap * 2 : 64;
        L->t = realloc(L->t, L->cap * sizeof(Tup));
        if (!L->t) die("out of memory");
    }
    L->t[L->n++] = *x;
}

static int gW, gC, gLevelNew;
static long gStep;                       /* l*p : the amount added per lift digit */
static u64 gFull[MAXW];
static u64 gB[MAXK][MAXC][MAXW];         /* gB[i][a]: times blocked by coordinate i with digit a */
static u64 gSuf[MAXK + 1][MAXW];         /* union of gB[r][*] over r >= i */
static int gDigits[MAXK];
static const Tup *gBase;
static TupList *gOut;
static long long gNodes, gWitnessFree, gImproper;
static int gUseBound;
#define KEEPWF 4
static int gWfDigits[KEEPWF][MAXK];      /* digits of the first few witness-free completions */

/* alternative (a) of the definition at level L: some prime q | L divides all but at most
   one coordinate  <=>  for some i, gcd(L, all coordinates except i) > 1.                */
static int proper_by_gcd(const int *w, int L)
{
    int rest = L;
    for (int q = 2; q <= rest; q++) {
        if (rest % q) continue;
        while (rest % q == 0) rest /= q;
        int not_div = 0;
        for (int i = 0; i < K; i++) if (w[i] % q) not_div++;
        if (not_div <= 1) return 1;
    }
    return 0;
}

static void lift_dfs(int i, const u64 *cov)
{
    gNodes++;
    for (int x = 0; x < gW; x++)                    /* can the rest still block every time? */
        if ((cov[x] | gSuf[i][x]) != gFull[x]) return;
    if (i == K) {                                   /* every time is blocked: no witness */
        if (gWitnessFree < KEEPWF) memcpy(gWfDigits[gWitnessFree], gDigits, sizeof gDigits);
        gWitnessFree++;
        Tup t;
        memset(&t, 0, sizeof t);
        for (int r = 0; r < K; r++) t.w[r] = gBase->w[r] + (int)(gDigits[r] * gStep);
        if (!proper_by_gcd(t.w, gLevelNew)) { gImproper++; tl_push(gOut, &t); }
        return;
    }
    if (gUseBound) {
        /* the unassigned coordinates block at most sum_r max_a |U & B[r][a]| of the
           still unblocked times U; if that is less than |U| no completion blocks all */
        int unc = 0, sum = 0;
        for (int x = 0; x < gW; x++) unc += popc(gFull[x] & ~cov[x]);
        for (int r = i; r < K && sum < unc; r++) {
            int best = 0;
            for (int a = 0; a < gC; a++) {
                int g = 0;
                for (int x = 0; x < gW; x++) g += popc(gB[r][a][x] & ~cov[x]);
                if (g > best) best = g;
            }
            sum += best;
        }
        if (sum < unc) return;
    }
    u64 nc[MAXW];
    for (int a = 0; a < gC; a++) {
        for (int x = 0; x < gW; x++) nc[x] = cov[x] | gB[i][a][x];
        gDigits[i] = a;
        lift_dfs(i + 1, nc);
    }
}

/* Appends to `out` every improper c-lift (level c*l) of the level-l vector `base`.
   Times: t = j/(c*l*p).  By the symmetry j -> -j only 1 <= j <= c*l*p/2 is needed.
   If c | j the time is a level-l time, and `base` has no witness there (checked below),
   and a lift does not change j*w mod 1 at such a time; so only c not dividing j is used. */
static void lift_tuple(const Tup *base, int l, int c, TupList *out, int use_bound)
{
    long lp = (long)l * P, Lp = lp * c;
    if (c < 2 || c > MAXC) die("lift factor out of range");

    /* check that base really has no witness at level l (it must lie in I(K,P,l)) */
    for (long j = 1; 2 * j <= lp; j++) {
        int blocked = 0;
        for (int i = 0; i < K && !blocked; i++) {
            long x = (j * base->w[i]) % lp, d = x <= lp - x ? x : lp - x;
            if ((long)(K + 1) * d < lp) blocked = 1;
        }
        if (!blocked) die("internal: base vector of a lift has a witness");
    }

    int T = 0;
    static long tj[MAXT];
    for (long j = 1; 2 * j <= Lp; j++) if (j % c) { if (T >= MAXT) die("too many times"); tj[T++] = j; }
    gW = (T + 63) / 64; gC = c; gStep = lp; gLevelNew = l * c; gBase = base; gOut = out; gUseBound = use_bound;
    memset(gFull, 0, sizeof gFull);
    for (int t = 0; t < T; t++) gFull[t / 64] |= (u64)1 << (t % 64);
    for (int i = 0; i < K; i++)
        for (int a = 0; a < c; a++) {
            long w = base->w[i] + a * lp;
            u64 *b = gB[i][a];
            for (int x = 0; x < gW; x++) b[x] = 0;
            for (int t = 0; t < T; t++) {
                long x = (tj[t] * w) % Lp, d = x <= Lp - x ? x : Lp - x;
                if ((long)(K + 1) * d < Lp) b[t / 64] |= (u64)1 << (t % 64);
            }
        }
    for (int x = 0; x < gW; x++) gSuf[K][x] = 0;
    for (int i = K - 1; i >= 0; i--)
        for (int x = 0; x < gW; x++) {
            u64 u = gSuf[i + 1][x];
            for (int a = 0; a < c; a++) u |= gB[i][a][x];
            gSuf[i][x] = u;
        }
    u64 zero[MAXW];
    memset(zero, 0, sizeof zero);
    lift_dfs(0, zero);
}

static void row_to_tup(const unsigned char *c, Tup *t)
{
    memset(t, 0, sizeof *t);
    for (int i = 0; i < K; i++) t->w[i] = c[i];
}

/* ------------------------------------------------------------------------- */
/* Modes                                                                       */
/* ------------------------------------------------------------------------- */

static int mode_level1(const char *outname)
{
    level_one();
    printf("LEVEL ONE  p=%d k=%d  n=%d classes  each class covers m=%d times\n", P, K, N, M);
    printf("  search nodes: %lld\n", nodes1);
    printf("  covering sets with at most %d distinct classes that contain class 1: %lld\n", K, sets_with1);
    int tau = 0;
    for (int s = 1; s <= K; s++) {
        if (sets_by_size[s] == 0) continue;
        if (!tau) tau = s;
        printf("    size %2d: %10lld sets containing class 1, %9lld unit orbits of sets\n",
               s, sets_by_size[s], canon_by_size[s]);
    }
    printf("  smallest number of classes in a cover (tau): %d\n", tau);
    printf("  unit orbits of covering %d-multisets = orbits of I(%d,%d,1): %zu\n", K, K, P, nrows);
    u128 total = 0; long long multisets = 0;
    for (size_t i = 0; i < nrows; i++) {
        int orbit = N / stabilizer_size(rows[i].c);
        multisets += orbit;
        total += (u128)orbit * perm_count(rows[i].c) * ((u128)1 << K);
    }
    printf("  covering %d-multisets (all, not up to units): %lld\n", K, multisets);
    printf("  |I(%d,%d,1)| as ordered vectors with signs: ", K, P); print_u128(total); printf("\n");
    printf("  among the sets that contain class 1: irredundant covers on %d distinct classes: %lld; "
           "covers on %d distinct classes: %lld\n", K, irr_K_with1, K - 1, cov_K1_with1);
    FILE *f = fopen(outname, "w");
    if (!f) die("cannot open output file");
    for (size_t i = 0; i < nrows; i++) {
        for (int j = 0; j < K; j++) fprintf(f, j ? " %d" : "%d", rows[i].c[j]);
        fputc('\n', f);
    }
    fclose(f);
    printf("  wrote %zu orbit representatives to %s\n", nrows, outname);
    return 0;
}

static int mode_cascade(const char *inname, const char *outname)
{
    FILE *in = fopen(inname, "r"), *out = fopen(outname, "w");
    if (!in || !out) die("cannot open files");
    long long orbits = 0, died[8] = {0}, alive32 = 0, closed_terminal = 0, open_terminal = 0;
    long long total_nodes = 0;
    int levels[5] = {2, 4, 8, 16, 32};
    for (;;) {
        unsigned char c[MAXK]; int v, got = 0;
        for (int j = 0; j < K; j++) { if (fscanf(in, "%d", &v) != 1) break; c[j] = (unsigned char)v; got++; }
        if (got == 0) break;
        if (got != K) die("bad orbit file");
        orbits++;
        Tup r; row_to_tup(c, &r);
        TupList cur = {0}, nxt = {0}, f2 = {0};
        tl_push(&cur, &r);
        for (int j = 0; j < K; j++) fprintf(out, j ? " %d" : "%d", c[j]);
        fprintf(out, " :");
        int l = 1, dead_at = 0;
        for (int s = 0; s < 5; s++) {
            nxt.n = 0;
            for (size_t i = 0; i < cur.n; i++) { gNodes = 0; lift_tuple(&cur.t[i], l, 2, &nxt, 0); total_nodes += gNodes; }
            l *= 2;
            fprintf(out, " l%d=%zu", levels[s], nxt.n);
            if (s == 0) for (size_t i = 0; i < nxt.n; i++) tl_push(&f2, &nxt.t[i]);
            TupList tmp = cur; cur = nxt; nxt = tmp;
            if (cur.n == 0) { dead_at = levels[s]; died[s]++; break; }
        }
        if (!dead_at) {
            alive32++;
            if ((K + 1) % 2) die("terminal step needs K+1 even");
            int c7 = (K + 1) / 2;
            fprintf(out, " ALIVE-AT-32 | level %d from the %zu members of F_2:", K + 1, f2.n);
            long long imp_total = 0;
            printf("  orbit");
            for (int j = 0; j < K; j++) printf(" %d", c[j]);
            printf(": alive at level 32; level-%d step over %zu level-2 members\n", K + 1, f2.n);
            for (size_t i = 0; i < f2.n; i++) {
                TupList t14 = {0};
                gNodes = gWitnessFree = gImproper = 0;
                lift_tuple(&f2.t[i], 2, c7, &t14, 1);
                total_nodes += gNodes;
                imp_total += gImproper;
                printf("    level-2 member");
                for (int j = 0; j < K; j++) printf(" %d", f2.t[i].w[j]);
                printf(": nodes=%lld witness-free completions=%lld improper after gcd=%lld\n",
                       gNodes, gWitnessFree, gImproper);
                for (long long q = 0; q < gWitnessFree && q < KEEPWF; q++) {
                    printf("      witness-free completion, digits a_i (w_i + a_i*2p):");
                    for (int j = 0; j < K; j++) printf(" %d", gWfDigits[q][j]);
                    printf("  -> tuple:");
                    for (int j = 0; j < K; j++) printf(" %ld", f2.t[i].w[j] + gWfDigits[q][j] * 2L * P);
                    printf("\n");
                }
                fprintf(out, " [wf=%lld imp=%lld]", gWitnessFree, gImproper);
                fflush(stdout);
                free(t14.t);
            }
            fprintf(out, " l%d=%lld", K + 1, imp_total);
            if (imp_total == 0) closed_terminal++; else open_terminal++;
        }
        fputc('\n', out);
        free(cur.t); free(nxt.t); free(f2.t);
    }
    fclose(in); fclose(out);
    printf("CASCADE  p=%d k=%d\n", P, K);
    printf("  level-one orbits read: %lld\n", orbits);
    for (int s = 0; s < 5; s++)
        printf("  F becomes empty at level %2d: %lld orbits\n", levels[s], died[s]);
    printf("  still alive at level 32: %lld orbits\n", alive32);
    printf("  of these, empty at level %d: %lld; NOT empty at level %d: %lld\n",
           K + 1, closed_terminal, K + 1, open_terminal);
    printf("  lift search nodes in total: %lld\n", total_nodes);
    long long closed = died[0] + died[1] + died[2] + died[3] + died[4] + closed_terminal;
    printf("  orbits shown eventually proper: %lld of %lld\n", closed, orbits);
    printf("  RESULT: %s\n", closed == orbits
           ? "every level-one orbit has an empty improper fiber at some level"
           : "SOME ORBIT WAS NOT CLOSED");
    printf("  wrote %s\n", outname);
    return closed == orbits ? 0 : 1;
}

static int mode_tiny(const char *route)
{
    level_one();
    int fac[16], nf = 0;
    for (const char *s = route; *s && nf < 16; ) {
        int v = (int)strtol(s, (char **)&s, 10);
        if (v >= 2) fac[nf++] = v;
        if (*s == ',') s++; else if (*s && (*s < '0' || *s > '9')) break;
    }
    printf("TINY p=%d k=%d orbits=%zu", P, K, nrows);
    u128 total = 0;
    for (size_t i = 0; i < nrows; i++)
        total += (u128)(N / stabilizer_size(rows[i].c)) * perm_count(rows[i].c) * ((u128)1 << K);
    printf(" L1="); print_u128(total);
    TupList *cur = calloc(nrows ? nrows : 1, sizeof(TupList));
    for (size_t i = 0; i < nrows; i++) { Tup r; row_to_tup(rows[i].c, &r); tl_push(&cur[i], &r); }
    int l = 1;
    for (int s = 0; s < nf; s++) {
        total = 0;
        for (size_t i = 0; i < nrows; i++) {
            /* every lift is computed twice, without and with the counting bound; the
               two results must be identical */
            TupList nxt = {0}, nx2 = {0};
            for (size_t j = 0; j < cur[i].n; j++) lift_tuple(&cur[i].t[j], l, fac[s], &nxt, 0);
            for (size_t j = 0; j < cur[i].n; j++) lift_tuple(&cur[i].t[j], l, fac[s], &nx2, 1);
            if (nxt.n != nx2.n || (nxt.n && memcmp(nxt.t, nx2.t, nxt.n * sizeof(Tup))))
                die("internal: the counting bound changed a lift result");
            free(nx2.t);
            free(cur[i].t); cur[i] = nxt;
            total += (u128)(N / stabilizer_size(rows[i].c)) * perm_count(rows[i].c) * ((u128)1 << K) * (u128)nxt.n;
        }
        l *= fac[s];
        printf(" L%d=", l); print_u128(total);
    }
    printf("\n");
    for (size_t i = 0; i < nrows; i++) {
        printf("ORBIT");
        for (int j = 0; j < K; j++) printf(" %d", rows[i].c[j]);
        printf("\n");
    }
    return 0;
}

int main(int argc, char **argv)
{
    if (argc < 4) {
        fprintf(stderr, "usage: %s level1 P K OUT | cascade P K ORBITS OUT | tiny P K c1,c2,..\n", argv[0]);
        return 2;
    }
    setup(atoi(argv[2]), atoi(argv[3]));
    if (!strcmp(argv[1], "level1") && argc == 5) return mode_level1(argv[4]);
    if (!strcmp(argv[1], "cascade") && argc == 6) return mode_cascade(argv[4], argv[5]);
    if (!strcmp(argv[1], "tiny") && argc == 5) return mode_tiny(argv[4]);
    if (!strcmp(argv[1], "tiny") && argc == 4) return mode_tiny("");
    fprintf(stderr, "bad arguments\n");
    return 2;
}
