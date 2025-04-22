import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@given(u'I launch a new Chrome browser for admission')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()

@when(u'I have open Greatify URL')
def step_impl(context):
    context.driver.get("https://qashok.greatifystg.school/school/login")
    time.sleep(1)



@then(u'I have enter the username and password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='name1']").send_keys("HCSCHOOL0205")
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//*[@placeholder='Enter Password']").send_keys("Ashok@98")
    time.sleep(4)
    context.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(4)


@then(u'Navigate to Admission and fees module')
def step_impl(context):
    time.sleep(3)
    # navigate Admission and Fees Management
    context.driver.find_element(By.XPATH, "//*[@id='leadManagementSection']").click()
    time.sleep(3)
    # navigate Configuration
    context.driver.find_element(By.XPATH, "(//*[@id='sideConfiguration'])[1]").click()
    time.sleep(3)
    # navigate template
    context.driver.find_element(By.XPATH, "//*[@id='pills-time-table']").click()
    time.sleep(2)

    context.driver.find_element(By.XPATH, "//*[@id='pills-time-table']").click()
    time.sleep(2)

    context.driver.find_element(By.XPATH, "//*[@id='pills-time-table']").click()
    time.sleep(2)