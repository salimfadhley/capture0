import click
import copy
import json
import logging
import os
import uuid
from flask import Flask, request, make_response
from typing import Mapping

log = logging.getLogger(__name__)

app = Flask(__name__)

SAVE_DIR = os.path.join(os.path.expanduser("~"), "capture0")


@app.route('/')
def hello_world():
    return 'Hello World!'


def store_data(dataset: str, record: Mapping):
    record = copy.copy(record)
    id = str(uuid.uuid1())
    dataset_dir = os.path.join(SAVE_DIR, dataset)
    record["uuid"] = id

    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    file_path = os.path.join(dataset_dir, "%s.json" % id)

    with open(file_path, "w") as output_file:
        output_file.write(json.dumps(record))
        log.info("Saved %s" % file_path)


@app.route('/save/<string:dataset>', methods=["POST"])
def save(dataset):
    log.info(request.content_type)
    log.info(request.data)
    data = json.loads(request.data.decode("UTF-8"))

    store_data(dataset, data)

    return make_response("OK")


@click.command()
@click.option("--port", default=59893, help="Which port should the server run on?")
@click.option("--host", default="0.0.0.0", help="Which interface should the server run on?")
def main(host, port):
    logging.basicConfig()
    logging.getLogger("").setLevel(logging.INFO)
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()
