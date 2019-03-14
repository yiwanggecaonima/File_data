#-*-coding:UTF-8-*-
import requests
from lxml import etree
import selenium.webdriver
import time
from tqdm import tqdm

# browser = selenium.webdriver.Chrome()
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
# res = browser.get("https://pic.sogou.com/pics?query=%CB%EF%D9%B3%B1%DA%D6%BD&p=40230500&st=255&mode=255&policyType=0")
# time.sleep(0.8)
# doc = etree.HTML(browser.page_source)
# imgs =doc.xpath("//div[@id='imgid']/ul/li/a[@class='picContainer']/img/@src")
# l = []
# for img in imgs:
#     l.append(img)

imgs = ['https://i02picsos.sogoucdn.com/1b7a1e78e5e899a8', 'https://i02picsos.sogoucdn.com/037580522523e306', 'https://i04picsos.sogoucdn.com/46fb651630e13b3b', 'https://i03picsos.sogoucdn.com/e90d49ad48abeea4', 'https://i01picsos.sogoucdn.com/bbee52198daf9087', 'https://i02picsos.sogoucdn.com/7aa466a1257bf230', 'https://i01picsos.sogoucdn.com/777c80ef62b9cb7d', 'https://i02picsos.sogoucdn.com/49ca0e73aba70841', 'https://i04picsos.sogoucdn.com/4c2459ed562051c8', 'https://i03picsos.sogoucdn.com/e03d610c9564cdfc', 'https://i02picsos.sogoucdn.com/72b60eb76320cac2', 'https://i02picsos.sogoucdn.com/5c4e364305d8c0ed', 'https://i03picsos.sogoucdn.com/a78bf457af76682d', 'https://i01picsos.sogoucdn.com/754b30a20c5f2c8a', 'https://i01picsos.sogoucdn.com/6f5a0b235825a9d7', 'https://i04picsos.sogoucdn.com/1e289f51f9d3d361', 'https://i04picsos.sogoucdn.com/384987703aeb40e8', 'https://i01picsos.sogoucdn.com/2203b1709abce9f8', 'https://i04picsos.sogoucdn.com/d7f476f4be017568', 'https://i03picsos.sogoucdn.com/b5ecd748b918797c', 'https://i02picsos.sogoucdn.com/6464e909689a0aff', 'https://i03picsos.sogoucdn.com/37926d5ad34ce1c4', 'https://i02picsos.sogoucdn.com/7450cab585134302', 'https://i01picsos.sogoucdn.com/f8d3a1f38194db2e', 'https://i01picsos.sogoucdn.com/30d6d1c4ea0114b4', 'https://i04picsos.sogoucdn.com/0a4f43b46aab6b0b', 'https://i02picsos.sogoucdn.com/24b98e5f793c7157', 'https://i04picsos.sogoucdn.com/eef5ce7effedad5b', 'https://i01picsos.sogoucdn.com/fee55ff986d3a037', 'https://i04picsos.sogoucdn.com/f78351dc8b412c65', 'https://i01picsos.sogoucdn.com/eaf35b6a736a8bfc', 'https://i01picsos.sogoucdn.com/a0a36121deae4955', 'https://i02picsos.sogoucdn.com/754e9c7a32145a66', 'https://i04picsos.sogoucdn.com/a8262d11ff72fed7']
start = time.time()
for i,url in enumerate(imgs):
    size = i +1
    path = "/home/parrot/PycharmProjects/My_Crawl/进度条/ihome/" + str(i) + ".jpg"
    response = requests.get(url,stream = True)
    chunk_size = 1024 # 每次1024
    content_size = len(imgs) # 大小
    print("文件大小："+str(round(float(content_size/chunk_size/1024),4))+"[MB]")
    with open(path,'wb') as file:
        for data in response.iter_content(chunk_size=chunk_size):
            file.write(data)
        file.close()
    # f.set_description("processing {}".format(f))
    print('\r'+"已经下载："+int(size/content_size*100)*"█" +"【"+str(round(float(size/content_size)*100,2))+"%"+"】",end="")
    end = time.time()
    print("总耗时:"+str(end-start)+"秒")
