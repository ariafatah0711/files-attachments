# flip_flop.py
def encode(text: str) -> str:
    out = []
    for c in text:
        bits = f"{ord(c):08b}"      # jadi biner 8-bit
        rev = bits[::-1]            # dibalik
        out.append(chr(int(rev, 2))) # balik ke char
    return "".join(out)

if __name__ == "__main__":
    plain = "FGTE{FLAG_EXAMPLE}"
    cipher = encode(plain)

    # simpan ke file
    with open("cipher.txt", "wb") as f:
        f.write(cipher.encode("latin-1"))

    print("Ciphertext disimpan ke cipher.txt")
