from datetime import datetime
import sqlite3
import requests
import selectorlib



URL = 'http://programmer100.pythonanywhere.com/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect('tempwebscraping/tempdata.db')
cursor = connection.cursor()

def scrape(url):
    request = requests.get(url=url,headers=HEADERS)
    content = request.text
    
    return content


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_string('''
                                                     temp:
                                                        css: "#temperatureId > b"
                                                     ''')
    value = extractor.extract(source)['temp']
    return value


def storetemp(data):
    date = datetime.now()
    present = date.strftime("%Y-%m-%d-%H:%M:%S")
    cursor.execute("INSERT INTO temp VALUES(?,?)",(data,present))
    connection.commit()
        

if __name__=="__main__":
    source = scrape(URL)
    extracted = extract(source=source)
    storetemp(extracted)
