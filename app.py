import streamlit as st
from PIL import Image
import pytesseract
import io

st.title("eBay Auto Lister - OCR Tool")

# Upload image file
uploaded_file = st.file_uploader("Upload an image of the part label", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        # Read file bytes and open as an image using PIL
        image_bytes = uploaded_file.read()
        image_pil = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # Show the uploaded image
        st.image(image_pil, caption="Uploaded Image", use_column_width=True)

        # Extract text using pytesseract
        text = pytesseract.image_to_string(image_pil)

        # Show the extracted text
        st.subheader("Extracted Text")
        st.text(text)

    except Exception as e:
        st.error(f"An error occurred: {e}")
