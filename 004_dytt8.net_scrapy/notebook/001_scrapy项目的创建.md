## 创建项目
- scrapy startproject dytt8
- cd dytt8
- scrapy genspider dytt8alex dytt8.net

你会得到如下的目录结构

```bash
.
├── dytt8
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   └── settings.cpython-38.pyc
│   ├── settings.py
│   └── spiders
│       ├── dytt8alex.py
│       ├── __init__.py
│       └── __pycache__
│           ├── dytt8alex.cpython-38.pyc
│           └── __init__.cpython-38.pyc
└── scrapy.cfg

```


## 先随便玩一下

打开 dytt8/dytt8/spiders/dytt8alex.py

修改成如下内容
（其实其他都没改，就Dytt8alexSpider.parse()方法里面的代码）

```python
import scrapy


class Dytt8alexSpider(scrapy.Spider):

    name = 'dytt8alex'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://dytt8.net/']

    def parse(self, response):
        # 打印一下，看看这个response是个什么东西
        print(response)
        print(response.text)
```

运行一下： scrapy genspider dytt8alex

看到结果之后，你应该知道两个事情

scrapy.Spider这个基本类，大概干什么事情
response 是什么
