import json
import uuid


f = open('chitchat.json')

data = json.load(f)

json_dict = {}


for l in data:
    for sms in data[l]["messages"]:
        new_text = ""
        for each_sms in sms:
            # concatenating the text
            new_text += " " + each_sms["text"]
            each_sms["text"] = new_text
            # added topic and parent_id
            each_sms["topic"] = "chitchat"
            each_sms["parent_id"] = str(uuid.uuid4())
    # data[l]["messages"] = data[l]["messages"][-1]
    for mes in data[l]["messages"]:
        del mes[0:len(mes)-1]
    flag = False
    count = 0
    for msge in data[l]["messages"]:
        for obj in msge:
            obj["body"] = obj["text"].lstrip()
            del obj["text"]
            obj["author"] = obj["sender"]
            del obj["sender"]
            # adding parent body
            if not flag:
                prev_txt = obj["body"]
                obj["parent_body"] = None
            else:
                obj["parent_body"] = prev_txt
                prev_txt = obj["body"]
            count += 1
            if count != 0:
                flag = True

    # updating the json dictionary
    json_dict[l] = data[l]["messages"]
    # print(json_dict[l][0])


jsonString = json.dumps(json_dict, indent=4)
jsonFile = open("preprocessed_chitchat.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

# with open("preprocessed_chitchat.json", "w") as outfile:
#     outfile.write(json_object)

f.close()
