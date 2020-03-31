import requests
import re
import uuid
from bs4 import BeautifulSoup

#俺のエロ本URLとコンテンツ番号の取得
url = "http://oreno-erohon.com/content/"
contents = "174319";
r = requests.get(url+contents)
soup = BeautifulSoup(r.text,'lxml')
imgs = soup.find_all('img',src=re.compile('.+725x1024.jpg'))
i =0
for img in imgs:    
        print(img['src'])
        r = requests.get(img['src'])
        with open(str('./picture/'+contents+'/')+str(i)+str('.jpg'),'wb') as file:
                file.write(r.content)
        i=i+1
