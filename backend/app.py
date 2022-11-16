from flask import Flask, jsonify, request
import urllib
import json
import config

app = Flask(__name__)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)


@app.route('/query', methods = ['GET'])
def query():
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
        f"fq=topic:{' '.join(_get_topics())}"
    ]
    qtext = urllib.parse.quote(qtext)
    query = "&".join([qtext]+query_params)
    query = f'{URL_solr}{CORE_NAME}/query?q={query}'

    resp = urllib.request.urlopen(query)
    docs = json.load(resp)['response']['docs']

    response = {
        "response": docs[0]['body'],
    }
    return jsonify(response)


@app.route('/filter_toggle', methods = ['POST'])
def toggle_topics():
    js=request.get_json()
    topic = str(js['text'])
    return jsonify(config.toggle(topic))

def _get_topics():
    return [topic for topic,state in config.read()['topics'].items() if state]

