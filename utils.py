import json


def read(path):
    with open(path, 'r') as f:
        return f.read()


def read_json(path):
    return json.loads(read(path))

FREQ_MAP = read_json('frequency_map.json')