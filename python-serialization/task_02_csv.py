#!/usr/bin/python3
"""Defines the convert_csv_to_json function."""

import csv
import json


def convert_csv_to_json(filename):
    try:
        d = []
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                d.append(row)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(d, f)

        return True
    except (
            FileNotFoundError,
            Exception
        ):
        return False
