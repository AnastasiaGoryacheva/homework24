import os

from flask import Flask, request, abort, Response

from utils import construct_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.post("/perform_query")
def perform_query() -> Response:
    try:
        cmd_1 = request.args["cmd_1"]
        value_1 = request.args["value_1"]
        cmd_2 = request.args["cmd_2"]
        value_2 = request.args["value_2"]
        file_name = request.args["file_name"]
    except Exception:
        abort(400, "Incorrect query")
    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        abort(400, "File not found")

    with open(file_path, encoding='utf-8') as file:
        result = construct_query(cmd_1, value_1, file)
        if cmd_2 and value_2:
            result = construct_query(cmd_2, value_2, result)

        result = "\n".join(result)

    return app.response_class(result, content_type="text/plain")


if __name__ == '__main__':
    app.run(debug=True)
