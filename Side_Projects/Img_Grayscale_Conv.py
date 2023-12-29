"""
Build a web app capable of taking photos
and converting them to grayscale
"""

import streamlit as st
from PIL import Image

with st.expander("Start Camera"):

    # Start the Camera
    camera_image = st.camera_input("Camera")

    if camera_image:
        # Create a pillow image instance
        img = Image.open(camera_image)

        # Convert the pillow image to the grayscale
        gray_img = img.convert("L")

        # Render the grayscale image on the webpage
        st.image(gray_img)

