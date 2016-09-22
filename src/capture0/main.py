import json
import logging
from typing import Mapping, Any

import click
from capture0.config import CONFIG
from capture0.storage import store_data
from flask import Flask, request, make_response, send_from_directory

log = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/save/<string:dataset>', methods=["POST"])
def save(dataset: Mapping[str, Any]):
    log.info(request.content_type)
    log.info(request.data)
    data = json.loads(request.data.decode("UTF-8"))

    store_data(dataset, data)

    return make_response("OK")


@app.route('/')
def home_page():
    return send_from_directory(CONFIG["STATIC"], "index.html")


@app.route('/<path:path>')
def static_content(path):
    log.info("Attempting to serve static content: %s" % path)
    return send_from_directory(CONFIG["STATIC"], path)


@click.command()
@click.option("--port", default=59893, help="Which port should the server run on?")
@click.option("--host", default="0.0.0.0", help="Which interface should the server run on?")
@click.option("--static", default=CONFIG["STATIC"], help="Where will the static files be located")
def main(host, port, static):
    logging.basicConfig()
    logging.getLogger("").setLevel(logging.INFO)
    logging.info("Serving static content from %s" % static)
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()
