import requests
import urllib.request
import xlsxwriter
from bs4 import BeautifulSoup
import webbrowser
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotVisibleException
from optparse import OptionParser

class SportsOracles():

    def Insta(self, username, password):
        PATH = r"C:\download\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(PATH)

        driver.get("https://www.instagram.com/")

        #login
        time.sleep(2)
        try:
            username1 = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        except:
            time.sleep(3)
            try:
                username1 = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
            except:
                print("COMPUTER TOO SLOW TRY AGAIN")

            print("USERNAME FAILED")
        password1 = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        username1.clear()
        password1.clear()
        username1.send_keys(str(username))
        password1.send_keys(str(password))
        login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        #save your login info?
        time.sleep(3)
        try:
            notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            time.sleep(5)
            notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        #turn on notif
        time.sleep(3)
        try:
            notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            time.sleep(5)
            notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        #searchbox
        time.sleep(2)

        try:
            profile = driver.find_element(By.LINK_TEXT,str(username)).click()
        except:
            print("ERROR1")

        time.sleep(3)
        get_url = driver.current_url
        URL = "https://www.instagram.com/" + username + "/"
        if get_url == URL:
            try:
                profile = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[3]/a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']").click()
                print("SUCCESS")
            except:
                time.sleep(5)
                profile = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[3]/a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']").click()
                get_url1 = driver.current_url
                URL2 = "https://www.instagram.com/" + username + "/following/"
                if get_url1 == URL2:
                    print('SUCCESS')
        else:
            print("ERROR2")

        time.sleep(3)
        people = driver.find_elements(By.CSS_SELECTOR, "._aano ._aba8._abcm:nth-of-type(n) ._ab97._ab9f")
        FollowingList = []
        for element in people:
            if "ollowing" in element.text:
                pass
            else:
                FollowingList.append(element.text)

        link3 = "/html/body/div[2]/div/div/div//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']/div[1]/div"
        instruct = "document.querySelector(" + link3 + ").scrollBy(0,1000)"
        xpath_element = " /html/body/div[2]//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']"
        following = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[3]/a[@role='link']//span[@class='_ac2a']/span")
        followers = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']//span[@class='_ac2a']/span")
        FollowerNum = followers.text
        FollowingNum = following.text
        FollowingScroll = ((int(FollowingNum)/12)+1)*3

        fBody = driver.find_element(By.XPATH, xpath_element)
        scroll = 0
        while scroll < FollowingScroll:
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',fBody)
            scroll += 1
              # add appropriate wait here, of course. 1-2 seconds each
            time.sleep(2)

        try:
            people = driver.find_elements(By.CSS_SELECTOR, "._aano ._aba8._abcm:nth-of-type(n) ._ab97._ab9f")

            for element in people:
                if "ollowing" in element.text:
                    pass

                elif element.text in FollowingList:
                    pass
                else:
                    FollowingList.append(element.text)
        except:
            print("ERROR5")

        print(FollowingList)
        print(len(FollowingList))
        driver.close()
        return FollowingList
    def Insta2(self, username, password):
        PATH = r"C:\download\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(PATH)

        driver.get("https://www.instagram.com/")

        #login
        time.sleep(2)
        try:
            username1 = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        except:
            time.sleep(3)
            try:
                username1 = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
            except:
                print("COMPUTER TOO SLOW TRY AGAIN")

            print("USERNAME FAILED")
        password1 = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        username1.clear()
        password1.clear()
        username1.send_keys(str(username))
        password1.send_keys(str(password))
        login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        #save your login info?
        time.sleep(3)
        try:
            notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            time.sleep(5)
            notnow = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        #turn on notif
        time.sleep(3)
        try:
            notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        except:
            time.sleep(5)
            notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()
        #searchbox
        time.sleep(2)

        try:
            profile = driver.find_element(By.LINK_TEXT,str(username)).click()

        except:
            print("ERROR1")

        time.sleep(3)
        get_url = driver.current_url
        URL = "https://www.instagram.com/"+ username + "/"
        if get_url == URL:
            try:
                profile = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']").click()
                print("SUCCESS")

            except:
                time.sleep(5)
                profile = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']/div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']").click()
                get_url1 = driver.current_url
                URL2 = "https://www.instagram.com/" + username + "/followers/"
                if get_url1 == URL2:
                    print('SUCCESS')
                else:
                    print("ERROR2")

        time.sleep(3)
        people = driver.find_elements(By.CSS_SELECTOR, "._aano ._aba8._abcm:nth-of-type(n) ._ab97._ab9f")
        FollowerList = []
        for element in people:
            if "remove" in element.text:
                pass
            else:
                print(element.text)
                fixed1 = element.text
                fixed2 = fixed1.replace("follow", "")
                FollowerList.append(fixed2)


        link3 = "/html/body/div[2]/div/div/div//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']/div[1]/div"
        instruct = "document.querySelector(" + link3 + ").scrollBy(0,1000)"
        xpath_element = " /html/body/div[2]//div[@class='x1uhb9sk']/div[1]/div/div[2]/div/div/div[@role='dialog']/div/div[@role='dialog']/div/div/div[@class='_aano']"
        followers = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main[@role='main']//section/ul/li[2]/a[@role='link']//span[@class='_ac2a']/span")
        FollowerNum = followers.text
        FollowerScroll = ((int(FollowerNum)/12)+1)*3
        fBody = driver.find_element(By.XPATH, xpath_element)
        scroll = 0
        while scroll < FollowerScroll:
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',fBody)
            scroll += 1
              # add appropriate wait here, of course. 1-2 seconds each
            time.sleep(2)

        try:
            people = driver.find_elements(By.CSS_SELECTOR, "._aano ._aba8._abcm:nth-of-type(n) ._ab97._ab9f")
            for element in people:
                if "remove" in element.text:
                    pass

                elif element.text in FollowerList:
                    pass
                else:
                    print(element.text)
                    fixed1 = element.text
                    fixed2 = fixed1.replace("follow", "")
                    FollowerList.append(fixed2)
        except:
            print("ERROR5")

        print(FollowerList)
        print(len(FollowerList))
        return FollowerList
    def InstaCheck(self, FollowingList, FollowerList):
        NotFollowingYou = []
        for element in FollowingList:
            if element in FollowerList:
                pass
            elif "\nVerified" in element:
                pass
            else:
                NotFollowingYou.append(element)
        print(NotFollowingYou)
        return NotFollowingYou
def main():

        time1 = time.perf_counter()
        username = input("Type Your Instagram Username:\n")
        password = input("Type Your Instagram Password (this is a temporary local instance, no worries): \n")
        temp = username
        temp2 = password
        Following = SportsOracles().Insta(temp, temp2)
        time2 = time.perf_counter()
        time3 = time2-time1
        print(time3, " sec")
        time4 = time.perf_counter()
        Followers = SportsOracles().Insta2(temp, temp2)
        time5 = time.perf_counter()
        time6 = time2-time1
        print(time6, " sec")
        Rude = SportsOracles().InstaCheck(Following, Followers)




if __name__ == "__main__":
    main()
