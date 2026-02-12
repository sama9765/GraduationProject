import time
import os
import csv
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def linkScrapper(link):
    driver = webdriver.Firefox()
    driver.get(link[0])
    comment_list = []
    time.sleep(4)

    comment_section = driver.find_element(By.ID, "comments")
    driver.execute_script("arguments[0].scrollIntoView();", comment_section)
    time.sleep(5)

    for _ in range(100):
        try:
            print("Current Scroll Number: ", _)
            driver.execute_script("window.scrollBy(0, 1000);")  # Scroll down 1000px
            if _ < 3:
                time.sleep(5)
            else:
                time.sleep(1)
        except:
            break

    section1 = comment_section.find_element(By.ID, 'sections')
    section1_content = section1.find_element(By.ID, 'contents')

    comment_threads = section1_content.find_elements(By.TAG_NAME, 'ytd-comment-thread-renderer')

    for comment_ in comment_threads:
        comment_body = comment_.find_element(By.ID, 'expander')
        comment_list.append(comment_body.text)

    print("Total Comments: ", len(comment_list))

    with open(f"{link[1]}.txt", "w", encoding="utf-8") as file:
        for comment in comment_list:
            file.write(comment + "\n")

    driver.close()
    
links = [
	 ["https://www.youtube.com/watch?v=iyFe0M0zQ0g", "friends funny 2"],
	 ["https://www.youtube.com/watch?v=AGoskvYiQUc","friends last scene- sad"],
	 ["https://www.youtube.com/watch?v=xB60P7ybtP8","friends reunion"],
	 ["https://www.youtube.com/watch?v=k10ETZ41q5o","conjuring trailer- fear, anxiety"],
	 ["https://www.youtube.com/watch?v=dVmOvmH4dL4","Big bang theory-funny"],
	 ["https://www.youtube.com/watch?v=JkBQ53wmn5s","big bang theory-sad"],
 	 ["https://www.youtube.com/watch?v=TWB31WFomz4", "endgame, i am ironman - sad"]]

for link in links:
    linkScrapper(link)
