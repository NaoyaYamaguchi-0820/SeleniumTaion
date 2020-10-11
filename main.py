import time
import datetime
from selenium import webdriver

driver = webdriver.Chrome(executable_path= 'C:\\Users\\naoya\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\chromedriver_binary\\chromedriver.exe')

driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=R3as8E6_Hk25fEKE8jiPZAP3vGlF6fZAkT_xCIYiawJUMVc2NkxIWjlXTThJMjJTRk1XMlhKVVA2TyQlQCN0PWcu')

time.sleep(5)

sokuteibi = driver.find_element_by_class_name("office-form-question-textbox")

sokuteibi.send_keys(datetime.datetime.now().strftime('%Y/%m/%d'))

