
import streamlit as st
from PIL import Image
import pytesseract
import re
import io

st.set_page_config(page_title="eBay Auto Lister", layout="centered")

st.title("eBay Auto Listing Tool")
st.write("Upload an auto part photo to generate a draft eBay listing.")

uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # OCR
    from PIL import Image

# Convert Streamlit UploadedFile to PIL image
image_pil = Image.open(image).convert("RGB")  # Ensure it's in a supported mode
text = pytesseract.image_to_string(image_pil)
    st.subheader("Extracted Text")
    st.text(text)

    # Extract part number
    part_number_match = re.findall(r'\b\d{5}-\d{5}\b', text)
    part_number = part_number_match[0] if part_number_match else "N/A"
    brand = "Denso" if "DENSO" in text.upper() else "Unknown"
    voltage = "12V" if "12V" in text else "N/A"

    # Generate listing
    title = f"OEM {brand} Radiator Fan Control Module {part_number} Toyota 12V"
    description = f"This is a genuine {brand} fan control module, part number {part_number}, removed from a working vehicle. It's tested and in good working condition. Compatible with various Toyota models. 12V operation."

    st.subheader("Generated eBay Listing")
    st.text_area("Title", title)
    st.text_area("Description", description)
    st.text(f"Brand: {brand}")
    st.text(f"Part Number: {part_number}")
    st.text(f"Voltage: {voltage}")
    st.success("Copy this info to eBay or save for later.")
