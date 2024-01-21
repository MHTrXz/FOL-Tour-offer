import graph


def checkConnection(cities):
    output = list()
    for i in range(len(cities) - 1):
        if graph.GraphQuery('connected', "'" + cities[i] + "'", "'" + cities[i + 1] + "'", True):
            output.append(cities[i])
    return output
