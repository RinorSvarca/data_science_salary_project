# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 01:19:34 2020

@author: rinor
"""

import glassdoor_scraper as gs
import pandas as pd

path = r"C:/Users/rinor/source/data_science_salary_project/chromedriver.exe"

df = gs.get_jobs('data scientist', 15, False, path, 15)

df