import streamlit as st
from PIL import Image, ImageChops, ImageEnhance
from PIL.ExifTags import TAGS
import os
import time
import pandas as pd

# --- CONFIG ---
st.set_page_config(page_title="GOKUL Lab | Forensic Suite", page_icon="🛡️", layout="wide")

# --- ADVANCED ANIMATED CSS ---
st.markdown("""
<style>
    .stApp { background: #010409; }
    
    /* GOKUL NAME GRADIENT */
    .gokul-header {
        font-size: 45px;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(to right, #ff0000, #fffb00, #00ffd5, #002bff, #ff00c8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 400%;
        animation: rainbow 5s linear infinite;
        letter-spacing: 4px;
    }

    /* RESULT ANIMATIONS */
    @keyframes zoomIn {
        from { transform: scale(0.5); opacity: 0; }
        to { transform: scale(1.2); opacity: 1; }
    }
    
    .real-result {
        font-size: 60px;
        color: #28a745;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 20px #28a745;
        animation: zoomIn 0.8s ease-out forwards;
        border: 4px solid #28a745;
        padding: 20px;
        border-radius: 15px;
    }

    .fake-result {
        font-size: 60px;
        color: #ff4b4b;
        font-weight: bold;
        text-align: center;
        text-shadow: 0 0 20px #ff4b4b;
        animation: zoomIn 0.8s ease-out forwards;
        border: 4px solid #ff4b4b;
        padding: 20px;
        border-radius: 15px;
    }

    @keyframes rainbow { 0% { background-position: 0% 50%; } 100% { background-position: 100% 50%; } }

    /* CARD BOX */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 212, 255, 0.2);
        padding: 25px;
        border-radius: 20px;
    }
</style>
""", unsafe_allow_html=True)

def perform_ela(img_path, quality=90):
    original = Image.open(img_path).convert('RGB')
    resaved_path = "resaved.jpg"
    original.save(resaved_path, 'JPEG', quality=quality)
    resaved = Image.open(resaved_path)
    ela_img = ImageChops.difference(original, resaved)
    extrema = ela_img.getextrema()
    max_diff = max([ex[1] for ex in extrema]) or 1
    scale = 255.0 / max_diff
    return ImageEnhance.Brightness(ela_img).enhance(scale), max_diff

# --- SIDEBAR ---
with st.sidebar:
    st.markdown('<p class="gokul-header">GOKUL</p>', unsafe_allow_html=True)
    st.info("🛰️ SYSTEM: ONLINE")
    st.write("---")
    st.write("Mode: **FORENSIC DEEP SCAN**")

# --- MAIN UI ---
st.markdown("<h1 style='text-align: center; color: white;'>TRUTH CIRCLE AI</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📷 SOURCE")
        st.image(uploaded_file, use_container_width=True)
    
    if st.button("🚀 START SCAN"):
        with st.status("🔍 Analyzing Pixels...") as status:
            time.sleep(1.5)
            ela_res, score = perform_ela("temp.jpg")
            status.update(label="Scanning Complete!", state="complete")
        
        with col2:
            st.markdown("### 🧬 HEATMAP")
            st.image(ela_res, use_container_width=True)
        
        st.write("---")
        
        # --- SIMPLE ANIMATED RESULT ---
        if score > 55:
            st.markdown('<div class="fake-result">🚨 FAKE</div>', unsafe_allow_html=True)
            st.error("Digital manipulation detected. This image is NOT authentic.")
        else:
            st.markdown('<div class="real-result">✅ REAL</div>', unsafe_allow_html=True)
            st.success("No artifacts found. This image is AUTHENTIC.")
            
    os.remove("temp.jpg")
