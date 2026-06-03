from flask import Flask, render_template
from routes.item_routes import item_bp

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(item_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)