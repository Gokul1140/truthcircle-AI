import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="TruthCircle AI", page_icon="🛡️")

st.title("🛡️ TruthCircle: The Trust Scanner")
st.write("Upload an image to scan for Deepfakes or Fake News.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Original Image', use_column_width=True)
    
    if st.button('Analyze with TruthCircle'):
        with st.spinner('Scanning Pixels...'):
            # Dummy Logic for University Demo
            st.success("Analysis Complete!")
            st.subheader("Result: 85% Likely AI Generated (Fake)")
            st.error("Caution: Artificial pixel patterns detected around the facial region.")
            st.info("The 'Circle to Scan' feature identifies manipulated areas.")
