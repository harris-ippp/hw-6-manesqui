import requests
from bs4 import BeautifulSoup

url =  "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

with open("ELECTION_ID", "w") as out:
    for row in soup.find_all("tr", "election_item"):
        id_number = row["id"].split("-")[2]
        year = row.find("td", "year first").contents[0]
        out.write("{} {}\n".format(year,id_number))
