### 微博定时发唐诗三百首

用 `crontab` 定时调用 `weibotang300.py` 来定时发送微博。

`crawler.py` 从 [維基文庫 - 唐詩三百首](https://zh.wikisource.org/zh-hant/%E5%94%90%E8%A9%A9%E4%B8%89%E7%99%BE%E9%A6%96) 爬取唐诗内容。

`tang300.v4.json` 为整理后的唐诗文件。

由于新浪微博字数限制，`poem2png.py` 将唐诗转化为图片后发送。字体选用 [文悦古体仿宋](http://wytype.com/typeface/WyueGutiFangsong/) 但会有部分字缺失。
