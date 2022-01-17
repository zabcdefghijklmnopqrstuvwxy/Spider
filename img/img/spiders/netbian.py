import scrapy
from img.items import ImgItem

class NetbianSpider(scrapy.Spider):
    name = 'netbian'
    allowed_domains = ['www.netbian.com']
    start_urls = ['http://www.netbian.com/']

    def parse(self, response):
        item = ImgItem()
        item['image_urls'] = response.xpath("//img//@src").extract()
        yield item
        new_url = response.xpath("//div[@class='page']//@href").extract()
        if len(new_url) > 0:
            url_copy = []
            url_copy[:] = ['http://www.netbian.com%s'% item for item in new_url]
            for url in url_copy:
                print("image url is " + url) 
                yield scrapy.Request(url,callback=self.parse)



