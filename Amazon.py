from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace 'path_to_chromedriver' with the actual path to chromedriver.exe
driver = webdriver.Chrome()

# Open Amazon homepage
driver.get("https://www.amazon.ca")
time.sleep(5)


# Find and click on "All option"
All_option = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[4]/div[1]/a")
All_option.click()
time.sleep(3)

# Find and click on "New Releases"
Newreleases_option = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/ul[1]/li[3]/a")
Newreleases_option.click()
time.sleep(3)

# Select a product
Select_product = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/ol/li[1]/div/div[2]/div/a[2]/span/div")
Select_product.click()
time.sleep(3)

# Select quantity and add to cart
Select_Quantity_Dropdown = driver.find_element("id","selectQuantity")
Select_Quantity_Dropdown.click()
time.sleep(3)

Select_Quantity = driver.find_element("id","quantity_5")
Select_Quantity.click()
time.sleep(3)

add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()
time.sleep(3)

# Proceed to checkout
add_to_cart_button = driver.find_element("id","sc-buy-box-ptc-button")
add_to_cart_button.click()
time.sleep(3)

# Enter email input field,
Email_input_field = driver.find_element("id","ap_email")
Email_input_field.send_keys("name@gmail.com")
time.sleep(3)

# find and click on continue
Select_continue_button = driver.find_element("id","continue")
Select_continue_button.click()
time.sleep(3)

Select_continue_button = driver.find_element("id","continue")
Select_continue_button.click()
time.sleep(3)

# Find and Input otp
EnterOtp_field = driver.find_element("id","cvf-input-code")
EnterOtp_field.send_keys("ThankU")
time.sleep(3)

# Close the browser
driver.quit()
