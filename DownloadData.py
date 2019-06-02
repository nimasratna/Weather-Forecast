import scrapy

class weatherSpider(scrapy.Spider):
    url = "https://sample.openweathermap.org/data/2.5/forecast?q=warsaw,us&mode=xml&appid=b70a99d1f4072dd67b2975520507abcf"

    def parse(self, response):
        pass

