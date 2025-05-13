from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time

#--- Task 3: Write a Program to Extract this Data
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url ="https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

time.sleep(3)

li_elements = driver.find_elements(By.TAG_NAME, "li")
search_results = [li for li in li_elements if 'cp-search-result-item' in li.get_attribute("class")]

print(f"Found {len(search_results)} search results")

results=[]

for item in search_results:
    try:
        #--- Title ---
        title_element = item.find_element(By.CLASS_NAME, "cp-title")
        title = title_element.text.strip()

        #--- Authors---
        author_elements = item.find_elements(By.CLASS_NAME,"author-link")
        authors = "; ".join([a.text.strip() for a in author_elements])

        #---Format + Year ---
        format_div = item.find_element(By.CLASS_NAME, "cp-format-info")
        format_span = format_div.find_element(By.CLASS_NAME, 'display-info')
        format_primary = format_span.find_element(By.CLASS_NAME, "display-info-primary")
        format_year = format_primary.text.strip()
        format_year = format_year.split(" | ")[0].strip()

        #---Strore in dict---
        book_data ={
            "Title": title,
            "Author": authors,
            "Format-Year": format_year
        }
        results.append(book_data)
    
    except Exception as e:
        print(f"Skipped an entry due to error: {e}")

df=pd.DataFrame(results)
print(df)

#--- Task 4: Write out the Data ---

df.to_csv("get_books.csv", index = False)

with open("get_books.json", "w", encoding = "utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii= False)


driver.quit()