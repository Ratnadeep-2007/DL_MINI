"""Prepare a single handwritten digit to look like an MNIST image."""

import numpy as np
from PIL import Image, ImageOps


def prepare_digit(image):
    """Return a centered 28x28 image, or None when the image is blank."""
    # Composite transparent uploads onto white before converting to grayscale.
    image = image.convert("RGBA")
    background = Image.new("RGBA", image.size, "white")
    image = Image.alpha_composite(background, image).convert("L")
    pixels = np.array(image)
    if int(pixels.max()) - int(pixels.min()) < 30:
        return None

    # MNIST uses a light digit on black. Detect the background from the edges.
    border = np.concatenate((pixels[0], pixels[-1], pixels[:, 0], pixels[:, -1]))
    if border.mean() > 127:
        image = ImageOps.invert(image)
    image = ImageOps.autocontrast(image)

    # Remove empty margins and fit the digit into a 20x20 box, preserving shape.
    mask = image.point(lambda value: 255 if value > 30 else 0)
    bounds = mask.getbbox()
    if bounds is None:
        return None
    digit = image.crop(bounds)
    scale = 20 / max(digit.size)
    size = (max(1, round(digit.width * scale)), max(1, round(digit.height * scale)))
    digit = digit.resize(size, Image.Resampling.LANCZOS)
    canvas = Image.new("L", (28, 28), 0)
    canvas.paste(digit, ((28 - digit.width) // 2, (28 - digit.height) // 2))

    # Center the ink's mass, as in MNIST, rather than only its bounding box.
    pixels = np.array(canvas, dtype="float32")
    rows, columns = np.indices(pixels.shape)
    center_x = (columns * pixels).sum() / pixels.sum()
    center_y = (rows * pixels).sum() / pixels.sum()
    centered = Image.new("L", (28, 28), 0)
    centered.paste(canvas, (round(13.5 - center_x), round(13.5 - center_y)))
    return np.array(centered)
