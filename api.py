from flask import Flask, jsonify, request
from keras.models import load_model
import numpy as np
import base64
import sys
from flask_cors import CORS
import cv2


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route('/predict', methods=['POST'])
def predict():
    if mnist:
        json = request.json
        image = json['image']
        jpeg_original = base64.b64decode(bytes(image.split(',')[1], "utf-8"))
        jpeg_as_np = np.frombuffer(jpeg_original, dtype=np.uint8)
        image = cv2.imdecode(jpeg_as_np, cv2.IMREAD_GRAYSCALE)
        cv2.imwrite('image_original.jpeg', image)
        image = cv2.resize(image, (28, 28), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite('image_resized.jpeg', image)
        image = cv2.bitwise_not(image)
        cv2.imwrite('image_inverted.jpeg', image)
        image = image.reshape(1, 28, 28, 1)
        image = image / 255.0
        print(image)
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

