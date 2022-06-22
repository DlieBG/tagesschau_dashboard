interesting_phrases = [
    "FC",
]

corona = 'Corona'

alias = {
    'Corona-Pandemie': corona,
    'Coronavirus': corona,
    'Coronavirus in Deutschland': corona,
    'Covid-19': corona,
    'SARS-CoV-2': corona,
    
    'Abschiebungen': 'Abschiebung',
    
    'Abtreibungen': 'Abtreibung',
    
    'AFD': 'AfD',
    
    'Atomkraft': 'Atomenergie',
    'Atomkraftwerke': 'Atomenergie',
    
    'Baden Württemberg': 'Baden-Württemberg',
    
    'Booster-Impfstoff': 'Booster',
    
    'Coronaimpfstoffe': 'Corona-Impfstoff',
    
    'Cum Ex': 'Cum-Ex',
    
    'Cyber-Attacke': 'Cyberangriff',
    'Cyberangriffe': 'Cyberangriff',
    
    'Deutsch Bahn': 'Deutsche Bahn',
    
    'documentafifteen': 'documenta15',
    
    'Elektroautos': 'Elektroauto',
    
    'Energiekonzerne': 'Energiekonzern',
    
    'Energiekosten': 'Energiepreis',
    'Energiepreise': 'Energiepreis',
    
    'Entlastungen': 'Entlastung',
    
    'Erneuerbare Energien': 'Erneuerbare Energie',
        
    'EUGH': 'EuGH',
    
    'Exporte': 'Export',
        
    'Finnalnd': 'Finnland',
    
    'Flughäfen': 'Flughafen',
    
    'Formel1': 'Formel 1',
    'Formel 1 (Extern)': 'Formel 1',
    
    'Frankkreich': 'Frankreich',
    
    'Frauenfußball': 'Frauen-Fußball',
    'Fussball': 'Fußball',
    'Fußball Bundesliga': 'Fußball-Bundesliga',
    'Fußball-Europameisterschaft': 'Fußball-EM',
    
    'Gaslieferungen': 'Gaslieferung',
    
    'Gesundheits App': 'Gesundheits-App',
    'Gesundheitsapps': 'Gesundheits-App',
    
    'Gewerkschaften': 'Gewerkschaft',
    
    'Häfen': 'Hafen',
    
    'Hauptverammlung': 'Hauptversammlung',
    
    'Heizungen': 'Heizung',
    
    'Hepatitits': 'Hepatitis',
    
    'IG Metall': 'IG-Metall',
    
    'Immobilien-Branche': 'Immobilienbranche',
    
    'Impfstoffe': 'Impfstoff',
    'Impfstoffdosen': 'Impfstoff',
    
    'Infekionsschutzgesetz': 'Infektionsschutzgesetz',
    
    'Islamischer Saat': 'IS',
    
    'ISS Raumstation': 'ISS',
    
    'Kryptogeld': 'Kryptowährung',
    'Kryptowährungen': 'Kryptowährung',
    
    '#kt22': 'kt22',
    
    'Lieferengpässe': 'Lieferengpass',
    
    'LNG Flüssiggas': 'LNG',
    
    'Long Covid': 'Long-Covid',
    
    'Lugansk': 'Luhansk',
    
    'Maskenaffäre': 'Masken-Affäre',
    
    'McDonalds': "McDonald's",
    
    'Mercedes': 'Mercedes-Benz',
    
    'Mieten': 'Miete',
    
    'NewYork': 'New York',
    
    'Nordrehien-Westfalen': 'Nordrhein-Westfalen',
    
    #'Panzerhaubitzen': 'Panzer',
    
    'Personalproblem': 'Personalmangel',
    
    'Präsidentenwahl': 'Präsidentschaftswahl',
    
    'Schleswig Holstein': 'Schleswig-Holstein',
    
    'Schwangerschaftsabbrüche': 'Schwangerschaftsabbruch',
    
    'Seenotretter': 'Seenotrettung',
    
    'Sexueller Missbrauch': 'Sexuelle Gewalt',
    'Sexuelle Übergriffe': 'Sexuelle Gewalt',
    
    'Sjewjerodonzek': 'Sjewjerodonezk',
    
    'Photovoltaik': 'Solarenergie',
    'Solar': 'Solarenergie',
    'Solarbranche': 'Solarenergie',
    'Solaranlagen': 'Solarenergie',
    'Solarzellen': 'Solarenergie',
    
    'Spekulationen': 'Spekulation',
    
    'Spritkosten': 'Spritpreise',
    
    #'Staatsfonds': 'Staatsanleihen'
    
    'Staatsverschuldung': 'Staatsschulden',
    
    'Steuern': 'Steuer',
    
    'tagesschau': 'Tagesschau',
    
    #'Todesurteil': 'Todesstrafe',
    
    'US-Waffenrecht': 'US-Waffengesetze',
    
    'Verbraucherzentralen': 'Verbraucherzentrale',
    
    'Verfassungschutz': 'Verfassungsschutz',
    
    'Verbrennungsmotoren': 'Verbrennungsmotor',
    
    'Vfl Wolfsburg': 'VFL Wolfsburg',
    #'VfB Wolfsburg': 'VFL Wolfsburg',
    
    'Volkswagen': 'VW',
    
    'Waffenrecht': 'Waffengesetze',
    #'Waffenkontrolle': 'Waffengesetze',
    
    'Wahlen': 'Wahl',
    
    'Waldbrände': 'Waldbrand',
    
    'Wasserknappheit': 'Wassermangel',
    
    'Weizenpreise': 'Weizenpreis',
    
    'Windenergie': 'Windkraft',
    'Windkraftanlagen': 'Windkraft',
    
    'WIrtschaft': 'Wirtschaft',
    
    'WM2022': 'WM 2022',
    
    'Youtube': 'YouTube',
    'YouTube Shorts': 'YouTube',
    
    'Zugunglueck': 'Zugunfall',
    'Zugunglück': 'Zugunfall',
    #'Zugkollision': 'Zugunfall',
    'Zugverkehr': 'Zug',
    'Züge': 'Zug',
}

class Cleaner:

    def __init__(self):
        self.interesting = set()

    def clean(self, tag):
        if self.check_interesting(tag):
            self.interesting.add(tag)
        
        clean_tag = alias.get(tag)
        if clean_tag:
            return clean_tag
        return tag

    def unique(self, seq):
        seen = set()
        for item in seq:
            if item not in seen:
                seen.add(item)
                yield item
    
    def check_interesting(self, tag):
        return any(phrase in tag for phrase in interesting_phrases) 
    
    def get_interesting_tags(self):
        return list(self.interesting)