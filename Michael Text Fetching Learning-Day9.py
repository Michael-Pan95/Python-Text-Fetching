#Day 9 6-23

#下载图片
import urllib.request
from bs4 import  BeautifulSoup
import re

def download(url,filename):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla"})
    resource = urllib.request.urlopen(req)
    with open(filename,"wb") as file:
        file.write(resource.read())

# url="http://www.tuku.cn"
# req = urllib.request.Request(url,headers={"User-Agent":"Mozilla"})
# resource = urllib.request.urlopen(req)
# page = BeautifulSoup(resource,"html.parser")
#
# regex =r'http://.*\.jpg'
# pattern = re.compile(regex)
# match = pattern.findall(str(page))
# match = re.findall(r"http://.*\.jpg",str(page))
# i=0
#
# for item in match:
#
#     # download(item,item[-20:])#倒数20个字符 ：表示范围，-20到底
#     try:
#         download(str(item),r'images\\'+str(i)+".jpg")
#         print(item)
#         i+=1
#     except: pass



#京东对抗日记
# url="http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%B1%DA%D6%BD&fr=ala&ala=1&pos=0&alatpl=wallpaper&oriquery=%E5%A3%81%E7%BA%B8#z=0&pn=&ic=0&st=-1&face=0&s=0&lm=-1"
# req = urllib.request.Request(url,headers={"User-Agent":"Mozilla"})
# resource = urllib.request.urlopen(req)
# page = BeautifulSoup(resource,"html.parser")
#
# regex =r'http://.*\.jpg'
# pattern = re.compile(regex)
# match = pattern.findall(str(page))
# # match = re.findall(r"http://.*\.jpg",str(page))
# i=0
# for item in match:
#     print(item)
#     # download(item,item[-20:])#倒数20个字符 ：表示范围，-20到底
#     download(str(item),r'images\\'+str(i)+".jpg")
#     i+=1

# url="http://www.bilibili.com/"
# req = urllib.request.Request(url,headers={"User-Agent":"Mozilla"})
# resource = urllib.request.urlopen(req)
# page = BeautifulSoup(resource,"html.parser")
#
# regex =r'http://.*\.jpg'
# pattern = re.compile(regex)
# match = pattern.findall(str(page))
# # match = re.findall(r"http://.*\.jpg",str(page))
# i=0
# for item in match:
#     # download(item,item[-20:])#倒数20个字符 ：表示范围，-20到底
#     download(item,r'images\\'+str(i))
#     print(item)
#     i+=1

#实战京东
def jdCR(url):
    # url="http://item.jd.com/2269354.html"
    req = urllib.request.Request(url,headers={"User-Agent":"Mozilla"})
    resource = urllib.request.urlopen(req)
    page = BeautifulSoup(resource,"html.parser")

    # info = page.find_all("div",{"class":"fl"})[0]
    # info = re.findall(r'[0-9]*',str(info))

    title =page.find_all("title")
    title = re.findall(r'>(【.*)【',str(title))[0]


    info = re.findall(r'skuid: ([0-9]*)', str(page))
    # for item in info:
    #     if item!="":
    #         info=re.findall(r'[0-9]*',item)
    #         break

    for item in info:
        if item!="":
            info=item
            break


    idcode =info
    price_url = "http://p.3.cn/prices/mgets?skuIds=J_" + str(idcode)
    price_con=urllib.request.urlopen(price_url)
    for item in price_con:
        print(idcode +"  " + title+ ":" +  re.findall(r'[-0-9]*\.[0-9]{2}',str(item))[0])


for i in range(100):
    try:
        jdCR("http://item.jd.com/"+str(2269375+i)+".html")
    except:
        print("error:" + str(i))