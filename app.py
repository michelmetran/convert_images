"""
_summary_

:return: _description_
:rtype: _type_
"""


from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for
from PIL import Image

app = Flask(
    import_name=__name__,
    static_url_path='/static',
    static_folder="./templates/static",
)

print(app.static_folder)
print(app.static_url_path)


# Paths
project_path = Path(__file__).parent


@app.route('/')
def hello():
    """
    Renderiza o index.html

    :return: _description_
    """
    return render_template("index.html")


@app.route("/convert", methods=["POST", "GET"])
def convert():
    """
    Renderiza o Resto

    :return: _description_
    """
    if request.method == "POST":
        file = request.files["image"]
        format = request.form.get("format")

        #
        input_filename, x = file.filename.split('.')
        print(input_filename)
        format = format.lower()
        output_filename = f'{input_filename}.{format}'

        with Image.open(file) as image:
            file_path = Path(app.static_folder) / output_filename
            print(f'sssss {file_path}')

            # Convert
            image.convert('RGB').save(fp=file_path)

            # URL
            image_url = url_for('static', filename=output_filename)
            print(f'URL da imagem é {image_url}')            

        return render_template("convert.html", image_url=image_url)

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
