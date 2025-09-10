import scrapy
from scrapy.loader import ItemLoader
from work_three.items import WorkThreeItem

class PythonSpider(scrapy.Spider):
    name = "python"
    allowed_domains = ["pythonjobs.github.io"]
    start_urls = ["https://pythonjobs.github.io/"]

    def parse(self, response):
        for job in response.xpath('//div[@class="job"]'):
            loader = ItemLoader(item=WorkThreeItem(), selector=job)
            # title
            loader.add_xpath('title', './/h1/a/text()')

            # location and date — using span[@class="info"], usually the first two spans
            info_spans = job.xpath('.//span[@class="info"]/text()').getall()
            location = info_spans[0].strip() if len(info_spans) > 0 else None
            date = info_spans[1].strip() if len(info_spans) > 1 else None
            category = info_spans[3].strip() if len(info_spans) > 1 else None
            loader.add_value('location', location)
            loader.add_value('date', date)
            loader.add_value('Category', category)

            yield loader.load_item()
