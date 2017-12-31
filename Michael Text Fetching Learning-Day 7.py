# Michael Text Fetching Learning-Day 7

# 文件读取
# with open("warandpeace.txt","r") as file:
#     for row in file:
#         print(len(row))
#
# #单词分割
#
# with open("warandpeace.txt","r") as file:
#     data = file.read()
#     words = data.split()
#
#     for word in words:
#         pass
#     #      print(word)
#     #
#     # print(len(words))
#
# #词频统计
# from collections import Counter
# count = Counter(words).most_common(100)
# # print(count)
#
# #写文件
# with open("wordcount.csv","w") as file:
#     for item in count:
#         print(item)
#         # file.write("\""+item[0] + "\",\"" + str(item[1]) + "\"\n" ) #item 是一个tuple
#         #file.write(item[0] + "," + str(item[1]) + "n" )这种写法如果有特殊字符或者逗号都会使excel读写出错
#         #我们加入“”作为定界符，这样就避免了问题
#         #\--escape
#
#         #借用单引号，我们可以简化上述表达式：
#         #file.write('"'+item[0] + '","' + str(item[1]) + '"\n' )
#         # file.write("\"" + item[0] + "\",\"" + str(round(item[1]/en(words),8)*1000) + "‰\"\n")#土方法千分号格式
#         file.write('"' + item[0] + '","'+ '{:.2%}'.format(item[1]/len(words))+ '"\n')


# head{head{title,link,meta},body{aside{div{header,nav}... },article...}}


# Shanghai university news
# http: // news.shu.edu.cn / Default.aspx?tabid = 446

import urllib.request  # 下载了urllib5但是没使用(已经解决，包名和类名分开)
import re
from bs4 import BeautifulSoup


def readpage(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    return soup


page = readpage("http://www.shu.edu.cn/Default.aspx?tabid=8464")
# 搜索功能
# data = page.find_all("a",attrs={"class":"Normal"})
# for item in data:
#     print(item["title"])
#
# with open("shunews.csv","w") as file:
#     for item in data:
#         file.write('"' + item["title"] + '"\n')
# # for item in page:
# #     print(item)

data = page.find_all("a", attrs={"id": re.compile("HRCMS.*")})
for item in data:
    print(item)
    print(item.text)
