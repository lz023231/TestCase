#-*- coding: UTF-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui



# 一直等待某元素可见，默认超时10秒
def now_show(driver,locator, timeout=10):
    try:
        #ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return True
    except TimeoutException:
        return False

# 一直等待某个元素消失，默认超时10秒
def not_show(driver,locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return True
    except TimeoutException:
        return False