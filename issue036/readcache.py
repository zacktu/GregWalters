### readcache.py

import xml.etree.ElementTree as et

tree = et.parse('cache.loc')
et.dump(tree)

w = tree.find('.//waypoint')

for w1 in w:
    print('w1.tag = ', w1.tag)
    if w1.tag == "name":
        # Get text of cache name up to the phrase "Open Cache: "
        CacheName = w1.text[:w1.text.find("Open Cache: ") - 1]
        # Get the text between "Open Cache: " and "Cache Type: "
        OpenCache = w1.text[w1.text.find("Open Cache: ")  \
            +12:w1.text.find("Cache Type: ")-1]
        print('OpenCache = ', OpenCache)
        # More of the same
        CacheType = w1.text[w1.text.find("Cache Type: ") \
            +12:w1.text.find("Cache Size: ")-1]
        print('CacheType = ', CacheType)
        CacheSize = w1.text[w1.text.find("Cache Size: ") \
            +12:w1.text.find("Difficulty: ")-1]
        print('CacheSize = ', CacheSize)
        Difficulty = w1.text[w1.text.find("Difficulty: ") \
            +12:w1.text.find(" Terrain : ")-1]
        print('Difficulty = ', Difficulty)
        Terrain = w1.text[w1.text.find("Terrain : ")+12:]
        print('Terrain = ', OpenCache)
