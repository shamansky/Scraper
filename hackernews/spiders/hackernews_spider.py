import scrapy

class HackernewsSpider(scrapy.Spider):
    name = 'hackernews'
    start_urls = [
    'https://news.ycombinator.com/',
    ]

    def parse(self, response):
        news = response.css('.athing')
        for item in news:
            yield {
                'rank': item.css('span.rank::text').get(),
                'title': item.css('.storylink::text').get(),
                'link': item.css('.storylink::attr(href)').get(),
            }
