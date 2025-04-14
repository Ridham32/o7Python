import requests
from bs4 import BeautifulSoup
import webbrowser
import time

url ="https://en.wikipedia.org/wiki/Anime"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
#print(soup)

for i in soup.find_all("h1"):
    print(i.text)

for i in soup.find_all("p"):
    print(i.text)

for i in soup.find_all("a"):
    print(i['href'])

###### Scraping the Image of an Anime Eye
for span in soup.find_all("span",class_="mw-default-size notpageimage"):
    img_tag = span.find("img")
    if img_tag and 'src' in img_tag.attrs:
        print("https:"+ img_tag["src"])
    else:
        print("Failed to retrieve the webpage.")

######  Content in the side table

for table in soup.find_all("table",class_="sidebar sidebar-collapse nomobile nowraplinks hlist"):
        for div in table.find_all("div",class_="sidebar-list-title-c"):
            print(div.get_text(strip=True))


########## Scraping the headings
for div in soup.find_all("div",class_="mw-heading mw-heading3"):
        for i in div.find_all("h3"):
            print(i.text)


######### Going to top five websites in the reference list
link_List = []
for div in soup.find_all("div",class_="reflist"):
    for li in div.find_all("li"):
        for span in li.find_all("span",class_="reference-text"):
            for i in span.find_all("a"):
                href = i.get("href")
                if href:
                    link_List.append(href)
a=0
valid_link=[]
for link in link_List:
    if link.startswith("http"):
        valid_link.append(link)

for i in valid_link:
    a=a+1
    print("##",a,"## ",i)
time.sleep(5)

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

for link in valid_link[:5]:
    webbrowser.get(chrome_path).open(link)

    time.sleep(10)









