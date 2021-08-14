### readcache.py

import xml.etree.ElementTree as et

tree = et.parse('cache.loc')
et.dump(tree)