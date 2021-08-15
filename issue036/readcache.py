### readcache.py

import xml.etree.ElementTree as et

tree = et.parse('cache.loc')
et.dump(tree)

w = tree.find('.//waypoint')

for w1 in w:
    #print('w1.tag = ', w1.tag)
    if w1.tag == "name":
        # Get text of cache name up to the phrase "Open Cache: "
        CacheName = w1.text[:w1.text.find("Open Cache: ") - 1]
        # Get the text between "Open Cache: " and "Cache Type: "
        OpenCache = w1.text[w1.text.find("Open Cache: ")  \
            +12:w1.text.find("Cache Type: ")-1]
        # More of the same
        CacheType = w1.text[w1.text.find("Cache Type: ") \
            +12:w1.text.find("Cache Size: ")-1]
        CacheSize = w1.text[w1.text.find("Cache Size: ") \
            +12:w1.text.find("Difficulty: ")-1]
        Difficulty = w1.text[w1.text.find("Difficulty: ") \
            +12:w1.text.find(" Terrain : ")-1]
        Terrain = w1.text[w1.text.find("Terrain : ")+12:]
        if w1.keys():
            for name, value in w1.items():
                if name == 'id':
                    CacheID = value
    elif w1.tag == "coord":
        if w1.keys():
            for name, value in w1.items():
                if name == "lat":
                    Lat = value
                elif name == "lon":
                    Lon = value
    elif w1.tag == "type":
        GType = w1.text
    elif w1.tag == "link":
        if w1.keys():
            for name, value in w1.items():
                Info = value
        Link = w1.text
print("Cache Name: ",CacheName)
print("Cache ID: ",CacheID)
print("Open Cache: ",OpenCache)
print("Cache Type: ",CacheType)
print("Cache Size: ",CacheSize)
print("Difficulty: ", Difficulty)
print("Terrain: ",Terrain)
print("Lat: ",Lat)
print("Lon: ",Lon)
print("GType: ",GType)
print("Link: ",Link)

print('finished')