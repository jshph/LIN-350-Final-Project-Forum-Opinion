from bs4 import BeautifulSoup
import requests
import unicodedata
import lxml
import re
import string

soup = BeautifulSoup(open("ABSA15_Laptops_Test.xml"), "lxml-xml")

tag = soup.Opinion

for ele in soup.find_all():
    if len(ele.attrs) > 0:
        print(ele.attrs)

    
