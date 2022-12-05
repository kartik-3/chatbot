import json

with open('./preprocessed_chitchat.json','r') as fp:
    js = json.load(fp)

corpus = []
for id,conv in js.items():
    for msg in conv:
        if len(msg) != 1:
            input()
    corpus.append(msg[0])

with open('./flat2.json','w') as fp:
    fp.write(json.dumps(corpus, indent=4))