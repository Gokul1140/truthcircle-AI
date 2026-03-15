 import streamlit as st
from PIL import Image, ImageChops, ImageEnhance
import os
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="TruthCircle AI", page_icon="🛡️", layout="centered")

# --- NEON GLOW CSS ---
st.markdown("""
    <style>
    /* Main Background */
    .main { background: radial-gradient(circle, #020024 0%, #090979 35%, #00d4ff 100%); color: white; }
    
    /* Neon Title Glow */
    .glow-text {
        font-size: 45px;
        color: #fff;
        text-align: center;
        text-shadow: 0 0 10px #00d4ff, 0 0 20px #00d4ff, 0 0 40px #00d4ff;
        font-weight: bold;
        padding-bottom: 10px;
    }
    
    /* Box Styling */
    div.stButton > button {
        background: linear-gradient(45deg, #00d4ff, #0022ff);
        color: white;
        border: none;
        padding: 15px 32px;
        font-size: 20px;
        border-radius: 50px;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.6);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        box-shadow: 0 0 30px #00d4ff;
        transform: scale(1.05);
    }
    
    /* Image Border Glow */
    img {
        border-radius: 15px;
        border: 2px solid #00d4ff;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.4);
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
    ela_img = ImageEnhance.Brightness(ela_img).enhance(scale)
    return ela_img

# --- UI START ---
st.markdown('<p class="glow-text">TRUTH CIRCLE AI</p>', unsafe_allow_html=True)
st.write("### 🛡️ Next-Gen Forensic Image Analyzer")

uploaded_file = st.file_uploader("Drop your image to expose the truth...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("#### 📸 Input Image")
        st.image(uploaded_file, use_container_width=True)
    
    if st.button("🚀 INITIATE NEURAL SCAN"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Fake scanning effect for style
        for i in range(101):
            time.sleep(0.015)
            progress_bar.progress(i)
            status_text.text(f"Scanning Pixels: {i}%")
        
        ela_res = perform_ela("temp.jpg")
        
        with col2:
            st.write("#### 🧬 Forensic Heatmap")
            st.image(ela_res, use_container_width=True)
        
        st.markdown("---")
        st.subheader("📊 Analysis Result")
        
        # Calculate some 'fake' intensity for the heatmap to make it real
        extrema = ela_res.convert("L").getextrema()
        if extrema[1] > 50:
            st.error("⚠️ CRITICAL ALERT: Digital Manipulation Detected!")
            st.write("This image shows significant pixel inconsistencies in the highlighted areas.")
        else:
            st.success("✅ SCAN CLEAR: Image appears to be Authentic.")

    os.remove("temp.jpg")
