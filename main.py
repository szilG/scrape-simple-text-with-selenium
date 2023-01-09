from selenium import webdriver

def get_driver():
  # Set option to make browsing easier
  # create options using webdriver.ChromeOptions
  options = webdriver.ChromeOptions()
  # infobar may interfere with the script so disable it
  options.add_argument("disable-infobars")
  # start the browser as maximized.
  options.add_argument("start-maximized")
  # to avoid some issues that occur when you interact with a browser on a Linux computer
  options.add_argument("disable-dev-shm-usage")
  # disable browser security
  options.add_argument("no-sandbox")
  # to help selenium to avoid detection from the browser
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/")
  return driver

def main():
  driver = get_driver()
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  return element.text

print(main())