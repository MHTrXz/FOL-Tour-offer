import graph


def checkConnection(cities):
    calc = {x: dict() for x in cities}
    for k, v in calc.items():
        for i in graph.GraphQuery('connected', "'" + k + "'"):
            if i != k:
                calc[k][i] = list()
                for j in graph.GraphQuery('connected', "'" + i + "'"):
                    if j != i and k != j:
                        calc[k][i].append(j)

    outputs = calculate(cities, calc)

    if len([len(x) for x in outputs if x[-1] in cities]):
        print('Tours:')
        for i in outputs:
            print('->'.join(i))

        maxL = max([len(x) for x in outputs if x[-1] in cities])
        bTour = list()
        for i in outputs:
            if len(i) == maxL:
                bTour = i
                break
        print('\nBest Tour: ', '->'.join(bTour))
        return list(set(bTour))
    else:
        return -1
def calculate(cities, calc):
    print('1st query: ', cities)
    print('Graphs:')
    for k1, v1 in calc.items():
        print(k1)
        for k2, v2 in v1.items():
            print('\t', k2, '\t', v2)

    outputs = []
    for k1, v1 in calc.items():
        for k2, v2 in v1.items():
            outputs.append([k1, k2])
            for city in v2:
                if city in cities:
                    outputs.append([k1, k2, city])

    length = len(outputs)
    for i in range(length):
        for j in range(length):
            if outputs[i][-1] == outputs[j][0] and outputs[i][0] != outputs[j][-1]:
                outputs.append(outputs[i] + outputs[j][1:])
    return outputs
