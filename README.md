# SymbOS Art Repository

Official curated repository for SymbOS/MSX compatible artworks.

## 🎨 Gallery

Browse the gallery at: https://mgoulartbr.github.io/symbos-art-repository/

## 🚀 Submit your artwork

1. Click the **Fork** button (top right)
2. Go to the `/art` folder
3. Upload your files following the naming convention below
4. Click **"Contribute"** → **Open Pull Request**

## 📁 File Naming Convention

Each artwork **must** include two files with the **same base name**:

| File | Description |
|------|-------------|
| `title.png` (or `.jpg`) | Preview image |
| `title.SGX` | SymbOS graphic file |

### With author credit (recommended)

Use **double underscore** `__` to separate title from author:

kenshiro_city__zezinho2345.png
kenshiro_city__zezinho2345.SGX

This will display as: **"kenshiro city"** — *by zezinho2345*

### Without author credit

cool_wallpaper.png
cool_wallpaper.SGX

This will display as: **"cool wallpaper"** — *by Unknown*

## 📋 Submission Rules

Each artwork **MUST** include:
- One PNG or JPEG file
- One corresponding `.SGX` file
- Both files must share the same base name
- Files must be placed inside the `/art` folder

**Valid examples:**
- `title__author.png` + `title__author.SGX` ✅
- `title.png` + `title.SGX` ✅

**Invalid examples:**
- `title.png` only (missing SGX) ❌
- `author.SGX` only (missing image) ❌
- Files outside `/art` folder ❌

## 🔧 Allowed resolutions (SGX)

- 256×212
- 512×212
- 512×424

# AI Prompt suggestion

Create a retro pixel art wallpaper using ONLY the official 16-color SymbOS palette.

STRICT COLOR LIMIT — Do not use any colors outside this exact RGB list:

- 0  (255,255,146)
- 1  (0,0,0)
- 2  (255,146,0)
- 3  (146,0,0)
- 4  (0,255,255)
- 5  (0,0,146)
- 6  (146,146,255)
- 7  (0,0,255)
- 8  (255,255,255)
- 9  (0,146,0)
- 10 (0,255,0)
- 11 (255,0,255)
- 12 (255,255,0)
- 13 (146,146,146)
- 14 (255,146,146)
- 15 (255,0,0)

Style requirements:

- True 16-color pixel art
- No gradients unless simulated using dithering
- No blended or intermediate colors
- Hard shading and strong contrast
- MSX / 8-bit / early 16-bit aesthetic
- Clean pixel edges
- No modern digital painting effects
- No soft lighting
- No color smoothing
- No anti-aliasing

Resolution: 256x212 or 512x212 (MSX-style scaling)

Theme: [ENTER THE DETAILED THEME HERE]

The image must look like it was originally designed within a strict 16-color hardware limitation.
