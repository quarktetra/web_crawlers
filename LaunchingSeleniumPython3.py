browser="Chrome"
#browser="FF"
url="https://www.indeed.com/"

if  browser=="FF":
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    driver = webdriver.Firefox( executable_path='C:\Python3_scheduled\geckodriver.exe')    # get gecko from https://github.com/mozilla/geckodriver/releases
if  browser=="Chrome":
    from selenium import webdriver
    driver = webdriver.Chrome('C:\Python3_scheduled\chromedriver.exe')    # get chrome driver from https://chromedriver.chromium.org/downloads

driver.get(url)
driver.implicitly_wait(10)
