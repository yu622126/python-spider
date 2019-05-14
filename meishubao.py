import os
import re
import time
import urllib
import requests
from lxml import etree
def get_html(url, encoding='utf-8'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = encoding
    return response.text
def crawl_each_job_page(job_url):
    sub_page = etree.HTML(html)
    sub_get = sub_page.xpath("//ul[@class='p_falls']//li/a/img/@src")
    for image_src in sub_get:
        # 发送请求，下载图片
        # 创建文件夹
        dirname = 'E:/' + 'meishubao'
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        file = image_src.split('/')[-1]
        filemane = file.split("!")[0]
        filepath = dirname + '/' + filemane
        print("%s图片正在下载....." % filemane)
        # pic = urllib.request.urlopen(image_src)
        urllib.request.urlretrieve(image_src,filepath)
        print("%s图片结束下载....." % filemane)



if  __name__ == '__main__':
    page = "https://www.meishubao.com/gallery/"
    response=get_html(url=page)
    html= etree.HTML(response)
    sub_urls =html.xpath("//section/nav/a/@href")
    for sub_url in sub_urls:
        sub_url ="https:"+sub_url
        # print(sub_url)
        responses = get_html(sub_url)
        msb_html = etree.HTML(responses)
        pic_html = msb_html.xpath("//ul[@class='p_list2 li-num6 wh130x130']//li/a/@href")
        for pic_htmls in pic_html:
            # print(pic_htmls)
            image_html = "https:"+pic_htmls
            html = get_html(image_html)
            crawl_each_job_page(html)
            # print(image_html)
            time.sleep(1)

