import json

with open('task3.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for i in data['intents']:
        print("Intent:", i['intent'])
        print("\tExamples:\t")
        for j in i['examples']:
            print("\t\tText:\t\t", j['text'])

