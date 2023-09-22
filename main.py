from taxii2client.v20 import Server, Collection
from stix2 import Filter, TAXIICollectionSource, CompositeDataSource
from DataSources import DataSources

attacks = {
    "enterprise_attack": "95ecc380-afe9-11e4-9b6c-751b66dd541e",
    "mobile_attack": "2f669986-b40b-4423-b720-4396ca6a462b",
    "ics_attack": "02c3ef24-9cd4-48f3-a99f-b74ce24f1d34"
}


def select_src(attack):
    collection = Collection(f"https://cti-taxii.mitre.org/stix/collections/{attacks[attack]}/")
    return TAXIICollectionSource(collection)


def combine_src():
    fullsrc = CompositeDataSource()
    collection = Collection(f"https://cti-taxii.mitre.org/stix/collections/{attacks['enterprise_attack']}/")
    enterpriseSrc = TAXIICollectionSource(collection)
    collection = Collection(f"https://cti-taxii.mitre.org/stix/collections/{attacks['mobile_attack']}/")
    mobileSrc = TAXIICollectionSource(collection)
    collection = Collection(f"https://cti-taxii.mitre.org/stix/collections/{attacks['ics_attack']}/")
    icsSrc = TAXIICollectionSource(collection)
    fullsrc.add_data_sources([enterpriseSrc, mobileSrc, icsSrc])
    return fullsrc


# Makes dictionary where relationship are stored either from target to source or vice versa depending on param
# unique and appendable can either be "source_ref" or "target_ref" which refer to json attributes
def mitigation_pairing(reverse):
    if reverse:
        unique = "target_ref"
        appendable = "source_ref"
    else:
        unique = "source_ref"
        appendable = "target_ref"

    mitigation_map = {}
    relations = src.query([Filter("type", "=", "relationship"),
                          Filter('relationship_type', '=', "mitigates")])
    for rel in relations:
        if rel[unique] in mitigation_map.keys():
            mitigation_map[rel[unique]].append(rel[appendable])
        else:
            mitigation_map[rel[unique]] = [rel[appendable]]

    return mitigation_map


def attacks_to_sources(weighted):
    attacks_map = {}
    queriedAttacks = src.query([Filter("type", "=", "attack-pattern")])

    if weighted:
        for attack in queriedAttacks:
            attacks_map[attack["id"]] = []
            for source in attack["external_references"]:
                attacks_map[attack["id"]].append(DataSources(source["name"], source["url"]))
    else:
        for attack in queriedAttacks:
            attacks_map[attack["id"]] = []
            for source in attack["external_references"]:
                if source["name"] not in attacks_map[attack["id"]]:
                    attacks_map[attack["id"]].append(source["name"])


def sources_to_attacks(weighted):
    source_map = {}
    queriedAttacks = src.query([Filter("type", "=", "attack-pattern")])

    if weighted:
        for attack in queriedAttacks:
            for source in attack["external_references"]:
                current = DataSources(source["name"], source["url"])
                if current not in source_map.keys():
                    source_map[current] = [attack["id"]]
                else:
                    source_map[current].append(attack["id"])

    else:
        for attack in queriedAttacks:
            for source in attack["external_references"]:
                if source["name"] not in source_map.keys():
                    source_map[source["name"]] = [attack["id"]]
                else:
                    source_map[source["name"]].append(attack["id"])


src = select_src("mobile_attack")
print(mitigation_pairing(False))
