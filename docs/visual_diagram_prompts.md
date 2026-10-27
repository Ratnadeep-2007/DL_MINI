# Image generation prompts

Created with the built-in ImageGen tool. The two final PNGs are in this directory.
The prediction bars and learning curves are illustrative, not measured results.

## Project overview

Use case: infographic-diagram.
Create ONE exceptionally polished professional landscape 16:9 educational infographic, 3840x2160 if possible, for a university handwritten digit recognition project. This is image 1 of a matched pair. It should feel like a premium keynote slide designed by a top information designer: deep midnight navy background, crisp off-white typography, electric cyan connectors, restrained orange TensorFlow accent, subtle fine technical grid, dimensional illustrative visuals, generous spacing. Clear, large, perfectly readable text. No clutter, no gibberish, no invented metrics.

Title: "Handwritten Digit Recognition"
Subtitle: "Project overview • From a handwritten number to a prediction"
Small badge: "01 / UNDERSTAND THE PROJECT"

Strong central left-to-right visual story with five clearly connected numbered stages:
1 "DRAW OR UPLOAD" — large beautiful browser/canvas illustration with a handwritten black 7 on white, cursor or stylus and small upload icon. Caption "Streamlit interface • app.py". Include recognizable Streamlit red crown logo.
2 "PREPARE THE IMAGE" — illustrated progression from off-center digit on white to tight crop to centered luminous white 7 on a dark pixel grid. Caption "Grayscale • Auto-invert • Crop • Center". Small file label "preprocessing.py". Micro-label "28 × 28 grayscale".
3 "RECOGNIZE THE DIGIT" — expressive elegant layered convolutional neural network visualization, translucent stacked feature-map planes and neural connections, small recognizable TensorFlow orange logo and Keras red square K logo. Caption "Saved CNN • model.keras".
4 "SHOW THE RESULT" — clean small output visualization with giant "7" and bars labeled "7", "2", "9". No percentage values; label "Illustrative prediction". Caption "Predicted digit + top 3 scores". No invented numerical scores.
Arrange these four stages beautifully across the middle; exactly four stages, numbered 1 through 4.

Lower third: visually distinct three-panel explanatory strip titled "WHAT POWERS IT?"
Panel "TRAINING" with small MNIST digit mosaic showing handwritten numbers 0–9 and a code file icon; copy "training.py", "55,000 train • 5,000 validation", "10,000 separate test images". 
Panel "TECHNOLOGY" with accurately recognizable Python blue/yellow snakes logo, Streamlit red crown mark, TensorFlow orange TF logo, Keras red square K logo, and NumPy blue cube logo, each with matching name. Avoid any logos of technologies outside this project.
Panel "RUN LOCALLY" with simple terminal illustration and copy "start.bat", "Python + Streamlit", "Draw one digit or upload an image".

Footer tiny but readable: "Training happens separately. The app loads a saved model to make predictions."
Attribution in small bottom margin: "Based on Digit Recognition by HelixCipher • Modified project • CC BY 4.0"
Keep science correct: single digit classification only, not OCR text recognition. Do not claim measured accuracy or retraining. Use technical illustration, authentic recognizable logos, and strong hierarchy to make this visually stunning and presentation-ready. No external slide border, no watermark.

## Architecture and data flow

Use case: scientific-educational infographic-diagram.
Create ONE stunning professional landscape 16:9 presentation infographic, 3840x2160 if possible, for a real handwritten single-digit recognition Python project. Image 2 in a matched premium keynote pair. Deep midnight navy background, delicate blueprint grid, bright cyan illuminated connectors, white readable type, orange TensorFlow accents, red Keras and Streamlit logos, dimensional translucent CNN feature-map illustrations. Exceptional information design, elegant spacing, exact clear labels. Large readable text, no clutter.

Title "Architecture & Data Flow"
Subtitle "Train offline. Recognize digits in real time."
Badge upper right "02 / SYSTEM ARCHITECTURE"

Three clearly separated horizontal sections, accurately connected directed arrows.

TOP SECTION "A / OFFLINE TRAINING" with orange accent.
Five left-to-right modules:
1 database cylinder plus tiny handwritten digit mosaic. Title "MNIST". Text "60,000 development images", "10,000 held-out test images".
2 split/branch icon. Title "Prepare & split". Text "Normalize to [0, 1]", "55,000 train / 5,000 validation".
3 small neural-network graphic and recognizable orange TensorFlow logo plus red Keras K logo. Title "Train CNN". Text "Augment training only", "Adam + cross-entropy".
4 checkpoint / tuning icon. Title "Select & evaluate". Text "Best validation loss", "Reduce learning rate", "Final test evaluation".
5 file/cube artifact icon. Title "model.keras". Text "Saved model".
Arrows connect 1 > 2 > 3 > 4 > 5. Arrow down from saved model to live CNN inference module only. Training path depicts updated training.py, not a claim retraining was performed.

MIDDLE SECTION "B / LIVE PREDICTION" with cyan accent.
Five equally spaced left-to-right modules with elegant visual miniatures:
1 "Draw / upload", browser with stylus, black handwritten 7 on white canvas and upload icon, recognizable red Streamlit logo. Caption "app.py".
2 "Preprocess", illustrated transition of digit crop becoming a centered white digit on black. Caption "Grayscale • Auto-invert", "Crop • Resize • Center", "preprocessing.py".
3 "Input tensor", clearly illustrated pixel grid. Caption "28 × 28 × 1", "Normalize to [0, 1]", "Batch: (1, 28, 28, 1)".
4 "CNN inference", beautiful layered glowing feature maps with small TensorFlow and Keras logos. Caption "Load saved weights", "10 softmax scores".
5 "Prediction", large glowing digit 7 and three small score bars with labels 7, 2, 9 without percentage values. Caption "Digit + top 3 scores", "Illustrative output".
Clear arrows connecting every middle stage left-to-right. Keep training and inference distinct.

BOTTOM SECTION "C / INSIDE THE CNN" with slim connected architecture graphic.
Six blocks in exact order, with intermediate tensor shapes clearly printed:
"Input" / "28 × 28 × 1"
"Conv 32 + Pool" / "26×26×32 → 13×13×32"
"Conv 64 + Pool" / "11×11×64 → 5×5×64"
"Conv 64" / "3 × 3 × 64"
"Flatten + Dense" / "576 → 128"
"Softmax" / "10 classes: 0–9"
Use actual stacked feature-map planes for convolution blocks, network nodes for dense layer, small ten output nodes for softmax. This should visually explain architecture, not just boxes.
Fine line beneath: "3×3 convolutions + ReLU  •  2×2 max pooling  •  Dropout 0.3 after Dense 128 during training"
Small footer "130,890 trainable parameters  |  Python • Streamlit • TensorFlow • Keras • NumPy • Pillow"
Attribution bottom margin: "Based on Digit Recognition by HelixCipher • Modified project • CC BY 4.0"

Constraints: no accuracy percentage, no claims of measured improvement, no invented project components, no cloud deployment, no transformer or LLM. All arrows technically correct. No extra software logos. All text perfectly spelled. This is an impressive polished university presentation architecture infographic, technical and visually rich.

## Architecture correction

Edit this architecture infographic. Preserve the entire design, layout, all existing text, logos, colors, typography, dimensions, all illustrations and all other connectors exactly. Correct ONLY the saved-model connector: the arrow currently descends vertically from the top-row "model.keras" artifact into the middle-row "Prediction" output panel. That is technically incorrect. Remove that connector and replace it with a clean cyan elbow connector that leaves the bottom of "model.keras", turns left within the open gap between rows A and B, and then points DOWN into the top of the "CNN inference" panel (the fourth module in row B, horizontally near 68% image width). Its arrowhead must terminate at the top edge of CNN inference, never at Prediction. No crossing any text. The horizontal connector from CNN inference to Prediction remains unchanged. Also in the tiny bottom right Softmax node illustration ensure class labels are in order 0,1,2,3,4,5,6,7,8,9, with no duplicate 7; otherwise preserve that illustration. Do not alter any other part of the infographic.

