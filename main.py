from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

driver = webdriver.Chrome()
login_email = 'email@gmail.com'
login_password = 'Test123!!'
post_text = 'Hello World!!'

try:
    # Navigate to the page asking to accept cookies so it won't ask again later
    driver.get('https://mbasic.facebook.com/cookie/consent_prompt/?next_uri=https%3A%2F%2Fmbasic.facebook.com%2F&refsrc=deprecated&_rdr')

    # Find the buttons and click on the first one 'Refuse optional cookies'
    buttons = driver.find_elements(By.NAME, 'accept_only_essential')
    ActionChains(driver).click(buttons[0]).perform()

    # Wait for the email input to be present to avoid the 'element not found' exception
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, 'email')))

    # Find the email input, insert the email
    driver.find_element(By.NAME, 'email').send_keys(login_email)

    # Find the password input, insert the password
    driver.find_element(By.NAME, 'pass').send_keys(login_password)

    # Find the login button and click
    login_button = driver.find_element(By.NAME, 'login')
    ActionChains(driver).click(login_button).perform()

    # Here it is necessary to create the management of two-factor authentication
    # input('Press enter after you have passed two-factor authentication and stored the browser')

    # Wait for the textarea to be present to avoid the 'element not found' exception
    WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.NAME, 'xc_message')))

    # Find the textarea, write the post text
    driver.find_element(By.NAME, 'xc_message').send_keys(post_text)

    # Find the button to publish the post and click
    post_button = driver.find_element(By.NAME, 'view_post')
    ActionChains(driver).click(post_button).perform()
    sleep(20)

finally:
    # Close the browser
    driver.quit()
