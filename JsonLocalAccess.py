import json


def update_json(source, target, attack, data):
    with open(f"data/{source}_{target}_{attack}.json", 'w') as out:
        json.dump(data, out, indent=0)


def access_json(source, target, attack):
    with open("data/mit_tech_m.json", 'r') as indata:
        return json.load(indata)


def access_mit_tech_e(data, write):
    if write:
        update_json("mit", "tech", "e", data)
    else:
        return access_json("mit", "tech", "e")


def access_tech_mit_e(data, write):
    if write:
        update_json("tech", "mit", "e", data)
    else:
        return access_json("tech", "mit", "e")


def access_comp_tech_e(data, write):
    if write:
        update_json("comp", "tech", "e", data)
    else:
        return access_json("comp", "tech", "e")


def access_tech_comp_e(data, write):
    if write:
        update_json("tech", "comp", "e", data)
    else:
        return access_json("tech", "comp", "e")


def access_mit_tech_m(data, write):
    if write:
        update_json("mit", "tech", "m", data)
    else:
        return access_json("mit", "tech", "m")


def access_tech_mit_m(data, write):
    if write:
        update_json("tech", "mit", "m", data)
    else:
        return access_json("tech", "mit", "m")


def access_comp_tech_m(data, write):
    if write:
        update_json("comp", "tech", "m", data)
    else:
        return access_json("comp", "tech", "m")


def access_tech_comp_m(data, write):
    if write:
        update_json("tech", "comp", "m", data)
    else:
        return access_json("tech", "comp", "m")


def access_mit_tech_i(data, write):
    if write:
        update_json("mit", "tech", "i", data)
    else:
        return access_json("mit", "tech", "i")


def access_tech_mit_i(data, write):
    if write:
        update_json("tech", "mit", "i", data)
    else:
        return access_json("tech", "mit", "i")


def access_comp_tech_i(data, write):
    if write:
        update_json("comp", "tech", "i", data)
    else:
        return access_json("comp", "tech", "i")


def access_tech_comp_i(data, write):
    if write:
        update_json("tech", "comp", "i", data)
    else:
        return access_json("tech", "comp", "i")
