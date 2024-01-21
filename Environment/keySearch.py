from keyFeature import *


def keySearch(userInput):
    userInput = [x.lower() for x in userInput.replace(".", '').split(' ') if x != '']

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

    return destinationKey, countryKey, regionKey, climateKey, budgetKey, activityKey, demographicsKey, durationKey, \
           cuisineKey, historyKey, natural_wonderKey, accommodationKey, languageKey
