# Easy example of crawler based on scrapy


## quick start
    create virtual env
        virtualenv --system-site-packages --python="/usr/bin/python2.7" --prompt="(env: ${PWD##*/})" env
    activate env
        source env/bin/activate
    install scrapy
        pip install Scrapy
        pip install Twisted==16.0.0   # only for python2.7
    run crawler
        scrapy crawl yts__am -o data/yts__am.json
        python run_spider.py # alternative



## start own project from zero
    pip install Scrapy
    pip install Twisted==16.0.0   # only for python2.7
    scrapy startproject my_crawler ./
    scrapy genspider yts__am yts.am


## scrapy tutorial
    https://doc.scrapy.org/en/latest/intro/tutorial.html


## The MIT License
    https://opensource.org/licenses/MIT


## developed by Jen-Soft
    https://www.upwork.com/freelancers/~0110273df78bbbfce4