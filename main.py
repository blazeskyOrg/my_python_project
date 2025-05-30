# Import the Flask class
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Route for the root URL
@app.route("/", methods=["GET"])
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
