# Lyre Restaurant & Café — website proposal

A website proposal for **Lyre Restaurant & Café**, Beach Road, Hulhumalé, Maldives.

| Path | What it is |
|---|---|
| `index.html` | Single-page prototype (static HTML/CSS/JS, no build step) |
| `docs/brand-book.md` | Brand book, research, website spec and the master AI website-build prompt |
| `assets/img/` | Lyre's own photography and logo |
| `assets/video/bodugola-signature-*.mp4` | Hero video for the signature product (landscape 16:9 + portrait 4:5), with posters |
| `assets/video/carrot-juice-reel.mp4` | Trimmed from Lyre's own carrot-juice reel (drinks section) |
| `tools/render_signature_video.py` | Re-renders the Bodugola video from `assets/img/bodugola.webp` |

Preview locally:

```sh
python3 -m http.server 8000   # then open http://localhost:8000
```

Re-render the hero video (needs `pillow`, `numpy`, `imageio-ffmpeg`):

```sh
python3 tools/render_signature_video.py all
```

Items shown with a dashed **confirm** tag need the owner's input before launch (see `docs/brand-book.md` §32).
