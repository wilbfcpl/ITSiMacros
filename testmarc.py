import os, os.path
#import pymarc
from pymarc import MARCReader
import re
import sys

with open('testmarc.mrc', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        print(record.title)


fh.close()
