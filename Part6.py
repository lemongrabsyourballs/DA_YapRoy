import scrapy
class spidervar(scrapy.Spider):
    name = "spidersity"
    start_url = ["http://172.17.50.43/varsity"]
    def parse(self, response):
        css_selector = 'img'
        response.css(css_selector)
        for link in response.css(css_selector):
            new_xsel = '@src'
            yield {
                'Header Link':link.xpath(new_xsel).extract_first
            }