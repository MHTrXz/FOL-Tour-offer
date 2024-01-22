from FlatFact import FlatFactQuery

features = ["destination", "country", "region", "climate", "budget", "activity", "demographics", "duration", "cuisine",
            "history", "natural_wonder", "accommodation", "language"]


def findCities(keyFeatures):
    output = set(keyFeatures[0])
    for feature in range(1, len(keyFeatures)):
        for option in keyFeatures[feature]:
            output = output.intersection(FlatFactQuery(features[feature], "'" + option + "'")) if len(
                output) > 0 else FlatFactQuery(features[feature], "'" + option + "'")
    return list(output)


def findCitiesUnion(keyFeatures):
    output = set(keyFeatures[0])
    for feature in range(1, len(keyFeatures)):
        for option in keyFeatures[feature]:
            output = output.union(FlatFactQuery(features[feature], "'" + option + "'")) if len(
                output) > 0 else FlatFactQuery(features[feature], "'" + option + "'")
    return list(output)
