from taxii2client.v20 import Collection
from stix2 import Filter, TAXIICollectionSource, CompositeDataSource
from DataSources import DataSources


class DataAccessPoint:

    def __init__(self, *args):
        self.src = None
        if len(args) == 0:
            self.combine_src()
        elif len(args) == 1 and \
                (args[0] == "enterprise_attack" or
                 args[0] == "mobile_attack" or
                 args[0] == "ics_attack"):
            self.select_src(args[0])
        else:
            raise ValueError("Illegal Argument Exception. Args expected: 0 or 1 string. "
                             "Must match enterprise, mobile or ics attack as: type_attack. Ex.: ics_attack")

    # Stores collection url IDs of different type of attacks
    attacks = {
        "enterprise_attack": "95ecc380-afe9-11e4-9b6c-751b66dd541e",
        "mobile_attack": "2f669986-b40b-4423-b720-4396ca6a462b",
        "ics_attack": "02c3ef24-9cd4-48f3-a99f-b74ce24f1d34"
    }

    # Switches the source (src) given the input string which has to match
    # "enterprise_attack", "mobile_attack", or "ics_attack"
    # It returns a TAZIICollectionSource Object
    def select_src(self, attack):
        collection = Collection(f"https://cti-taxii.mitre.org/stix/collections/{self.attacks[attack]}/")
        self.src = TAXIICollectionSource(collection)

    # Connects to enterprise attacks file
    # It returns a TAZIICollectionSource Object
    def src_enterprise(self):
        return self.select_src("enterprise_attack")

    # Connects to mobile attacks file
    # It returns a TAZIICollectionSource Object
    def src_mobile(self):
        return self.select_src("mobile_attack")

    # Connects to ics attacks file
    # It returns a TAZIICollectionSource Object
    def src_ics(self):
        return self.select_src("ics_attack")

    # Switches the source (src) to query all three database files (Enterprise, Mobile, ICS)
    # It returns a CompositeDataSource Object
    def combine_src(self):
        fullsrc = CompositeDataSource()
        collection = Collection(f"https://cti-taxii.mitre.org/stix/collections/{self.attacks['enterprise_attack']}/")
        enterpriseSrc = TAXIICollectionSource(collection)
        collection = Collection(f"https://cti-taxii.mitre.org/stix/collections/{self.attacks['mobile_attack']}/")
        mobileSrc = TAXIICollectionSource(collection)
        collection = Collection(f"https://cti-taxii.mitre.org/stix/collections/{self.attacks['ics_attack']}/")
        icsSrc = TAXIICollectionSource(collection)
        fullsrc.add_data_sources([enterpriseSrc, mobileSrc, icsSrc])
        self.src = fullsrc

    # Makes Hashmap/Dictionary where relationship are stored either from target to source or vice versa depending
    # on params.
    # Relation type defines what kind of relations is getting mapped
    def relations(self, source, target, reltype):
        relation_map = {}
        query_relations = self.src.query([Filter("type", "=", "relationship"),
                                     Filter('relationship_type', '=', reltype)])
        for rel in query_relations:
            if rel[source] in relation_map.keys():
                relation_map[rel[source]].append(rel[target])
            else:
                relation_map[rel[source]] = [rel[target]]

        return relation_map

    # Returns HashMap/dictionary with attacks as keys and a list of associated data sources.
    # Some attacks might have the same data source but from a different link, so it's possible to have the lists url
    # specific or more generic. URL specific is preferred here for more accuracy
    def attacks_to_sources(self, weighted):
        attacks_map = {}
        queriedAttacks = self.src.query([Filter("type", "=", "attack-pattern")])

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
    def sources_to_attacks(self, weighted):
        source_map = {}
        queriedAttacks = self.src.query([Filter("type", "=", "attack-pattern")])

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

    # Calls and returns relations of type mitigation as mitigation to technique
    def mitigate_to_technique(self):
        return self.relations("source_ref", "target_ref", "mitigates")

    # Calls and returns relations of type mitigation as technique to mitigation
    def technique_to_mitigate(self):
        return self.relations("target_ref", "source_ref", "mitigates")

    # Calls and returns relations of type detection as data source to technique
    def datasource_to_technique(self):
        return self.relations("source_ref", "target_ref", "detects")

    # Calls and returns relations of type mitigation as technique to data source
    def technique_to_datasource(self):
        return self.relations("target_ref", "source_ref", "detects")

    # Returns dictionary of pairs ordered in descending order. There will be a limit=int number of pairs
    def get_key_values(self, reldict, limit):
        keys = sorted(reldict, key=lambda k: len(reldict[k]), reverse=True)

        valueLen = []
        outDict = []

        keys = keys[:limit]
        # keys = keys[::-1]  FOR REVERSING LIST

        for key in keys:
            valueLen.append(len(reldict[key]))

        limit = min(limit, len(keys))

        for k in range(limit):
            keys[k] = self.src.get(keys[k])["name"]
            outDict.append((keys[k], valueLen[k]))

        return outDict

        # with open("data/mit_tech_m.json", 'w') as out:
        #     json.dump(outDict, out)

        # plt.barh(keys, valueLen)
        # plt.show()
        # return keys, valueLen

    # Get techniques per kill phase
    def get_technique_phase(self):
        phases = {}
        query_techniques = self.src.query([Filter("type", "=", "attack-pattern")])
        for technique in query_techniques:
            query_mitigations = self.src.query([Filter("type", "=", "relationship"),
                                                Filter('relationship_type', '=', "mitigates"),
                                                Filter("target_ref", "=", technique["id"])])

            query_components = self.src.query([Filter("type", "=", "relationship"),
                                               Filter('relationship_type', '=', "detects"),
                                               Filter("target_ref", "=", technique["id"])])

            for phase in technique["kill_chain_phases"]:
                if phases[phase["name"]] is None:
                    phases[phase["name"]] = [1, len(query_mitigations), len(query_components)]
                else:
                    phases[phase["name"]][0] += 1
                    phases[phase["name"]][1] += len(query_mitigations)
                    phases[phase["name"]][2] += len(query_components)
        return phases
