#!/usr/bin/python3
"""Serializing and Deserializing with XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize the dictionary into XML file"""

    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """read the XML data and return a deserialized py dict"""

    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for child in root:
        result[child.tag] = value
    return result
