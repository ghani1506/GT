import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Gulintangan Brunei",
    page_icon="🥁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSET_PATH = Path(__file__).parent / "assets" / "gong.jpg"
GONG_DATA_URI = ""
if ASSET_PATH.exists():
    encoded = base64.b64encode(ASSET_PATH.read_bytes()).decode("utf-8")
    GONG_DATA_URI = f"data:image/jpeg;base64,{encoded}"

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<style>
:root {{
  --gong-size: clamp(58px, 10.8vw, 136px);
  --gap: clamp(7px, 1.35vw, 18px);
  --gold: #f5d47a;
  --deep: #080b10;
}}

* {{ box-sizing: border-box; -webkit-tap-highlight-color: transparent; }}
html, body {{
  margin: 0;
  width: 100%;
  min-height: 100%;
  overflow: hidden;
  touch-action: manipulation;
  user-select: none;
  -webkit-user-select: none;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: radial-gradient(circle at 50% 12%, #273044 0%, #101722 42%, #05070a 100%);
  color: #fff;
}}

.app {{
  position: relative;
  width: 100vw;
  height: 100vh;
  min-height: 720px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: clamp(14px, 2.2vw, 28px);
  isolation: isolate;
}}

.app::before {{
  content: "";
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 22% 18%, rgba(245, 212, 122, 0.14), transparent 22%),
    radial-gradient(circle at 78% 30%, rgba(255, 255, 255, 0.08), transparent 18%),
    repeating-linear-gradient(135deg, rgba(245,212,122,0.055) 0 2px, transparent 2px 18px);
  z-index: -2;
}}

.air-mulih {{
  position: absolute;
  inset: 18px;
  border: 1px solid rgba(245, 212, 122, 0.22);
  border-radius: 26px;
  pointer-events: none;
  z-index: -1;
}}

.air-mulih::before, .air-mulih::after {{
  content: "";
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  width: min(720px, 78vw);
  height: 34px;
  opacity: 0.34;
  background:
    radial-gradient(ellipse at center, rgba(245,212,122,0.55) 0 18%, transparent 19%),
    repeating-radial-gradient(ellipse at center, transparent 0 10px, rgba(245,212,122,0.18) 11px 12px, transparent 13px 22px);
}}
.air-mulih::before {{ top: 18px; }}
.air-mulih::after {{ bottom: 18px; }}

.topbar {{
  width: min(1100px, 100%);
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  z-index: 4;
}}

.tool-btn {{
  appearance: none;
  border: 1px solid rgba(245, 212, 122, 0.38);
  background: rgba(0,0,0,0.42);
  color: #fff;
  border-radius: 999px;
  min-height: 42px;
  padding: 0 15px;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: .02em;
  backdrop-filter: blur(10px);
  cursor: pointer;
}}

.settings-panel {{
  display: none;
  position: absolute;
  top: 72px;
  right: clamp(16px, 2.2vw, 28px);
  width: min(340px, calc(100vw - 32px));
  padding: 16px;
  border-radius: 18px;
  border: 1px solid rgba(245, 212, 122, 0.35);
  background: rgba(5, 8, 12, 0.9);
  box-shadow: 0 18px 60px rgba(0,0,0,0.45);
  backdrop-filter: blur(18px);
  z-index: 10;
  text-align: left;
}}
.settings-panel.open {{ display: block; }}
.settings-panel label {{ display: block; font-size: 13px; color: rgba(255,255,255,.82); margin: 10px 0 6px; }}
.settings-panel input[type=file] {{ width: 100%; color: #fff; font-size: 12px; }}
.settings-panel input[type=range] {{ width: 100%; }}
.settings-panel select {{
  width: 100%;
  min-height: 40px;
  border-radius: 12px;
  border: 1px solid rgba(245,212,122,.35);
  background: rgba(255,255,255,.08);
  color: #fff;
  padding: 0 10px;
  font-weight: 700;
}}
.settings-panel option {{ color: #111; }}
.small {{ color: rgba(255,255,255,.62); font-size: 12px; line-height: 1.35; margin-top: 8px; }}

.brand {{
  width: min(1100px, 100%);
  text-align: center;
  margin-top: clamp(2px, 1vw, 12px);
  margin-bottom: clamp(18px, 3.2vw, 42px);
}}

h1 {{
  margin: 0;
  font-size: clamp(32px, 6.5vw, 76px);
  line-height: .95;
  letter-spacing: .02em;
  font-weight: 900;
  text-transform: uppercase;
  color: #ffe7a6;
  text-shadow: 0 2px 0 #7a5415, 0 18px 38px rgba(0,0,0,.55);
}}
.credit {{
  margin-top: 12px;
  font-size: clamp(13px, 2.2vw, 18px);
  color: rgba(255,255,255,.78);
  letter-spacing: .1em;
}}

.instrument {{
  width: min(1320px, 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(18px, 3vw, 42px) clamp(8px, 2vw, 26px);
  border-radius: 34px;
  background: linear-gradient(180deg, rgba(255,255,255,.085), rgba(255,255,255,.03));
  border: 1px solid rgba(245, 212, 122, .18);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.08), 0 28px 90px rgba(0,0,0,.42);
}}

.keyboard {{
  position: relative;
  width: calc((var(--gong-size) * 8) + (var(--gap) * 7));
  height: calc((var(--gong-size) * 2) + (var(--gap) * 1.35));
  max-width: 100%;
}}

.row.bottom {{
  position: absolute;
  left: 0;
  bottom: 0;
  display: grid;
  grid-template-columns: repeat(8, var(--gong-size));
  gap: var(--gap);
  justify-content: center;
  align-items: center;
}}

.sharp-row {{
  position: absolute;
  inset: 0;
  pointer-events: none;
}}

.sharp-row .gong {{
  position: absolute;
  top: 0;
  left: var(--x);
  transform: translateX(-50%);
  pointer-events: auto;
  z-index: 2;
}}

.sharp-row .gong.hit {{
  animation: sharpGongVibrate 145ms linear both;
}}

.gong {{
  position: relative;
  width: var(--gong-size);
  height: var(--gong-size);
  aspect-ratio: 1 / 1;
  border-radius: 50%;
  border: clamp(2px, .45vw, 5px) solid rgba(245, 212, 122, .75);
  background-image: url('{GONG_DATA_URI}');
  background-size: 112% 112%;
  background-position: center;
  background-repeat: no-repeat;
  box-shadow:
    inset -8px -10px 18px rgba(0,0,0,.52),
    inset 7px 8px 15px rgba(255,255,255,.12),
    0 9px 0 rgba(89, 57, 15, .62),
    0 18px 28px rgba(0,0,0,.48);
  cursor: pointer;
  transform: translateZ(0);
  will-change: transform, filter;
  overflow: hidden;
}}

.gong::before {{
  content: "";
  position: absolute;
  inset: 22%;
  border-radius: 50%;
  background: radial-gradient(circle at 38% 32%, rgba(255,255,255,.42), rgba(245,212,122,.18) 34%, rgba(0,0,0,.3) 72%);
  box-shadow: inset 0 5px 12px rgba(255,255,255,.12), inset 0 -8px 14px rgba(0,0,0,.35);
  opacity: .52;
}}

.gong::after {{
  content: "";
  position: absolute;
  inset: -28%;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,.28), transparent 36%);
  transform: scale(.1);
  opacity: 0;
}}

.gong.hit {{
  animation: gongVibrate 145ms linear both;
  filter: brightness(1.24) saturate(1.12);
}}
.gong.hit::after {{ animation: ripple 190ms ease-out both; }}

@keyframes gongVibrate {{
  0% {{ transform: translate(0,0) scale(1); }}
  18% {{ transform: translate(-1.6px, .8px) scale(.955); }}
  36% {{ transform: translate(1.4px, -1px) scale(1.018); }}
  54% {{ transform: translate(-.9px, 1px) scale(.984); }}
  72% {{ transform: translate(.8px, -.6px) scale(1.006); }}
  100% {{ transform: translate(0,0) scale(1); }}
}}
@keyframes ripple {{
  from {{ transform: scale(.1); opacity: .55; }}
  to {{ transform: scale(1.18); opacity: 0; }}
}}
@keyframes sharpGongVibrate {{
  0% {{ transform: translateX(-50%) translate(0,0) scale(1); }}
  18% {{ transform: translateX(-50%) translate(-1.6px, .8px) scale(.955); }}
  36% {{ transform: translateX(-50%) translate(1.4px, -1px) scale(1.018); }}
  54% {{ transform: translateX(-50%) translate(-.9px, 1px) scale(.984); }}
  72% {{ transform: translateX(-50%) translate(.8px, -.6px) scale(1.006); }}
  100% {{ transform: translateX(-50%) translate(0,0) scale(1); }}
}}

@media (orientation: landscape) and (max-height: 560px) {{
  :root {{ --gong-size: clamp(38px, 10.2vh, 78px); --gap: clamp(6px, 1.5vh, 12px); }}
  .app {{ min-height: 100vh; padding: 10px; }}
  .brand {{ margin-bottom: 10px; }}
  h1 {{ font-size: clamp(24px, 7vh, 44px); }}
  .credit {{ margin-top: 5px; font-size: 12px; }}
  .instrument {{ padding: 12px 8px; }}
  .keyboard {{ height: calc((var(--gong-size) * 2) + (var(--gap) * 1.1)); }}
}}

@media (max-width: 430px) {{
  :root {{ --gong-size: clamp(42px, 11.4vw, 58px); --gap: 7px; }}
  .app {{ min-height: 690px; padding: 12px 8px; }}
  .instrument {{ border-radius: 24px; }}
  .keyboard {{ width: calc((var(--gong-size) * 8) + (var(--gap) * 7)); }}
}}
</style>
</head>
<body>
<div id="app" class="app">
  <div class="air-mulih"></div>

  <div class="topbar">
    <button id="settingsBtn" class="tool-btn" type="button">Sound</button>
    <button id="fullscreenBtn" class="tool-btn" type="button">Fullscreen</button>
  </div>

  <div id="settingsPanel" class="settings-panel">
    <label>Tone</label>
    <select id="toneSelect" aria-label="Choose instrument tone">
      <option value="caklempong" selected>Caklempong</option>
      <option value="gamelan">Gamelan</option>
      <option value="bell">Bell</option>
      <option value="kalimba">Kalimba</option>
    </select>
    <label>Upload 13 real gong samples, optional</label>
    <input id="sampleUpload" type="file" accept="audio/*" multiple />
    <label>Volume</label>
    <input id="volume" type="range" min="0.4" max="2.2" step="0.05" value="1.55" />
    <div class="small">Choose a synthesized tone or upload real Gulintangan/Caklempong samples. Uploaded files are loaded in your browser only.</div>
  </div>

  <header class="brand">
    <h1>Gulintangan Brunei</h1>
    <div class="credit">created by - G-Haz</div>
  </header>

  <main class="instrument" aria-label="Gulintangan Brunei instrument">
    <div class="keyboard" aria-label="Keyboard-style gong layout">
      <section class="sharp-row" aria-label="Sharp notes positioned between natural notes">
        <button class="gong" style="--x: 12.5%;" data-note="C#" data-freq="277.18" aria-label="C sharp gong, between C and D"></button>
        <button class="gong" style="--x: 25%;" data-note="D#" data-freq="311.13" aria-label="D sharp gong, between D and E"></button>
        <button class="gong" style="--x: 50%;" data-note="F#" data-freq="369.99" aria-label="F sharp gong, between F and G"></button>
        <button class="gong" style="--x: 62.5%;" data-note="G#" data-freq="415.30" aria-label="G sharp gong, between G and A"></button>
        <button class="gong" style="--x: 75%;" data-note="A#" data-freq="466.16" aria-label="A sharp gong, between A and B"></button>
      </section>
      <section class="row bottom" aria-label="Natural notes">
        <button class="gong" data-note="C" data-freq="261.63" aria-label="C gong"></button>
        <button class="gong" data-note="D" data-freq="293.66" aria-label="D gong"></button>
        <button class="gong" data-note="E" data-freq="329.63" aria-label="E gong"></button>
        <button class="gong" data-note="F" data-freq="349.23" aria-label="F gong"></button>
        <button class="gong" data-note="G" data-freq="392.00" aria-label="G gong"></button>
        <button class="gong" data-note="A" data-freq="440.00" aria-label="A gong"></button>
        <button class="gong" data-note="B" data-freq="493.88" aria-label="B gong"></button>
        <button class="gong" data-note="C2" data-freq="523.25" aria-label="high C gong"></button>
      </section>
    </div>
  </main>
</div>

<script>
const app = document.getElementById('app');
const gongs = Array.from(document.querySelectorAll('.gong'));
const fullscreenBtn = document.getElementById('fullscreenBtn');
const settingsBtn = document.getElementById('settingsBtn');
const settingsPanel = document.getElementById('settingsPanel');
const volume = document.getElementById('volume');
const sampleUpload = document.getElementById('sampleUpload');
const toneSelect = document.getElementById('toneSelect');

let audioCtx = null;
let master = null;
let limiter = null;
let uploadedBuffers = [];
let unlocked = false;

function ensureAudio() {{
  if (!audioCtx) {{
    audioCtx = new (window.AudioContext || window.webkitAudioContext)({{ latencyHint: 'interactive' }});
    limiter = audioCtx.createDynamicsCompressor();
    limiter.threshold.value = -9;
    limiter.knee.value = 12;
    limiter.ratio.value = 12;
    limiter.attack.value = 0.002;
    limiter.release.value = 0.11;
    master = audioCtx.createGain();
    master.gain.value = Number(volume.value);
    master.connect(limiter);
    limiter.connect(audioCtx.destination);
  }}
  if (audioCtx.state === 'suspended') audioCtx.resume();
}}

function makeNoiseBuffer(duration = 0.38) {{
  const sampleRate = audioCtx.sampleRate;
  const buffer = audioCtx.createBuffer(1, Math.floor(sampleRate * duration), sampleRate);
  const data = buffer.getChannelData(0);
  for (let i = 0; i < data.length; i++) {{
    const decay = Math.pow(1 - i / data.length, 3.2);
    data[i] = (Math.random() * 2 - 1) * decay;
  }}
  return buffer;
}}

function playUploaded(index) {{
  const buffer = uploadedBuffers[index % uploadedBuffers.length];
  const src = audioCtx.createBufferSource();
  src.buffer = buffer;
  const gain = audioCtx.createGain();
  gain.gain.value = 1.35;
  src.connect(gain);
  gain.connect(master);
  src.start();
}}

function playSynth(freq) {
  const tone = toneSelect.value || 'caklempong';
  if (tone === 'bell') return playBell(freq);
  if (tone === 'kalimba') return playKalimba(freq);
  if (tone === 'gamelan') return playGamelan(freq);
  return playCaklempong(freq);
}

function playBell(freq) {
  const now = audioCtx.currentTime;
  const out = audioCtx.createGain();
  out.gain.setValueAtTime(0.001, now);
  out.gain.exponentialRampToValueAtTime(1.15, now + 0.004);
  out.gain.exponentialRampToValueAtTime(0.0007, now + 2.6);
  out.connect(master);
  const partials = [1, 2.01, 2.99, 4.21, 5.43, 6.8];
  const gains = [0.56, 0.28, 0.2, 0.13, 0.09, 0.06];
  partials.forEach((p, i) => {
    const osc = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq * p, now);
    g.gain.setValueAtTime(gains[i], now);
    g.gain.exponentialRampToValueAtTime(0.0007, now + (2.4 - i * 0.22));
    osc.connect(g); g.connect(out); osc.start(now); osc.stop(now + 2.7);
  });
}

function playKalimba(freq) {
  const now = audioCtx.currentTime;
  const out = audioCtx.createGain();
  out.gain.setValueAtTime(0.001, now);
  out.gain.exponentialRampToValueAtTime(1.25, now + 0.003);
  out.gain.exponentialRampToValueAtTime(0.0008, now + 1.15);
  out.connect(master);
  const partials = [1, 2.015, 3.03, 5.01];
  const gains = [0.78, 0.22, 0.10, 0.045];
  partials.forEach((p, i) => {
    const osc = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    osc.type = i === 0 ? 'triangle' : 'sine';
    osc.frequency.setValueAtTime(freq * p, now);
    g.gain.setValueAtTime(gains[i], now);
    g.gain.exponentialRampToValueAtTime(0.0008, now + (0.9 - i * 0.11));
    osc.connect(g); g.connect(out); osc.start(now); osc.stop(now + 1.2);
  });
}

function playGamelan(freq) {
  const now = audioCtx.currentTime;
  const out = audioCtx.createGain();
  out.gain.setValueAtTime(0.001, now);
  out.gain.exponentialRampToValueAtTime(1.22, now + 0.005);
  out.gain.exponentialRampToValueAtTime(0.0008, now + 1.75);
  out.connect(master);
  const partials = [1, 1.52, 2.36, 3.18, 4.71, 6.1];
  const gains = [0.72, 0.36, 0.22, 0.16, 0.09, 0.06];
  partials.forEach((p, i) => {
    const osc = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    osc.type = i < 2 ? 'sine' : 'triangle';
    osc.frequency.setValueAtTime(freq * p, now);
    osc.frequency.exponentialRampToValueAtTime(freq * p * 0.988, now + 0.35);
    g.gain.setValueAtTime(gains[i], now);
    g.gain.exponentialRampToValueAtTime(0.0008, now + (1.65 - i * 0.12));
    osc.connect(g); g.connect(out); osc.start(now); osc.stop(now + 1.85);
  });
  addMetalNoise(freq, 0.18, 0.32, 5.2);
}

function playCaklempong(freq) {
  const now = audioCtx.currentTime;
  const out = audioCtx.createGain();
  out.gain.setValueAtTime(0.001, now);
  out.gain.exponentialRampToValueAtTime(1.18, now + 0.006);
  out.gain.exponentialRampToValueAtTime(0.0008, now + 1.2);
  out.connect(master);

  const partials = [1, 2.02, 2.74, 3.41, 4.83];
  const gains = [0.82, 0.32, 0.23, 0.16, 0.1];
  partials.forEach((p, i) => {
    const osc = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    osc.type = i === 0 ? 'sine' : 'triangle';
    osc.frequency.setValueAtTime(freq * p, now);
    osc.frequency.exponentialRampToValueAtTime(freq * p * 0.992, now + 0.22);
    g.gain.setValueAtTime(gains[i], now);
    g.gain.exponentialRampToValueAtTime(0.0008, now + (i === 0 ? 1.35 : 0.65));
    osc.connect(g);
    g.connect(out);
    osc.start(now);
    osc.stop(now + 1.45);
  });
  addMetalNoise(freq, 0.16, 0.28, 3.2);
}

function addMetalNoise(freq, amount, duration, mult) {
  const now = audioCtx.currentTime;
  const noise = audioCtx.createBufferSource();
  noise.buffer = makeNoiseBuffer(duration);
  const filter = audioCtx.createBiquadFilter();
  filter.type = 'bandpass';
  filter.frequency.value = freq * mult;
  filter.Q.value = 4.5;
  const ng = audioCtx.createGain();
  ng.gain.setValueAtTime(amount, now);
  ng.gain.exponentialRampToValueAtTime(0.0005, now + Math.max(0.1, duration - 0.06));
  noise.connect(filter);
  filter.connect(ng);
  ng.connect(master);
  noise.start(now);
}

function animate(gong) {{
  gong.classList.remove('hit');
  void gong.offsetWidth;
  gong.classList.add('hit');
  if (navigator.vibrate) navigator.vibrate(12);
}}

function hit(gong, index) {{
  ensureAudio();
  animate(gong);
  if (uploadedBuffers.length) playUploaded(index);
  else playSynth(Number(gong.dataset.freq));
}}

gongs.forEach((gong, index) => {{
  gong.addEventListener('pointerdown', (e) => {{
    e.preventDefault();
    hit(gong, index);
  }}, {{ passive: false }});
}});

const keyMap = ['w','e','t','y','u','a','s','d','f','j','k','l',';'];
window.addEventListener('keydown', (e) => {{
  const idx = keyMap.indexOf(e.key.toLowerCase());
  if (idx >= 0 && gongs[idx]) hit(gongs[idx], idx);
}});

volume.addEventListener('input', () => {{
  ensureAudio();
  master.gain.value = Number(volume.value);
}});

sampleUpload.addEventListener('change', async (e) => {{
  ensureAudio();
  const files = Array.from(e.target.files || []).slice(0, 13);
  uploadedBuffers = [];
  for (const file of files) {{
    const arr = await file.arrayBuffer();
    try {{
      const decoded = await audioCtx.decodeAudioData(arr.slice(0));
      uploadedBuffers.push(decoded);
    }} catch (err) {{ console.warn('Could not decode', file.name, err); }}
  }}
}});

settingsBtn.addEventListener('pointerdown', (e) => {{
  e.preventDefault();
  e.stopPropagation();
  settingsPanel.classList.toggle('open');
}}, {{ passive: false }});

async function enterFullscreen() {{
  const elem = document.documentElement;
  try {{
    if (!document.fullscreenElement && elem.requestFullscreen) await elem.requestFullscreen();
    else if (document.fullscreenElement && document.exitFullscreen) await document.exitFullscreen();
  }} catch (err) {{
    console.warn('Fullscreen blocked by browser or iframe:', err);
  }}
}}

fullscreenBtn.addEventListener('pointerdown', (e) => {{
  e.preventDefault();
  e.stopPropagation();
  ensureAudio();
  enterFullscreen();
}}, {{ passive: false }});

app.addEventListener('pointerdown', () => {{
  if (!unlocked) {{
    ensureAudio();
    unlocked = true;
  }}
}}, {{ once: true }});
</script>
</body>
</html>
"""

components.html(html, height=920, scrolling=False)
