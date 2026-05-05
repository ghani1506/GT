# Gulintangan Brunei

Created by - G-Haz

A low-latency Streamlit musical interface using browser-side Web Audio for fast touch response.

## Files
- `app.py` - main Streamlit app
- `assets/gong.jpg` - gong image used on every pad
- `requirements.txt` - Streamlit dependency
- `.streamlit/config.toml` - deployment configuration

## Deploy to Streamlit Cloud
1. Upload all files to a GitHub repository.
2. In Streamlit Cloud, create a new app from the repository.
3. Set the main file path to `app.py`.
4. Deploy.

## Sound
The app includes built-in synthesized metallic gong tones so it works immediately. For a more authentic Gulintangan/Caklempong texture, upload your own `.wav`, `.mp3`, or `.ogg` samples using the sound uploader inside the app. Playback remains browser-side for low latency.

## Mobile fullscreen note
Mobile browsers require fullscreen to be triggered by a direct tap. Use the `Fullscreen` button after the app loads. On iOS Safari, fullscreen behavior may still depend on Safari and Streamlit iframe restrictions.
