"""
_summary_

:return: _description_
:rtype: _type_

"routes": [{"src": "/(.*)", "dest": "app.py"}]
"""

from sanic import Sanic
from sanic.response import json

app = Sanic(name=__name__)


@app.route('/', name='root')
@app.route('/<path:path>', name='test')
async def index(request, path=""):
    """
    _summary_

    :param request: _description_
    :type request: _type_
    :param path: _description_, defaults to ""
    :type path: str, optional
    :return: _description_
    :rtype: _type_
    """
    return json({'hello': path})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
