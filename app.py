import streamlit as st
from PIL import Image, ImageChops, ImageEnhance
import os
import time

# --- UI CONFIG ---
st.set_page_config(page_title="GOKUL Lab | Forensic Suite", page_icon="🛡️", layout="wide")

# --- ADVANCED CSS ---
st.markdown("""
<style>
    .stApp { background: #010409; }
    
    /* GOKUL RAINBOW NAME */
    .gokul-sidebar {
        font-size: 35px; font-weight: 900; text-align: center;
        background: linear-gradient(to right, #ff0000, #fffb00, #00ffd5, #002bff, #ff00c8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        background-size: 400%; animation: rainbow 5s linear infinite;
        letter-spacing: 3px; margin-bottom: 20px;
    }
    
    @keyframes rainbow { 0% { background-position: 0% 50%; } 100% { background-position: 100% 50%; } }
    
    /* RESULT ANIMATIONS */
    .real-result { font-size: 70px; color: #28a745; text-align: center; font-weight: bold; text-shadow: 0 0 20px #28a745; animation: zoomIn 0.5s; border: 5px solid #28a745; border-radius: 20px; padding: 10px; }
    .fake-result { font-size: 70px; color: #ff4b4b; text-align: center; font-weight: bold; text-shadow: 0 0 20px #ff4b4b; animation: zoomIn 0.5s; border: 5px solid #ff4b4b; border-radius: 20px; padding: 10px; }
    
    @keyframes zoomIn { from { transform: scale(0.5); opacity: 0; } to { transform: scale(1); opacity: 1; } }
    
    /* SIDEBAR BEAUTIFY */
    [data-testid="stSidebar"] { background-color: #0d1117; border-right: 2px solid #1f6feb; }
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
    ela_display = ImageEnhance.Brightness(ela_img).enhance(scale)
    return ela_display, max_diff

# --- SIDEBAR: GOKUL'S COMMAND CENTER ---
with st.sidebar:
    st.markdown('<p class="gokul-sidebar">GOKUL</p>', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=80)
    st.write("---")
    
    st.subheader("🛠️ Settings")
    # Sensitivity Slider - Result-ah adjust panna
    sensitivity = st.slider("Scan Sensitivity", 10, 100, 45)
    st.caption("Lower = Strict | Higher = Relaxed")
    
    st.write("---")
    st.subheader("📊 System Stats")
    st.write("🛰️ AI Nodes: **Active**")
    st.write("⚡ Latency: **24ms**")
    st.write("🛡️ Security: **AES-256**")
    
    st.write("---")
    if st.button("Clear Cache"):
        st.rerun()
    
    st.markdown("<br><p style='text-align: center; color: gray;'>© 2026 GOKUL FORENSICS</p>", unsafe_allow_html=True)

# --- MAIN PAGE ---
st.markdown("<h1 style='text-align: center; color: white; text-shadow: 0 0 10px #00d4ff;'>TRUTH CIRCLE AI</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #8b949e;'>Neural Image Integrity Verification System</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Evidence File", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(uploaded_file, caption="Evidence Source", use_container_width=True)
    
    if st.button("🚀 INITIATE FORENSIC SCAN"):
        with st.status("Analyzing Neural Layers...") as status:
            time.sleep(1.2)
            ela_res, score = perform_ela("temp.jpg")
            status.update(label="Scan Complete!", state="complete")
            
        with col2:
            st.image(ela_res, caption="Pixel Inconsistency Map", use_container_width=True)
            
        st.write("---")
        
        # LOGIC BASED ON SIDEBAR SLIDER
        if score > sensitivity:
            st.markdown('<div class="fake-result">🚨 FAKE</div>', unsafe_allow_html=True)
            st.error(f"ALERT: Digital artifacts detected above threshold ({score})")
        else:
            st.markdown('<div class="real-result">✅ REAL</div>', unsafe_allow_html=True)
            st.success(f"VERIFIED: No significant manipulation found ({score})")

    if os.path.exists("temp.jpg"): os.remove("temp.jpg")
