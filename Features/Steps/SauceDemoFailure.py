from behave import *
from selenium import webdriver


@given('Launching Chrome browser')
def LaunchDriver(context):
    context.driver = webdriver.Chrome("C:\\Users\Asus\\Downloads\\chromedriver_win32\\chromedriver.exe")
    context.driver.maximize_window()

@when('I am on Demo Login Page')
def SauceDemoPage(context):
    context.driver.get("https://www.saucedemo.com/")


@when('I fill account information to account LockedOutUser to the Username "{user}" to the Password "{pswd}"')
def EnterCredentials(context, user, pswd):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element("id", "user-name").send_keys(user)
    context.driver.find_element("id", "password").send_keys(pswd)


@when('I click Login Button')
def ActionLogin(context):
    context.driver.find_element("xpath", "//input[@type='submit']").click()


@then('I verify the Error Message contains the text "Sorry, this user has been banned. "')
def VerifyPageLogo(context):
    status2 = context.driver.find_element("xpath", "//h3[contains(text(),'Epic sadface: Sorry, this user has been locked out.')]").is_displayed()
    print(status2)
    assert status2 is True
    # assert status2 == "Epic sadface: Sorry, this user has been locked out."
