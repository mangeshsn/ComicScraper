import scrapy
import re
import urllib
import os
from scrapy.http import HtmlResponse
class CommitStrip(scrapy.Spider):
	name = "extract_all"
	start_urls = [
	'http://www.commitstrip.com/en/',
	]
	dict = {}
	
	def parse(self, response):
		list = []
		data = response.xpath('//div[@class="wp-pagenavi"]/a[@class="nextpostslink"]/@href').extract()
		
		if(len(data) != 0):
			yield scrapy.Request(url=str(data[0]), callback=self.parse)
		comic_url = response.xpath('//div[@class="excerpt"]/section/a/@href').extract()
		
		for i in comic_url:
			yield scrapy.Request(url=str(i), callback=self.parse)
		data1 = response.xpath('//div[@class="entry-content"]/p/img/@src').extract()
		for j in data1:
			
			file_name = j.split('/')[7]
			print file_name
			testfile = urllib.URLopener()
			fullfilename = os.path.join('images/', file_name)
			testfile.retrieve(j.encode('utf-8'), fullfilename)