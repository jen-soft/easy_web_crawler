import os
from scrapy.crawler import CrawlerProcess
from scrapy.cmdline import execute, get_project_settings
from my_crawler.spiders.yts__am import YtsAmSpider


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def main():
    result_file_path = os.path.join(BASE_DIR, 'data/debug_data.json')
    if os.path.exists(result_file_path):
        os.remove(result_file_path)

    settings = get_project_settings()
    settings.update({
        'LOG_FILE':     None,  # default stdout
        # 'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_URI':     result_file_path,
        'FEED_FORMAT':  'json',
    })
    crawler = CrawlerProcess(settings)
    spider = YtsAmSpider()
    crawler.crawl(spider)
    crawler.start()
    crawler.stop()
    spider.log('--------------------------------------------------------------')
    spider.log('file saved at {file_path}'.format(file_path=result_file_path))


if __name__ == "__main__":
    main()

