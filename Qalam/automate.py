import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Qalam import LoginID, Password


class Automate(webdriver.Chrome):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        dir = os.path.join(os.getcwd(), "chromedriver_win32", "chromedriver.exe")
        super(Automate, self).__init__(dir, options=options)
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def LoginPage(self):
        self.get("https://qalam.nust.edu.pk/")
        self.find_element(By.ID, 'login').send_keys(LoginID)
        self.find_element(By.ID, 'password').send_keys(Password)
        # self.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        try:
            WebDriverWait(self, 15).until(EC.title_is('Odoo'))
        except Exception as e:
            print('An error has occured...')
            exit()
        self.find_element(By.ID, 'sidebar_main_toggle').click()

    def GetACResultsPage(self):
        self.LoginPage()
        self.find_element(By.CSS_SELECTOR, 'a[href="/student/results/"]').click()
        return self.page_source

    def GetPCResultsPage(self):
        self.LoginPage()
        self.find_element(By.CSS_SELECTOR, 'a[href="/student/results/"]').click()
        self.find_element(By.XPATH, '//*[@id="page_content_inner"]/div/div/div/div/div/ul[1]/li[2]/a').click()
        return self.page_source

    # def GetMenuPage(self, item = 'Dashboard'):
    #     self.LoginPage()
    #     self.find_element(By.CSS_SELECTOR, f'li[title="{item}"]').click()
    #     return self.page_source