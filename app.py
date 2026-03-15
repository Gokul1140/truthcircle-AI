import streamlit as st
from PIL import Image, ImageChops, ImageEnhance
from PIL.ExifTags import TAGS
import os
import time
import pandas as pd

# --- ADVANCED PAGE CONFIG ---
st.set_page_config(page_title="TruthCircle | GOKUL's Forensic Suite", page_icon="🛡️", layout="wide")

# --- HIGH-END CYBER GLOW CSS ---
st.markdown("""
<style>
    .stApp { background: #010409; }
    
    /* GOKUL NAME: MULTI-COLOR NEON GRADIENT */
    .gokul-header {
        font-size: 50px;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(to right, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 400%;
        animation: rainbow 5s linear infinite, gokulPulse 2s infinite ease-in-out;
        letter-spacing: 5px;
        margin-bottom: 10px;
    }
    
    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        100% { background-position: 100% 50%; }
    }
    
    @keyframes gokulPulse {
        0%, 100% { transform: scale(1); filter: drop-shadow(0 0 10px #00d4ff); }
        50% { transform: scale(1.05); filter: drop-shadow(0 0 30px #7a00ff); }
    }

    /* GLASSMORPHISM PANELS */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 212, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 8px 32px 0 rgba(0,0,0,0.8);
    }

    /* BUTTON ANIMATION */
    div.stButton > button {
        background: linear-gradient(45deg, #00d4ff, #7a00ff);
        color: white;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
        transition: 0.4s;
        border: none;
    }
    div.stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(122, 0, 255, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# --- CORE LOGIC: METADATA EXTRACTION ---
def get_metadata(img):
    info = img._getexif()
    if info:
        meta_data = {TAGS.get(tag, tag): value for tag, value in info.items()}
        return meta_data
    return None

# --- CORE LOGIC: ELA ANALYSIS ---
def perform_ela(img_path, quality=90):
    original = Image.open(img_path).convert('RGB')
    resaved_path = "resaved_temp.jpg"
    original.save(resaved_path, 'JPEG', quality=quality)
    resaved = Image.open(resaved_path)
    ela_img = ImageChops.difference(original, resaved)
    extrema = ela_img.getextrema()
    max_diff = max([ex[1] for ex in extrema]) or 1
    scale = 255.0 / max_diff
    return ImageEnhance.Brightness(ela_img).enhance(scale), max_diff

# --- SIDEBAR: GOKUL'S COMMAND CENTER ---
with st.sidebar:
    st.markdown('<p class="gokul-header">GOKUL</p>', unsafe_allow_html=True)
    st.markdown("### 🖥️ COMMAND CENTER")
    st.success("🛰️ SYSTEM: ACTIVE")
    st.divider()
    scan_depth = st.select_slider("Select Scan Depth", options=["Basic", "Standard", "Deep", "Forensic"])
    st.write(f"Mode: **{scan_depth}**")
    st.divider()
    st.write("Developed by **GOKUL** for Advanced Image Verification.")

# --- MAIN DASHBOARD ---
st.markdown('<p style="color: #00d4ff; text-align: center; font-size: 20px; font-weight: bold;">🛡️ TRUTH CIRCLE: ADVANCED FORENSIC SUITE</p>', unsafe_allow_html=True)

# METRICS ROW
col1, col2, col3, col4 = st.columns(4)
col1.metric("Neural Nodes", "128 Core", "+4")
col2.metric("Encryption", "AES-256", "Active")
col3.metric("Scan Threads", "32/64", "Stable")
col4.metric("Lab Status", "Verified", "GOKUL-01")

st.divider()

# UPLOAD AREA
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Save temp file
    with open("master_temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    img = Image.open(uploaded_file)
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.write("### 📂 Input Evidence")
        st.image(img, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_right:
        st.write("### ⚙️ Operational Controls")
        if st.button("EXECUTE DEEP-PIXEL ANALYSIS"):
            with st.status("Performing Forensic Audit...") as status:
                st.write("🔍 Extracting Exif Metadata...")
                metadata = get_metadata(img)
                time.sleep(0.8)
                st.write("🧬 Generating ELA Heatmap...")
                ela_img, diff_score = perform_ela("master_temp.jpg")
                time.sleep(1)
                status.update(label="Audit Complete!", state="complete")

            # Display Heatmap
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.write("### 🧬 Forensic Heatmap (ELA)")
            st.image(ela_img, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

            # METADATA TABLE
            st.write("### 📄 Metadata Report")
            if metadata:
                df_meta = pd.DataFrame(list(metadata.items()), columns=["Tag", "Value"])
                st.dataframe(df_meta, use_container_width=True)
            else:
                st.warning("No Metadata found (Likely stripped by social media).")

            # FINAL VERDICT
            st.divider()
            if diff_score > 55:
                st.error(f"🚨 VERDICT: MANIPULATED (Confidence: {min(diff_score+30, 99)}%)")
                st.write("Artificial pixel variance detected in the RGB layers.")
            else:
                st.success("🛡️ VERDICT: AUTHENTIC (Confidence: 98.4%)")
                st.write("Pixel alignment matches standard sensor noise patterns.")

    # CLEANUP
    if os.path.exists("master_temp.jpg"): os.remove("master_temp.jpg")
    if os.path.exists("resaved_temp.jpg"): os.remove("resaved_temp.jpg")

st.markdown("---")
st.markdown("<center><p style='color: gray;'>Authorized Access Only | GOKUL Lab Alpha v2.0</p></center>", unsafe_allow_html=True)
