import scrapy
class Spider(scrapy.Spider):
    name = 'spidersity'
    start_urls = ["http://172.17.50.43/varsity"]
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield{'Image Link': x.xpath(newsel).extract_first()}
            PageSel = '.next a ::attr(href)'
            next_page = response.css(PageSel).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback = self.parse
                )