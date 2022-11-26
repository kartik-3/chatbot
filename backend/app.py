from flask import Flask, jsonify, request, make_response
import urllib
import json
import config
import os 
app = Flask(__name__)

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/query', methods = ['GET','OPTIONS'])
def query():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    URL_solr = config.read()['URL_solr']
    CORE_NAME = config.read()['CORE_NAME']
    topics = config.read()['topics']
    js=request.get_json()
    qtext = str(js['text'])
    query_params = [
        'q.op=OR',
        'defType=dismax',
        'fl=*,score',
        'rows=20',
        'qf=parent_body',
        # f"fq=topic:{' '.join(config.get_topics())}"
    ]
    qtext = urllib.parse.quote(qtext)
    query = "&".join([qtext]+query_params)
    query = f'{URL_solr}{CORE_NAME}/query?q={query}'

    page = urllib.request.urlopen(query)
    docs = json.load(page)['response']['docs']

    response = {
        "response": docs[0]['body'] if docs else "No results found"
    }
    return _corsify(jsonify(response))

@app.route('/filter_toggle', methods = ['POST','OPTIONS'])
def toggle_topics():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    js=request.get_json()
    topic = str(js['text'])
    return _corsify(jsonify(config.toggle(topic)))

if __name__ == "__main__":
    if os.path.exists('./backend'): os.chdir('./backend')
    app.run(host="0.0.0.0", port=9999)