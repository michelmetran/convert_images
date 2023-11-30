"""
_summary_

:return: _description_
:rtype: _type_
"""


import os
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for
from PIL import Image

app = Flask(__name__)


os.get_terminal_size()

# Paths
project_path = Path(__file__).parent
print(project_path)


# html = project_path /
# print(html.is_file())


@app.route('/')
def hello():
    return render_template("index.html")


@app.route("/convert", methods=["POST", "GET"])
def convert():
    if request.method == "POST":
        file = request.files["image"]
        format = request.form.get("format")

        #
        outputimage, x = file.filename.split('.')
        format = format.lower()
        outputimage = outputimage + "." + format

        with Image.open(file) as image:
            path = Path('static/images/') / outputimage
            image.convert('RGB').save(fp=path)

            # os.rename(outputimage, path)
            # filepath = 'images/' + outputimage
            image_url = url_for('static', filename=path)
            print(image_url)

        return render_template("convert.html", image_url=path)

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
