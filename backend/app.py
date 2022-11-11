from flask import Flask, jsonify, request,send_file
import urllib
from config import URL_solr,CORE_NAME
import json

app = Flask(__name__)
@app.route('/query', methods = ['GET'])
def query():
    js=request.get_json()
    qtext = str(js['text'])
    query_params = [
        'q.op=OR',
        'defType=dismax',
        'fl=*,score',
        'rows=20',
        'qf=parent_body']

    qtext = urllib.parse.quote(qtext)
    query = "&".join([qtext]+query_params)
    query = f'{URL_solr}{CORE_NAME}/query?q={query}'

    resp = urllib.request.urlopen(query)
    docs = json.load(resp)['response']['docs']

    response = {
        "response": docs[0]['body'],
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)