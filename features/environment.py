from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# ---------------------- GLOBAL HOOKS ----------------------

def before_all(context):
    print("\n Test execution started for all features")
    context.global_data = {}

def after_all(context):
    print("\n All features execution completed")


# ---------------------- FEATURE LEVEL HOOKS ----------------------

def before_feature(context, feature):
    print(f"\n Starting Feature: {feature.name}")

def after_feature(context, feature):
    print(f" Completed Feature: {feature.name}")


# ---------------------- SCENARIO LEVEL HOOKS ----------------------\
def before_scenario(context, scenario):
    print(f"\n Starting Scenario: {scenario.name}")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()

def after_scenario(context, scenario):
    print(f" Completed Scenario: {scenario.name}")
    if hasattr(context, "driver"):
        context.driver.quit()


# ---------------------- STEP LEVEL HOOKS ----------------------

def before_step(context, step):
    print(f"️ Starting Step: {step.name}")

def after_step(context, step):
    if step.status == "passed":
        print(f" Step Passed: {step.name}")
    elif step.status == "failed":
        print(f" Step Failed: {step.name}")
