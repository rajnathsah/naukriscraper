import scrapy
import os
from scrapy import Selector

class PythonJobSpider(scrapy.Spider):
    name = 'pythonjob'
    
    def start_requests(self):
        urls = [
            'https://www.naukri.com/python-jobs-in-hyderabad',
            ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self,response):
        
        outdirpath = os.path.join((os.getcwd()), 'scrapefiles')
        page = response.url.split('/')[3]        
        filename = os.path.join(outdirpath, 'python-%s.html' % page) 
        
        for link in response.xpath('//*[@data-url]').getall():
            sel = scrapy.Selector(text=link)            
            yield {
                'jobtitle':sel.xpath('string(//div/span/ul/li[@title])').extract_first(),
                'joburl':sel.xpath('//div/@data-url').extract_first(),
                'companyname':sel.xpath('//div/span/span/span[@class="org"]/text()').extract_first(),
                'experience':sel.xpath('//div/span/span[@class="exp"]/text()').extract_first(),
                'location':sel.xpath('//div/span/span[@class="loc"]/span/text()').extract_first(), 
                'skills':sel.xpath('//div/span/div/span[@class="skill"]/text()').extract_first(),
                'moredesc':sel.xpath('//div/span/div[2][@class="more desc"]/span/text()').extract_first(),
                'salary':sel.xpath('//div/div/span[@class="salary"]/text()').extract_first(), 
                'postedby':sel.xpath('//div/div/div/a[@class="rec_name"]/text()').extract_first(),
                'dayposted':sel.xpath('//div/div/div/span[@class="date"]/text()').extract_first(),          
                }

            
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
                
        next_page = response.xpath('/html/head/link[contains(@rel,"next")]/@href').extract_first()
        
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback = self.parse
                )