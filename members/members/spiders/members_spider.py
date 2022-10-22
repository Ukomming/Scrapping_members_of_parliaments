import scrapy
from ..items import MembersItem


class MembersSpider(scrapy.Spider):
    name = 'Members'
    start_urls = [
        'https://www.parliament.gh/mps?az&P=0',
        'https://www.parliament.gh/mps?az&P=a',
        'https://www.parliament.gh/mps?az&P=14',
        'https://www.parliament.gh/mps?az&P=1e',
        'https://www.parliament.gh/mps?az&P=28',
        'https://www.parliament.gh/mps?az&P=32',
        'https://www.parliament.gh/mps?az&P=3c',
        'https://www.parliament.gh/mps?az&P=46',
        'https://www.parliament.gh/mps?az&P=50',
        'https://www.parliament.gh/mps?az&P=5a',
        'https://www.parliament.gh/mps?az&P=64',
        'https://www.parliament.gh/mps?az&P=6e',
        'https://www.parliament.gh/mps?az&P=78',
        'https://www.parliament.gh/mps?az&P=82',
        'https://www.parliament.gh/mps?az&P=8c',
        'https://www.parliament.gh/mps?az&P=96',
        'https://www.parliament.gh/mps?az&P=a0',
        'https://www.parliament.gh/mps?az&P=aa',
        'https://www.parliament.gh/mps?az&P=b4',
        'https://www.parliament.gh/mps?az&P=be',
        'https://www.parliament.gh/mps?az&P=c8',
        'https://www.parliament.gh/mps?az&P=d2',
        'https://www.parliament.gh/mps?az&P=dc',
        'https://www.parliament.gh/mps?az&P=e6',
        'https://www.parliament.gh/mps?az&P=f0',
        'https://www.parliament.gh/mps?az&P=fa',
        'https://www.parliament.gh/mps?az&P=104',
        'https://www.parliament.gh/mps?az&P=10e'
    ]

    def parse(self, response):
        items = MembersItem()
        names = len(response.xpath("//center/b[@class='padd']/text()").getall())
        for num in range(0, names):
            yield {
                'name': response.xpath("//center/b[@class='padd']/text()").getall()[num],
                'party': response.xpath("//center/p/text()").getall()[num],
                'constituency': response.xpath("//center/b[2]/text()").getall()[num],
                'region': response.xpath("//p/following-sibling::span/text()").getall()[num]


            }
# response.xpath("//center/b[@class='padd']/text()").getall()   name
# response.xpath("//center/p/text()").getall()    party
# response.xpath("//center/b[2]/text()").getall()  constituency
# response.xpath("//center/span/text()").getall()  region
