import csv
from pyswip import Prolog

prolog = Prolog()


def loadData():
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

    dataset = open('../Datasets/Destinations.csv')
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


loadData()


def FlatFactQuery(factor, parameter, city='City'):
    output = set()
    for city in list(prolog.query(factor + "(" + city + ", " + parameter + ")")):
        output.add(city['City'])
    return output


if __name__ == '__main__':
    print(FlatFactQuery("budget", "'Low'"))
