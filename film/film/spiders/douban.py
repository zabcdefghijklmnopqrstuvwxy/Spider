import scrapy

from film.items import FilmItem 

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        titles = response.xpath("//div[@class='pic']//@alt").extract()
        scores_div = response.xpath("//div[@class = 'star']//span[@class='rating_num']")
       
        scores = scores_div.xpath("string(.)").extract()

        item = FilmItem()

        for title,score in zip(titles,scores):
            print("title="+title + "score" + score)
            item['title'] = title
            item['score'] = score
        
            yield item

        filmurl = response.xpath("//div[@class='paginator']//@href").extract()
        
        if len(filmurl) > 0:
           url_copy = []
           url_copy[:] = ['https://movie.douban.com/top250%s' % item for item in filmurl]
           
           for url in url_copy:
               print("url is " + url)
               yield scrapy.Request(url,callback=self.parse)    
        

