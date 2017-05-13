import scrapy
import re
import urllib
import os
from scrapy.http import HtmlResponse
class CommitStrip(scrapy.Spider):
	name = "xkcd"
	start_urls = [
	'https://xkcd.com/1/',
	]
	
	
	def parse(self, response):
		img_url = response.xpath('//div[@id="comic"]/img/@src').extract()
		next =  response.xpath('//a[@rel="next"]/@href').extract()[0]
		title = response.xpath('//div[@id="ctitle"]/text()').extract()[0]
		next_url = 'https://xkcd.com' + str(next)
		file_url = 'http:'+str(img_url[0])
		file_name = file_url.split('/')[4]
		testfile = urllib.URLopener()
		fullfilename = os.path.join('xkcd_images/', file_name)
		print file_url
		testfile.retrieve(file_url.encode('utf-8'), fullfilename)
		if(len(next)!=0):
			yield scrapy.Request(url=next_url, callback=self.parse)
		
		pass
