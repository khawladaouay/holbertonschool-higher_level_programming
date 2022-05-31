#!/usr/bin/python3
"""load_from_json_file"""
import json


def load_from_json_file(filename):
    """load_from_json_file function that
    creates an Object from a “JSON file”"""

    with open(filename, "r") as f:
        json_object = json.load(f.read())
    return json_object
