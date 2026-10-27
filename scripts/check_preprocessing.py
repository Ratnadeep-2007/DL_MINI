"""Check input handling and run the saved CNN on a synthetic stroke."""

from pathlib import Path
import os
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np
from PIL import Image, ImageDraw, ImageOps
from preprocessing import prepare_digit


def stroke(position=(20, 30), scale=1):
    image = Image.new("L", (280, 280), "white")
    x, y = position
    ImageDraw.Draw(image).rectangle((x, y, x + 8 * scale - 1, y + 60 * scale - 1), fill=0)
    return image


reference = prepare_digit(stroke())
assert reference.shape == (28, 28) and reference.dtype == np.uint8
assert np.array_equal(reference, prepare_digit(stroke((140, 150))))
assert np.array_equal(reference, prepare_digit(ImageOps.invert(stroke())))

# Transparent PNGs must have the same result as a white background.
transparent = Image.new("RGBA", (280, 280), (0, 0, 0, 0))
ImageDraw.Draw(transparent).rectangle((20, 30, 27, 89), fill=(0, 0, 0, 255))
assert np.array_equal(reference, prepare_digit(transparent))
for color in ("white", "black", "gray"):
    assert prepare_digit(Image.new("L", (280, 280), color)) is None
assert prepare_digit(Image.new("RGBA", (40, 40), (0, 0, 0, 0))) is None

# A small source digit must be enlarged, not left tiny inside the 28x28 image.
small = Image.new("L", (40, 40), "white")
ImageDraw.Draw(small).rectangle((2, 2, 4, 7), fill=0)
small_digit = prepare_digit(small)
assert Image.fromarray(small_digit).getbbox()[3] - Image.fromarray(small_digit).getbbox()[1] == 20
rows, columns = np.indices(reference.shape)
assert abs((columns * reference).sum() / reference.sum() - 13.5) <= 0.5
assert abs((rows * reference).sum() / reference.sum() - 13.5) <= 0.5
print("Preprocessing checks passed: position, polarity, transparency, blanks, size, centering.")

import tensorflow as tf
model = tf.keras.models.load_model(ROOT / "model.keras")
batch = reference.reshape(1, 28, 28, 1).astype("float32") / 255
probabilities = model(batch, training=False).numpy()[0]
assert probabilities.shape == (10,) and np.isfinite(probabilities).all()
assert np.isclose(probabilities.sum(), 1, atol=1e-5)
print("Saved-model inference passed: 10 finite probabilities that sum to 1.")
print("These synthetic checks do not measure handwriting recognition accuracy.")
