from flask import Flask, jsonify, request,send_file
import urllib
import json
from configparser import ConfigParser
import ast
  
configur = ConfigParser()
configur.read('config.ini')
# print ("Installation Library : ", ast.literal_eval(configur.get('tools','topic_dict')))
topic_dict = ast.literal_eval(configur.get('topic dictionary','topic_dict'))
print(topic_dict)
topic_dict['All'] = not topic_dict['All']
print(topic_dict)
URL_solr = configur.get('tools','URL_solr')
print(URL_solr)
CORE_NAME = configur.get('tools','CORE_NAME')
print(CORE_NAME)
print(not ast.literal_eval(configur['topic dictionary']["topic_dict"])["All"])
# configur.write('topic dictionary', topic_dict)
configur.remove_section('topic dictionary')
print(configur.sections())
configur.add_section('topic dictionary')
configur.set("topic dictionary", "topic_dict", str(topic_dict))
with open("config.ini", 'w') as configfile:
        configur.write(configfile)


def write_to_file(file_name):
    with open(file_name, 'w') as configfile:
        configur.write(configfile)


def remove_readd_section(section, topic_dictionary):
    configur.remove_section('topic dictionary')
    configur.add_section('topic dictionary')
    configur.set("topic dictionary", "topic_dict", str(topic_dictionary))


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


@app.route('/query', methods = ['POST'])
def topic_toggle():
    js=request.get_json()
    topic = str(js['text'])
    topic_dict[topic] = not topic_dict[topic]
    return jsonify(topic_dict)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999)