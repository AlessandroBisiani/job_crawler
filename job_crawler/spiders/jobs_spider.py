#!/usr/bin/env python3

import scrapy

class StackOverflowSpider(scrapy.Spider):
    """Scrape job postings for skill requirements related to python
    """

    name = 'stack_overflow_jobs'
    download_delay = 2
    start_urls = [
        'https://stackoverflow.com/jobs?l=berlin&d=20&u=Km&tl=python'
        ]

    def parse(self, response):
        for post in response.css('div.-job'):
            yield {
                'job_title':
                    post.css('div.-job h2 > a::attr(title)').get(),
                'company':
                    post.css('div.-job h3 > span::text').get()
                    .splitlines()[0],
                'link':
                    post.css('div.-job h2 > a::attr(href)').get(),
                'skills':
                    post.css('div.-job > div > div > div a::text').getall()
            }

        """
        for href in response.css('.s-pagination > a:last-child::attr(href)'):
            yield response.follow(href, callback=self.parse)
        """
        #response.follow() uses anchors' href attribute automatically
        for a in response.css('.s-pagination > a'):
            yield response.follow(a, callback=self.parse)
