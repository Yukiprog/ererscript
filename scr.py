import requests
import re
import uuid
from bs4 import BeautifulSoup

url = "http://oreno-erohon.com/content/70377"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
imgs = soup.find_all('img',src=re.compile('.+724x1024.png'))
i =0
for img in imgs:    
        print(img['src'])
        r = requests.get(img['src'])
        with open(str('./picture/')+str(i)+str('.png'),'wb') as file:
                file.write(r.content)
        i=i+1
