import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Interactive Caklempong",
    page_icon="🥁",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
      .stApp {
        background:
          radial-gradient(circle at top left, rgba(245,197,66,.20), transparent 32%),
          radial-gradient(circle at bottom right, rgba(20,104,80,.24), transparent 34%),
          linear-gradient(135deg, #080806 0%, #15110b 46%, #06150f 100%);
      }
      .block-container { padding-top: 1.3rem; padding-bottom: 1rem; }
      [data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(14,13,10,.96), rgba(24,17,8,.96));
        border-right: 1px solid rgba(245,197,66,.18);
      }
      .app-hero {
        border: 1px solid rgba(245,197,66,.25);
        border-radius: 28px;
        padding: 26px 28px;
        margin-bottom: 18px;
        background:
          linear-gradient(135deg, rgba(255,255,255,.08), rgba(255,255,255,.025)),
          radial-gradient(circle at 12% 20%, rgba(245,197,66,.22), transparent 28%);
        box-shadow: 0 22px 60px rgba(0,0,0,.30);
      }
      .app-hero h1 { margin: .1rem 0 .35rem; font-size: clamp(2rem, 5vw, 4.5rem); letter-spacing: -0.055em; color: #fff4ca; }
      .app-hero p { margin: 0; color: rgba(255,248,220,.82); font-size: 1.05rem; }
      .eyebrow { color: #f5c542; text-transform: uppercase; letter-spacing: .18em; font-size: .78rem; font-weight: 800; }
      .creator { margin-top: 14px; display: inline-flex; padding: 8px 14px; border-radius: 999px; background: rgba(245,197,66,.12); border: 1px solid rgba(245,197,66,.32); color: #ffe7a2; font-weight: 800; }
    </style>
    """,
    unsafe_allow_html=True,
)

DEFAULT_NOTES = [
    # Bottom row: 8 main caklempong gongs, arranged like white keys.
    {"label": "1", "key": "A", "freq": 392.00, "row": "natural", "pos": 0},
    {"label": "2", "key": "S", "freq": 440.00, "row": "natural", "pos": 1},
    {"label": "3", "key": "D", "freq": 493.88, "row": "natural", "pos": 2},
    {"label": "4", "key": "F", "freq": 523.25, "row": "natural", "pos": 3},
    {"label": "5", "key": "J", "freq": 587.33, "row": "natural", "pos": 4},
    {"label": "6", "key": "K", "freq": 659.25, "row": "natural", "pos": 5},
    {"label": "7", "key": "L", "freq": 739.99, "row": "natural", "pos": 6},
    {"label": "8", "key": ";", "freq": 783.99, "row": "natural", "pos": 7},
    # Top row: sharp/alternate tones, positioned above the gaps like a keyboard.
    {"label": "1#", "key": "W", "freq": 415.30, "row": "sharp", "pos": 0.62},
    {"label": "2#", "key": "E", "freq": 466.16, "row": "sharp", "pos": 1.62},
    {"label": "4#", "key": "T", "freq": 554.37, "row": "sharp", "pos": 3.62},
    {"label": "5#", "key": "Y", "freq": 622.25, "row": "sharp", "pos": 4.62},
    {"label": "6#", "key": "U", "freq": 698.46, "row": "sharp", "pos": 5.62},
]


def file_to_data_url(uploaded_file, fallback_mime="application/octet-stream"):
    if uploaded_file is None:
        return None
    data = uploaded_file.getvalue()
    mime = getattr(uploaded_file, "type", None) or fallback_mime
    return f"data:{mime};base64,{base64.b64encode(data).decode('utf-8')}"


st.markdown(
    """
    <div class="app-hero">
      <div class="eyebrow">Brunei Digital Instrument</div>
      <h1>Interactive Caklempong</h1>
      <p>Professional low-latency touch instrument inspired by Brunei's Air Muleh heritage motif.</p>
      <div class="creator">created by - G-Haz</div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Instrument Studio")
    st.write("Upload .jpg/.png artwork for the circular caklempong pads. If fewer images are uploaded than notes, the app reuses them.")
    images = st.file_uploader(
        "Pad .jpg/.png images",
        type=["jpg", "jpeg", "png", "webp"],
        accept_multiple_files=True,
    )
    st.write("Upload real caklempong hits for original texture. Files map to the 8 bottom gongs first, then the top sharp notes.")
    samples = st.file_uploader(
        "Caklempong audio samples",
        type=["wav", "mp3", "ogg", "m4a"],
        accept_multiple_files=True,
    )
    volume = st.slider("Volume", 0.0, 1.0, 0.85, 0.01)
    sustain = st.slider("Sample/synth decay", 0.2, 4.0, 1.7, 0.1)
    pad_size = st.slider("Pad size", 88, 180, 128, 4)

image_urls = [file_to_data_url(f, "image/jpeg") for f in images] if images else []
sample_urls = [file_to_data_url(f, "audio/wav") for f in samples] if samples else []

# JSON is built manually enough for controlled values; base64 data URLs are safe as strings after repr.
notes_js = str(DEFAULT_NOTES).replace("'", '"')
images_js = str(image_urls).replace("'", '"')
samples_js = str(sample_urls).replace("'", '"')

component_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<style>
  :root {{
    --pad-size: {pad_size}px;
    --gap: 18px;
    --gold: #f5c542;
    --deep-gold: #8b581b;
    --emerald: #0f6f54;
    --bg: #090805;
    --panel: #15120b;
    --text: #fff8dc;
  }}
  html, body {{
    margin: 0;
    background: transparent;
    color: var(--text);
    font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    touch-action: manipulation;
    user-select: none;
    -webkit-user-select: none;
    -webkit-tap-highlight-color: transparent;
  }}
  .wrap {{
    width: 100%;
    min-height: 560px;
    padding: 20px 10px 30px;
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
    border-radius: 28px;
    background:
      radial-gradient(circle at 12% 14%, rgba(245,197,66,.18), transparent 25%),
      radial-gradient(circle at 88% 80%, rgba(15,111,84,.20), transparent 30%),
      linear-gradient(135deg, rgba(16,13,7,.92), rgba(7,18,13,.92));
    border: 1px solid rgba(245,197,66,.22);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 22px 60px rgba(0,0,0,.28);
  }}
  .wrap::before {{
    content: "";
    position: absolute;
    inset: 0;
    opacity: .18;
    pointer-events: none;
    background-image:
      radial-gradient(circle at 20px 30px, rgba(245,197,66,.45) 0 3px, transparent 4px),
      radial-gradient(circle at 84px 30px, rgba(245,197,66,.35) 0 3px, transparent 4px),
      url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='260' height='80' viewBox='0 0 260 80'%3E%3Cpath d='M0 40 C35 0 65 80 100 40 S165 0 200 40 S235 80 260 40' fill='none' stroke='%23f5c542' stroke-width='3' stroke-linecap='round'/%3E%3Cpath d='M46 31 C32 12 22 17 18 29 C34 24 38 35 46 31ZM73 48 C91 66 103 58 105 45 C88 54 83 42 73 48ZM145 31 C131 12 121 17 117 29 C133 24 137 35 145 31ZM172 48 C190 66 202 58 204 45 C187 54 182 42 172 48ZM226 31 C212 12 202 17 198 29 C214 24 218 35 226 31Z' fill='%23f5c542' fill-opacity='.55'/%3E%3C/svg%3E");
    background-size: 120px 120px, 120px 120px, 260px 80px;
    background-position: 0 0, 60px 60px, center top;
  }}
  .stage-header {{
    max-width: 1100px;
    margin: 0 auto 22px;
    position: relative;
    z-index: 1;
    display: grid;
    gap: 12px;
    text-align: center;
  }}
  .stage-title {{
    font-size: clamp(24px, 5vw, 46px);
    font-weight: 900;
    letter-spacing: -.04em;
    color: #fff3c4;
    text-shadow: 0 8px 30px rgba(0,0,0,.42);
  }}
  .credit {{
    justify-self: center;
    padding: 8px 15px;
    border-radius: 999px;
    background: rgba(245,197,66,.12);
    border: 1px solid rgba(245,197,66,.34);
    color: #ffe9a7;
    font-weight: 800;
    letter-spacing: .02em;
  }}
  .status {{
    display: flex;
    gap: 10px;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
  }}
  .pill {{
    background: rgba(245, 197, 66, 0.12);
    border: 1px solid rgba(245, 197, 66, 0.35);
    border-radius: 999px;
    padding: 8px 13px;
    font-size: 14px;
  }}
  .keyboard {{
    max-width: calc((var(--pad-size) * 8) + (var(--gap) * 7));
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(8, var(--pad-size));
    grid-template-rows: calc(var(--pad-size) * .68) var(--pad-size);
    column-gap: calc(var(--gap) * .72);
    row-gap: 16px;
    justify-items: center;
    align-items: center;
    position: relative;
    z-index: 1;
    padding: 28px 18px;
    border-radius: 28px;
    background: linear-gradient(180deg, rgba(255,255,255,.065), rgba(255,255,255,.02));
    border: 1px solid rgba(255,255,255,.10);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.08);
  }}
  .pad {{
    width: var(--pad-size);
    height: var(--pad-size);
    border-radius: 50%;
    border: 4px solid rgba(255, 224, 138, .95);
    background:
      radial-gradient(circle at 42% 35%, rgba(255,255,255,.18), transparent 25%),
      radial-gradient(circle, #d59b2d 0%, #8b581b 55%, #35200a 100%);
    box-shadow:
      inset 0 10px 20px rgba(255,255,255,.14),
      inset 0 -14px 24px rgba(0,0,0,.42),
      0 14px 30px rgba(0,0,0,.42),
      0 0 0 7px rgba(245,197,66,.07);
    color: white;
    position: relative;
    overflow: hidden;
    cursor: pointer;
    display: grid;
    place-items: center;
    transform: translateZ(0);
    will-change: transform, filter;
    contain: layout paint style;
  }}

  .pad.natural {
    grid-row: 2;
  }
  .pad.sharp {
    grid-row: 1;
    width: calc(var(--pad-size) * .72);
    height: calc(var(--pad-size) * .72);
    align-self: end;
    background:
      radial-gradient(circle at 38% 30%, rgba(255,255,255,.20), transparent 23%),
      radial-gradient(circle, #ffe49a 0%, #a66a1d 48%, #160d04 100%);
    border-color: rgba(255,236,174,.98);
    box-shadow:
      inset 0 8px 16px rgba(255,255,255,.16),
      inset 0 -12px 22px rgba(0,0,0,.50),
      0 12px 24px rgba(0,0,0,.45),
      0 0 0 6px rgba(245,197,66,.06);
  }
  .pad img {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: .88;
    pointer-events: none;
  }}
  .pad::after {{
    content: "";
    position: absolute;
    inset: 28%;
    border-radius: 50%;
    background: radial-gradient(circle at 40% 35%, rgba(255,255,255,.2), rgba(255,209,86,.34) 35%, rgba(35,20,4,.7) 72%);
    box-shadow: inset 0 8px 10px rgba(255,255,255,.08), inset 0 -9px 13px rgba(0,0,0,.45);
    pointer-events: none;
  }}
  .pad.active {{
    transform: scale(.965);
    filter: brightness(1.25) saturate(1.15);
  }}
  .label, .note, .key {{ display: none; }}
  #fullscreenBtn {{
    position: fixed;
    top: 12px;
    right: 12px;
    z-index: 9999;
    padding: 10px 14px;
    border-radius: 999px;
    border: 1px solid rgba(245, 197, 66, .45);
    background: rgba(0, 0, 0, .62);
    color: white;
    font-size: 15px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 8px 22px rgba(0,0,0,.28);
    backdrop-filter: blur(8px);
    touch-action: manipulation;
  }}
  #fullscreenBtn:active {{ transform: scale(.96); }}
  body:fullscreen, html:fullscreen {{
    background: #121212;
  }}
  .wrap:fullscreen, body:fullscreen .wrap, html:fullscreen .wrap {{
    min-height: 100vh;
    display: grid;
    align-content: center;
    padding-top: 56px;
  }}
  @media (max-width: 980px) {{
    :root {{ --pad-size: min({pad_size}px, 10.2vw); --gap: 10px; }}
    .keyboard {{ overflow-x: auto; justify-content: start; }}
  }}
  @media (max-width: 640px) {{
    :root {{ --pad-size: 72px; --gap: 8px; }}
    .keyboard {{ grid-template-columns: repeat(8, var(--pad-size)); overflow-x: auto; padding-left: 14px; padding-right: 14px; }}
  }}
</style>
</head>
<body>
<button id="fullscreenBtn" type="button" aria-label="Toggle fullscreen">⛶ Fullscreen</button>
<div class="wrap" id="instrumentWrap">
  <div class="stage-header">
    <div class="stage-title">Interactive Caklempong</div>
    <div class="credit">created by - G-Haz</div>
    <div class="status" style="display:none"><div class="pill" id="audioStatus"></div></div>
  </div>
  <div class="keyboard" id="keyboard"></div>
</div>
<script>
const notes = {notes_js};
const imageUrls = {images_js};
const sampleUrls = {samples_js};
const masterVolume = {volume};
const decaySeconds = {sustain};

let audioCtx = null;
let masterGain = null;
let buffers = new Map();
let unlocked = false;

const keyboard = document.getElementById('keyboard');
const statusEl = document.getElementById('audioStatus');
const fullscreenBtn = document.getElementById('fullscreenBtn');
const fullscreenTarget = document.documentElement;

function updateFullscreenLabel() {{
  fullscreenBtn.textContent = document.fullscreenElement ? '✕ Exit fullscreen' : '⛶ Fullscreen';
}}

async function toggleFullscreen() {{
  try {{
    if (!document.fullscreenElement) {{
      await fullscreenTarget.requestFullscreen();
    }} else {{
      await document.exitFullscreen();
    }}
  }} catch (err) {{
    console.warn('Fullscreen request failed:', err);
  }} finally {{
    updateFullscreenLabel();
  }}
}}

function initAudio() {{
  if (!audioCtx) {{
    audioCtx = new (window.AudioContext || window.webkitAudioContext)({{ latencyHint: 'interactive' }});
    masterGain = audioCtx.createGain();
    masterGain.gain.value = masterVolume;
    masterGain.connect(audioCtx.destination);
  }}
  if (audioCtx.state === 'suspended') audioCtx.resume();
  unlocked = true;
  statusEl.textContent = sampleUrls.length ? 'Audio ready: sample mode' : 'Audio ready: synth fallback';
  preloadSamples();
}}

async function preloadSamples() {{
  if (!audioCtx || buffers.size || !sampleUrls.length) return;
  await Promise.all(sampleUrls.map(async (url, i) => {{
    try {{
      const arr = await fetch(url).then(r => r.arrayBuffer());
      const buf = await audioCtx.decodeAudioData(arr);
      buffers.set(i, buf);
    }} catch (e) {{
      console.warn('Could not decode sample', i, e);
    }}
  }}));
}}

function playSample(index) {{
  const buffer = buffers.get(index % Math.max(1, sampleUrls.length));
  if (!buffer) return false;
  const now = audioCtx.currentTime;
  const source = audioCtx.createBufferSource();
  source.buffer = buffer;
  const gain = audioCtx.createGain();
  gain.gain.setValueAtTime(0.0001, now);
  gain.gain.exponentialRampToValueAtTime(1.0, now + 0.006);
  gain.gain.exponentialRampToValueAtTime(0.0001, now + Math.min(decaySeconds, buffer.duration));
  source.connect(gain).connect(masterGain);
  source.start(now);
  source.stop(now + Math.min(buffer.duration, decaySeconds + 0.15));
  return true;
}}

function playSynth(freq) {{
  const now = audioCtx.currentTime;
  const out = audioCtx.createGain();
  out.gain.setValueAtTime(0.0001, now);
  out.gain.exponentialRampToValueAtTime(0.95, now + 0.004);
  out.gain.exponentialRampToValueAtTime(0.0001, now + decaySeconds);

  const partials = [1, 2.03, 2.71, 3.94, 5.12];
  const levels = [0.8, 0.34, 0.25, 0.14, 0.08];
  partials.forEach((p, i) => {{
    const osc = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    osc.type = i === 0 ? 'sine' : 'triangle';
    osc.frequency.setValueAtTime(freq * p, now);
    osc.frequency.exponentialRampToValueAtTime(freq * p * 0.996, now + decaySeconds);
    g.gain.value = levels[i];
    osc.connect(g).connect(out);
    osc.start(now);
    osc.stop(now + decaySeconds + 0.05);
  }});

  const noiseBuffer = audioCtx.createBuffer(1, audioCtx.sampleRate * 0.03, audioCtx.sampleRate);
  const data = noiseBuffer.getChannelData(0);
  for (let i = 0; i < data.length; i++) data[i] = (Math.random() * 2 - 1) * (1 - i / data.length);
  const noise = audioCtx.createBufferSource();
  noise.buffer = noiseBuffer;
  const ng = audioCtx.createGain();
  ng.gain.value = 0.09;
  noise.connect(ng).connect(out);
  noise.start(now);

  const compressor = audioCtx.createDynamicsCompressor();
  compressor.threshold.value = -16;
  compressor.knee.value = 18;
  compressor.ratio.value = 4;
  compressor.attack.value = 0.002;
  compressor.release.value = 0.08;
  out.connect(compressor).connect(masterGain);
}}

function trigger(index) {{
  initAudio();
  const pad = document.querySelector(`[data-index="${{index}}"]`);
  if (pad) {{
    pad.classList.add('active');
    setTimeout(() => pad.classList.remove('active'), 90);
  }}
  if (!playSample(index)) playSynth(notes[index].freq);
}}

notes.forEach((n, i) => {{
  const pad = document.createElement('button');
  pad.className = `pad ${{n.row || 'natural'}}`;
  pad.dataset.index = i;
  const pos = Number.isFinite(n.pos) ? n.pos : i;
  pad.style.gridColumn = `${{Math.floor(pos) + 1}} / span 1`;
  if (n.row === 'sharp') pad.style.transform = `translateX(${{(pos - Math.floor(pos)) * 100}}%)`;
  pad.setAttribute('aria-label', `Play caklempong note ${{n.label}}`);
  if (imageUrls.length) {{
    const img = document.createElement('img');
    img.src = imageUrls[i % imageUrls.length];
    img.alt = '';
    pad.appendChild(img);
  }}
  pad.addEventListener('pointerdown', (e) => {{
    e.preventDefault();
    pad.setPointerCapture?.(e.pointerId);
    trigger(i);
  }}, {{ passive: false }});
  keyboard.appendChild(pad);
}});

window.addEventListener('keydown', (e) => {{
  if (e.repeat) return;
  const idx = notes.findIndex(n => n.key.toLowerCase() === e.key.toLowerCase());
  if (idx >= 0) trigger(idx);
}});

fullscreenBtn.addEventListener('click', (e) => {{
  e.preventDefault();
  e.stopPropagation();
  initAudio();
  toggleFullscreen();
}}, {{ passive: false }});

document.addEventListener('fullscreenchange', updateFullscreenLabel);

// Warm audio as soon as user touches anywhere in the component.
window.addEventListener('pointerdown', initAudio, {{ once: true, passive: true }});

// Mobile-friendly option: first double-tap anywhere on the instrument also enters fullscreen.
let lastTap = 0;
window.addEventListener('pointerdown', (e) => {{
  const now = Date.now();
  if (now - lastTap < 320 && !document.fullscreenElement) toggleFullscreen();
  lastTap = now;
}}, {{ passive: true }});
</script>
</body>
</html>
"""

components.html(component_html, height=max(680, int(pad_size * 2.2) + 300), scrolling=False)

with st.expander("Deployment notes"):
    st.markdown(
        """
        - Push this project to GitHub, then deploy `app.py` on Streamlit Community Cloud.
        - For the most realistic caklempong sound, upload actual recorded one-shot samples in the sidebar.
        - The browser handles playback directly using Web Audio, which keeps hit response fast and avoids Streamlit interaction delay.
        """
    )
