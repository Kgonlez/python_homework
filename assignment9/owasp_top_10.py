from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://owasp.org/www-project-top-ten/")
time.sleep(3)

vulnerability_links = driver.find_elements(By.XPATH, '//section[contains(@class, "page-body")]//ul/li/a[strong]')
results = []

for vuln in vulnerability_links[:10]:
    try:
        title_element = vuln.find_element(By.TAG_NAME, "strong")
        title= title_element.text.strip()
    except:
        title = ""
    href= vuln.get_attribute('href')

    results.append({"Title": title, "Link":href})

print(results)

df= pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False)

driver.quit()
