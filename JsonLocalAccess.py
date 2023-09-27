import json


# Writes to local file in data folder storing relations.
# Takes as input the source and target reference as well as the attack type as files are saved as:
#       source_target_attack.json
# Data parameter is the object to write
def update_relation_json(source, target, attack, data):
    with open(f"data/{source}_{target}_{attack}.json", 'w') as out:
        json.dump(data, out, indent=2)


# Writes to local file in data folder storing phases.
# Takes as input the attack type as files are saved as:
#       phases_attack.json
# The other three parameters are the attack, mitigation, and component dictionaries with phases as keys to be stored
def update_phases(attack, tech, mit, source):
    with open(f"data/phases_{attack}.json", 'w') as out:
        output = [tech, mit, source]
        json.dump(output, out, indent=2)


# Accesses local file in data folder storing relations.
# Takes as input the source and target reference as well as the attack type as files are saved as:
#       source_target_attack.json
# Limit parameter is the number of objects returned
def access_relation_json(source, target, attack, limit):
    with open(f"data/{source}_{target}_{attack}.json", 'r') as indata:
        return json.load(indata)[:limit]


# Accesses local file in data folder storing phases.
# Takes as input the attack type as files are saved as:
#       phases_attack.json
def access_phases(attack):
    with open(f"data/phases_{attack}.json", 'r') as indata:
        return json.load(indata)


# List of helper functions to update or read local json files.
# They are tailored to access a specific source_target_attack.json.
# Expected 2 arguments:
# Boolean to specify whether wish is to write or not
# Write:         True                |              False
#          Data=Json data to write   |  Limit=number of records to return
def access_mit_tech_e(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("mit", "tech", "e", data)
    elif not write:
        return access_relation_json("mit", "tech", "e", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_tech_mit_e(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("tech", "mit", "e", data)
    elif not write:
        return access_relation_json("tech", "mit", "e", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_comp_tech_e(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("comp", "tech", "e", data)
    elif not write:
        return access_relation_json("comp", "tech", "e", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_tech_comp_e(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("tech", "comp", "e", data)
    elif not write:
        return access_relation_json("tech", "comp", "e", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_mit_tech_m(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("mit", "tech", "m", data)
    elif not write:
        return access_relation_json("mit", "tech", "m", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_tech_mit_m(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("tech", "mit", "m", data)
    elif not write:
        return access_relation_json("tech", "mit", "m", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_comp_tech_m(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("comp", "tech", "m", data)
    elif not write:
        return access_relation_json("comp", "tech", "m", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_tech_comp_m(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("tech", "comp", "m", data)
    elif not write:
        return access_relation_json("tech", "comp", "m", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_mit_tech_i(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("mit", "tech", "i", data)
    elif not write:
        return access_relation_json("mit", "tech", "i", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_tech_mit_i(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write:
        update_relation_json("tech", "mit", "i", data)
    elif not write:
        return access_relation_json("tech", "mit", "i", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_comp_tech_i(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("comp", "tech", "i", data)
    elif not write:
        return access_relation_json("comp", "tech", "i", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")


def access_tech_comp_i(write, **kwargs):
    data = kwargs.get('data', None)
    limit = kwargs.get('limit', None)
    if write and data is not None:
        update_relation_json("tech", "comp", "i", data)
    elif not write:
        return access_relation_json("tech", "comp", "i", limit)
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json or limit -> int of objects to return")
