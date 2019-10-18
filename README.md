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
scrapy startproject <project name>
```
It will directory with project name with following contents.

```python
<project name>/
    scrapy.cfg            # deploy configuration file
    <project name>/             # project's Python module, you'll import your code from here
        __init__.py
        items.py          # project items definition file
        middlewares.py    # project middlewares file
        pipelines.py      # project pipelines file
        settings.py       # project settings file
        spiders/          # a directory where you'll later put your spiders
            __init__.py
```



