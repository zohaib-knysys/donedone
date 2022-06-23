from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys


def susti():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://3dusernetltd.harvestapp.com/time")
    email = driver.find_element(By.ID,'email')
    email.send_keys('ahasan@knysys.com')
    password = driver.find_element(By.ID,'password')
    password.send_keys('knysys@123')
    time.sleep(2)

    driver.find_element(By.ID,'log-in').send_keys(Keys.RETURN)
    time.sleep(5)

    driver.get("https://2-app.donedone.com/5606/project/15980?default_filter_id=6&sort=updated-recent&due_type=-1&search_term=#777&page=1")
    time.sleep(5)

    Demail = driver.find_element(By.ID,'txtEmail')
    Demail.send_keys('ahasan@knysys.com')
    Dpassword = driver.find_element(By.ID,'txtPassword')
    Dpassword.send_keys('knysys@123')
    driver.find_element(By.ID,'btnSubmit').send_keys(Keys.RETURN)

    time.sleep(2)
    driver.get("https://2-app.donedone.com/5606/project/15980?default_filter_id=6&sort=updated-recent&due_type=-1&search_term=#777&page=1")

    time.sleep(5)
    task_number = '#'+str(sys.argv[2])
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[1]/div/input').send_keys(task_number)
    time.sleep(2)

    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[3]/div/table/tr[2]').click()
    time.sleep(2)

    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/main/div/div/div[2]/div[1]/div/div/i').click()

    time.sleep(8)
    iframe = driver.find_element(By.XPATH,'//iframe[@class="harvest-iframe"]')
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/button[1]').click()
    time.sleep(5)

    window_before = driver.window_handles[0]
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    driver.find_element(By.CLASS_NAME,'account').click()
    time.sleep(3)
    driver.switch_to.window(window_before)
    time.sleep(2)
    iframe = driver.find_element(By.XPATH,'//iframe[@class="harvest-iframe"]')
    driver.switch_to.frame(iframe)
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/form/div[5]/div[1]/button').click()
    time.sleep(5)
    driver.close()
    return "you saved your precious 5 minutes !!!"

def more_susti():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://3dusernetltd.harvestapp.com/time")
    email = driver.find_element(By.ID,'email')
    email.send_keys('ahasan@knysys.com')
    password = driver.find_element(By.ID,'password')
    password.send_keys('knysys@123')
    time.sleep(2)
    driver.find_element(By.ID,'log-in').send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_elements(By.XPATH,'//span[contains(text(), "Stop")]')[0].click()
    print('Got ya')
    time.sleep(5)
    driver.close()
    return "Remember to start again !!"

if __name__ == "__main__":
    if len(sys.argv) == 3:
        if sys.argv[1] == "start":
            susti()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "stop":
            more_susti()
        else:
            print('Neend mai hai kya?')
    else:
        print('Task Number bhi dalna hai !!')