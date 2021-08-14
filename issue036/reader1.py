### reader1.py

import xml.etree.ElementTree as et

tree = et.parse('people.xml')
et.dump(tree)

person = tree.findall('.//person')
for p in person:
    for dat in p:
        print("Element: %s - Data: %s" % (dat.tag,dat.text))