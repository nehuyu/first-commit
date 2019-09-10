import requests
from bs4 import BeautifulSoup
import math
import sys 

COMMITS_PER_PAGE = 35

args = sys.argv
if(len(args) == 1): 
    print("ERROR! Repositry URL is necessary.")
    exit(0)

url = args[1]

r = requests.get(url)

soup = BeautifulSoup(r.text,"html.parser")

commits_number = soup.find(class_="commits").find(class_="text-emphasized").text.replace(" ","").replace("\n","").replace(",", "")

page_number = math.ceil(int(commits_number) / COMMITS_PER_PAGE) 
print(url + "/commits/master?page=" + str(page_number))
