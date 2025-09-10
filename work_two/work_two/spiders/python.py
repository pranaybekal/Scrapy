import scrapy
from scrapy.loader import ItemLoader
from work_two.items import WorkTwoItem


class PythonSpider(scrapy.Spider):
    name = "python"
    allowed_domains = ["remote.co"]
    base_url = "https://remote.co/remote-jobs/developer"
    
    def start_requests(self):
        yield scrapy.Request(url=self.base_url, callback=self.parse, meta={'page': 1})

    def parse(self, response):
        jobs = response.xpath('//div[@class="sc-jKCcyx ipEJuJ"]')

        if not jobs:
            self.logger.info(f"No jobs found on page {response.meta['page']}, stopping pagination.")
            return

        for job in jobs:
            loader = ItemLoader(item=WorkTwoItem(), selector=job)

            # Add data to item using relative XPath
            loader.add_xpath('title', './/a//span[@class="sc-fzEeWY jYWVDl"]/text()')
            loader.add_xpath('date', './/span[@class="sc-mCPZq iEMKpn"]/text()')
            loader.add_xpath('location', './/span[@class="sc-fdZtqL beUnFW"]/text()')

            # Salary processing
            salary_items = job.xpath('.//li[contains(@class,"sc-hxaYUE")]/text()').getall()
            salary_items = [s.strip() for s in salary_items if s.strip()]
            salary = "Not Mentioned"
            for s in salary_items:
                if "$" in s:
                    salary = s
                    break
            loader.add_value('salary', salary)

            yield loader.load_item()

        # Pagination: Go to next page
        next_page = response.meta['page'] + 1
        next_url = f"{self.base_url}?page={next_page}"
        self.logger.info(f"Crawling page {next_page}: {next_url}")
        yield scrapy.Request(url=next_url, callback=self.parse, meta={'page': next_page})
