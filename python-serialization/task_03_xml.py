#!/usr/bin/python3
"""Defines the serialize_to_xml and deserialize_from_xml functions."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes and saves the dictionary to the given file as XML.

    Parameters:
        dictionary: The dictionary to serialize.
        filename: The file to save the dictionary to."""
    data = ET.Element("data")

    for k, v in dictionary.items():
        d = ET.SubElement(data, k)
        d.text = str(v)

    tree = ET.ElementTree(data)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """Deserializes data from an XML file and returns it.

    Parameters:
        filename: The file to read the data from.

    Returns: The deserialized data."""
    tree = ET.parse(filename)
    data = tree.getroot()
    res = {}

    for d in data:
        res[d.tag] = d.text

    return res
