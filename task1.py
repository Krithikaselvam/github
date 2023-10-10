from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
driver=webdriver.Chrome(options=chrome_options)
driver.get('http://10.89.1.12:8080/tops/product')
username_field = driver.find_element(By.XPATH,'//*[@id="j_username"]')
password_field = driver.find_element(By.XPATH,'//*[@id="j_password"]')
username_field.send_keys("krithikaselvam")
password_field.send_keys("tekV2023")
login_button = driver.find_element(By.XPATH,'//*[@id="user-details"]/input[3]')
login_button.click()
driver.implicitly_wait(10)
tbody=driver.find_element(By.XPATH,'/html/body/div[1]/ul/li[2]/a')
print(tbody.text)
tbody.click()
time.sleep(10)
search_bar =driver.find_element(By.XPATH,"/html/body/form/div/div[1]/div/div[1]/div[2]/label/input")
search_bar.clear()
time.sleep(5)
engineer_name = input("Enter the Name:")
search_bar.send_keys(engineer_name)
time.sleep(5)
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
'''cells=driver.find_elements(By.XPATH,'//*[@id="projectListTable"]/tbody/tr/td[9]/stage')
print(type(cells))
if driver.find_element(By.XPATH,'//*[@id="projectListTable"]/tbody/tr[1]/td[9]/stage').text == 'In Progress':
    print(driver.find_element(By.XPATH,'//*[@id="projectListTable"]/tbody/tr[1]/td[2]').text)
for cell in cells :
    print(cell.text)
project_name=driver.find_elements(By.XPATH,'//*[@id="projectListTable"]/tbody/tr/td[2]')
for name in project_name:
    print(name.text)'''

cells = driver.find_elements(By.XPATH, '//*[@id="projectListTable"]/tbody/tr/td[9]/stage')
project_name = driver.find_elements(By.XPATH, '//*[@id="projectListTable"]/tbody/tr/td[2]')
project_name1 = driver.find_element(By.XPATH, '//*[@id="projectListTable"]/tbody/tr[1]/td[2]')
print(project_name1.text)

in_progress_count = 0

for cell, name in zip(cells, project_name):
    if "In progress" in cell.text:
        in_progress_count += 1
        print("Project Count:", in_progress_count, "Project Name:", name.text )
    

driver.close()
driver.quit()

