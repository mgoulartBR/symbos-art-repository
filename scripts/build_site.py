import os, json, shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
ART_DIR = REPO_ROOT / "art"
SITE_DIR = REPO_ROOT / "_site"
SITE_ART_DIR = SITE_DIR / "art"
SITE_DATA = SITE_DIR / "gallery.json"
SITE_INDEX = REPO_ROOT / "site" / "index.html"

IMG_EXTS = {".png", ".jpg", ".jpeg"}

def main():
    if not ART_DIR.exists():
        raise SystemExit("Missing /art directory")

    # Reset _site
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir(parents=True, exist_ok=True)

    # Copy index.html
    if not SITE_INDEX.exists():
        raise SystemExit("Missing site/index.html")
    shutil.copy2(SITE_INDEX, SITE_DIR / "index.html")

    # Copy art folder (only relevant files)
    SITE_ART_DIR.mkdir(parents=True, exist_ok=True)

    # Build mapping: base -> {image?, sgx?}
    entries = {}
    for p in ART_DIR.iterdir():
        if p.is_dir():
            continue
        ext = p.suffix.lower()
        base = p.stem
        if ext in IMG_EXTS or ext == ".sgx":
            entries.setdefault(base, {})
            if ext in IMG_EXTS:
                entries[base]["image"] = p
            elif ext == ".sgx":
                entries[base]["sgx"] = p

    items = []
    for base, d in entries.items():
        if "image" in d and "sgx" in d:
            img_src = d["image"]
            sgx_src = d["sgx"]

            # copy files into _site/art/
            shutil.copy2(img_src, SITE_ART_DIR / img_src.name)
            shutil.copy2(sgx_src, SITE_ART_DIR / sgx_src.name)

            items.append({
                "base": base,
                "image": f"./art/{img_src.name}",
                "sgx": f"./art/{sgx_src.name}",
            })

    # sort newest-ish by filename for now (simples); dá pra melhorar depois
    items.sort(key=lambda x: x["base"].lower())

    with open(SITE_DATA, "w", encoding="utf-8") as f:
        json.dump({"items": items}, f, ensure_ascii=False, indent=2)

    print(f"Built gallery with {len(items)} items")

if __name__ == "__main__":
    main()
