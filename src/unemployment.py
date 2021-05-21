import requests
import json
import prettytable

class Unemployment:
    def __init__(self, startYear, endYear):
        headers = {'Content-type': 'application/json'}
        data = json.dumps({"seriesid": ['CUUR0000SA0','SUUR0000SA0'],"startyear":f"{str(startYear)}", "endyear":f"{str(endYear)}"})
        p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
        self.json_data = json.loads(p.text)

    def load(self):
        try:
            for dataSeries in self.json_data['Results']['series']:
                    self.x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
                    self.seriesId = dataSeries['seriesID']
                    for item in dataSeries['data']:
                        year = item['year']
                        period = item['period']
                        value = item['value']
                        footnotes=""
                        for footnote in item['footnotes']:
                            if footnote:
                                footnotes = footnotes + footnote['text'] + ','
                        if 'M01' <= period <= 'M12':
                            self.x.add_row([self.seriesId,year,period,value,footnotes[0:-1]])
        except KeyError:
            print("ERROR: Could not locate a key. Has the daily query limit been reached?")
            return
            
    def display_table(self):
        try: 
            output = open(self.seriesId + '.txt','w')
            output.write (self.x.get_string())
            output.close()
        except AttributeError:
            print("ERROR: Could not find attribute, proceeding to display previous table:")
        results = open('SUUR0000SA0.txt', 'r')
        for result in results:
            print(result)
        results.close()