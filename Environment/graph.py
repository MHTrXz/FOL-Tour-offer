import csv
from pyswip import Prolog

prolog = Prolog()


def loadData():
    prolog.retractall("directly_connected(_, _)")
    prolog.retractall("connected(_, _)")

    dataset = open('../Datasets/Adjacency_matrix.csv')
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


loadData()


def GraphQuery(factor, X, Y, isBool=False):
    if isBool:
        return bool(prolog.query(factor + "(" + X + ", " + Y + ")"))
    output = []
    for city in prolog.query(factor + "(" + X + ", " + Y + ")"):
        output.append(city[Y])
    return output


if __name__ == "__main__":
    print(GraphQuery("directly_connected", "'Ottawa'", "X"))
    print(GraphQuery("connectedL3", "'Ottawa'", "'Tokyo'", True))
