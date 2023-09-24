from taxii2client.v20 import Collection
from stix2 import Filter, TAXIICollectionSource, CompositeDataSource
from DataSources import DataSources


# Stores collection url IDs of different type of attacks
attacks = {
    "enterprise_attack": "95ecc380-afe9-11e4-9b6c-751b66dd541e",
    "mobile_attack": "2f669986-b40b-4423-b720-4396ca6a462b",
    "ics_attack": "02c3ef24-9cd4-48f3-a99f-b74ce24f1d34"
}


# Switches the source (src) given the input string which has to match
# "enterprise_attack", "mobile_attack", or "ics_attack"
# It returns a TAZIICollectionSource Object
def select_src(attack):
    collection = Collection(f"https://cti-taxii.mitre.org/stix/collections/{attacks[attack]}/")
    return TAXIICollectionSource(collection)


# Switches the source (src) to query all three database files (Enterprise, Mobile, ICS)
# It returns a CompositeDataSource Object
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


# Makes Hashmap/Dictionary where relationship are stored either from target to source or vice versa depending on param
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


# Returns HashMap/dictionary with attacks as keys and a list of associated data sources.
# Some attacks might have the same data source but from a different link, so it's possible to have the lists url
# specific or more generic. URL specific is preferred here for more accuracy
def attacks_to_sources(weighted):
    attacks_map = {}
    queriedAttacks = src.query([Filter("type", "=", "attack-pattern")])

    if weighted:
        for attack in queriedAttacks:
            attacks_map[attack["id"]] = []
            for source in attack["external_references"]:
                try:
                    current = DataSources(source["source_name"], source["url"])
                except KeyError:
                    current = DataSources(source["source_name"], None)
                attacks_map[attack["id"]].append(current)
    else:
        for attack in queriedAttacks:
            attacks_map[attack["id"]] = []
            for source in attack["external_references"]:
                if source["source_name"] not in attacks_map[attack["id"]]:
                    attacks_map[attack["id"]].append(source["source_name"])

    return attacks_map


# Returns HashMap/dictionary with data sources as keys and a list of associated attacks.
# Some attacks might have the same data source but from a different link, so it's possible to have the lists url
# specific or more generic. URL generic is preferred here because we are more interested in the names
def sources_to_attacks(weighted):
    source_map = {}
    queriedAttacks = src.query([Filter("type", "=", "attack-pattern")])

    if weighted:
        for attack in queriedAttacks:
            for source in attack["external_references"]:
                try:
                    current = DataSources(source["source_name"], source["url"])
                except KeyError:
                    current = DataSources(source["source_name"], None)
                if current not in source_map.keys():
                    source_map[current] = [attack["id"]]
                else:
                    source_map[current].append(attack["id"])

    else:
        for attack in queriedAttacks:
            for source in attack["external_references"]:
                if source["source_name"] not in source_map.keys():
                    source_map[source["source_name"]] = [attack["id"]]
                else:
                    source_map[source["source_name"]].append(attack["id"])

    return source_map


src = select_src("mobile_attack")
print(attacks_to_sources(True))
