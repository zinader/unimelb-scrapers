import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import unicodedata
import re
import matplotlib.pyplot as plt
import numpy as np
import json
import seaborn as sns


URL = "https://handbook.unimelb.edu.au/2021/courses/b-arts/majors-minors-specialisations"

r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html.parser') 
   
# Dict to be converted to df
majors = {}
links = soup.findAll('td')

for i in links:
	#remove the no. of credits which is 100 for arts
    if(i.text!="100" ):
        print("{ label: '" + i.text + "'," , "core: []},")