from flask import Flask, jsonify, request
from keras.models import load_model
from PIL import Image
import numpy as np
import base64
from io import BytesIO
import sys


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    if mnist:
        json = request.json
        image = Image.open(BytesIO(base64.b64decode(json['image'])))
        image = image.resize((28, 28))
        image = image.convert('L')
        image = np.array(image)
        image = image.reshape(1, 28, 28, 1)
        image /= 255.0
        response = mnist.predict([image])[0]
        digit, acc = np.argmax(response), max(response)
        return jsonify({'digit': str(digit), 'acc': str(acc)})


if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345

    mnist = load_model('mnist.h5')
    print("Model loaded")
    app.run(port=port, debug=True)

