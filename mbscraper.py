import scrapy


class MusicBankSpider(scrapy.Spider):
    name = "musicbank_spider"
    start_urls = ['http://www.kbs.co.kr/2tv/enter/musicbank/view/old/2032684_107102.html']

    def parse(self, response):
        num = 1
        NEXT_PAGE_SELECTOR = '.content a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        while "http://www.kbs.co.kr/2tv/enter/musicbank/view/old/" not in next_page:
            next_page = response.css(NEXT_PAGE_SELECTOR)[num].extract()
            num += 1
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)