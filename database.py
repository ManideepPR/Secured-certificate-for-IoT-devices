from pymongo import MongoClient
client = MongoClient()
db = client.pythonbicookbook
files = db.files
f = open('cert.txt')
text = f.read()
with open('cert.txt', 'r') as file:
    info = file.read().rstrip('\n')
doc = {
"file_name": "cert.txt",
"contents" : info }
files.insert(doc)