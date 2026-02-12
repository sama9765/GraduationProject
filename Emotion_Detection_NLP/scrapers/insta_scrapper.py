from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
URL = "https://www.instagram.com/"
driver.get(URL)
comment_list = []
time.sleep(4)

username = driver.find_element(By.NAME, 'username')
username.send_keys('--INSTA USERNAME--')

password = driver.find_element(By.NAME, 'password')
password.send_keys('--PASSWORD--')

login_button = driver.find_element(By.XPATH, "//div[text()='Log in']")
login_button.click()

time.sleep(10)

with open("commentscrape/comments.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Comment"])
    search_icon = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Search']")
    search_icon.click()

    time.sleep(7)
    i = 0

    def searchfunction(i):

        #li = ['natgeo','animalplanet','harlowandsage','thedogist','theminimalists','thegoodtrade','voguemagazine','marvel entertainmnt','netflixus','espn','bbcearth','steveyeun','CNN',"nytimes",'Pubity', 'Nba', 'fifa']
        # li = ['washingtonpost','financialtimes','thegoodquote','psych_today','selfcareisforeveryone','unicef','humanrightswatch','earthpix']

        # li = [
        # "9GAG",
        # "Daquan",
        # "Pubity",
        # "F*ckjerry",
        # "Memes",
        # "LadBible",
        # "Funnyhoodvidz",
        # "Epicfunnypage",
        # "The Fat Jewish",
        # "Worldstar"
        # ]

        li = [
    "NASA",
    "National Geographic",
    "TED",
    "Interesting Engineering",
    "Science Channel",
    "Futurism",
    "WIRED",
    "Business Insider",
    "SpaceX",
    "Tech Insider"
]



        search_input = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Search input']")
        search_input.send_keys(li[i])

        time.sleep(5)

        try:
            search_click = driver.find_element(By.CSS_SELECTOR,
                                               '.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1cy8zhl.x1oa3qoh.x1nhvcw1')
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(search_click)).click()
        except Exception as e:
            print(f"Couldn't click on the search result for {li[i]}. Error: {e}. Moving to next.")
            return  # Skip to the next item in the list

        time.sleep(4)

        scroll_times = 40
        for scr in range(scroll_times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        posts = driver.find_elements(By.CLASS_NAME, '_aagu')

        for post1 in posts:
            try:
                post1.click()
                time.sleep(2)

                div1 = driver.find_element(By.CSS_SELECTOR,
                                           '.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd')
                div2 = div1.find_element(By.CSS_SELECTOR,
                                         '.x78zum5.xdt5ytf.x1iyjqo2.xs83m0k.x2lwn1j.x1odjw0f.x1n2onr6.x9ek82g.x6ikm8r.xdj266r.x11i5rnm.x4ii5y1.x1mh8g0r.xexx8yu.x1pi30zi.x18d9i69.x1swvt13')
                div3 = div2.find_element(By.CSS_SELECTOR, '._a9z6._a9za')

                element1 = div3.find_element(By.CSS_SELECTOR,
                                             "div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1:nth-of-type(3)")

                element2 = element1.find_element(By.CSS_SELECTOR,
                                                 ".x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1")
                element3 = element2.find_element(By.CSS_SELECTOR,
                                                 ".x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1")
                time.sleep(2)

                commentlist = element3.find_elements(By.CSS_SELECTOR,
                                                     ".x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1")
                for comment in commentlist:
                    try:
                        ulist1 = comment.find_element(By.CLASS_NAME, '_a9ym')
                        ulist2 = ulist1.find_element(By.CSS_SELECTOR,
                                                     ".x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x2lah0s.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xggy1nq.x11njtxf")
                        ulist3 = ulist2.find_element(By.CSS_SELECTOR, '._a9zj._a9zl')
                        time.sleep(0.1)
                        ulist4 = ulist3.find_element(By.CSS_SELECTOR, '._a9zm')
                        time.sleep(0.1)
                        ulist5 = ulist4.find_element(By.CSS_SELECTOR, '._a9zo')
                        time.sleep(0.1)
                        ulist6 = ulist5.find_element(By.CSS_SELECTOR, '._a9zr')
                        time.sleep(0.1)
                        ulist7 = ulist6.find_element(By.CSS_SELECTOR, '._a9zs')
                        time.sleep(0.1)
                        gg = ulist7.text
                        comment_list.append(gg)
                    except Exception as e:
                        print(f"Error extracting comment: {e}")
                        continue  # Move to the next comment

                print('-' * 80)

                close_post = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Close']")
                close_post.click()

            except Exception as e:
                print(f"Error processing post: {e}")
                continue  # Move to the next post

        time.sleep(5)
        i += 1

        try:
            search_icon = driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Search']")
            search_icon.click()
        except Exception as e:
            print(f"Error clicking search icon: {e}")
            return  # If search icon click fails, exit the function

        if i < len(li):
            searchfunction(i)

    searchfunction(i)

    with open("commentscrape/comments6.json", "w", encoding="utf-8") as json_file:
        json.dump(comment_list, json_file, ensure_ascii=False, indent=4)

driver.close()