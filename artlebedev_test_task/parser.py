from pprint import pprint
import json

with open(
    file='data-85-structure-3.json', mode='r', encoding='utf-8'
) as read_file:
    data = json.load(read_file)
    pprint(data[235]['data'])
