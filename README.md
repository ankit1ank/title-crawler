## Title Crawler

A web crawler that prints title of all web pages is crawls. And does so in 40 lines of python.

#### How to use:
You need [Requests](http://docs.python-requests.org/en/master/) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) installed either globally or in a virtualenv.

Download the `titlecrawler.py` file.
Run the script using the command below:

```
python titlecrawler.py
```

By default, the script starts crawling with `http://news.ycombinator.com` as the beginning url. You can change the seed url by using the following command.

```
python titlecrawler.py https://moz.com/top500
```