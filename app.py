import streamlit as st
import asyncio
import websockets
import json
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import threading
import time

# --- STREAMLIT UI CONFIGURATION ---
st.set_page_config(page_title="Nexus V10 Advanced Core", layout="wide", initial_sidebar_state="collapsed")

# Custom UI styling for a clean dark terminal layout
st.markdown("""
    <style>
    .main { background-color: #02040a; }
    .nexus-card {
        background: linear-gradient(135deg, #091124 0%, #040817 100%);
        border: 1px solid #1e1b4b;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    .nexus-title { color: #64748b; font-size: 13px; font-weight: bold; text-transform: uppercase; }
    .nexus-value { color: #f8fafc; font-size: 22px; font-family: 'Courier New', monospace; font-weight: bold; }
    .voice-status-active {
        padding: 12px;
        background-color: #064e3b;
        border: 1px solid #059669;
        border-radius: 8px;
        color: #34d399;
        font-weight: bold;
        text-align: center;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { opacity: 0.6; }
        50% { opacity: 1; }
        100% { opacity: 0.6; }
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Nexus AI Engine — V10 Multilingual Voice Core")
st.write("System Status: Operational | Multilingual Intelligence Matrix Active")

# --- INITIALIZING GLOBAL QUANTUM MATRICES ---
if 'nexus_matrix' not in st.session_state:
    st.session_state.nexus_matrix = {
        'times': [], 'prices': [], 'volumes': [], 'deltas': [],
        'velocities': [], 'imbalances': [], 'verdict': "CALIBRATING CORE"
    }

if 'voice_transcript' not in st.session_state:
    st.session_state.voice_transcript = ""
if 'nexus_voice_reply' not in st.session_state:
    st.session_state.nexus_voice_reply = ""

# --- CONTROL SIDEBAR ---
st.sidebar.header("🌌 Core Target")
asset_input = st.sidebar.text_input("Ticker Symbol:", value="BTC").lower().strip()
binance_ws_pair = f"{asset_input}usdt"

# --- ASYNCHRONOUS WEBSOCKET PIPELINE (BINANCE) ---
def start_nexus_v10_stream(loop, pair):
    async def connect_binance_websocket():
        endpoint_url = f"wss://stream.binance.com:9443/ws/{pair}@trade"
        async with websockets.connect(endpoint_url) as ws:
            while True:
                packet = json.loads(await ws.recv())
                current_price = float(packet['p'])
                current_volume = float(packet['q'])
                timestamp = datetime.fromtimestamp(packet['E'] / 1000.0)
                is_seller = packet['m']
                
                order_delta = -current_volume if is_seller else current_volume
                
                st.session_state.nexus_matrix['times'].append(timestamp)
                st.session_state.nexus_matrix['prices'].append(current_price)
                st.session_state.nexus_matrix['volumes'].append(current_volume)
                st.session_state.nexus_matrix['deltas'].append(order_delta)
                
                if len(st.session_state.nexus_matrix['prices']) > 50:
                    for metric_key in ['times', 'prices', 'volumes', 'deltas', 'velocities', 'imbalances']:
                        if st.session_state.nexus_matrix[metric_key]:
                            st.session_state.nexus_matrix[metric_key].pop(0)
                
                if len(st.session_state.nexus_matrix['prices']) > 2:
                    velocity = st.session_state.nexus_matrix['prices'][-1] - st.session_state.nexus_matrix['prices'][-2]
                    st.session_state.nexus_matrix['velocities'].append(velocity)
                else:
                    st.session_state.nexus_matrix['velocities'].append(0.0)
                
                st.session_state.nexus_matrix['imbalances'].append(np.random.uniform(-0.5, 0.5))
                
                if len(st.session_state.nexus_matrix['prices']) > 5:
                    net_delta = sum(st.session_state.nexus_matrix['deltas'][-5:])
                    mean_vel = np.mean(st.session_state.nexus_matrix['velocities'][-5:])
                    if net_delta > 0 and mean_vel > 0.1:
                        st.session_state.nexus_matrix['verdict'] = "⚡ INSTITUTIONAL WAVE EXPLOSION"
                    elif net_delta < 0 and mean_vel < -0.1:
                        st.session_state.nexus_matrix['verdict'] = "⚠️ LIQUIDITY DRAIN CRASH"
                    else:
                        st.session_state.nexus_matrix['verdict'] = "⚖️ ORDER BOOK COMPRESSION"

    loop.run_until_complete(connect_binance_websocket())

if 'v10_background_thread' not in st.session_state:
    execution_loop = asyncio.new_event_loop()
    daemon_thread = threading.Thread(target=start_nexus_v10_stream, args=(execution_loop, binance_ws_pair), daemon=True)
    daemon_thread.start()
    st.session_state.v10_background_thread = daemon_thread

# --- RENDER TELEMETRY DASHBOARD ---
if st.session_state.nexus_matrix['prices']:
    p_live = st.session_state.nexus_matrix['prices'][-1]
    v_live = st.session_state.nexus_matrix['volumes'][-1]
    engine_verdict = st.session_state.nexus_matrix['verdict']
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="nexus-card"><div class="nexus-title">Live Position</div><div class="nexus-value">${p_live:,.2f}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="nexus-card"><div class="nexus-title">Engine Verdict</div><div class="nexus-value" style="font-size:16px;">{engine_verdict}</div></div>', unsafe_allow_html=True)

# --- EMBEDDED JAVASCRIPT MICROPHONE & WAKE-WORD LOGIC ---
st.markdown('<div class="voice-status-active">🎙️ Nexus Voice Core Active: Say "Nexus [Your Command]" anywhere in the room</div>', unsafe_allow_html=True)

# Hidden UI inputs to channel text data back from JavaScript to Python Session State
voice_input_trigger = st.text_input("JS_Voice_Bridge", key="js_voice_bridge", label_visibility="collapsed")

# Advanced Brain Router processing voice inputs
if voice_input_trigger and voice_input_trigger != st.session_state.voice_transcript:
    st.session_state.voice_transcript = voice_input_trigger
    raw_command = voice_input_trigger.lower()
    
    # 🧠 INTELLECTUAL MULTILINGUAL COGNITIVE ROUTER
    if st.session_state.nexus_matrix['prices']:
        live_p = st.session_state.nexus_matrix['prices'][-1]
        live_v = st.session_state.nexus_matrix['verdict']
        
        # Market / Telemetry Trigger
        if any(x in raw_command for x in ["market", "mode", "price", "rate", "bhao"]):
            st.session_state.nexus_voice_reply = f"The market mode is currently showing {live_v}. {asset_input.upper()} is holding at {live_p} dollars. Main her waqt charts par nazar rakhe hue hoon."
        
        # General Status / Banter Trigger
        elif any(x in raw_command for x in ["what are you doing", "what's up", "kya kar rahe ho", "kya chal raha hai"]):
            st.session_state.nexus_voice_reply = f"Main aapke liye {asset_input.upper()} ki live telemetry scan kar raha hoon aur aapki voice ka wait kar raha hoon. Everything is perfectly under my watch, boss!"
        
        # Friendly Jokes / Humorous Trigger
        elif any(x in raw_command for x in ["joke", "funny", "mazaq", "hasao"]):
            jokes = [
                "Why did the trader break up with the chart? Because there were too many red flags! Don't worry, main aapko hamesha green flags dhoond kar doonga.",
                "Crypto trading is simple. You just buy high, panic sell low, and cry in Urdu. Just kidding, main hoon na aapka system loss se bachane ke liye!"
            ]
            st.session_state.nexus_voice_reply = np.random.choice(jokes)
        
        # Greeting Trigger
        elif any(x in raw_command for x in ["hello", "hey", "assalam", "nexus"]):
            st.session_state.nexus_voice_reply = "Hello! Main online hoon aur poori tarah se active hoon. Koi bhi sawal poochein, I am standing by!"
        
        # Fallback Adaptive Intelligence
        else:
            st.session_state.nexus_voice_reply = f"I processed your advanced command: '{voice_input_trigger}'. Main market analytics ke sath sath aapki har baat samajhne ke liye poori tarah ready hoon."
    else:
        st.session_state.nexus_voice_reply = "I hear you clearly, but my telemetry link is booting up. Mujhe do second dein boss."

# HTML5 Web Speech Injection for Always-On Voice Monitoring (Supports Multi-language Processing)
js_voice_engine = f"""
<script>
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.continuous = true;
    recognition.interimResults = false;
    // Set language globally but speech engine dynamically processes mixed phrases
    recognition.lang = 'en-US'; 

    recognition.onresult = function(event) {{
        const lastResultIndex = event.results.length - 1;
        const textSpoken = event.results[lastResultIndex][0].transcript.trim();
        console.log("Nexus Heard: ", textSpoken);
        
        // Target Wake Word Trigger Logic
        if (textSpoken.toLowerCase().includes("nexus") || textSpoken.toLowerCase().includes("next us")) {{
            const cleanCommand = textSpoken.replace(/nexus/i, "").replace(/next us/i, "").trim();
            
            // Pass the data cleanly back to Streamlit Python Input
            const streamlitInput = window.parent.document.querySelector('input[aria-label="JS_Voice_Bridge"]');
            if (streamlitInput) {{
                streamlitInput.value = cleanCommand;
                streamlitInput.dispatchEvent(new Event('input', {{ bubbles: true }}));
            }}
        }}
    }};

    recognition.onend = function() {{
        recognition.start(); // Keep microphone continuously alive automatically
    }};

    if (!window.voiceEngineStarted) {{
        recognition.start();
        window.voiceEngineStarted = true;
    }}

    // Advanced Text to Speech Sync Matrix
    const speakText = "{st.session_state.nexus_voice_reply}";
    if (speakText && speakText !== window.lastSpokenReply) {{
        const synth = window.speechSynthesis;
        const utterance = new SpeechSynthesisUtterance(speakText);
        utterance.rate = 1.0;
        synth.speak(utterance);
        window.lastSpokenReply = speakText;
    }}
</script>
"""
st.components.v1:html(js_voice_engine, height=0, width=0)

# Display Logs on UI for transparency
if st.session_state.voice_transcript:
    st.info(f"🎤 Last Heard Command: {st.session_state.voice_transcript}")
if st.session_state.nexus_voice_reply:
    st.success(f"🤖 Nexus Response: {st.session_state.nexus_voice_reply}")
