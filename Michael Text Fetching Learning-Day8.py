#Day8 6-22

#assignment yesterday
# import urllib.request
# from bs4 import  BeautifulSoup
# url = "http://buffalo.craigslist.org/search/cto"
# page = urllib.request.urlopen(url)
# soup = BeautifulSoup(page,"html.parser")
#
# for listing in soup.find_all("span",{"class":"txt"}):
#     for item in soup.find_all("a",attrs={"class":"hdrlnk"}): #这种搜索不认ID这个
#     # for item in soup.find_all("a", id={"txt"})
#         print(item.text)
#     for item in listing.find_all("span",{"class":"price"})
#         print(item.text)
#     print("\n")

#大众点评对抗爬虫手记
import urllib.request
import re
from bs4 import  BeautifulSoup


def day8dazhong(n):
  try:
    url = "http://www.dianping.com/shop/177062" +"{:0>2d}".format(n)
    req = urllib.request.Request(url,headers={"User-Agent":"Mozilla"})
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page,"html.parser")
    name=""
    for item in soup.find_all("meta",attrs={"itemprop":"name"}):
            name=item["content"]
    print(name)

    tel=""
    for item in soup.find_all("p",attrs={"class":"expand-info tel"}):
        tel+=item.text
    tel.strip()
    print(tel)

    address=""
    for item in soup.find_all("div",attrs={"class":"expand-info address"}):
        for region in item.find_all("span",{"itemprop":"locality region"}):
            address += region.text
        for street in item.find_all("span",{"itemprop":"street-address"}):
            address += street.text
    address = '"' + address.split()[0]+" : "+address.split()[1] + '"'
    print(address.split()[0]+" : "+address.split()[1])


    comment=[]
    for listing in soup.find_all("ul",{"class":"comment-list J-list"}):
        for item in listing.find_all("p",attrs={"class":"desc"}):
            if "..." in item.text:continue
            comment.append(item.text + '\n')
            print(item.text+'\n')

    with open("day8大众点评抓取177062" +"{:0>2d}".format(n) +".txt","w",encoding="UTF-8-sig") as file:
        file.write(name+'\n')
        file.write(address+'\n')
        for i in comment:
            file.write(i)
  except : pass

# for i in range(50): day8dazhong(i)



#regular expression
#greedy（默认） 表示尽可能多匹配，reluctant（重复符号加个？）最短符合要求


url = "http://www.dianping.com/shop/17706230"
req = urllib.request.Request(url,headers={"User-Agent":"Mozilla"})
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page,"html.parser")

pattern = re.compile("口味：[0-9.]*")
match = re.findall(pattern,soup.text)

for item in match:
    print(item)





