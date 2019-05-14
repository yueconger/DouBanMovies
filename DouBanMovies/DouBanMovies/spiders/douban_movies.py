# -*- coding: utf-8 -*-
import scrapy


class DoubanMoviesSpider(scrapy.Spider):
    name = 'douban_movies'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }
    character_url = 'https://movie.douban.com/celebrity/{character_id}/'  # 人物信息
    rewards_url = 'https://movie.douban.com/celebrity/{character_id}/awards/'  # 人物获奖信息
    chara_movies_url = 'https://movie.douban.com/celebrity/{character_id}/movies/'  # 人物作品页信息
    chara_partners_url = 'https://movie.douban.com/celebrity/{character_id}/partners/'  # 人物相关信息

    def parse(self, response):
        pass
