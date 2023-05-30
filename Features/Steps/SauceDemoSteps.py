from behave import *
from selenium import webdriver


@given('I launch Chrome browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome("C:\\Users\Asus\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()


@when('I am on the Demo Login Page')
def SaudeDemoPage(context):
    context.driver.get("https://www.saucedemo.com/")


@when('I fill the account information to account StandardUser to the Username "{user}" to the Password "{pswd}"')
def EnterCredentials(context, user, pswd):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element("id", "user-name").send_keys(user)
    context.driver.find_element("id", "password").send_keys(pswd)


@when('I click the Login Button')
def ActionLogin(context):
    context.driver.find_element("xpath", "//input[@type='submit']").click()



@then('I am redirected to the Demo Main Page "{prdct}"')
def SauceDemoMainPage(context, prdct):

    textu = context.driver.find_element("xpath", "//span[@class='title']").text

    if textu == "Products":
        assert prdct == textu


@then('I verify the App Logo exists')
def VerifyPageLogo(context):
    try:
        status = context.driver.find_element("xpath", "//div[contains(text(),'Swag Labs')]").is_displayed()

    except:
        context.driver.close
    print(status)
    assert status is True

