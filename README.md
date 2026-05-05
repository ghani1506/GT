# Interactive Caklempong — created by G-Haz Streamlit App

A low-latency, touch-first virtual caklempong keyboard for Streamlit.

The hit/touch response is handled entirely in the browser using the Web Audio API, so playing a note does **not** wait for a Streamlit server rerun.

## Features

- Circular caklempong keys arranged like a keyboard.
- Upload `.jpg`, `.jpeg`, `.png`, or `.webp` images for the circular keys.
- Optional upload of original caklempong samples for authentic texture.
- Fast touch, mouse, and computer-keyboard playback.
- Web Audio sample preloading and short attack envelope to reduce clicks/distortion.
- Fallback synthesized gong-like sound when no samples are uploaded.

## File structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/config.toml
├── assets/
│   └── placeholder.svg
└── samples/
    └── README.md
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload these files to the repository.
3. Go to Streamlit Community Cloud.
4. Choose your repository.
5. Set the main file path to `app.py`.
6. Deploy.

## Getting authentic caklempong texture

For the most original sound, record or obtain clean individual caklempong hits and upload them in the app sidebar.
Recommended sample format:

- WAV, MP3, OGG, or M4A.
- One note per file.
- Trim silence at the start.
- Normalize gently; avoid clipping.
- Use dry recordings without heavy room echo.

The app maps uploaded samples to pads in order. Upload 8 samples for the default 8-note layout.


## Fullscreen mode

Use the `⛶ Fullscreen` button in the top-right corner of the instrument. On mobile, a quick double-tap inside the instrument also requests fullscreen. Audio still triggers with `pointerdown` through the browser Web Audio API, so fullscreen does not add Streamlit rerun latency.


## Interface design

The interface includes a professional dark-gold stage, circular caklempong pads, fullscreen mode, and an Air Muleh/Ayer Muleh-inspired flowing Brunei heritage motif background.
