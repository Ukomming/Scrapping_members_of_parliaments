import scrapy
from ..items import MembersItem


class MembersSpider(scrapy.Spider):
    name = 'Members'
    start_urls =[
        'https://www.parliament.gh/mps?az&P=0',
    ]


    def parse(self, response):
        items = MembersItem()
        names = len(response.xpath("//center/b[@class='padd']/text()").getall())
        for num in range(0, names):
            name = response.xpath("//center/b[@class='padd']/text()").getall()[num],
            party = response.xpath("//center/p/text()").getall()[num],
            constituency = response.xpath("//center/b[2]/text()").getall()[num],
            region = response.xpath("//p/following-sibling::span/text()").getall()[num]

            items['name'] = name
            items['party'] = party
            items['constituency'] = constituency
            items['region'] = region
            yield items
            for a in response.xpath("//a[@class='square goldenrod']/@href").getall():
                yield response.follow(a, callback=self.parse)



