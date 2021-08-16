"""
w_currents.py
Returns current conditions, forecast and alerts for a given zipcode from WeatherUnderground.com.
Usage: python wonderground.py [options]
Options:
    -h, --help Show this help
    -l, --location City,State to use
    -z, --zip Zipcode to use as location

Examples:
    w_currents.py -h (shows this help information)
    w_currents.py -z 80013 (uses the zip code 80013 as location)
"""

from xml.etree import ElementTree as ET
import urllib
import sys
import getopt

class CurrentInfo:

    '''
    This routine retrieves the current condition xml data from WeatherUnderground.com
    based off of the zip code or Airport Code...
    currently tested only with Zip Code and Airport code
    For location,
        if zip code use something like 80013 (no quotes)
        if airport use something like "KDEN" (use double quotes)
        if city/state (US) use something like "Aurora,%20CO" or "Aurora,CO" (use double quotes)
        if city/country, use something like "London,%20England" (use double quotes)
    '''

    def getCurrents(self,debuglevel,Location):

        if debuglevel > 0:
            print("Location = %s" % Location)

        try:
            CurrentConditions = 'http://api.wunderground.com/auto/wui/geo/WXCurrentObXML/index.xml?query=%s' % Location
            urllib.socket.setdefaulttimeout(8)
            usock = urllib.urlopen(CurrentConditions)
            tree = ET.parse(usock)
            usock.close()
        except:
            print('ERROR - Current Conditions - Could not get information from server...')
            if debuglevel > 0:
                print(Location)
                sys.exit(2)

        # Get Display Location
        for loc in tree.findall("//full"):
                self.location = loc.text

        # Get Observation time
        for tim in tree.findall("//observation_time"):
            self.obtime = tim.text

        # Get Current conditions
        for weather in tree.findall("//weather"):
            self.we = weather.text

        # Get Temp
            for TempF in tree.findall("//temperature_string"):
                self.tmpB = TempF.text

        #Get Humidity
            for hum in tree.findall("//relative_humidity"):
                self.relhum = hum.text

        # Get Wind info
            for windstring in tree.findall("//wind_string"):
                self.winds = windstring.text

        # Get Barometric Pressure
            for pressure in tree.findall("//pressure_string"):
                self.baroB = pressure.text

    def output(self):
        print('Weather Information From Wunderground.com')
        print('Weather info for %s ' % self.location)
        print(self.obtime)
        print('Current Weather - %s' % self.we)
        print('Current Temp - %s' % self.tmpB)
        print('Barometric Pressure - %s' % self.baroB)
        print('Relative Humidity - %s' % self.relhum)
        print('Winds %s' % self.winds)


    def DoIt(self,Location):
        self.getCurrents(1,Location)
        self.output()

def usage():
    print(__doc__)

def main(argv):
    print('Entering Main with argv = ', argv)
    location = 28792
    try:
        opts, args = getopt.getopt(argv, "hz:l:", ["help=", "zip=", "location="])
        print('opts = ', opts)
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-l", "--location"):
            location = arg
        elif opt in ("-z", "--zip"):
            location = arg

    print ('Now to get current info')
    currents = CurrentInfo()
    print('and now to Do It')
    currents.DoIt(location)

#===========================================================
# Main loop
#===========================================================
if __name__ == "__main__":
    main(sys.argv[1:])