import json
import logging
import random
import uuid
from typing import Mapping, Any

import click
import flask
from capture0.config import CONFIG
from capture0.forms.home_form import home_form_instance_factory
from capture0.storage import store_data
from capture0_data.online_handles import get_companies

log = logging.getLogger(__name__)


app = flask.Flask(__name__)
app.secret_key = str(uuid.uuid1())


@app.route('/save/<string:dataset>', methods=["POST"])
def save(dataset: Mapping[str, Any]):
    log.info(flask.request.content_type)
    log.info(flask.request.data)
    data = json.loads(flask.request.data.decode("UTF-8"))

    store_data(dataset, data)

    return flask.make_response("OK")


def get_random_company_names():
    raw_companies = get_companies()
    random.shuffle(raw_companies)
    random_companies = raw_companies[:20]

    return [c.company for c in random_companies]

@app.route('/')
def home_page():
    company_names = get_random_company_names()
    form = home_form_instance_factory(company_names)
    return flask.render_template('index.html.j2', form=form)


@app.route('/<path:path>')
def static_content(path):
    log.info("Attempting to serve static content: %s" % path)
    return flask.send_from_directory(CONFIG["STATIC"], path)

@app.route('/companies')
def companies():
    companies = get_companies()
    return flask.jsonify([c.company for c in companies])


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
