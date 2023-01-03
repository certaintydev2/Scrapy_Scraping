import re
import scrapy
import json



search_string = input("enter keyward: ")
# kewward search 
search_string = search_string.replace(' ', '+')

class ProductSpider(scrapy.Spider):
    # create spider class 
    name = "product"
    start_urls = ['https://insert_url']
    
    def parse(self, response):
    # this function is responsiable to extract all links for one page     
        urls = response.xpath('//*[@id="result-1"]/h4/a/@href').extract()  
        for i in urls:
            yield scrapy.Request(i, self.parse2)
        
    def parse2(self,response):
     # extract pdf urls    
        pdf_file = []
        for j in response.xpath('//a'):
            href= j.xpath('/@href').extract()
            if '.pdf' in href:
                pdf_file.append(href)
        
        item = {'pdf_file' : pdf_file}
        
        yield item



    
    