import os

# --- CONFIG ---
USERNAME = "ariafatah0711"   # ganti sesuai username kamu
REPO = "files-attachments"   # ganti sesuai nama repo kamu
BRANCH = "main"              # default "main" atau "master"

# --- SKIP FOLDERS ---
IGNORE_DIRS = {".git", "git", "__pycache__", ".vscode", ".idea", ".DS_Store"}

# --- GENERATE LINKS ---
base_url = f"https://raw.githubusercontent.com/{USERNAME}/{REPO}/refs/heads/{BRANCH}/"

links = []

for root, dirs, files in os.walk("."):
    # hapus folder yang harus di-skip dari iterasi
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

    for file in files:
        if file in {"gen.py", "link.md"}:
            continue

        path = os.path.join(root, file).replace("\\", "/").lstrip("./")
        links.append(base_url + path)

# --- OUTPUT ---
with open("link.md", "w") as f:
    for link in links:
        f.write(link + "\n")

print(f"[+] Generated {len(links)} links and saved to link.md ✅")
