"""
# question1:
51job.com is one of the job searching portals in China. Customers are allowed to search for jobs
by keywords and location. Write a Python program to extract the job data off 51job.com for
further analysis.
Find the job data related to the keyword JAVA and location in Shanghai. Include the job title,
company, monthly pay, and release date in the data file. Save the job data to a CSV file ready to
be opened in Microsoft Excel.
Extract at least 3 pages of the job data if the jobs are listed in multiple pages.
"""
# Michael learning - Day 6

import urllib.request
from bs4 import BeautifulSoup
import re


# 函数说明：num表示需要读取几页，如若超过搜索的范围，则返回所有结果
def question1(num):
    url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=020000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=Java&keywordtype=2&curr_page=" + str(
        1) + "&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    maxp = soup.find_all("span", {"class", "og_but"})
    for item in re.findall(r"[0-9]*", str(maxp[0])):
        if item != "":
            maxp = item
            break
    print(maxp)

    if (num >= int(maxp)):
        num = maxp

    for i in range(1, 1 + num):
        url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=020000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=Java&keywordtype=2&curr_page=" + str(
            i) + "&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9"

        req = urllib.request.Request(url, headers={"User-Agent": "Opera"})
        page = urllib.request.urlopen(req)
        soup = BeautifulSoup(page, "html.parser")

        name = []
        name.append("职位")
        for item in soup.find_all("p", {"class": re.compile("t1.*")}):
            name.append(item.text)

        company = []
        for item in soup.find_all("span", {"class": "t2"}):
            company.append(item.text)

        monthly_pay = []
        for item in soup.find_all("span", {"class": "t4"}):
            monthly_pay.append(item.text)

        print(str(len(name)) + '\n ' + str(len(company)) + '\n' + str(len(monthly_pay)))
        with open("day8question1.csv", "a+", encoding="UTF-8-sig") as file:
            for i in range(len(name)):
                file.write('"' + str(name[i]) + '","' + str(company[i]) + '","' + str(monthly_pay[i]) + '"\n')
            file.close()


question1(4)
