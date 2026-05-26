"""Yellow Pin Travel Website"""

import os
import json
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    """Home page"""

    return render_template('index.html')


@app.route("/about")
def about():
    """About page"""

    return render_template('about.html')


@app.route("/services")
def services():
    """Services page"""

    return render_template('services.html')


@app.route("/contact")
def contact():
    """Contact page"""

    return render_template('contact.html')


@app.route("/privacy")
def privacy():
    """Privacy page"""

    return render_template('privacy.html')


@app.route("/terms")
def terms():
    """Terms and conditions page"""

    return render_template('terms.html')


@app.route("/accessibility")
def accessability():
    """Accessibility page"""

    return render_template('accessibility.html')


@app.route("/picsapi")
def picsapi():
    """API route to send img file paths and names"""

    path = "static/images/rand_stock"
    file_list = os.listdir(path)
    
    path_list = []
    for file in file_list:
        path_list.append(os.path.join(path, file))

    json_list = json.dumps(path_list)

    return json_list

if __name__ == "__main__":
    app.run(debug=True)
