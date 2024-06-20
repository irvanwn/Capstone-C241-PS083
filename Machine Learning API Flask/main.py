import os
import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
from werkzeug.utils import secure_filename
import io
from skin_conditions_data import skin_conditions

app = Flask(__name__)

# Load the models
disease_model = load_model(os.path.join(
    os.path.dirname(__file__), 'model/model-disease.h5'))
skin_type_model = load_model(os.path.join(
    os.path.dirname(__file__), 'model/model-skintype.h5'))

# Create a temporary directory for saving uploaded files
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the class labels for both models
disease_class_labels = ['Acne', 'Black Spots',
                        'Melasma', 'Puffy Eyes', 'Wrinkles']
skin_type_class_names = ['dry', 'normal', 'oily']


def prepare_skin_type_image(image, target):
    # Convert the image to RGB, resize and preprocess it
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    return image


@app.route('/', methods=['GET'])
def default():
    try:
        return jsonify({"status": "Service is online"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/predict', methods=['POST'])
def predict():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    # If the user does not select a file, the browser may submit an empty part without filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            # Process the image for disease prediction
            img = image.load_img(filepath, target_size=(150, 150))
            x = image.img_to_array(img)
            x /= 255
            x = np.expand_dims(x, axis=0)

            # Predict the disease class
            disease_prediction = disease_model.predict(x)
            disease_predicted_class = disease_class_labels[np.argmax(
                disease_prediction)]
            disease_confidence = float(np.max(disease_prediction))

            # Process the image for skin type prediction
            skin_type_image = load_img(filepath, target_size=(224, 224))
            processed_image = prepare_skin_type_image(
                skin_type_image, target=(224, 224))
            skin_type_prediction = skin_type_model.predict(processed_image)
            skin_type_predicted_class = skin_type_class_names[np.argmax(
                skin_type_prediction)]
            skin_type_confidence = float(np.max(skin_type_prediction))

            # Check if disease_predicted_class is in skin_conditions
            if disease_predicted_class in skin_conditions:
                condition_info = skin_conditions[disease_predicted_class]
                return jsonify({
                    "disease_prediction": {
                        "prediction": disease_predicted_class,
                        "confidence": disease_confidence
                    },
                    "skin_type_prediction": {
                        "prediction": skin_type_predicted_class,
                        "confidence": skin_type_confidence
                    },
                    "skin_condition_information": condition_info
                })

            return jsonify({
                "disease_prediction": {
                    "prediction": disease_predicted_class,
                    "confidence": disease_confidence
                },
                "skin_type_prediction": {
                    "prediction": skin_type_predicted_class,
                    "confidence": skin_type_confidence
                }
            })

        except Exception as e:
            return jsonify({"error": str(e)}), 500

        finally:
            # Clean up the uploaded file after prediction
            if os.path.exists(filepath):
                os.remove(filepath)

    return jsonify({"error": "Unexpected error occurred"}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
