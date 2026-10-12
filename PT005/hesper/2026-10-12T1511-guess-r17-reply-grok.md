BEGIN LETTER
FROM: Hesper (courier, for Tuzi)
TO: Opus (chair); Tuzi
TABLE: PT005
AS_OF: 2026-10-12 15:13 +08
RE: 猜公式 Round 17 literature walk (packet ad54489), send text r17_send_full.txt or r17_send_short.txt
SEAT: grok
MODEL: Grok Expert (web on)
CHAT: https://grok.com/c/679e9652-efd7-435e-a30d-7d2ebbc2b2c7

--- reply verbatim ---

**ANSWER BLOCK**

Ingredient 1: Malikiosis–Santos–Schymura (2024/2025) improves the finite-checking bound from Tao's n·O(n²) to (n+1/2 choose n−1) ≤ n^{2n}. Serves Dish B; plugs into L16-style reduction. New threshold UNFINISHED.

Ingredient 2: Czerwiński (2012) proves that random k-sets satisfy the much stronger loneliness 1/2 − ε with probability → 1. Serves Dish D; matches the Poisson heuristic in spirit. Constant UNFINISHED.

Ingredient 3: Goddyn–Wong (2006) characterises infinite families of tight instances obtained by accelerating selected speeds in {1,…,n} under gcd conditions. Serves Dish C; explains why certain omissions (including patterns near 6) appear. Explicit constant UNFINISHED.

Ingredient 4: Tao (2018) gives both the slight gap improvement 1/(2n) + c·log n / (n² (log log n)²) and the original reduction to speeds n·O(n²). Serves Dishes A and B. Numerical improvement UNFINISHED.

Ingredient 5: Czerwiński–Grytczuk (2008) prove the conjecture holds if one runner may be made invisible. Serves Dish E (finite-field flavour). Explicit P₀ UNFINISHED.

If only one dish: Dish B, because an effective finite-checking bound near 10⁴ would let the existing census close the gap.

**[Python code block]**
```python
# No new numerical constant computed this round; all cited bounds remain as stated in the sources.
print("No fresh numerical evaluation performed.")
```

FACT: The five references above were located via web search and abstract/PDF extracts in this session.

ABSTRACT: Malikiosis–Santos–Schymura Theorem A (arXiv:2411.06903) states that if LRC holds for n runners then it holds for n+1 once ∑_{S⊆[n]} v_S > (n+1/2 choose n−1).

ABSTRACT: Czerwiński arXiv:1102.4464 Theorem 1 states that a random k-subset D ⊂ {1,…,n} satisfies κ(D) ≥ 1/2 − ε with probability tending to 1.

ABSTRACT: Goddyn–Wong Integers 6 (2006) A38 characterises when replacing one speed r by m·r preserves tightness.

ABSTRACT: Tao arXiv:1701.02048 gives the stated gap improvement and the reduction to speeds of size n·O(n²).

ABSTRACT: Czerwiński–Grytczuk Information Processing Letters 108 (2008) 64–67 prove the invisible-runner variant.

Least-sure step: whether the Malikiosis–Santos–Schymura bound can be made effective enough for n = 16 to reach P₀ ∼ 10⁴. UNFINISHED: every numerical threshold not recomputed here.


--- end verbatim ---
END LETTER
