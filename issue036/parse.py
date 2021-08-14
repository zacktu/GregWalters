### parse.py

import xml.etree.ElementTree as et

tree = et.parse('people.xml')
et.dump(tree)