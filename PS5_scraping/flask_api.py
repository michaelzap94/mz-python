import flask
import logging
import asyncio
from flask import request, jsonify
from main import main
from constants import RETAILERS

app = flask.Flask(__name__)
app.config["DEBUG"] = True

try:
    loop = asyncio.get_event_loop()
except Exception as e:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# A route to return all of the available entries in our catalog.
@app.route('/api/ps5/all', methods=['GET'])
def api_all():
    app.logger.info('executing')
    retailers_info_list = main(loop)
    retailers_names = RETAILERS.keys()
    data_zip = zip(retailers_names, retailers_info_list)
    data = dict(data_zip)
    return jsonify(data)

app.run()