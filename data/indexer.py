import os
import pysolr
import requests
import json

CORE_NAME = "chitchat"
GCP_IP = "34.135.219.198"


def delete_core(core=CORE_NAME):
    print(os.system('sudo su - solr -c "/opt/solr/bin/solr delete -c {core}"'.format(core=core)))


def create_core(core=CORE_NAME):
    print(os.system(
        'sudo su - solr -c "/opt/solr/bin/solr create -c {core} -n data_driven_schema_configs"'.format(
            core=core)))

# collection

# collection = [{
#     "id": 1,
#     "first_name": "Chickie",
#     "last_name": "Proven",
#     "email": "cproven0@alexa.com",
#     "age": 77,
#     "pincodes": [2121212, 3232323]
# }, {
#     "id": 2,
#     "first_name": "Dex",
#     "last_name": "Bofield",
#     "email": "dbofield1@about.com",
#     "age": 88,
#     "pincodes": [2121212, 3232323]
# }, {
#     "id": 3,
#     "first_name": "Saba",
#     "last_name": "Ace",
#     "email": "sace2@craigslist.org",
#     "age": 55,
#     "pincodes": [2121212, 3232323]
# }, {
#     "id": 4,
#     "first_name": "Hymie",
#     "last_name": "Patterfield",
#     "email": "hpatterfield3@plala.or.jp",
#     "age": 22,
#     "pincodes": [2121212, 3232323]
# }, {
#     "id": 5,
#     "first_name": "Chiarra",
#     "last_name": "Cornils",
#     "email": "ccornils4@patch.com",
#     "age": 23,
#     "pincodes": [2121212, 3232323]
# }]

with open('chitchat/flat_chitchat_2.json', 'r') as f:
    data = json.load(f)

class Indexer:
    def __init__(self):
        self.solr_url = f'http://{GCP_IP}:8983/solr/'
        self.connection = pysolr.Solr(self.solr_url + CORE_NAME, always_commit=True, timeout=500)

    def do_initial_setup(self):
        # delete_core()
        create_core()

    def create_documents(self, docs):
        print(self.connection.add(docs))

    def add_fields(self):
        data = {
            "add-field": [
                # fields for submissions doc
                {
                    "name": "body",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "id",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "created_at",
                    "type": "pdate",
                    "multiValued": False
                },
                {
                    "name": "parent_id",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "parent_body",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "topic",
                    "type": "string",
                    "multiValued": False
                },
                {
                    "name": "author",
                    "type": "string",
                    "multiValued": False
                }
            ]
        }

        print(requests.post(self.solr_url + CORE_NAME + "/schema", json=data).json())


if __name__ == "__main__":
    i = Indexer()
    # i.do_initial_setup()    
    # i.add_fields()
    # i.replace_fields()
    i.create_documents(data)
    