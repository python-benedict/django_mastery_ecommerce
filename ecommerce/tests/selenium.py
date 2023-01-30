import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#fixture: A collection of data that django knows how to import into a database. or small function we attach to test before they are runed.
@pytest.fixture(scope='function') 
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance
    """
    options = Options() # Assinging a Options method to a variable called options
    options.headless = False # making the options headless to be false so that all the test wont show on a browser for us to see but will rather run on the background
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    browser.close()
