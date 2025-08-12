import streamlit as st
from PIL import Image, ImageEnhance

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)


st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")



with st.expander("Open lens"):
    camera_image = st.camera_input('Camera')


if camera_image:
    img = Image.open(camera_image)

    gray_img = img.convert("L")

    #st.image(gray_img)

    brightness_factor1 = st.slider("Brightness", 0.0, 2.0, 1.0, 0.1, key="slider1")

    adjusted_image1 = adjust_brightness(gray_img, brightness_factor1)
    st.image(adjusted_image1, caption=f"Adjusted Image (Brightness: {brightness_factor1})", use_container_width=True)

if uploaded_image:
    userimg =Image.open(uploaded_image)
    gray_userimg = userimg.convert("L")
    #st.image(gray_userimg)

    brightness_factor2 = st.slider("Brightness", 0.0, 2.0, 1.0, 0.1, key="slider2")

    adjusted_image2 = adjust_brightness(gray_userimg, brightness_factor2)
    st.image(adjusted_image2, caption=f"Adjusted Image (Brightness: {brightness_factor2})", use_container_width=True)