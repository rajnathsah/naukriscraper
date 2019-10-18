# Scrape naukri.com using Scrapy

# Requirements

1. [Python](https://www.python.org/downloads/)
2. [Scrapy](https://scrapy.org/)
3. [Scrapyd](https://scrapyd.readthedocs.io/en/stable/)

This project extract data from [Naukri](www.naukri.com) and save it in a folder using scrapy framework.

To scrape any website, understanding of [DOM](https://www.w3schools.com/whatis/whatis_htmldom.asp) and [xpath](https://www.w3schools.com/xml/xpath_intro.asp) is helpful. Xpath is easy to understand, for this project i used [Xpather](http://xpather.com/) to prepare the needed xpath query.

### Creating project in scrapy

Run below command to create project

```python
scrapy startproject naukriscraper
```
It will directory with project name with following contents.

```python
naukriscraper/
    scrapy.cfg            # deploy configuration file
    naukriscraper/             # project's Python module, you'll import your code from here
        __init__.py
        items.py          # project items definition file
        middlewares.py    # project middlewares file
        pipelines.py      # project pipelines file
        settings.py       # project settings file
        spiders/          # a directory where you'll later put your spiders
            __init__.py
```

Add spider to project, by creating python_spider.py in spiders directory.

```python
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
```

Defined USER_AGENT and FEED_URI in settings.py file

Run the spider to scrape data from project top directory.
```python
scrapy crawl pythonjob
```
This will crawl and link and save the file in scrapefiles folder.
