# MITRE-Data-Visualization

This app parses through the [Mitre Cyber Threat Intelligence Repository](https://github.com/mitre/cti) expressed in STIX 2.0 via the ATT&CK TAXII server that implements the 2.0 version of the TAXII specification.

The database is subdivided into three domains:
- Enterprise attacks
- Mobile attacks
- Ics attacks
  
All of these can be shuffled through in the graphs.

## Relationship Visualization
The first graph represents relation ships between *attack techniques*, *mitigations*, and *data components*
 - Attack Techniques (attack-pattern) are patterns used by adversaries to attempt to compromise targets
 - Mitigations (course-of-action) are actions taken either to prevent an attack or to respond to an attack
 - Data Components are components of data sources that detect attack patterns

The graph will give an overview of the following:
 - Techniques with the most mitigations
 - Techniques with the most data components that detect them
 - Mitigations that mitigate the most techniques
 - Data Components that detect the most attack patterns

![image](https://github.com/FrancescoHamar/MITRE-Data-Visualization/assets/92935796/2054dc21-816c-42e7-9159-eaa3ce683963)


## Kill Chain Visualization
The second graph represents the number of *attack patterns*, *mitigations*, and *data components* that appear in each phase of the kill chain.
This gives an overview of which phases are the most exposed given the ratio of techniques per mitigations/data sources.

There is the option to shuffle through the different domains here as well as some of them even mention additional phases in the kill chain.

![image](https://github.com/FrancescoHamar/MITRE-Data-Visualization/assets/92935796/e127a065-cec4-42c7-bc31-62cc0b9e2bf9)

