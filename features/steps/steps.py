from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@given("launch chrome page")
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()

@when("open greatify home page")
def step_impl(context):
    context.driver.get("https://qaashokkumar.greatifystg.school/school/login")

@then("verify that the logo present on the page")
def step_impl(context):
    logo = context.driver.find_element(By.XPATH, "//*[@class='school_logo']")
    assert logo.is_displayed()

@then("close browser")
def step_impl(context):
    context.driver.quit()
