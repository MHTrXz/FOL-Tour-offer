import csv
from pyswip import Prolog

prolog = Prolog()


def loadData():
    prolog.retractall("destination(_, _, _, _, _, _, _, _, _, _, _, _, _)")

    dataset = open('../Datasets/Destinations.csv')
    skip = True
    for i in csv.reader(dataset):
        if skip:
            skip = False
            continue
        add = "destination("
        for j in range(12):
            add += "'" + i[j].replace("'", '"').replace(' ', '-').lower() + "', "
        add += "'" + i[12].replace("'", '"').replace(' ', '-').lower() + "')"
        prolog.assertz(add)


loadData()


def IntegratedQuery(country='_', region='_', climate='_', budget='_', activity='_', demographics='_', duration='_',
                    cuisine='_', history='_', natural_wonder='_', accommodation='_', language='_'):
    output = set()
    for city in list(prolog.query(
            "destination(City, " + country + ", " + region + ", " + climate + ", " + budget + ", " + activity + ", " + demographics + ", " + duration + ", " + cuisine + ", " + history + ", " + natural_wonder + ", " + accommodation + ", " + language + ")")):
        output.add(city['City'])
    return list(output)


if __name__ == "__main__":
    print(IntegratedQuery(budget="'low'"))
