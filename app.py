import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Gulintangan Brunei",
    page_icon="🟡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSET_PATH = Path(__file__).parent / "assets" / "gong.jpg"
try:
    gong_b64 = base64.b64encode(ASSET_PATH.read_bytes()).decode("utf-8")
except FileNotFoundError:
    gong_b64 = ""

gong_img = f"data:image/jpeg;base64,{gong_b64}" if gong_b64 else ""

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<title>Gulintangan Brunei</title>
<style>
    :root {{
        --gold: #f6c453;
        --gold-soft: rgba(246, 196, 83, 0.32);
        --bg1: #08111f;
        --bg2: #15233a;
        --panel: rgba(255, 255, 255, 0.075);
        --white: #f8fafc;
        --muted: rgba(248, 250, 252, 0.72);
        --gong-size: clamp(76px, 9.2vw, 132px);
        --sharp-size: clamp(68px, 8vw, 116px);
    }}

    * {{ box-sizing: border-box; -webkit-tap-highlight-color: transparent; }}

    html, body {{
        margin: 0;
        min-height: 100%;
        overflow-x: hidden;
        background:
            radial-gradient(circle at 15% 5%, rgba(246,196,83,0.20), transparent 27%),
            radial-gradient(circle at 85% 20%, rgba(120,76,24,0.22), transparent 33%),
            linear-gradient(135deg, var(--bg1), var(--bg2));
        color: var(--white);
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        touch-action: manipulation;
        user-select: none;
    }}

    body::before {{
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        opacity: 0.18;
        background-image:
            repeating-linear-gradient(45deg, transparent 0 18px, rgba(246,196,83,0.18) 18px 20px),
            repeating-linear-gradient(-45deg, transparent 0 28px, rgba(255,255,255,0.10) 28px 30px);
        mask-image: linear-gradient(to bottom, black 0%, transparent 82%);
    }}

    .app {{
        width: 100%;
        min-height: 100vh;
        padding: 20px 18px 34px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        gap: 16px;
    }}

    .topbar {{
        width: min(1180px, 100%);
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 14px;
    }}

    .brand {{ text-align: left; }}

    h1 {{
        margin: 0;
        font-size: clamp(2.05rem, 5.5vw, 4.8rem);
        line-height: 0.96;
        letter-spacing: -0.06em;
        font-weight: 900;
        text-shadow: 0 12px 30px rgba(0,0,0,0.45);
    }}

    .credit {{
        margin-top: 8px;
        color: var(--gold);
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: lowercase;
        font-size: clamp(0.78rem, 2.2vw, 1rem);
    }}

    .controls {{
        display: flex;
        align-items: center;
        justify-content: flex-end;
        gap: 10px;
        flex-wrap: wrap;
    }}

    .control-card {{
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 9px 12px;
        border: 1px solid rgba(246,196,83,0.28);
        background: rgba(0,0,0,0.24);
        border-radius: 18px;
        backdrop-filter: blur(12px);
        box-shadow: 0 12px 28px rgba(0,0,0,0.20);
    }}

    label {{
        color: var(--muted);
        font-size: 0.82rem;
        font-weight: 700;
    }}

    select, input[type="range"], button {{
        font: inherit;
    }}

    select {{
        border: 0;
        border-radius: 999px;
        padding: 9px 34px 9px 12px;
        background: rgba(255,255,255,0.12);
        color: white;
        outline: none;
        font-weight: 800;
    }}

    option {{ background: #111827; color: white; }}

    input[type="range"] {{
        width: 122px;
        accent-color: var(--gold);
        cursor: pointer;
    }}

    .fs-btn {{
        border: 1px solid rgba(246,196,83,0.35);
        color: var(--white);
        background: linear-gradient(135deg, rgba(246,196,83,0.28), rgba(255,255,255,0.10));
        padding: 11px 14px;
        border-radius: 16px;
        cursor: pointer;
        font-weight: 900;
        box-shadow: 0 12px 28px rgba(0,0,0,0.22);
    }}

    .stage {{
        width: min(1220px, 100%);
        margin-top: 4px;
        padding: clamp(16px, 3vw, 26px);
        border-radius: 34px;
        border: 1px solid rgba(246,196,83,0.18);
        background:
            linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.025)),
            radial-gradient(circle at 50% 0%, rgba(246,196,83,0.16), transparent 46%);
        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.12),
            0 30px 75px rgba(0,0,0,0.35);
        position: relative;
    }}

    .air-mulih {{
        position: absolute;
        inset: 14px;
        border-radius: 27px;
        pointer-events: none;
        border: 1px solid rgba(246,196,83,0.12);
        opacity: 0.55;
        background:
            radial-gradient(circle at 8% 10%, rgba(246,196,83,0.20) 0 3px, transparent 4px),
            radial-gradient(circle at 92% 90%, rgba(246,196,83,0.18) 0 3px, transparent 4px),
            repeating-linear-gradient(90deg, transparent 0 48px, rgba(246,196,83,0.075) 48px 50px);
    }}

    .keyboard {{
        position: relative;
        min-height: calc(var(--gong-size) * 2.05);
        width: min(1120px, 100%);
        margin: 10px auto 0;
        padding-top: calc(var(--sharp-size) * 0.82);
    }}

    .bottom-row {{
        position: relative;
        z-index: 1;
        display: grid;
        grid-template-columns: repeat(8, var(--gong-size));
        justify-content: center;
        gap: clamp(10px, 1.6vw, 20px);
    }}

    .sharp-layer {{
        position: absolute;
        left: 50%;
        top: 0;
        transform: translateX(-50%);
        width: calc((var(--gong-size) * 8) + (clamp(10px, 1.6vw, 20px) * 7));
        height: var(--sharp-size);
        z-index: 3;
        pointer-events: none;
    }}

    .gong {{
        width: var(--gong-size);
        height: var(--gong-size);
        border: 0;
        border-radius: 50%;
        background-image: url('{gong_img}');
        background-size: 112% 112%;
        background-position: center center;
        background-repeat: no-repeat;
        overflow: hidden;
        cursor: pointer;
        touch-action: manipulation;
        position: relative;
        pointer-events: auto;
        box-shadow:
            inset -10px -12px 18px rgba(0,0,0,0.48),
            inset 8px 10px 18px rgba(255,255,255,0.18),
            0 13px 26px rgba(0,0,0,0.46),
            0 0 0 1px rgba(246,196,83,0.10);
        transition: transform 45ms linear, filter 45ms linear, box-shadow 45ms linear;
    }}

    .gong::after {{
        content: "";
        position: absolute;
        inset: 13%;
        border-radius: 50%;
        background: radial-gradient(circle at 35% 28%, rgba(255,255,255,0.22), transparent 28%), radial-gradient(circle, rgba(246,196,83,0.06), transparent 64%);
        pointer-events: none;
        mix-blend-mode: screen;
    }}

    .gong.sharp {{
        position: absolute;
        top: 0;
        width: var(--sharp-size);
        height: var(--sharp-size);
        transform: translateX(-50%);
        filter: brightness(0.95) saturate(1.08);
        box-shadow:
            inset -9px -11px 16px rgba(0,0,0,0.52),
            inset 7px 9px 14px rgba(255,255,255,0.16),
            0 12px 24px rgba(0,0,0,0.48),
            0 0 0 1px rgba(246,196,83,0.10);
    }}

    .gong.hit {{
        animation: gongHit 180ms cubic-bezier(.2, .9, .2, 1.1);
        filter: brightness(1.2) saturate(1.2);
        box-shadow:
            inset -8px -10px 15px rgba(0,0,0,0.42),
            inset 8px 11px 18px rgba(255,255,255,0.22),
            0 0 0 7px rgba(246,196,83,0.18),
            0 20px 34px rgba(0,0,0,0.50);
    }}

    @keyframes gongHit {{
        0% {{ transform: scale(1); }}
        34% {{ transform: scale(0.90); }}
        64% {{ transform: scale(1.07); }}
        100% {{ transform: scale(1); }}
    }}

    .gong.sharp.hit {{
        animation: sharpHit 180ms cubic-bezier(.2, .9, .2, 1.1);
    }}

    @keyframes sharpHit {{
        0% {{ transform: translateX(-50%) scale(1); }}
        34% {{ transform: translateX(-50%) scale(0.90); }}
        64% {{ transform: translateX(-50%) scale(1.07); }}
        100% {{ transform: translateX(-50%) scale(1); }}
    }}

    .hint {{
        margin-top: 18px;
        text-align: center;
        color: var(--muted);
        font-weight: 700;
        font-size: 0.88rem;
    }}

    @media (max-width: 840px) {{
        :root {{
            --gong-size: clamp(68px, 19vw, 98px);
            --sharp-size: clamp(60px, 15.5vw, 84px);
        }}

        .app {{ padding: 14px 8px 28px; }}

        .topbar {{
            align-items: center;
            flex-direction: column;
            text-align: center;
        }}
        .brand {{ text-align: center; }}
        .controls {{ justify-content: center; }}

        .stage {{
            padding: 12px 7px 18px;
            border-radius: 24px;
        }}

        .keyboard {{
            width: 100%;
            overflow-x: auto;
            padding-left: 10px;
            padding-right: 10px;
            scrollbar-width: none;
        }}
        .keyboard::-webkit-scrollbar {{ display: none; }}

        .bottom-row {{
            grid-template-columns: repeat(8, var(--gong-size));
            min-width: calc((var(--gong-size) * 8) + 70px);
            padding-left: 28px;
            padding-right: 28px;
        }}
        .sharp-layer {{
            min-width: calc((var(--gong-size) * 8) + 70px);
        }}
    }}
</style>
</head>
<body>
<div class="app" id="appRoot">
    <div class="topbar">
        <div class="brand">
            <h1>Gulintangan Brunei</h1>
            <div class="credit">created by - G-Haz</div>
        </div>
        <div class="controls">
            <div class="control-card">
                <label for="toneSelect">Tone</label>
                <select id="toneSelect" aria-label="Select tone">
                    <option value="caklempong" selected>Caklempong</option>
                    <option value="gamelan">Gamelan</option>
                    <option value="bell">Bell</option>
                    <option value="kalimba">Kalimba</option>
                </select>
            </div>
            <div class="control-card">
                <label for="volumeSlider">Volume</label>
                <input id="volumeSlider" type="range" min="0" max="100" value="100" aria-label="Volume" />
            </div>
            <button class="fs-btn" id="fullscreenBtn" type="button">⛶ Fullscreen</button>
        </div>
    </div>

    <div class="stage">
        <div class="air-mulih"></div>
        <div class="keyboard" id="keyboard">
            <div class="sharp-layer" id="sharpLayer"></div>
            <div class="bottom-row" id="bottomRow"></div>
        </div>
        <div class="hint">Select a tone, then tap the gongs. Notes begin from C3.</div>
    </div>
</div>

<script>
(() => {{
    const naturalNotes = [
        {{ note: "C3", freq: 130.8128 }},
        {{ note: "D3", freq: 146.8324 }},
        {{ note: "E3", freq: 164.8138 }},
        {{ note: "F3", freq: 174.6141 }},
        {{ note: "G3", freq: 195.9977 }},
        {{ note: "A3", freq: 220.0000 }},
        {{ note: "B3", freq: 246.9417 }},
        {{ note: "C4", freq: 261.6256 }}
    ];

    const sharpNotes = [
        {{ note: "C#3", freq: 138.5913, between: [0, 1] }},
        {{ note: "D#3", freq: 155.5635, between: [1, 2] }},
        {{ note: "F#3", freq: 184.9972, between: [3, 4] }},
        {{ note: "G#3", freq: 207.6523, between: [4, 5] }},
        {{ note: "A#3", freq: 233.0819, between: [5, 6] }}
    ];

    const bottomRow = document.getElementById("bottomRow");
    const sharpLayer = document.getElementById("sharpLayer");
    const toneSelect = document.getElementById("toneSelect");
    const volumeSlider = document.getElementById("volumeSlider");
    const fullscreenBtn = document.getElementById("fullscreenBtn");
    const keyboard = document.getElementById("keyboard");

    let audioCtx = null;
    let masterGain = null;
    let compressor = null;
    let limiter = null;
    let unlocked = false;

    function initAudio() {{
        if (audioCtx) return;
        audioCtx = new (window.AudioContext || window.webkitAudioContext)({{ latencyHint: "interactive" }});

        masterGain = audioCtx.createGain();
        masterGain.gain.value = 0.72;

        compressor = audioCtx.createDynamicsCompressor();
        compressor.threshold.value = -18;
        compressor.knee.value = 18;
        compressor.ratio.value = 8;
        compressor.attack.value = 0.002;
        compressor.release.value = 0.09;

        limiter = audioCtx.createDynamicsCompressor();
        limiter.threshold.value = -4;
        limiter.knee.value = 0;
        limiter.ratio.value = 20;
        limiter.attack.value = 0.001;
        limiter.release.value = 0.05;

        masterGain.connect(compressor);
        compressor.connect(limiter);
        limiter.connect(audioCtx.destination);
    }}

    async function unlockAudio() {{
        initAudio();
        if (audioCtx.state === "suspended") await audioCtx.resume();
        if (!unlocked) {{
            const buffer = audioCtx.createBuffer(1, 1, 22050);
            const source = audioCtx.createBufferSource();
            source.buffer = buffer;
            source.connect(masterGain);
            source.start(0);
            unlocked = true;
        }}
    }}

    function setVolume() {{
        initAudio();
        const raw = Number(volumeSlider.value) / 100;
        // Equal-power curve; max remains controlled by limiter/compressor to avoid harsh clipping.
        masterGain.gain.setTargetAtTime(0.18 + (raw * raw * 0.62), audioCtx.currentTime, 0.01);
    }}

    volumeSlider.addEventListener("input", setVolume);

    function envGain(start, attack, decay, sustain, release, totalDuration, peak = 1.0) {{
        const gain = audioCtx.createGain();
        const t = start;
        gain.gain.cancelScheduledValues(t);
        gain.gain.setValueAtTime(0.0001, t);
        gain.gain.exponentialRampToValueAtTime(Math.max(0.001, peak), t + attack);
        gain.gain.exponentialRampToValueAtTime(Math.max(0.001, sustain), t + attack + decay);
        gain.gain.setTargetAtTime(0.0001, t + totalDuration - release, release / 3);
        return gain;
    }}

    function makeOsc(freq, type, detune = 0) {{
        const osc = audioCtx.createOscillator();
        osc.type = type;
        osc.frequency.value = freq;
        osc.detune.value = detune;
        return osc;
    }}

    function connectToneNode(node, gain, destination = masterGain) {{
        node.connect(gain);
        gain.connect(destination);
    }}

    function playBell(freq) {{
        const now = audioCtx.currentTime;
        const duration = 2.6;
        const partials = [
            [1.000, 0.42, 0],
            [2.010, 0.22, 4],
            [2.710, 0.15, -3],
            [3.950, 0.10, 6]
        ];
        partials.forEach(([ratio, amp, detune]) => {{
            const o = makeOsc(freq * ratio, "sine", detune);
            const g = envGain(now, 0.005, 0.35, amp * 0.18, 1.8, duration, amp);
            connectToneNode(o, g);
            o.start(now); o.stop(now + duration + 0.08);
        }});
    }}

    function playKalimba(freq) {{
        const now = audioCtx.currentTime;
        const duration = 1.35;
        const pluck = makeOsc(freq, "triangle", 0);
        const body = makeOsc(freq * 2.02, "sine", 2);
        const sparkle = makeOsc(freq * 3.05, "sine", -5);
        const filter = audioCtx.createBiquadFilter();
        filter.type = "lowpass";
        filter.frequency.setValueAtTime(Math.min(5200, freq * 15), now);
        filter.Q.value = 0.45;
        filter.connect(masterGain);
        [[pluck, 0.50], [body, 0.18], [sparkle, 0.08]].forEach(([osc, amp]) => {{
            const g = envGain(now, 0.002, 0.12, amp * 0.12, 0.8, duration, amp);
            osc.connect(g); g.connect(filter);
            osc.start(now); osc.stop(now + duration + 0.08);
        }});
    }}

    function playGamelan(freq) {{
        const now = audioCtx.currentTime;
        const duration = 2.2;
        const filter = audioCtx.createBiquadFilter();
        filter.type = "bandpass";
        filter.frequency.value = Math.min(3600, freq * 6.2);
        filter.Q.value = 1.1;
        filter.connect(masterGain);
        const partials = [[1.00,0.38,0], [1.50,0.23,7], [2.01,0.18,-6], [2.74,0.13,5], [3.98,0.08,-8]];
        partials.forEach(([ratio, amp, detune]) => {{
            const o = makeOsc(freq * ratio, ratio < 1.1 ? "triangle" : "sine", detune);
            const g = envGain(now, 0.004, 0.28, amp * 0.20, 1.35, duration, amp);
            o.connect(g); g.connect(filter);
            o.start(now); o.stop(now + duration + 0.08);
        }});
    }}

    function playCaklempong(freq) {{
        const now = audioCtx.currentTime;
        const duration = 2.05;
        const filter = audioCtx.createBiquadFilter();
        filter.type = "bandpass";
        filter.frequency.value = Math.min(4200, freq * 7.8);
        filter.Q.value = 1.8;
        filter.connect(masterGain);

        const partials = [
            [1.00, 0.48, 0],
            [2.12, 0.26, -4],
            [2.92, 0.17, 5],
            [4.20, 0.10, -7]
        ];
        partials.forEach(([ratio, amp, detune]) => {{
            const o = makeOsc(freq * ratio, "sine", detune);
            const g = envGain(now, 0.003, 0.18, amp * 0.16, 1.2, duration, amp);
            o.connect(g); g.connect(filter);
            o.start(now); o.stop(now + duration + 0.08);
        }});

        // Short metallic strike noise.
        const noiseBuffer = audioCtx.createBuffer(1, Math.floor(audioCtx.sampleRate * 0.04), audioCtx.sampleRate);
        const data = noiseBuffer.getChannelData(0);
        for (let i = 0; i < data.length; i++) {{
            data[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / data.length, 2.2);
        }}
        const noise = audioCtx.createBufferSource();
        noise.buffer = noiseBuffer;
        const ng = envGain(now, 0.001, 0.018, 0.001, 0.025, 0.075, 0.10);
        const nf = audioCtx.createBiquadFilter();
        nf.type = "highpass";
        nf.frequency.value = 1200;
        noise.connect(nf); nf.connect(ng); ng.connect(masterGain);
        noise.start(now); noise.stop(now + 0.08);
    }}

    function playNote(freq) {{
        unlockAudio();
        setVolume();
        const tone = toneSelect.value;
        if (tone === "bell") playBell(freq);
        else if (tone === "kalimba") playKalimba(freq);
        else if (tone === "gamelan") playGamelan(freq);
        else playCaklempong(freq);
    }}

    function hitAnimation(el) {{
        el.classList.remove("hit");
        void el.offsetWidth;
        el.classList.add("hit");
        window.setTimeout(() => el.classList.remove("hit"), 190);
    }}

    function makeGong(noteObj, sharp=false) {{
        const btn = document.createElement("button");
        btn.className = sharp ? "gong sharp" : "gong";
        btn.type = "button";
        btn.setAttribute("aria-label", noteObj.note);
        btn.dataset.note = noteObj.note;
        btn.dataset.freq = noteObj.freq;
        btn.addEventListener("pointerdown", (e) => {{
            e.preventDefault();
            playNote(noteObj.freq);
            hitAnimation(btn);
        }}, {{ passive: false }});
        return btn;
    }}

    function layoutGongs() {{
        bottomRow.innerHTML = "";
        sharpLayer.innerHTML = "";

        naturalNotes.forEach(n => bottomRow.appendChild(makeGong(n, false)));

        // Put C# exactly between C and D, D# between D and E, F# between F and G, etc.
        const gap = parseFloat(getComputedStyle(bottomRow).columnGap || getComputedStyle(bottomRow).gap || 16);
        const gongSize = parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--gong-size"));
        const sharpSize = parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--sharp-size"));
        const startCenter = gongSize / 2;
        const step = gongSize + gap;

        sharpNotes.forEach(s => {{
            const [leftIdx, rightIdx] = s.between;
            const leftCenter = startCenter + leftIdx * step;
            const rightCenter = startCenter + rightIdx * step;
            const centerBetween = (leftCenter + rightCenter) / 2;
            const btn = makeGong(s, true);
            btn.style.left = centerBetween + "px";
            sharpLayer.appendChild(btn);
        }});
    }}

    function requestFullscreenMobileSafe() {{
        const elem = document.documentElement;
        if (!document.fullscreenElement && elem.requestFullscreen) {{
            elem.requestFullscreen().catch(() => {{}});
        }} else if (document.fullscreenElement && document.exitFullscreen) {{
            document.exitFullscreen().catch(() => {{}});
        }}
    }}

    fullscreenBtn.addEventListener("pointerdown", async (e) => {{
        e.preventDefault();
        await unlockAudio();
        requestFullscreenMobileSafe();
    }}, {{ passive: false }});

    document.body.addEventListener("pointerdown", () => {{ unlockAudio(); }}, {{ once: true, passive: true }});
    window.addEventListener("resize", () => requestAnimationFrame(layoutGongs));
    document.fonts && document.fonts.ready && document.fonts.ready.then(layoutGongs);
    layoutGongs();
}})();
</script>
</body>
</html>
"""

components.html(html, height=920, scrolling=False)
