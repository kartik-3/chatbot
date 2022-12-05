from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import urllib
import json
import config
import os 
app = Flask(__name__)
CORS(app)

@app.route('/query', methods = ['POST'])
def query():
    URL_solr = config.read()['URL_solr']
    CORE_NAME = config.read()['CORE_NAME']
    js=request.get_json()
    qtext = str(js['text'])
    query = create_query(qtext)
    query = f'{URL_solr}{CORE_NAME}/query?q={query}'

    page = urllib.request.urlopen(query)
    docs = json.load(page)['response']['docs']

    response = {
        "response": docs[0]['body'] if docs else "No results found"
    }
    return jsonify(response)

@app.route('/filter_topics', methods = ['POST'])
def filter_topics():
    js=request.get_json()
    topics = js['topics']

    #validate
    if not list(topics.keys()) == ['education','environment','healthcare','politics','technology']:
        return "Invalid config"
    return jsonify(config.set_topics(topics))

def create_query(qtext):
    topics = ['chitchat'] + config.get_topics()
    fq = "%20OR%20".join(map(lambda x: f'topic:{x}',topics))
    query_params = [
        'q.op=OR',
        'defType=dismax',
        'fl=*,score',
        'rows=200',
        'qf=parent_body',
        f'fq={fq}'
    ]
    qtext = urllib.parse.quote(qtext)
    query = "&".join([qtext]+query_params)
    return query

if __name__ == "__main__":
    if os.path.exists('./backend'): os.chdir('./backend')
    app.run(host="0.0.0.0", port=9999)