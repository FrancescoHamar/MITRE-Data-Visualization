import json


def update_relation_json(source, target, attack, data):
    with open(f"data/{source}_{target}_{attack}.json", 'w') as out:
        json.dump(data, out, indent=2)


def update_phases(attack, data):
    with open(f"data/phases_{attack}.json", 'w') as out:
        json.dump(data, out, indent=2)


def access_relation_json(source, target, attack, limit):
    with open(f"data/{source}_{target}_{attack}.json", 'r') as indata:
        return json.load(indata)[:limit]


def access_phases(attack):
    with open(f"data/phases_{attack}.json", 'r') as indata:
        return json.load(indata)


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
