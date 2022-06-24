names = {
    1: "Baden-Württemberg",
    2: "Bayern",
    3: "Berlin",
    4: "Brandenburg",
    5: "Bremen",
    6: "Hamburg",
    7: "Hesson",
    8: "Mecklenburg-Vorpommern",
    9: "Niedersachsen",
    10: "Nordrhein-Westfalen",
    11: "Rheinland-Pfalz",
    12: "Saarland",
    13: "Sachsen",
    14: "Sachsen-Anhalt",
    15: "Schleswig-Holstein",
    16: "Thüringen",
}

isoCodes = {
    1: "DE-BW",
    2: "DE-BY",
    3: "DE-BE",
    4: "DE-BB",
    5: "DE-HB",
    6: "DE-HH",
    7: "DE-HE",
    8: "DE-MV",
    9: "DE-NI",
    10: "DE-NW",
    11: "DE-RP",
    12: "DE-SL",
    13: "DE-SN",
    14: "DE-ST",
    15: "DE-SH",
    16: "DE-TH",
}

class RegionMatcher:

    def getName(self, regionId):
        name = names.get(regionId)
        if(name):
            return name
        return regionId

    def getIsoCode(self, regionId):
        isoCode = isoCodes.get(regionId)
        if(isoCode):
            return isoCode
        return regionId

    def match(self, regionId):
        region = Region()
        region.name = self.getName(regionId)
        region.isoCode = self.getIsoCode(regionId)
        region.id = regionId
        return region


class Region:
    id = ""
    name = ""
    isoCode = ""