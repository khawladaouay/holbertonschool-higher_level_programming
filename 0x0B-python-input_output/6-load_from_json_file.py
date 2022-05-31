#!/usr/bin/python3
"""load_from_json_file"""
import json


def load_from_json_file(filename):
    """load_from_json_file function that
    creates an Object from a “JSON file”"""

    with open(filename, encoding='utf-8') as f:
        json_object = json.loads(f.read())
    return json_object
