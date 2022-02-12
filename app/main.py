import os
import time
import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with


class AutoBuyBot:
    def __init__(self):
        self.driver = self.setUp()

    def setUp(self):
        options = Options()
        options.add_argument("start-maximized")
        options.add_extension(r"app\metamask_extension.crx")

        driver = webdriver.Chrome(
            "C:/Users/bajri/.vscode/chromedriver.exe", options=options)
        return driver

    def moboxLogin(self):
        self.driver.get(
            r"https://www.mobox.io/login/?redirect=https%3A%2F%2Fwww.mobox.io%2F%23%2F")
        # self.driver.find_element_by_xpath(
        #     r"//*[@id='app']/div/div[2]/div[2]/div/div[2]/div/div")
        self.driver.find_element(
            By.XPATH, "//*[@id='app']/div[2]/div/div[3]/div[1]/div[2]/input").send_keys("Your_GMail_Address")
        self.driver.find_element(
            By.XPATH, "//*[@id='app']/div[2]/div/div[3]/div[2]/div[2]/input").send_keys("Your_Mobox_Password")
        self.driver.find_element(
            By.XPATH, "//*[@id='app']/div[2]/div/button/span").click()

        return

    def openMoboxMarket(self):
        self.driver.switch_to.new_window()
        self.driver.get(
            r"https://www.mobox.io/home/#/iframe/momo?path=market&tab=0")

        return

    def metaMaskLogin(self):
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element(
            By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/button").click()
        self.driver.find_element(
            By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button").click()
        self.driver.find_element(
            By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]").click()

        time.sleep(1)
        # Secret Recovery Phrase
        secret_recovery_phrase = self.driver.find_element(
            By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/form/div[4]/div[1]/div/input")
        secret_recovery_phrase.clear()
        secret_recovery_phrase.send_keys("Your_Metamask_secret_recovery_phrase")

        # New Password
        self.driver.find_element(By.ID, "password").send_keys("Your_New_Passowrd")

        # password.send_keys("Password")
        return


if __name__ == "__main__":
    seleniumWorkFlow = AutoBuyBot()
    seleniumWorkFlow.moboxLogin()
    # seleniumWorkFlow.openMoboxMarket()
    seleniumWorkFlow.metaMaskLogin()


# pyautogui.click(1255, 206)
# time.sleep(0.28)
# pyautogui.click(960, 525)


# MetaMask secret recovery phrase
# pyautogui.click(700, 380)
# pyautogui.write("Secret Recovery Phrase TEXT")

# MetaMask new password
# pyautogui.click(710, 515)
# pyautogui.write("YOUR_PASSWORD")

# MetaMask confirm new password
# pyautogui.click(680, 620)
# pyautogui.write("YOUR_PASSWORD")

# Ticks "Terms of Usee" checkbox
# pyautogui.click(610, 700)

# Click "Import" button
# pyautogui.click(670, 770)

# Click "Import" button
# pyautogui.click(700, 642)

# driver.close()


# The following example may help you to make a better program
# frame_element = WebDriverWait(driver, 120).until(EC.visibility_of_element_located((By.name, "injectedUl"))
# driver.switchTo().frame(driver.find_element_by_name("injectedUl"));
# driver.find_element_by_id("email"))send_keys("abc@gmail.com");
# driver.find_element_by_id("password")send_keys("asdsa");
# driver.find_element_by_id("btnLogin")).click();


# driver.quit()
