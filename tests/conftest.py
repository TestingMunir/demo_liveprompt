import time
import pytest
from selenium import webdriver
from datetime import date
import re
import pandas as pd
import pytest
import os
from datetime import datetime
from pytest_html import extras


from Utilities.XLPANA import pd_writeData, pd_save_excel

#
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", )
    parser.addoption("--env", action="store", default="live",)
@pytest.fixture(scope="class")
def setup(request):
    global driver
    global gekodriver
    global env_name
    global file_path_automation_format
    global Auto_format_data
    global test_start_time

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        option = webdriver.ChromeOptions()
        # settings for geko driver
        # https://python.tutorialink.com/expected-browser-binary-location-but-unable-to-find-binary-in-default-location-no-mozfirefoxoptions-binary-capability-provided/
        # https://stackoverflow.com/questions/64034859/invalidargumentexception-message-binary-is-not-a-firefox-executable-error-usin
        # options = webdriver.FirefoxOptions()
        # options.binary_location = r'C:\Users\ustad.shafiyodin\AppData\Local\Mozilla Firefox\firefox.exe'
        # gekodriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        # --------------------------end of setting for geko driver-----------------------------------------------------------

        # display = Display(visible=0, size=(800, 800))
        # display.start()
        option.add_argument("--no-sandbox")  # Bypass OS security model
        #option.add_argument('--headless')
        # option.add_argument('--no-sandbox')
        # option.add_argument('--disable-dev-shm-usage')

        #chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        #chrome_options.add_argument("--disable-gpu")
        #chrome_options.add_argument("--no-sandbox")
        #chrome_options.add_argument("--window-size=1920,1080")

        # Connect to Selenium Grid
        #grid_url = "http://selenium-hub:4444/wd/hub"
        #driver = webdriver.Remote(
        #   command_executor=grid_url,
        #   options=chrome_options
        driver = webdriver.Chrome(options=option)

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    # selecting env_name from the command line default is dev
    env_name = request.config.getoption("env")
    if env_name == "live":
        driver.get("https://www.liveprompt.ai/")
    elif env_name == "uat":
        #Auto_format_data = pd_get_file(path=file_path_automation_format, )
        driver.get("https://uat.liveprompt.ai/")

    elif env_name == "dev":
        #Auto_format_data = pd_get_file(path=file_path_automation_format, )
        driver.get("https://dev.liveprompt.ai/")

    #start time of test case
    from datetime import datetime
    now = datetime.now()
    test_start_time = now.strftime("%H-%M-%S")
    driver.implicitly_wait(4)
    driver.maximize_window()

    # gekodriver.get("https://dev.netscribes.app/login")
    # gekodriver.implicitly_wait(3)
    # gekodriver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()




def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

## Customize report title
def pytest_html_report_title(report):
    report.title = "Live prompt.ai Automation Report"

# Add custom HTML to the summary section
from pytest_html import extras
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        extras.html("<p><strong>Tested by:</strong> Munir </p>"),
    ])


@pytest.fixture(scope="session")
def env_name(request):
    return request.config.getoption("env")



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        driver = getattr(item.cls, "driver", None)
        if report.when == "call" and report.failed:
            # Create screenshots folder if it doesn't exist
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            #create reports directory
            os.makedirs("Reports", exist_ok=True)
            print("screenshots_dir:-", screenshots_dir)
            testcase_node_list = report.nodeid.split("::")
            testcase_name_including_testfile_name = testcase_node_list[1] + "_" + testcase_node_list[2]
            testcase_name=testcase_node_list[2]
            current_subdir=os.getcwd()+"\\"+"screenshots" + "\\" + testcase_node_list[1]
            print("file name from report:", testcase_name_including_testfile_name)
            print("current_dir:", os.getcwd())
            print("current_subdir:", current_subdir)
            #create subdirectory
            #screenshots_sub_dir = os.path.join(os.getcwd(),testcase_node_list[1])
            os.makedirs(current_subdir, exist_ok=True)
            # Filename with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{testcase_name}_{timestamp}.png"
            file_path = os.path.join(current_subdir, file_name)
            print("file_name:-",file_name)
            driver.save_screenshot(file_path)
            screenshot = driver.get_screenshot_as_base64()
            #extra.append(pytest_html.extras.image(screenshot, ''))
            # Add clickable image (thumbnail → full image in new tab)
            html = f'''
            <div style="float:right; margin-left:10px; margin-bottom:0; padding-bottom:0; width:250px; aspect-ratio:16/9;">
                <a href="file://{file_path}" target="_blank" style="display:block; width:100%; height:100%;">
                    <img src="data:image/png;base64,{screenshot}" 
                         style="width:100%; height:100%; object-fit:cover; display:block; margin:0; padding:0;"/>
                </a>
            </div>
            '''
            extra.append(pytest_html.extras.html(html))

        report.extra = extra

