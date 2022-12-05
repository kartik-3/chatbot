import os
import pysolr
import requests
import json
if os.path.exists(dir:='./data'): os.chdir('./data')

CORE_NAME = "IRF22P4"
GCP_IP = "34.133.78.26"
url_solr = f'http://{GCP_IP}:8983/solr/'
url_core = url_solr+CORE_NAME
connection = pysolr.Solr(url_core, always_commit=True, timeout=500)


def add_fields():
    js = {
            "add-field": [
            {
                "name": "subreddit",
                "type": "string",
                "multiValued": False
            },
            {
                "name": "full_link",
                "type": "string",
                "multiValued": False
            },
            {
                "name": "author",
                "type": "string",
                "multiValued": False
            },
            {
                "name": "is_submission",
                "type": "boolean",
                "multiValued": False
            },
            {
                "name": "created_at",
                "type": "pdate",
                "multiValued": False
            },
            {
                "name": "topic",
                "type": "string",
                "multiValued": False
            },
            # submission fields
            # {
            #     "name": "title",
            #     "type": "string",
            #     "multiValued": False
            # },
            # {
            #     "name": "selftext",
            #     "type": "text_en",
            #     "multiValued": False
            # },
            #
            # comment fields
            {
                "name": "body",
                "type": "text_en",
                "multiValued": False
            },
            {
                "name": "parent_id",
                "type": "string",
                "multiValued": False
            },
            {
                "name": "parent_body",
                "type": "text_en",
                "multiValued": False
            },
            ]
        }
    print(requests.post(url_core+'/schema', json=js).json())
    
add_fields()

with open('./chitchat/flat_chitchat_2.json', 'r') as f:
    chitchat = json.load(f)
print(connection.add(chitchat))

with open('./redditData/comments-topic-labelled.json', 'r') as f:
    reddit = json.load(f)
print(connection.add(reddit))