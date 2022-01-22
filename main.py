from scraper import Scraper
from flask import Flask, request, Response
import json

app = Flask(__name__)


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

        return Response(
            json.dumps({"code": series_pub_code}),
            status=200,
            mimetype="application/json",
        )

    except Exception as error:
        return Response(
            json.dumps({"error": error}),
            status=500,
            mimetype="application/json",
        )


app.run()
