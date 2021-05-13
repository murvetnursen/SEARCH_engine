from flask import Flask, render_template, jsonify
from flask import request
from utils import scrape_url, scrape_url2, semantik, recursive_scrapper

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def index():
   return render_template("index.html")


@app.route("/frekans", methods =["POST"])
def frekans():
    request_data = request.get_json()
    sorted_dict =scrape_url(request_data.get("url") )
    return sorted_dict

@app.route("/scoring")
def scoring():
    return render_template("scoring.html")

@app.route("/scoring2", methods =["POST"])
def scoring2():
    request_data = request.get_json()
    first_five_keyword =scrape_url2(request_data.get("url") )
    return first_five_keyword

@app.route("/indexing")
def indexing():
    return render_template("indexing.html")
"""
@app.route("/test")
def test():
    return jsonify(recursive_helper("https://tr.wikipedia.org/wiki/Aziz_Sancar" ))"""

@app.route("/derinlikliurl",methods = ["POST"])
def derinlikliurl():
    request_data = request.get_json()
    print(request_data.get("url_list"))
    recursive_response = recursive_scrapper(request_data.get("url_list"))
    return jsonify(recursive_response)

@app.route("/semantik")
def semantic():
    return render_template("semantik.html")

@app.route("/analiz", methods = ["POST"])
def analiz():
    request_data = request.get_json()
    first_url = request_data.get("first_url")
    second_url = request_data.get("second_url")
    return jsonify(semantik(first_url,second_url))

@app.route("/login")
def login():
    return render_template("login.html")

app.run(debug=True)

