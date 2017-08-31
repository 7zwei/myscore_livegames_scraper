from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.PhantomJS()
browser.get("http://www.myscore.com.ua")
browser.find_element_by_xpath('//*[@id="fscon"]/ul/li[2]/span/a').click()
page_source = browser.page_source

soup = BeautifulSoup(page_source, 'html5lib')
divs = soup.findAll('table', class_ = 'soccer')
for match in divs:
    body = match.find('tbody')
    trs = body.findAll('tr')
    for tr in trs:
        match_info = []
        tds = tr.findAll('td')
        for td in tds:
            match_info.append(td.text.strip())
        print(match_info)
