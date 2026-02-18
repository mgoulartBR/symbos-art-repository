import os
import json
import shutil
import subprocess
import urllib.request
from pathlib import Path

# ==============================
# CONFIG
# ==============================

REPO_ROOT = Path(__file__).resolve().parents[1]
ART_DIR = REPO_ROOT / "art"
SITE_DIR = REPO_ROOT / "site"
SITE_ART_DIR = SITE_DIR / "art"
GALLERY_JSON = SITE_DIR / "gallery.json"
INDEX_FILE = SITE_DIR / "index.html"

IMG_EXTS = {".png", ".jpg", ".jpeg"}
SGX_EXT = ".sgx"

# ==============================
# GIT / AUTHOR DETECTION
# ==============================

def get_last_commit_sha(filepath: Path):
    try:
        sha = subprocess.check_output(
            ["git", "log", "-n", "1", "--pretty=format:%H", "--", str(filepath)],
            text=True
        ).strip()
        return sha or None
    except Exception:
        return None


def get_github_username_from_commit(sha: str):
    repo = os.environ.get("GITHUB_REPOSITORY")
    token = os.environ.get("GITHUB_TOKEN")

    if not repo or not token or not sha:
        return None

    url = f"https://api.github.com/repos/{repo}/commits/{sha}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")

    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read().decode("utf-8"))
        author = data.get("author")
        if author and "login" in author:
            return author["login"]
        return None
    except Exception:
        return None


def infer_author(filepath: Path):
    sha = get_last_commit_sha(filepath)
    if not sha:
        return "Unknown"

    login = get_github_username_from_commit(sha)
    return login or "Unknown"

# ==============================
# BUILD
# ==============================

def main():
    if not ART_DIR.exists():
        raise SystemExit("Missing 'art/' directory.")

    # Reset site
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)

    SITE_ART_DIR.mkdir(parents=True, exist_ok=True)

    entries = {}

    # Scan art folder
    for file in ART_DIR.iterdir():
        if file.is_dir():
            continue

        ext = file.suffix.lower()
        base = file.stem

        if ext in IMG_EXTS or ext == SGX_EXT:
            entries.setdefault(base, {})
            if ext in IMG_EXTS:
                entries[base]["image"] = file
            elif ext == SGX_EXT:
                entries[base]["sgx"] = file

    items = []

    for base, data in entries.items():
        if "image" in data and "sgx" in data:
            img_src = data["image"]
            sgx_src = data["sgx"]

            # Copy files
            shutil.copy2(img_src, SITE_ART_DIR / img_src.name)
            shutil.copy2(sgx_src, SITE_ART_DIR / sgx_src.name)

            author = infer_author(img_src)

            items.append({
                "id": base,
                "title": base,
                "author": author,
                "image": f"art/{img_src.name}",
                "sgx": f"art/{sgx_src.name}"
            })

    # Sort alphabetically
    items.sort(key=lambda x: x["id"].lower())

    # Save gallery.json
    with open(GALLERY_JSON, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)

    print(f"Built gallery with {len(items)} artworks.")


if __name__ == "__main__":
    main()
