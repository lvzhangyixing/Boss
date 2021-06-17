# Scrapy settings for Boss project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Boss'

SPIDER_MODULES = ['Boss.spiders']
NEWSPIDER_MODULE = 'Boss.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Boss (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Boss.middlewares.BossSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'Boss.middlewares.RandomUserAgent': 543,
    'Boss.middlewares.SeleniumMiddleware': 544,
    'Boss.middlewares.ProxyMiddleware': 545,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Boss.pipelines.MongodbPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

PROXIES = ['http://8.210.11.115:16308', 'http://8.210.11.115:16302',
           'http://47.242.13.24:10560', 'http://8.210.11.115:16303',
           'http://47.242.13.24:10561', 'http://8.210.11.115:16305',
           'http://47.242.13.24:10559', 'http://47.242.13.24:10556',
           'http://8.210.11.115:16300', 'http://8.210.11.115:16311',
           'http://8.210.11.115:18717', 'http://49.51.73.134:17594',
           'http://8.210.11.115:16298', 'http://47.242.13.24:10555',
           'http://49.51.73.134:17593', 'http://49.51.73.134:17592',
           'http://8.210.11.115:18719', 'http://8.210.11.115:16297',
           'http://8.210.11.115:16310', 'http://8.210.11.115:16306',
           'http://47.242.13.24:10558', 'http://47.242.13.24:10557',
           'http://8.210.11.115:16307', 'http://8.210.11.115:18718',
           'http://8.210.11.115:16304', 'http://8.210.11.115:16299',
           'http://47.242.13.24:10553', 'http://47.242.13.24:10554',
           'http://8.210.11.115:16309', ]
