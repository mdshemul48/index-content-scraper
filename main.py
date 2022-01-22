from scraper import Scraper
from util import create_series_publish_table, create_game_publish_table

from flask import Flask, request, Response
from flask_cors import CORS

import json

app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return "hello world"


@app.route("/series")
def getSeriesCode():
    try:
        requestLink = request.args["reqLink"]
        scraper = Scraper(requestLink)
        scraper.fetch_folder_info()
        seriesInfo = scraper.fetch_folder_item()
        scraper.close()
        publish_code = create_series_publish_table(seriesInfo)
        return Response(
            json.dumps({"code": publish_code}),
            status=200,
            mimetype="application/json",
        )

    except Exception as error:
        return Response(
            json.dumps({"error": error}),
            status=500,
            mimetype="application/json",
        )


@app.route("/game")
def get_game_publish_code():
    try:
        requestLink = request.args["reqLink"]
        scraper = Scraper(requestLink)
        files = scraper.fetch_root_file()
        scraper.close()
        publish_code = create_game_publish_table(files)
        return Response(
            json.dumps({"code": publish_code}),
            status=200,
            mimetype="application/json",
        )

    except Exception as error:
        return Response(
            json.dumps({"error": error}),
            status=500,
            mimetype="application/json",
        )


app.run(host="0.0.0.0", port=5000, debug=True)
