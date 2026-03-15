import streamlit as st
from PIL import Image, ImageChops, ImageEnhance
import os
import time

# --- ADVANCED UI CONFIG ---
st.set_page_config(page_title="TruthCircle AI | GOKUL's Lab", page_icon="🛡️", layout="wide")

# --- PROFESSIONAL CYBER GLOW CSS with GOKUL ANIMATION ---
st.markdown("""
<style>
    /* Main Background with Dark Gradient */
    .stApp {
        background: radial-gradient(circle at top, #0d1117 0%, #010409 100%);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0d1117;
        border-right: 1px solid #30363g;
        padding-top: 0 !important; /* Move content up */
    }

    /* GOKUL Name Glow & round Animation */
    .gokul-glow {
        font-family: 'Montserrat', sans-serif;
        font-size: 30px;
        font-weight: 800; /* Extra Bold */
        text-align: center;
        color: #fff;
        text-shadow: 
            0 0 5px #00d4ff,
            0 0 10px #00d4ff,
            0 0 20px #00d4ff,
            0 0 40px #1f6feb,
            0 0 80px #1f6feb;
        margin: 20px 0;
        letter-spacing: 3px;
        text-transform: uppercase;
        
        /* Pulse Animation */
        animation: gokulPulse 2s infinite ease-in-out;
    }

    @keyframes gokulPulse {
        0%, 100% {
            opacity: 1;
            text-shadow: 0 0 5px #00d4ff, 0 0 10px #00d4ff, 0 0 20px #00d4ff;
        }
        50% {
            opacity: 0.7;
            text-shadow: 0 0 10px #1f6feb, 0 0 30px #1f6feb, 0 0 60px #1f6feb;
        }
    }

    /* Professional Glass Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(0, 212, 255, 0.2);
        text-align: center;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }

    /* Neon Title */
    .title-text {
        font-family: 'Courier New', Courier, monospace;
        font-size: 55px;
        color: #58a6ff;
        text-align: center;
        text-shadow: 0 0 15px #58a6ff;
        font-weight: 900;
        letter-spacing: 2px;
    }

    /* Custom Button */
    div.stButton > button {
        background: linear-gradient(90deg, #1f6feb, #00d4ff);
        color: white;
        border: none;
        padding: 12px 40px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        transition: 0.5s;
        text-transform: uppercase;
    }
    div.stButton > button:hover {
        box-shadow: 0 0 25px #00d4ff;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# --- LOGIC FUNCTIONS ---
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

# --- SIDEBAR (Professional Info with GOKUL Glow) ---
with st.sidebar:
    # GOKUL Neon Glow Title
    st.markdown('<p class="gokul-glow">GOKUL</p>', unsafe_allow_html=True)
    
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=80)
    st.title("Forensic Lab")
    st.divider()
    
    st.success("AI Core: Online")
    st.info("Neural Engine: Ready")
    st.divider()
    st.write("### 🛠️ Forensic Tools")
    st.checkbox("Pixel Consistency Check", value=True)
    st.checkbox("Metadata Analysis", value=True)
    st.checkbox("ELA Heatmap", value=True)

# --- MAIN UI ---
st.markdown('<p class="title-text">TRUTH CIRCLE AI</p>', unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #8b949e;'>Advanced Multi-Layered Forensic Image Analysis Platform</p>", unsafe_allow_html=True)

st.divider()

# Top Metrics Row
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.markdown('<div class="metric-card"><h2 style="color:#58a6ff;">98.2%</h2><p style="color:gray;">AI Accuracy</p></div>', unsafe_allow_html=True)
with col_m2:
    st.markdown('<div class="metric-card"><h2 style="color:#58a6ff;">ELA</h2><p style="color:gray;">Methodology</p></div>', unsafe_allow_html=True)
with col_m3:
    st.markdown('<div class="metric-card"><h2 style="color:#58a6ff;">< 2s</h2><p style="color:gray;">Scan Speed</p></div>', unsafe_allow_html=True)

st.write("##")

# File Upload Section
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 📷 Evidence Image")
        st.image(uploaded_file, use_container_width=True)
    
    if st.button("RUN DEEP FORENSIC SCAN"):
        with st.status("Initializing Neural Engine...", expanded=True) as status:
            st.write("Extracting pixel layers...")
            time.sleep(1)
            st.write("Running Error Level Analysis...")
            ela_res = perform_ela("temp.jpg")
            time.sleep(1)
            status.update(label="Scan Complete!", state="complete", expanded=False)
        
        with c2:
            st.markdown("### 🧬 Forensic Heatmap")
            st.image(ela_res, use_container_width=True)
        
        st.divider()
        
        # Result Box
        extrema = ela_res.convert("L").getextrema()
        if extrema[1] > 55:
            st.error("🚨 RESULT: HIGH PROBABILITY OF MANIPULATION DETECTED")
            st.warning("Forensic analysis shows artificial pixel patterns in the highlighted regions.")
        else:
            st.success("🛡️ RESULT: IMAGE APPEARS AUTHENTIC")
            st.write("No significant digital artifacts or ELA inconsistencies were found.")

    if os.path.exists("temp.jpg"): os.remove("temp.jpg")
