import sys
import csv
import tkinter
import tkinter.messagebox
from tkintermapview import TkinterMapView
from pyswip import Prolog


class App(tkinter.Tk):
    APP_NAME = "map_view_demo.py"
    WIDTH = 800
    HEIGHT = 750  # This is now the initial size, not fixed.

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title(self.APP_NAME)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Configure the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Text area can expand/contract.
        self.grid_rowconfigure(1, weight=0)  # Submit button row; doesn't need to expand.
        self.grid_rowconfigure(2, weight=3)  # Map gets the most space.

        # Upper part: Text Area and Submit Button
        self.text_area = tkinter.Text(self)
        self.text_area.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.submit_button = tkinter.Button(self, text="Submit", command=self.process_text)
        self.submit_button.grid(row=1, column=0, pady=10, sticky="ew")

        # Lower part: Map Widget
        self.map_widget = TkinterMapView(self)
        self.map_widget.grid(row=2, column=0, sticky="nsew")

        self.marker_list = []  # Keeping track of markers

    def check_connections(self, results):
        # TODO 5: create the knowledgebase of the city and its connected destinations using Adjacency_matrix.csv
        return checkConnection(results)

    def process_text(self):
        """Extract locations from the text area and mark them on the map."""
        text = self.text_area.get("1.0", "end-1c")  # Get text from text area
        locations = self.extract_locations(text)  # Extract locations (you may use a more complex method here)

        # TODO 4: create the query based on the extracted features of user desciption
        ################################################################################################
        locations, inputText = self.extract_locations(text)

        output = "Flat Fact"
        output += "\nInput text: " + inputText
        output += "\nkey features:" + str(locations)

        results = findCities(locations)

        output += "\nfunded locations: " + str(results)

        finalResults = self.check_connections(results)
        output += "\n finale results: " + str(finalResults)

        output += "\n------------------\n"

        print(output)
        # file = open('output.txt', 'a')
        # file.write(output + '\n')
        # file.close()

        # TODO 6: if the number of destinations is less than 6 mark and connect them 
        ################################################################################################
        if 6 > len(finalResults) > 1:
            tkinter.messagebox.showinfo(title='Please wait ...',
                                        message='Please wait ... marking the tour route in map.')
            print('start mapping ------')
            self.mark_locations(finalResults)
            tkinter.messagebox.showinfo(title='Successful',
                                        message='Successfully marked. now you can see tour route in map.')
            print('down -------\n\n\n')
        else:
            tkinter.messagebox.showerror(title='Error', message='Information is not enough for specific destinations.')
            print('Information is not enough for specific destinations.')
            self.adderrorinfo('Information is not enough for specific destinations.')

    def mark_locations(self, locations):
        """Mark extracted locations on the map."""
        self.marker_list = []
        for address in locations:
            marker = self.map_widget.set_address(address, marker=True)
            if marker:
                self.marker_list.append(marker)
        self.connect_marker()
        self.map_widget.set_zoom(1)  # Adjust as necessary, 1 is usually the most zoomed out

    def connect_marker(self):
        print(self.marker_list)
        position_list = []

        for marker in self.marker_list:
            position_list.append(marker.position)

        if hasattr(self, 'marker_path') and self.marker_path is not None:
            self.map_widget.delete(self.marker_path)

        if len(position_list) > 0:
            self.marker_path = self.map_widget.set_path(position_list)

    def extract_locations(self, text):
        """Extract locations from text. A placeholder for more complex logic."""
        # Placeholder: Assuming each line in the text contains a single location name
        # TODO 3: extract key features from user's description of destinations
        ################################################################################################
        text = text.strip().replace("\n", " ")
        while text.find("  ") != -1:
            text = text.replace("  ", " ")

        userInput = [x.lower() for x in text.replace(".", '').split(' ') if x != '']

        destinationKey = []
        countryKey = []
        regionKey = []
        climateKey = []
        budgetKey = []
        activityKey = []
        demographicsKey = []
        durationKey = []
        cuisineKey = []
        historyKey = []
        natural_wonderKey = []
        accommodationKey = []
        languageKey = []

        for currentWord in userInput:
            if currentWord in destination:
                destinationKey.append(currentWord)
            if currentWord in country:
                countryKey.append(currentWord)
            if currentWord in region:
                regionKey.append(currentWord)
            if currentWord in climate:
                climateKey.append(currentWord)
            if currentWord in budget:
                budgetKey.append(currentWord)
            if currentWord in activity:
                activityKey.append(currentWord)
            if currentWord in demographics:
                demographicsKey.append(currentWord)
            if currentWord in duration:
                durationKey.append(currentWord)
            if currentWord in cuisine:
                cuisineKey.append(currentWord)
            if currentWord in history:
                historyKey.append(currentWord)
            if currentWord in natural_wonder:
                natural_wonderKey.append(currentWord)
            if currentWord in accommodation:
                accommodationKey.append(currentWord)
            if currentWord in language:
                languageKey.append(currentWord)

        return (destinationKey, countryKey, regionKey, climateKey, budgetKey, activityKey, demographicsKey, durationKey,
                cuisineKey, historyKey, natural_wonderKey, accommodationKey, languageKey), text

    def start(self):
        self.mainloop()


# TODO 1: read destinations' descriptions from Destinations.csv and add them to the prolog knowledge base
################################################################################################
# STEP1: Define the knowledge base of illnesses and their symptoms
prolog = Prolog()

prolog.retractall("destination(_)")
prolog.retractall("country(_, _)")
prolog.retractall("region(_, _)")
prolog.retractall("climate(_, _)")
prolog.retractall("budget(_, _)")
prolog.retractall("activity(_, _)")
prolog.retractall("demographics(_, _)")
prolog.retractall("duration(_, _)")
prolog.retractall("cuisine(_, _)")
prolog.retractall("history(_, _)")
prolog.retractall("natural_wonder(_, _)")
prolog.retractall("accommodation(_, _)")
prolog.retractall("language(_, _)")

dataset = open('Destinations.csv')
skip = True
for i in csv.reader(dataset):
    if skip:
        skip = False
        continue
    destination = i[0].replace("'", '"').replace(' ', '-').lower()
    prolog.assertz("destination('" + destination + "')")
    prolog.assertz("country('" + destination + "', '" + i[1].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz("region('" + destination + "', '" + i[2].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz("climate('" + destination + "', '" + i[3].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz("budget('" + destination + "', '" + i[4].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz("activity('" + destination + "', '" + i[5].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz(
        "demographics('" + destination + "', '" + i[6].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz("duration('" + destination + "', '" + i[7].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz("cuisine('" + destination + "', '" + i[8].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz("history('" + destination + "', '" + i[9].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz(
        "natural_wonder('" + destination + "', '" + i[10].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz(
        "accommodation('" + destination + "', '" + i[11].replace("'", '"').replace(' ', '-').lower() + "')")
    prolog.assertz("language('" + destination + "', '" + i[12].replace("'", '"').replace(' ', '-').lower() + "')")


def FlatFactQuery(factor, parameter, city='City'):
    output = set()
    for city in list(prolog.query(factor + "(" + city + ", " + parameter + ")")):
        output.add(city['City'])
    return output


# TODO 2: extract unique features from the Destinations.csv and save them in a dictionary
################################################################################################
destination = set()
country = set()
region = set()
climate = set()
budget = set()
activity = set()
demographics = set()
duration = set()
cuisine = set()
history = set()
natural_wonder = set()
accommodation = set()
language = set()

dataset = open('Destinations.csv')
skip = True

for row in csv.reader(dataset):
    if skip:
        skip = False
        continue
    destination.add(row[0].replace(' ', '-').lower())
    country.add(row[1].replace(' ', '-').lower())
    region.add(row[2].replace(' ', '-').lower())
    climate.add(row[3].replace(' ', '-').lower())
    budget.add(row[4].replace(' ', '-').lower())
    activity.add(row[5].replace(' ', '-').lower())
    demographics.add(row[6].replace(' ', '-').lower())
    duration.add(row[7].replace(' ', '-').lower())
    cuisine.add(row[8].replace(' ', '-').lower())
    history.add(row[9].replace(' ', '-').lower())
    natural_wonder.add(row[10].replace(' ', '-').lower())
    accommodation.add(row[11].replace(' ', '-').lower())
    language.add(row[12].replace(' ', '-').lower())

prolog.retractall("directly_connected(_, _)")
prolog.retractall("connected(_, _)")

dataset = open('Adjacency_matrix.csv')
cities = []
currentIndex = 1
for i in csv.reader(dataset):
    if len(cities) == 0:
        cities = i
        continue
    currentCity = i[0].replace("'", '"')
    for j in range(1, len(i)):
        if currentCity != cities[j] and i[j] == '1':
            prolog.assertz("directly_connected('" + currentCity + "', '" + cities[j].replace("'", '"') + "')")
    currentIndex += 1
prolog.assertz("connected(X, Y) :- directly_connected(X, Y)")  # level 1
prolog.assertz("connected(X, Y) :- directly_connected(Y, X)")  # level 1


# prolog.assertz("connected(X, Y) :- directly_connected(X, Z), directly_connected(Z, Y)")  # level 2
# prolog.assertz("connected(X, Y) :- directly_connected(Y, Z), directly_connected(Z, X)")  # level 2
# prolog.assertz("connected(X, Y) :- directly_connected(X, Z), directly_connected(Z, W), directly_connected(W, Y)")  # level 3
# prolog.assertz("connected(X, Y) :- directly_connected(Y, Z), directly_connected(Z, W), directly_connected(W, X)")  # level 3


def GraphQuery(factor, X, Y, isBool=False):
    if isBool:
        return bool(prolog.query(factor + "(" + X + ", " + Y + ")"))
    output = []
    for city in prolog.query(factor + "(" + X + ", " + Y + ")"):
        output.append(city[Y])
    return output


def findCities(keyFeatures):
    features = ["destination", "country", "region", "climate", "budget", "activity", "demographics", "duration",
                "cuisine", "history", "natural_wonder", "accommodation", "language"]
    output = set(keyFeatures[0])
    for feature in range(1, len(keyFeatures)):
        for option in keyFeatures[feature]:
            print(option)
            output = output.intersection(FlatFactQuery(features[feature], "'" + option + "'")) if len(
                output) > 0 else FlatFactQuery(features[feature], "'" + option + "'")
    return list(output)


def checkConnection(cities):
    output = list()
    for i in range(len(cities) - 1):
        if GraphQuery('connected', "'" + cities[i] + "'", "'" + cities[i + 1] + "'", True):
            output.append(cities[i])
    return output


if __name__ == "__main__":
    app = App()
    app.start()
