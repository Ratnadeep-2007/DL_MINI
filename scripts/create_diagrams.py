"""Create the two presentation images using Pillow (already a dependency)."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUTPUT = Path(__file__).resolve().parents[1] / "docs"
OUTPUT.mkdir(exist_ok=True)
INK = "#142D46"
MUTED = "#50657A"
BLUE = "#1768AC"
TEAL = "#087F83"


def font(size, bold=False):
    name = "calibrib.ttf" if bold else "calibri.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.truetype("DejaVuSans.ttf", size)


def page(number, title, subtitle):
    image = Image.new("RGB", (2400, 1350), "#F3F6FA")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 2400, 16), fill=TEAL)
    draw.text((90, 58), "DIGIT RECOGNITION  /  " + number, font=font(27, True), fill=TEAL)
    draw.text((90, 105), title, font=font(66, True), fill=INK)
    draw.text((92, 190), subtitle, font=font(32), fill=MUTED)
    draw.line((90, 1265, 2310, 1265), fill="#CFD9E3", width=2)
    draw.text((90, 1283), "Based on Digit Recognition by HelixCipher | Modified project | CC BY 4.0", font=font(24), fill=MUTED)
    draw.text((1935, 1283), "PYTHON + KERAS", font=font(24, True), fill=TEAL)
    return image, draw


def card(draw, box, title, lines, accent=BLUE, size=30):
    x, y, right, bottom = box
    draw.rounded_rectangle(box, radius=20, fill="white", outline="#D6E0E9", width=2)
    draw.rounded_rectangle((x, y, x + 9, bottom), radius=4, fill=accent)
    draw.text((x + 27, y + 24), title, font=font(34, True), fill=accent)
    for index, line in enumerate(lines):
        draw.text((x + 27, y + 80 + index * 43), line, font=font(size), fill=INK)


def arrow(draw, start, end, color=TEAL):
    draw.line((start, end), fill=color, width=5)
    x, y = end
    if abs(end[0] - start[0]) > abs(end[1] - start[1]):
        draw.polygon([(x, y), (x - 16, y - 10), (x - 16, y + 10)], fill=color)
    else:
        draw.polygon([(x, y), (x - 10, y - 16), (x + 10, y - 16)], fill=color)


image, draw = page("01", "Understand the project", "A small web app that learns digit shapes and predicts one handwritten number from 0 to 9.")
cards = [
    ("01  app.py", ["The Streamlit interface", "Draw on a 280 x 280 canvas", "or upload a PNG / JPG image."]),
    ("02  preprocessing.py", ["Make inputs resemble MNIST", "Grayscale, detect background,", "crop, resize and center the ink."]),
    ("03  model.keras", ["The saved, trained CNN", "Takes a 28 x 28 grayscale image", "and returns 10 probabilities."]),
    ("04  training.py", ["Teaches the CNN using MNIST", "Augments training images and", "saves the best validation weights."]),
    ("05  MNIST dataset", ["60,000 development images:", "55,000 training + 5,000 validation", "10,000 separate test images."]),
    ("06  Run the project", ["requirements.txt: dependencies", "start.bat: Windows app launcher", "docs/: these two diagrams"]),
]
for index, (title, lines) in enumerate(cards):
    x = 90 + (index % 3) * 750
    y = 285 + (index // 3) * 310
    card(draw, (x, y, x + 720, y + 275), title, lines, TEAL if index in (1, 4) else BLUE)
draw.text((95, 937), "THE MAIN IDEA", font=font(28, True), fill=TEAL)
for index, label in enumerate(["Your digit", "Prepare image", "CNN model", "Prediction 0-9"]):
    x = 90 + index * 565
    draw.rounded_rectangle((x, 1000, x + 480, 1110), radius=18, fill=INK)
    draw.text((x + 36, 1030), label, font=font(38, True), fill="white")
    if index < 3:
        arrow(draw, (x + 495, 1055), (x + 550, 1055))
draw.text((95, 1160), "Training happens separately. The app loads the saved model and only runs predictions.", font=font(34), fill=MUTED)
image.save(OUTPUT / "01_project_overview.png")

image, draw = page("02", "System architecture & data flow", "Two connected paths: learn the model once, then use it to recognize new handwritten digits.")
draw.text((90, 265), "A  /  OFFLINE TRAINING  -  training.py", font=font(29, True), fill=BLUE)
training_cards = [
    ("MNIST", ["60,000 development", "10,000 test images"]),
    ("Prepare + split", ["Normalize to [0, 1]", "55k train / 5k valid"]),
    ("Train CNN", ["Augment training only", "Adam + cross-entropy"]),
    ("Select + evaluate", ["Best validation loss", "Final test evaluation"]),
    ("model.keras", ["Save learned weights", "Load once in the app"]),
]
for index, (title, lines) in enumerate(training_cards):
    x = 90 + index * 450
    card(draw, (x, 320, x + 420, 510), title, lines, BLUE, 28)
    if index < 4:
        arrow(draw, (x + 424, 415), (x + 446, 415), BLUE)

draw.text((90, 565), "B  /  LIVE PREDICTION  -  app.py + preprocessing.py", font=font(29, True), fill=TEAL)
prediction_cards = [
    ("User input", ["Streamlit draw canvas", "or PNG / JPG upload"]),
    ("Prepare digit", ["Gray + auto-invert", "Crop + fit in 20 x 20", "Center in 28 x 28"]),
    ("Input tensor", ["Divide pixels by 255", "Shape: (1, 28, 28, 1)", "Values: [0, 1]"]),
    ("CNN inference", ["Use saved weights", "10 softmax outputs", "No training here"]),
    ("Display result", ["Highest score: digit", "Top 3 probabilities", "Prepared image preview"]),
]
for index, (title, lines) in enumerate(prediction_cards):
    x = 90 + index * 450
    card(draw, (x, 620, x + 420, 850), title, lines, TEAL, 28)
    if index < 4:
        arrow(draw, (x + 424, 730), (x + 446, 730))
# Connect the saved artifact to inference without crossing the prediction boxes.
draw.line([(2100, 510), (2100, 550), (1650, 550), (1650, 605)], fill=BLUE, width=4)
arrow(draw, (1650, 590), (1650, 615), BLUE)

draw.text((90, 907), "INSIDE THE CNN  /  130,890 TRAINABLE PARAMETERS", font=font(29, True), fill=BLUE)
layers = [
    ("28 x 28 x 1", "Input image"),
    ("Conv 32 + Pool", "26x26x32 > 13x13x32"),
    ("Conv 64 + Pool", "11x11x64 > 5x5x64"),
    ("Conv 64", "3 x 3 x 64"),
    ("Flatten + Dense", "576 > 128 / ReLU"),
    ("Softmax 10", "Digits 0 to 9"),
]
for index, (title, detail) in enumerate(layers):
    x = 90 + index * 375
    draw.rounded_rectangle((x, 970, x + 345, 1090), radius=16, fill=INK)
    draw.text((x + 18, 990), title, font=font(28, True), fill="white")
    draw.text((x + 18, 1040), detail, font=font(23), fill="#CFDFEF")
    if index < 5:
        arrow(draw, (x + 349, 1030), (x + 371, 1030))
draw.text((95, 1132), "All convolutions: 3 x 3, ReLU  |  Pooling: 2 x 2  |  Dropout: 0.3 after Dense 128 during training", font=font(29), fill=MUTED)
draw.text((95, 1180), "Probabilities are model scores; real-world accuracy depends on the handwriting and image quality.", font=font(29), fill=MUTED)
image.save(OUTPUT / "02_architecture_dataflow.png")
print("Created both diagrams in", OUTPUT)
