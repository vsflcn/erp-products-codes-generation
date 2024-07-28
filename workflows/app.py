from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

# Function to generate a unique product code
def generate_product_code(length=8):
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

# Route to generate a new product code
@app.route('/generate_code', methods=['GET'])
def generate_code():
    product_code = generate_product_code()
    return jsonify({"product_code": product_code})

# Route to generate multiple product codes
@app.route('/generate_codes', methods=['POST'])
def generate_codes():
    data = request.get_json()
    quantity = data.get('quantity', 1)
    codes = [generate_product_code() for _ in range(quantity)]
    return jsonify({"product_codes": codes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
