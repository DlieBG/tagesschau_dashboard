names = {
    0: "Deutschland",
    1: "Baden-Württemberg",
    2: "Bayern",
    3: "Berlin",
    4: "Brandenburg",
    5: "Bremen",
    6: "Hamburg",
    7: "Hessen",
    8: "Mecklenburg-Vorpommern",
    9: "Niedersachsen",
    10: "Nordrhein-Westfalen",
    11: "Rheinland-Pfalz",
    12: "Saarland",
    13: "Sachsen",
    14: "Sachsen-Anhalt",
    15: "Schleswig-Holstein",
    16: "Thüringen"
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
    16: "DE-TH"
}

regionResidents = {
    1: 11070000,
    2: 13080000,
    3: 3645000,
    4: 2512000,
    5: 569352,
    6: 1841000,
    7: 6266000,
    8: 1610000,
    9: 7982000,
    10: 17930000,
    11: 4085000,
    12: 990509,
    13: 4078000,
    14: 2208000,
    15: 2897000,
    16: 2143000
}

broadcasterNames = {
    1: "Südwestrundfunk",
    2: "Bayerischer Rundfunk",
    3: "Rundfunk Berlin-Brandenburg",
    4: "Rundfunk Berlin-Brandenburg",
    5: "Radio Bremen",
    6: "Norddeutscher Rundfunk",
    7: "Hessischer Rundfunk",
    8: "Norddeutscher Rundfunk",
    9: "Norddeutscher Rundfunk",
    10: "Westdeutscher Rundfunk",
    11: "Südwestrundfunk",
    12: "Saarländischer Rundfunk",
    13: "Mitteldeutscher Rundfunk",
    14: "Mitteldeutscher Rundfunk",
    15: "Norddeutscher Rundfunk",
    16: "Mitteldeutscher Rundfunk"
}

broadcasterNameShorthands = {
    1: "SWR",
    2: "BR",
    3: "rbb",
    4: "rbb",
    5: "",
    6: "NDR",
    7: "hr",
    8: "NDR",
    9: "NDR",
    10: "WDR",
    11: "SWR",
    12: "SR",
    13: "MDR",
    14: "MDR",
    15: "NDR",
    16: "MDR"
}

broadcasterRevenues = {
    1: 1065000000,
    2: 962000000,
    3: 429000000,
    4: 429000000,
    5: 46000000,
    6: 1020000000,
    7: 435000000,
    8: 1020000000,
    9: 1020000000,
    10: 1224000000,
    11: 1065000000,
    12: 68000000,
    13: 612000000,
    14: 612000000,
    15: 1020000000,
    16: 612000000
}

broadcasterEmployees = {
    1: 3244,
    2: 3163,
    3: 1481,
    4: 1481,
    5: 189,
    6: 3399,
    7: 1730,
    8: 3399,
    9: 3399,
    10: 3905,
    11: 3244,
    12: 567,
    13: 1975,
    14: 1975,
    15: 3399,
    16: 1975
}

broadcasterResidents = {
    1: 15000000,
    2: 12900000,
    3: 6000000,
    4: 6000000,
    5: 700000,
    6: 14200000,
    7: 6200000,
    8: 14200000,
    9: 14200000,
    10: 17900000,
    11: 15000000,
    12: 1000000,
    13: 8500000,
    14: 8500000,
    15: 14200000,
    16: 8500000
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

    def getRegionResidents(self, regionId):
        regionResident = regionResidents.get(regionId)
        if(regionResident):
            return regionResident
        return regionId

    def getBroadcasterName(self, regionId):
        broadcasterName = broadcasterNames.get(regionId)
        if(broadcasterName):
            return broadcasterName
        return regionId

    def getBroadcasterNameShorthand(self, regionId):
        broadcasterNameShorthand = broadcasterNameShorthands.get(regionId)
        if(broadcasterNameShorthand):
            return broadcasterNameShorthand
        return ""

    def getBroadcasterRevenue(self, regionId):
        broadcasterRevenue = broadcasterRevenues.get(regionId)
        if(broadcasterRevenue):
            return broadcasterRevenue
        return regionId

    def getBroadcasterEmployees(self, regionId):
        broadcasterEmployee = broadcasterEmployees.get(regionId)
        if(broadcasterEmployee):
            return broadcasterEmployee
        return regionId

    def getBroadcasterResidents(self, regionId):
        broadcasterResident = broadcasterResidents.get(regionId)
        if(broadcasterResident):
            return broadcasterResident
        return regionId

    def match(self, regionId):
        region = Region()
        region.id = regionId
        region.name = self.getName(regionId)
        region.isoCode = self.getIsoCode(regionId)
        region.regionResidents = self.getRegionResidents(regionId)
        region.broadcasterName = self.getBroadcasterName(regionId)
        region.broadcasterNameShorthand = self.getBroadcasterNameShorthand(regionId)
        region.broadcasterRevenue = self.getBroadcasterRevenue(regionId)
        region.broadcasterEmployees = self.getBroadcasterEmployees(regionId)
        region.broadcasterResidents = self.getBroadcasterResidents(regionId)
        return region


class Region:
    id = ""
    name = ""
    isoCode = ""
    regionResidents = ""
    broadcasterName = ""
    broadcasterNameShorthand = ""
    broadcasterRevenue = ""
    broadcasterEmployees = ""
    broadcasterResidents = ""
