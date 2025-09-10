# Scrapy settings for work_two project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "work_two"

SPIDER_MODULES = ["work_two.spiders"]
NEWSPIDER_MODULE = "work_two.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "work_two (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    # 'Cookie': 'bm_s=YAAQUJUjF9DNVuOYAQAA/Wa59QNicbbmd3yn62s1QTm9X7z4tZFKjed6D0crCFB78V6UiE6IA5OvRzynHm+OYzHC3ony2CIsScerCA4gFlAqcnWV6E2gsbBVTx3LidqTso2Bb02BQfQg/QyVPHL9NFyVpx4gCecK+9dqlZK//4u65wc8WdWhp4c6XaqY9j5+RPAFa7vpuc0TTxwrXeACjNcuZX+DzLWy6or6ETMnwVWSUDx0KGQRpCWdO9rbidd2G+Et/ODBi0ZnAQfExi+XBrWjpdPGHXJUhxEGJZBGCJJmERJ7/SW2znEMdb12nC4mbO5TU6TGFWiRviZfyHeLUN8qbJ/PP1TvsxzC7eYP56Iqp24WDpt9HEkRnGos67iGhhgDyYBWQLqwPJQFlnL+D3d4ZmrajjccfJA5p3tyhNydivr5ZRTfL6DZMTOSQCPDYp+6UDPQ0v63qnvvCCNl7zpalRjazWhkTSJqsDC9sgRMrNVlLu0T7MXRJGUAm7cT4N+BGWM4JjJLw7fKgdRdacqRGvDxe0TdVreLc3l33swsMdWWvzdY8zg=; vstr=f7a39f9a-93fd-4c0d-b759-258791c5a645; ref=3; vsutms=6228bfb3-4e76-46a8-8f1e-5e2720485b21#f7a39f9a-93fd-4c0d-b759-258791c5a645#606664dd-7cf5-418f-b3b5-dee4c4aee140#1756888362##||||; COOKIE_CONSENT={"key":"eyJuZWNlc3NhcnkiOnRydWUsImFuYWx5dGljcyI6dHJ1ZSwiYWR2ZXJ0aXNpbmciOnRydWUsInBlcnNvbmFsaXphdGlvbiI6dHJ1ZX0=","consent":{"necessary":true,"analytics":true,"advertising":true,"personalization":true},"accepted":true}; vstrType=1; _ga_DJ23BNLRSH=GS2.1.s1756888362$o10$g1$t1756890510$j60$l0$h0; _ga=GA1.1.891713533.1755078133; ajs_anonymous_id=c338f3f1-80c2-4d22-9bb4-c25a7f2189d7; bm_lso=5DE83CD0A73EC747F082BA47E92D817B1509C3564EF10AA530F6AB45B38A8F96~YAAQ3wFAFypewbKYAQAAoz7WzwTF68JewW0BZWOFzMFBWL9PCTL0Vkb5BsLlGRsLXkIDbmH7UMbI05VCVjiMR/Vx0xtVk3zgubEtPcMj7YQToXdYH/k/AoR0Ue6mrHFe0QcMm5VxAtYOfo8V7slQjg6cntrkLXp9FQeoIL9h2qbnMwEL2UZN7lznqXOl7atGZNF5kFymTNKR6E9CnpNMQNqAv/XKJxzJ2noXMKFxqoggWC1uyJpSlQlOaGUdaUtRa/9U8CViSuUkOsSK9HmCK6MZc4OQgiGN55APrL1s+GvFhnUnNZqkSeXQawRBDIMQWech/S7QMW3tvFwGE6860IXGVrE+qEgtrV7SKnFaAbGyNdKBNVvOnJyYJ7f6uaxnrVQbvceK+FemUiqhxDZeBqhl178rxIOGLOFMk6voDIt9cC7ilwCaBwDeWhR8a985x8SbCUjBXUC7131jsgk=^1755833582253; fs_uid=#o-215TGH-na1#dda7a25d-476e-4671-b3c6-5bdfd7d12d19:58b094eb-e995-4e6c-b85d-84721dc7f64b:1755833583404::1#/1787369585; x-georegion=104,IN,KA,MANGALORE,,,,,,12.86,74.84,GMT+5.50,,AS,,,45769,vhigh,5000; visitor_layeruid=c9467602-014c-46eb-b884-1e71a2ee1b17_1_rmc_GENRIC; ew_exp=eed16e85-6b2a-419d-8c13-474003f67c36_3_1_0_rmc_030925; ak_bmsc=F111A9A669043268CFC217256DEED2ED~000000000000000000000000000000~YAAQUZUjF/MPZeyYAQAAGe+0DhxYzirnNsMxz+LOzZ2FGWfhuEXh0fg+kdiwR2Gs/usibmOuZ65dKuXSphTDTdVRtRZdkynLgPoCFQulohT9wew8qgN8J71gbFpHK8JFWiYnQRz3EWsoTl5IutU7niGUlz1DB7W1IGMSqaPBcFpiyZi252Eui/mQ70uz/Y+Zl0sFvk0V+5HoF0JoEBdh1T6MYlLqCPhTuCQHnbfjTytaC9s129hcmsMzdPRrW83LEmdCA35U5sRpeFMUNEAOT8/33eQpI1LC2qxdNibSt1JfwHH+FE23Foo4u43Dt+cAu/yc3QlgcM0UEdWuCfmSAo07WA9VRXvSQMcKWUkfE/sEgGn7P5+v+F1quIqu6zmNy0JWqagsijPnhYolcLEuWWjEaLntGWoGkukGwZW78YxtZZLKPPNJ3CM0gff6CwHY8S+8mAFU0a/n0DC/Ww==; vssessionuid=2ddc7e2b-0a08-45bb-9c84-6ec8dccf0eee; fs_user=0; bm_sv=9E77FECEA45D2BC94A698C9917F43393~YAAQhdcLFzqSJOCYAQAAQ7fVDhzoHfjylGCc0dF7Sjrqk12YSUZjS9pNaDWoLCS+01RGRqsuKoAhS/J5yyiZFTo8wuFunewiGUtIefDEvdwF3+jOjzYjhGqjwiDS4ktFlOcktpCWtjCixwXGvNEsEHxqbaBg15LGF85tBrhh3sy3G3Nzz/EXGapri5z6YuCAkM721hpk+tr13kXdVtSk5jPotXnNrG8GvaM4Pz1xOwOqSjlstm1r/JaIg11DVf88~1; vsuid=606664dd-7cf5-418f-b3b5-dee4c4aee140; visitinfo=[City,]&[State,]&[Country,IN]&[PostalCode,]',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

FEED_EXPORT_FIELDS = ["title", "date", "location", "salary"]
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "work_two.middlewares.WorkTwoSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "work_two.middlewares.WorkTwoDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "work_two.pipelines.WorkTwoPipeline": 100,
   "work_two.pipelines.SaveToJsonPipeline": 200,
   "work_two.pipelines.SaveToSQLitePipeline": 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
