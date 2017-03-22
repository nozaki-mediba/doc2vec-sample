#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
import argparse
import csv
import io
import six


parser = argparse.ArgumentParser()
parser.add_argument("csv_file_path")
parser.add_argument("--encoding", default="utf_8")
options = parser.parse_args()

csv_reader = csv.reader(
    io.open(options.csv_file_path, "r", encoding=options.encoding),
    delimiter="\t",
    quotechar='"'
)

print("--- header ---\n{}\n".format(six.next(csv_reader)))
print("--- data ---")
for row in csv_reader:
    code = row[0]
    title = row[1]
    body = row[2]
    f = open('search_target/'+code+'.txt', 'w')
    f.write(title+'\n'+body)
    f.close()
