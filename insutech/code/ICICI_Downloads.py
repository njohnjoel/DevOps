# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 07:04:47 2021

@author: DUBBARS
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:10:54 2021

@author: AA
"""
import pandas as pd
from selenium import webdriver
import time




cols = ["CARD NUMBER","AGE"]
df = pd.read_csv(r"/proj/code/input/ic.csv", delimiter=',',usecols=cols)

downloadPath="/proj/code/output"

for index, row in df.iterrows():
    print(row['CARD NUMBER'], row['AGE'])
    options = webdriver.ChromeOptions()
    prefs = {}
    prefs["profile.default_content_settings.popups"]=0
    prefs["download.default_directory"]=downloadPath
    options.add_argument("--incognito")
    options.add_experimental_option("prefs", prefs)
    #options.addArguments("--no-sandbox"); # Bypass OS security model
    options.add_argument("--no-sandbox"); # Bypass OS security model
   # options.add_argument('headless')
 
    driver = webdriver.Chrome(options=options ,executable_path="/proj/software/chrome_driver/chromedriver")
    driver.maximize_window()
    driver.get("https://ilhc.icicilombard.com/Customer/iCard")
    
    #time.sleep(9) # Sleep for 60 seconds
    
    driver.find_element_by_id("NonRetail").click();
    
   # cnum="IL19093120100"
   # age="36"
    cnum=row['CARD NUMBER']
    age=int(row['AGE'])
 
    
    CardNumber = driver.find_element_by_name("CardNumber_CORPORATE")
    Cage = driver.find_element_by_name("AGE")
    CardNumber.send_keys(cnum)
    Cage.send_keys(age)
    
    driver.find_element_by_id("searchbtn").click();
    
    driver.find_element_by_id("SaveasPDF").click();
    
    
    
    
    time.sleep(3) # Sleep for 60 seconds
    driver.close()
driver.quit()
