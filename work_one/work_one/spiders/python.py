import scrapy
from scrapy.loader import ItemLoader
from work_one.items import WorkOneItem

class PythonSpider(scrapy.Spider):
    name = "python"
    allowed_domains = ["www.python.org"]
    start_urls = ["https://www.python.org/jobs/"]

    def parse(self, response):
        for job in response.xpath('//ol[@class="list-recent-jobs list-row-container menu"]/li'):
            # item['title'] = job.xpath('.//span[@class="listing-company-name"]/a/text()').extract()
            # item['location']=job.xpath('.//span[@class="listing-location"]/a/text()').extract()
            # item['posted']=job.xpath('.//span[@class="listing-posted"]/time/text()').extract()
            # item['skillSet']=job.xpath('.//span[@class="listing-job-type"]/a/text()').extract()
            # item['Category']=job.xpath('.//span[@class="listing-company-category"]/a/text()').extract()
            # # Yield as output (so Scrapy can export it)
            # yield item
            # Create an ItemLoader for each job
            l = ItemLoader(item=WorkOneItem(), selector=job)

            # Add fields
            l.add_xpath('title', './/span[@class="listing-company-name"]/a/text()')
            l.add_xpath('location', './/span[@class="listing-location"]/a/text()')
            l.add_xpath('posted', './/span[@class="listing-posted"]/time/text()')
            l.add_xpath('skillSet', './/span[@class="listing-job-type"]/a/text()')
            l.add_xpath('Category', './/span[@class="listing-company-category"]/a/text()')

            # Yield the loaded item (one per job)
            yield l.load_item()

