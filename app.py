import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.title("Handwritten Digit Recognition")

model = load_model("mnist_digit_model.h5", compile=False)


canvas = st_canvas(
    fill_color="black",
    stroke_width=10,
    stroke_color="white",
    background_color="black",
    width=280,
    height=280,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("Predict"):
    if canvas.image_data is not None:
        img = canvas.image_data
        img = Image.fromarray(img.astype("uint8")).convert("L")
        img = img.resize((28, 28))
        img = np.array(img) / 255.0
        img = img.reshape(1, 28, 28, 1)

        prediction = model.predict(img)
        st.success(f"Predicted Digit: {np.argmax(prediction)}")
