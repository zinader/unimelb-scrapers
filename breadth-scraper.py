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
import csv


URL = "https://handbook.unimelb.edu.au/search?types%5B%5D=subject&year=2021&subject_level_type%5B%5D=all&study_periods%5B%5D=all&area_of_study%5B%5D=all&org_unit%5B%5D=all&breadth_course_codes%5B%5D=B-SCI&campus_and_attendance_mode%5B%5D=all&page=1&sort=_score%7Cdesc"
z = 1;

with open('breadth_science.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Subject Name","Subject code"])
    #No. of pages written on the handbook page
    while(z<49):
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser') 
        z = z + 1;
        # Dict to be converted to df
        majors = {}
        links = soup.findAll('div',class_='search-result-item__name')


        for i in links:
            c = i.text
            subject_name = c[:-9]
            subject_code = c[-9:]
            writer.writerow([subject_name, subject_code])
            

        URL = "https://handbook.unimelb.edu.au/search?area_of_study%5B%5D=all&breadth_course_codes%5B%5D=B-SCI&campus_and_attendance_mode%5B%5D=all&org_unit%5B%5D=all&page=" + str(z) + "&sort=_score%7Cdesc&study_periods%5B%5D=all&subject_level_type%5B%5D=all&types%5B%5D=subject&year=2021"
        #print(URL)
