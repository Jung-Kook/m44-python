# naver에서 html 파일을 가지고 온다.
# BeautifulSoup 를 이용해서 parsing 한다.
# 실시간 검색어 10위까지 출력한다.

import requests
from bs4 import BeautifulSoup
url = 'https://www.naver.com/'git a

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
temp = soup.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul')
result = soup.find_all('span', class_='ah_k')
print(result)

num=1
for i in result[0:10]:
  print(num,i.text)
  num = num+1

print(temp.text)
