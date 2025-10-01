import json, sys
from pathlib import Path

CHALLENGE_PATH = Path(__file__).parent / "challenge.json"

NEW_FLAG = "FGTE{...}"
# -----------------------------------------

def main():
    if not CHALLENGE_PATH.exists():
        print("challenge.json not found at", CHALLENGE_PATH)
        return
    with open(CHALLENGE_PATH, "r") as f:
        ch = json.load(f)
    
    n = int(ch["n"])
    e = int(ch["e"])

    m = int.from_bytes(NEW_FLAG.encode(), "big")
    if m >= n:
        print("ERROR: flag integer >= n. The flag is too large for the modulus.")
        return

    c = pow(m, e, n)

    ch["ciphertext"] = str(c)
    with open(CHALLENGE_PATH, "w") as f:
        json.dump(ch, f, indent=2)

    print("Berhasil Update challange.json")

if __name__ == '__main__':
    main()
