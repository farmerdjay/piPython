import requests
import json
import urllib
from urllib import request, error, parse, robotparser
from html.parser import HTMLParser
import xml.dom.minidom

def printResults(data):
    theJSON = json.loads(data)
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    count = theJSON["metadata"]["count"]
    print(str(count), "events recorded")

    for i in theJSON["features"]:
        print("%45s : %2.1f" %(i["properties"]["place"], i["properties"]["mag"]))

# Create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encoutered comment:", data)
        pos = self.getpos()
        print("At line: ", pos[0], "position ", pos[1])


def main():
    # Print the current city's temperture
    r = requests.get("http://wttr.in")
    lines = r.text.split()

    findCity = False
    for i in range(len(lines)):
        if (lines[i] == "City:"):
            findCity = True
            print(lines[i+1], lines[i+2])

        if (findCity):
            if (lines[i] == "°F"):
                print(lines[i-1][14],lines[i-1][15],lines[i])
                break

    # Earthquakes that are greater than M4.5 in the past day from JSON
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
    webURL = urllib.request.urlopen(url)
    print(webURL.getcode())
    if (webURL.getcode() == 200):
        data = webURL.read()
        printResults(data)
    else:
        print("Error:", url)

    # Print comments and their location in HTML
    london = requests.get("http://wttr.in/london")
    parser = MyHTMLParser()
    parser.feed(london.text)

if __name__ == "__main__":
    main()

