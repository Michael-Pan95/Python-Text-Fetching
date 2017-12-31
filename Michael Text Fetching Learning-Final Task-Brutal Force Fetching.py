""""
# final task:
    Brutal Force Fetching
"""
import re
import random
import urllib.request
from bs4 import BeautifulSoup


# 注：所有商品信息都存储在一个文件中
#   此外请确保工作目录下有ProductImages文件夹以存储文件
def final(url, numid):
    req = urllib.request.Request(url, headers={"User-Agent": "Opera"})
    pageHtml = urllib.request.urlopen(req)
    pagehtml = BeautifulSoup(pageHtml, "html.parser")
    # return soup

    title = ""

    for item in pagehtml.find_all("title"):
        for titles in item:
            if titles != "":
                title = titles
                break

    oriPrice = []
    currentPrice = []
    numofreviews = []
    numofsales = []
    storePromotion = ""

    oriPrice = re.findall(r"originPrice: '([¥0-9]*\.[0-9]{2,})'", str(pagehtml))[0]
    currentPrice = re.findall(r"nowPrice: '([¥0-9]*\.[0-9]{2,})'", str(pagehtml))[0]
    tmps = pagehtml.find_all("span", {"class", "num"})
    numofreviews = int(tmps[0].text)
    numofsales = int(tmps[1].text)

    imgdownload(pagehtml, numid)

    # 查找下一个商品:
    for item in re.findall(r'"item_url"\.u002F(180pswu[0-9a-z]*)\\', str(pagehtml)):
        print(item)

    with open("13125034潘正宇.csv", "a+", encoding="UTF-8-sig") as file:
        file.write('"商品名称:",' + '"' + title + '"\n')
        file.write('"原价:",' + '"' + oriPrice + '"\n')
        file.write('"现价:",' + '"' + currentPrice + '"\n')
        file.write('"评价数目":,' + '"' + str(numofreviews) + '"\n')
        file.write('"销量:",' + '"' + str(numofsales) + '"\n')


def imgdownload(pagehtml, numid):
    # img download
    for item in pagehtml.find_all("img", {"id": "J_BigImg"}):
        imgurl = item["src"]
    req = urllib.request.Request(imgurl, headers={"User-Agent": "Opera"})
    imgresource = urllib.request.urlopen(req)
    with open(r'ProductImages\\ProductImage' + str(numid) + '.jpg', "wb") as file:
        file.write(imgresource.read())
        file.close()


url = "http://shop.mogujie.com/detail/18hxose?acm=1.ms.1.0.1187-1437-2579.yMhpP15ZDAE.44-0&ptp=1.WeUyg48e._items.1.ulTNH"
# numid=1

# 网页随机发生器

urlpool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
n = 0  # 记录成功的网页

# 观察到网页都是7位由数组和字母组合的item_id，这里用随机数生成构建7位数字进行尝试，成功20网页后停止
while (n < 20):
    try:
        randomPage = []
        urlitem = ""
        for i in range(7):
            randomPage.append(random.randint(0, 36))
        for i in randomPage:
            urlitem += urlpool[i]
        url = "http://shop.mogujie.com/detail/" + urlitem
        print(url)
        print(n)
        final(url, n)
        n += 1
    except:
        pass
