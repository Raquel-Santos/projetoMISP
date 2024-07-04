#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from pymisp import PyMISP
from pymisp import ExpandedPyMISP, MISPAttribute
from keys import misp_url, misp_key, misp_verifycert
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import argparse
import urllib3
import requests
requests.packages.urllib3.disable_warnings()


"""

Sample usage:

python3 add_filetype_object_from_csv.py -e <Event_UUID> -f <formated_file_with_attributes>.csv



"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add attributes to a MISP event from a semi-colon formated csv file')
    parser.add_argument("-e", "--event_uuid", required=True, help="Event UUID to update")
    parser.add_argument("-f", "--attr_file", required=True, help="Attribute CSV file path")
    args = parser.parse_args()

    pymisp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)

    f = open(args.attr_file, newline='')
    csv_reader = csv.reader(f, delimiter=";")

    for line in csv_reader:
       value = line[0]
       type = line[1]
       tags = line[2:]

       misp_attribute = MISPAttribute()
       misp_attribute.value = str(value)
       misp_attribute.type = str(type)
       
       
       
       for x in tags:
            misp_attribute.add_tag(x)
       r = pymisp.add_attribute(args.event_uuid, misp_attribute)
       print(line)
    print("\nAttributes successfully saved :)")
