import csv

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


def loadData():
    dataset = open('../Datasets/Destinations.csv')
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


loadData()

if __name__ == "__main__":
    print("destination: ", destination)
    print("country: ", country)
    print("region: ", region)
    print("climate: ", climate)
    print("budget: ", budget)
    print("activity: ", activity)
    print("demographics: ", demographics)
    print("duration: ", duration)
    print("cuisine: ", cuisine)
    print("history: ", history)
    print("natural_wonder: ", natural_wonder)
    print("accommodation: ", accommodation)
    print("language: ", language)
