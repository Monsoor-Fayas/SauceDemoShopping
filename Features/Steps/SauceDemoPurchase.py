from behave import *
from selenium import webdriver


@given('I am launching Chrome browser')
def LaunchBrowser(context):
    context.driver = webdriver.Chrome("C:\\Users\Asus\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # context.driver.maximize_window()

@when('I am in the Demo Login Page')
def SaudeDemoPage(context):
    context.driver.get("https://www.saucedemo.com/")


@when('I fill account information on account StandardUser to the Username "{user}" to the Password "{pswd}"')
def EnterCredentials(context, user, pswd):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element("id", "user-name").send_keys(user)
    context.driver.find_element("id", "password").send_keys(pswd)


@when('I clicked the Login Button')
def ActionLogin(context):
    context.driver.find_element("xpath", "//input[@type='submit']").click()



@then('I am redirected to Demo Main Page "{prdct}"')
def SauceDemoMainPage(context, prdct):
    try:
        textu = context.driver.find_element("xpath", "//span[@class='title']").text
        assert prdct == textu
    except:
        context.driver.close


@when('User sorts products from low price to high price "{filterLetter}"')
def SetFiler(context, filterLetter):
    context.driver.find_element("xpath", "//select[@class='product_sort_container']").click()
    context.driver.find_element("xpath", "//select[@class='product_sort_container']").send_keys(filterLetter)


@when('user adds lowest priced product')
def ProductSelection(context):
    context.driver.find_element("xpath", "//div[text() = 'Sauce Labs Onesie']").click()
    context.driver.find_element("xpath", "//button[@id='add-to-cart-sauce-labs-onesie']").click()


@when('user clicks on cart')
def AddToCart(context):
    context.driver.find_element("xpath", "//a[@class='shopping_cart_link']").click()


@when('user clicks on checkout')
def ChecksOut(context):
    context.driver.find_element("xpath", "//button[@id='checkout']").click()


@then('user enters firstname "{fname}" lastname "{lname}" zipcode "{zip}"')
def UserDetails(context, fname, lname, zip):
    context.driver.find_element("xpath", "//input[@id='first-name']").send_keys(fname)
    context.driver.find_element("xpath", "//input[@id='last-name']").send_keys(lname)
    context.driver.find_element("xpath", "//input[@id='postal-code']").send_keys(zip)


@then('user clicks Continue button')
def Continuation(context):
    context.driver.find_element("xpath", "//input[@id='continue']").click()


@then('I verify in Checkout overview page if the total amount for the added item is "{amnt}"')
def VerifyAmount(context, amnt):
    amount = context.driver.find_element("xpath", "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[8]").text
    assert amnt == amount


@when('user clicks Finish button')
def FinishButton(context):
    context.driver.find_element("xpath", "//button[@id='finish']").click()


@then('Thank You header is shown in Checkout Complete page')
def HeaderVerify(context):
    ordePlaced = context.driver.find_element("xpath", "//h2[contains(text(),'Thank you for your order!')]").is_displayed()
    assert ordePlaced is True
    context.driver.close()

