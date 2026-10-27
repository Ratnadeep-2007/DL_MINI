import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas
from preprocessing import prepare_digit


# Configure TensorFlow.
gpus = tf.config.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)
device_info = f"GPU: {len(gpus)} detected" if gpus else "Running on CPU"


@st.cache_resource
def load_model():
    return tf.keras.models.load_model('model.keras')


def show_prediction(image):
    """Use the same preprocessing and prediction for drawing and uploads."""
    digit = prepare_digit(image)
    if digit is None:
        st.info("Draw or upload one clear digit to get a prediction.")
        return

    st.write("### Model Input")
    st.image(digit, width=150, caption="Centered 28x28 digit")
    model_input = digit.reshape(1, 28, 28, 1).astype('float32') / 255.0
    probabilities = model.predict(model_input, verbose=0)[0]
    top3 = np.argsort(probabilities)[-3:][::-1]
    st.write(f"Predicted: {top3[0]}")
    for digit_number in top3:
        st.write(f"{digit_number}: {probabilities[digit_number] * 100:.1f}%")


model = load_model()
st.title("Digit Recognition")
st.caption(device_info)
st.write("Draw or upload a handwritten digit (0-9)")
tab1, tab2 = st.tabs(["Draw", "Upload Image"])

with tab1:
    col_canvas, col_result = st.columns(2)
    with col_canvas:
        canvas_result = st_canvas(
            fill_color="rgba(255, 255, 255, 1)",
            stroke_width=10,
            stroke_color="#000000",
            background_color="#FFFFFF",
            height=280,
            width=280,
            drawing_mode="freedraw",
            key="canvas"
        )
    with col_result:
        if (canvas_result is not None
                and canvas_result.image_data is not None
                and canvas_result.json_data
                and canvas_result.json_data.get("objects")):
            image = Image.fromarray(canvas_result.image_data.astype('uint8'))
            show_prediction(image)

with tab2:
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        col_input, col_result = st.columns(2)
        with col_input:
            st.write("### Input")
            st.image(image, width=200, caption="Input")
        with col_result:
            show_prediction(image)
