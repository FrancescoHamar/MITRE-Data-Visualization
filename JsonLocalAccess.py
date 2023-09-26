import json


def update_json(source, target, attack, data):
    with open(f"data/{source}_{target}_{attack}.json", 'w') as out:
        json.dump(data, out, indent=0)


def access_json(source, target, attack):
    with open("data/mit_tech_m.json", 'r') as indata:
        return json.load(indata)


def access_mit_tech_e(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("mit", "tech", "e", data)
    elif not write:
        return access_json("mit", "tech", "e")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_tech_mit_e(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("tech", "mit", "e", data)
    elif not write:
        return access_json("tech", "mit", "e")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_comp_tech_e(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("comp", "tech", "e", data)
    elif not write:
        return access_json("comp", "tech", "e")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_tech_comp_e(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("tech", "comp", "e", data)
    elif not write:
        return access_json("tech", "comp", "e")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_mit_tech_m(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("mit", "tech", "m", data)
    elif not write:
        return access_json("mit", "tech", "m")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_tech_mit_m(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("tech", "mit", "m", data)
    elif not write:
        return access_json("tech", "mit", "m")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_comp_tech_m(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("comp", "tech", "m", data)
    elif not write:
        return access_json("comp", "tech", "m")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_tech_comp_m(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("tech", "comp", "m", data)
    elif not write:
        return access_json("tech", "comp", "m")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_mit_tech_i(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("mit", "tech", "i", data)
    elif not write:
        return access_json("mit", "tech", "i")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_tech_mit_i(write, **kwargs):
    data = kwargs.get('data', None)
    if write:
        update_json("tech", "mit", "i", data)
    elif not write:
        return access_json("tech", "mit", "i")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_comp_tech_i(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("comp", "tech", "i", data)
    elif not write:
        return access_json("comp", "tech", "i")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")


def access_tech_comp_i(write, **kwargs):
    data = kwargs.get('data', None)
    if write and data is not None:
        update_json("tech", "comp", "i", data)
    elif not write:
        return access_json("tech", "comp", "i")
    else:
        raise ValueError("Expected 1 or 2 arguments: write -> Boolean, whether wish is to write or not; "
                         "data -> dict to dump in json")
