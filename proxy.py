# coding = utf8
import pymysql

# 简单mysql数据库
class sql():
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='cao',charset="utf8")
        self.cursor = self.conn.cursor()

    def insert(self):
        sql = "replace into Dangdang values(%s,%s,%s,%s);"
        v = ('t','b','d','hhhhhhhhhh')
        self.cursor.execute(sql,v)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    s = sql()
    s.insert()




# urllib代理
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener
proxy = '127.0.0.1:1080'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'httpS://' + proxy
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
    
    



import socks
import socket
from urllib import request
from urllib.error import URLError
socks.set_default_proxy(socks.SOCKS5, '127.0.0.1',9150)
socket.socket = socks.socksocket
headers = {'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
try:
    ret = request.Request('http://xfmro77i3lixucja.onion/',headers=headers)
    response = request.urlopen(ret)
    print(response.read().decode('utf-8'))
except URLError as e:
     print(e.reason)




# requests socks5代理
import requests
from lxml import etree
proxy = '127.0.0.1:9150'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy
}
s = requests.Session()
try:
    response = s.get('http://ow24et3tetp6tvmk.onion/',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
     print('Error', e.arg





# socks socket全局代理
import requests
import socks
import socket
from fake_useragent import UserAgent
ua=UserAgent()
headers = {'User-Agent': ua.random}
socks.set_default_proxy(socks.SOCKS5, '127.0.0.1',9150)
socket.socket = socks.socksocket
try:
    response = requests.get('https://thehiddenwiki.org/',verify=False)
    print(response.text)
    with open('google.html','wb') as f:
        f.write(response.content)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)




# requests 代理
import requests
from lxml import etree
from fake_useragent import UserAgent
ua=UserAgent()
headers = {'User-Agent': ua.random}
proxies = {'http':'http://127.0.0.1:1080'}
r =requests.get('https://www.gooogl.com/',proxies=proxies,verify=False)
doc = etree.HTML(r.text)
divs = doc.xpath("//div[@class='row']/div[@class='col-lg-3 col-sm-3 focus-box']")
for div in divs:
    link = div.xpath("./div/a/@href")[0] if len(div.xpath("./div/a/@href")) > 0 else None
    title =  div.xpath("./h3/text()")[0]
    print(title,link)




# socks代理使用
from sockshandler import SocksiPyHandler
import socks
from urllib.request import build_opener
import re
from selenium import webdriver
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
url = 'http://silkroad7rn2puhj.onion/?road=&reqpage=1'
proxy_handler = SocksiPyHandler(proxytype=socks.SOCKS5, proxyaddr='127.0.0.1', proxyport=9150)
opener = build_opener(proxy_handler)
resp = opener.open(url, timeout=60)
resp_html = resp.read().decode()
if 'CAPTCHA' in resp_html:
    img = re.compile(r'<img src="(.*?)">')
    img_link = re.findall(img,resp_html)[0]
    img_html = opener.open(img_link,timeout=40).read()
    with open('captcha.png','wb') as f:
        f.write(img_html)




# selenium web 代理使用
from selenium import webdriver
from sockshandler import SocksiPyHandler
import socks
from urllib.request import build_opener
from lxml import etree
import time
import re

def get_content(response):
    doc = etree.HTML(browser.page_source)
        # print(doc)
    divs = doc.xpath("//tr/td[1]/div[@id='vp']//tr/td[2]/div")
    # print(divs)
    for div in divs:
        link = div.xpath("./a[1]/@href")[0]

        title = div.xpath("./a[1]/text()")[0]
        Price = div.xpath("./b[2]/text()")[0].rstrip('/')
        view_list = div.xpath("./a[2]/@href")[0]
        Category = div.xpath("./a[3]/text()")[0]
        ShipsFrom= div.xpath("./span[@id='ah_ships']/text()")[0]
        print(title,Price,link,view_list,Category,ShipsFrom,sep='\n')
        print('\n\n')

chromeOptions = webdriver.ChromeOptions()
# 设置代理
chromeOptions.add_argument("--proxy-server=socks5://127.0.0.1:9150")
一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
browser = webdriver.Chrome(chrome_options = chromeOptions)
# 查看本机ip，查看代理是否起作用
browser.get("http://silkroad7rn2puhj.onion/?road=&reqpage=1")
time.sleep(20)
print(browser.page_source)
proxy_handler = SocksiPyHandler(proxytype=socks.SOCKS5, proxyaddr='127.0.0.1', proxyport=9150)
opener = build_opener(proxy_handler)
if 'CAPTCHA' in browser.page_source:
    img = r'<img src="(.*?)" />'
    img_link = re.findall(img,browser.page_source)[0]
    print(img_link)
    img_html = opener.open(img_link,timeout=40).read()
    with open('captcha.png','wb') as f:
        f.write(img_html)
    rr = browser.find_element_by_xpath("//form/input[1]")
    key = input('keys:')
    rr.send_keys(key)
    submit = browser.find_element_by_xpath("//form/input[2]")
    submit.click()
    # time.sleep(30)
    get_content(browser.page_source)
else:
    get_content(browser.page_source)

while 1:
    next_link = browser.find_element_by_xpath("//tr/td[1]/center/form/input[@type='submit']")
    if next_link:
        next_link.click()
        get_content(browser.page_source)

    else:
        break
    browser.quit()




# 顶岗实习签到
from appium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

server = 'http://localhost:4723/wd/hub'

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'm3note',
    'appPackage': 'com.gcykj.boss',
    'appActivity': '.ui.activity.account.LoginActivity',
    # 'unicodeKeyboard' : True,
    # 'resetKeyboard': True
}

# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': 'MI_NOTE_Pro',
#     'app': './weixin.apk'
# }
driver = webdriver.Remote(server, desired_caps)
# driver.tap([(120,100)], 400)
wait = WebDriverWait(driver, 15)
name = wait.until(EC.presence_of_element_located((By.ID, 'com.gcykj.boss:id/tv_account')))
# name.click()
name.send_keys('吴桐')
passwd = wait.until(EC.presence_of_element_located((By.ID, 'com.gcykj.boss:id/tv_passwd')))
passwd.send_keys('...')
login = wait.until(EC.presence_of_element_located((By.ID, 'com.gcykj.boss:id/login_btn')))
login.click()
time.sleep(2)
driver.tap([(450,450)], 400)
state = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'android.widget.RadioButton')))
state.click()
centent = wait.until(EC.presence_of_element_located((By.ID, 'interContent')))
centent.set_text('Today is another bad day. I am getting more and more rubbish.')
save = wait.until(EC.presence_of_element_located((By.ID, 'btnSave')))
save.click()
return_homepage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'android.widget.Button')))
return_homepage.click()
driver.close()



# 随便写的
import requests
from lxml import etree
base_url = 'http://www.bookschina.com'
response = requests.get('http://www.bookschina.com/books/children/').text
doc = etree.HTML(response)
# li_list = doc.xpath("//div[@id='webCategory']/div[@class='categoryInner']/ul/li")
# for li in li_list:
#     print(li)
#     link = base_url + li.xpath("./div[1]/h3/a/@href")[0]
#     print(link)

def parse(response):
    doc = etree.HTML(response)
    li_list = doc.xpath("//div[@class='listLeft']/div[@class='bookList']/ul/li")
    for li in li_list:
        title = li.xpath("./div[@class='infor']/h2/a/text()")[0]
        print(title)
        
li_list = doc.xpath("//div[@class='channelCategory']//div[@class='categoryInner']/ul[@class='category-list']/li")
for li in li_list:
    link = li.xpath(".//div[@class='category-infoInner']/p/a/@href")
    if len(link) >0 :
        for sub_link in link:
            content = requests.get(base_url + sub_link).text
            parse(content)
    else:
        sub_link = li.xpath(".//div[@class='category-infoInner']/h3/a/@href")[0]
        # print(base_url + sub_link)
        content = requests.get(base_url + sub_link).text
        parse(content)



# facebook实例
import re
import sys
import telnetlib
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree

def facebook(username, password):
    chromeOptions = webdriver.ChromeOptions()
    # 设置代理
    chromeOptions.add_argument("--proxy-server=socks5://127.0.0.1:1080")
    # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    driver = webdriver.Chrome(chrome_options=chromeOptions)
    driver.get('https://www.facebook.com')
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('login_form').submit()
    driver.implicitly_wait(10)
    driver.get('https://www.facebook.com/search/pages/?q=c%2B%2B&epa=SERP_TAB')

    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    driver.execute_script(js)
    driver.execute_script(js)
    driver.execute_script(js)
    driver.execute_script(js)
    time.sleep(3)

    doc = etree.HTML(driver.page_source)
    # print(doc)
    divs = doc.xpath("//*[@id='BrowseResultsContainer' or contains(@id,'BrowseScrollingPagerContainer')]")
    print(divs)
    for div in divs:
        links = div.xpath(".//div[@class='_gll']//a/@href")
        for link in links:
            print(link)
            driver.get(link)
            # doc = etree.HTML(driver.page_source)
            # ret = re.compile(r'<div class="_50f4">(.*?@.*?)</div>')
            # emails= re.findall(ret,driver.page_source)
            doc = etree.HTML(driver.page_source)
            base_url ='https://www.facebook.com'
            jianjie = doc.xpath("//div[@data-key='tab_about']/a/@href")
            print(jianjie)
            if len(jianjie) > 0:
                content = base_url+ jianjie[0]
                driver.get(content)
                ret = re.compile(r'<div class="_50f4">(.*?)</div>')
                email = re.findall(ret,driver.page_source)
                print(content,email)

    driver.get('https://www.facebook.com/pg/MountainviewCS/about/?ref=page_internal')
    # print(driver.page_source)
    time.sleep(5)

    # js = "var q=document.documentElement.scrollTop=10000"
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    link = driver.find_element_by_xpath("//*[@id='u_fetchstream_1_4']/div[2]/a/@href").text

    wait = WebDriverWait(driver, 15)
    ret = re.compile(r'<div class="_50f4">(.*?@.*?)</div>')
    emails= re.findall(ret,driver.page_source)
    for i in emails:
        print(i)

if __name__ == '__main__':
    print('==========================')
    facebook('wutong8773@163.com', '...')



from urllib.parse import urljoin
from sockshandler import SocksiPyHandler
import socks
from urllib.request import build_opener
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
proxy_handler = SocksiPyHandler(proxytype=socks.SOCKS5, proxyaddr='127.0.0.1', proxyport=1080)
opener = build_opener(proxy_handler)
url = 'https://www.facebook.com/'
resp = opener.open(url, timeout=60)
print(resp.read().decode())
