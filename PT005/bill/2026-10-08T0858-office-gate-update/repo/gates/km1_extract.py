# Copy sha256 of a km1.json, plus the survivor lines that are not l4=0.
# The raw file is not what gets published. Counts are not a new checker.
import hashlib, json, sys

def extract(path):
    raw = open(path, "rb").read()
    digest = hashlib.sha256(raw).hexdigest()
    text = raw.decode("utf-8", "replace")
    kept = []
    counts = {}
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        obj = None
    lists = []
    if isinstance(obj, dict):
        for key in ("persistent_lines", "survivor_lines"):
            value = obj.get(key)
            if isinstance(value, list):
                strings = [item for item in value if isinstance(item, str)]
                lists.append(key)
                counts[key] = {
                    "n": len(strings),
                    "l4=0": sum("l4=0" in item for item in strings),
                    "l8=0": sum("l8=0" in item for item in strings),
                    "PERSISTENT": sum("PERSISTENT" in item for item in strings),
                }
                kept.extend(item for item in strings if "l4=0" not in item)
    if not lists:
        kept = [line for line in text.splitlines() if "l4=0" not in line]
        counts["physical_lines_not_l4eq0"] = len(kept)
    return digest, len(raw), counts, kept

def main():
    src, dest = sys.argv[1], sys.argv[2]
    digest, nbytes, counts, kept = extract(src)
    with open(dest, "w", encoding="utf-8") as out:
        out.write("sha256 " + digest + "\n")
        out.write("bytes " + str(nbytes) + "\n")
        out.write("counts " + json.dumps(counts, sort_keys=True) + "\n")
        out.write("kept " + str(len(kept)) + "\n")
        out.write("BEGIN KEPT\n")
        for line in kept:
            out.write(line + "\n")
        out.write("END KEPT\n")

if __name__ == "__main__":
    main()
