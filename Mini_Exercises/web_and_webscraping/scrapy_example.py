
import scrapy

class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['https://books.toscrape.com']
    custom_settings = {
        #this is needed in order for unicode characters to display in json
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css('.price_color::text').extract_first(),
                'title': article.css('h3 > a::attr(title)').extract_first()
            }
            #this gets the href value for the next button
            next = response.css('.next > a::attr(href)').extract_first()
            #if there is a next button, this essentially loops back through the top bit.
            if next:
                yield response.follow(next, self.parse)