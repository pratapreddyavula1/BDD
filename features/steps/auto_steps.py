from behave import given, when, then
from selenium.webdriver.common.by import By

@given(u'launch the application')
def step_launch(context):
    context.driver.get("https://automationexercise.com/")

@when(u'navigate to the login page')
def step_login_page(context):
    context.driver.find_element(By.XPATH, "//a[normalize-space()='Signup / Login']").click()

@when(u'enter "{username}" and "{password}"')
def step_enter_credentials(context, username, password):
    context.driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys(username)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

@then(u'verify login result')
def step_verify(context):
    print("✅ Title of the page:", context.driver.title)

@then(u'close the browser')
def step_close(context):
    context.driver.quit()
