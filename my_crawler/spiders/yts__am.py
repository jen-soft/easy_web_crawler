# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Response, HtmlResponse


class YtsAmSpider(scrapy.Spider):
    name = 'yts__am'
    allowed_domains = ['yts.am']
    start_urls = ['https://yts.am/browse-movies']
    custom_settings = {
        # 'DOWNLOAD_TIMEOUT': 180,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'CLOSESPIDER_ITEMCOUNT': 10,
    }

    def parse(self, response):
        assert isinstance(response, HtmlResponse)  # to help the pycharm

        for i in range(3):
            url = 'https://yts.am/browse-movies?page={}'.format(i)
            yield response.follow(url, callback=self.parse)

        moves_links = response.xpath(
            '//a[@class="browse-movie-title"]/@href').extract()
        for url in moves_links:
            yield response.follow(url, callback=self.parse_move)

    def parse_move(self, response):
        assert isinstance(response, HtmlResponse)

        title = response.xpath(
            '//div[@id="movie-info"]/div/h1/text()').extract_first()
        result = response.xpath(
            '//div[@id="movie-info"]/div/h2/text()').extract()
        if len(result) == 2:
            yer, genre = result
        else:
            yer = result
            genre = 'N/A'


        likes = response.xpath(
            '//div[@id="movie-info"]//*[@id="movie-likes"]/text()'
        ).extract_first()
        raiting = response.xpath(
            '//div[@id="movie-info"]//*[@itemprop="ratingValue"]/text()'
        ).extract_first()
        imdb_url = response.xpath(
            '//div[@id="movie-info"]//div[@class="rating-row"]/a/@href'
        ).extract_first()
        poster_img_url = response.xpath(
            '//div[@id="movie-poster"]//img/@src'
        ).extract_first()

        sources = []
        s_ = response.xpath(
            '//div[@class="modal-torrent"]')
        for s in s_:
            resolution = s.xpath(
                './div[@class="modal-quality"]/@id').extract_first()
            file_size = s.xpath(
                './p[@class="quality-size"]/text()').extract_first()
            https_urls = s.xpath(
                './/a[contains(@href, "https://")]/@href').extract()
            magnet_urls = s.xpath(
                './/a[contains(@href, "magnet:")]/@href').extract()
            sources.append([resolution, file_size, https_urls, magnet_urls])

        synopsis = response.xpath(
            '//div[@id="synopsis"]/p//text()').extract_first()

        result = {
            'title': title,
            'yer': yer,
            'genre': genre,
            'likes': likes,
            'raiting': raiting,
            'imdb_url': imdb_url,
            'poster_img_url': poster_img_url,
            'sources': sources,
            'synopsis': synopsis,
        }
        yield result

