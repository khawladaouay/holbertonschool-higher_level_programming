#!/usr/bin/python3
import json


def load_from_json_file(filename):
	with open(filename, "r") as f:
		json_object = json.load(f)
	print(json_object)
	print(type(json_object))