import requests
from bs4 import BeautifulSoup

for line in open("ELECTION_ID"):
    id_codes = line.split()[-1]
    url = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(id_codes)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,"html.parser")


    year = line.split()[0]
    file_name = year+".csv"
    with open(file_name,"w") as out:
        out.write(resp.text)
