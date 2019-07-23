# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     medium_post
   Description :   
   Author :        Yalye
   date：          2019/7/23
-------------------------------------------------
"""
# https://medium.com/@aiswaryar/scrapping-medium-posts-using-scrapy-d5e8251dc008

import scrapy

class MediumPost(scrapy.Spider):
    name = 'medium'

    def start_requests(self):
        start_urls = ['https://medium.com/search/posts?q=Data%20Science']
        for url in start_urls:
            yield scrapy.Request(url, method='GET', callback=self.parse)

    def parse(self, response):
        response_data = response.text
        response_split = response_data.split("while(1);</x>")
        response_data = response_split[1]

        if 'paging' in response_data['payload']:
            data = response_data['payload']['paging']
            if 'next' in data:
                data = data['next']
                form_data = {
                    'ignoreIds': data['ignoreIds'],
                    'page':data['page'],
                    'pageSize':data['pageSize']
                }
                yield scrapy.Request('https://www.medium.com/search/posts?q=Data%20Science',method='POST',body=json.dumps(formdata),headers=header,cookies=cookie,callback=self.parse)
