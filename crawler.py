# -*- coding: utf-8 -*-
import json
import re
import urllib
import urllib2


def main():
    iurl = 'https://zh.wikisource.org/zh-hant/%E5%94%90%E8%A9%A9%E4%B8%89%E7%99%BE%E9%A6%96'
    content = urllib2.urlopen(iurl).read().decode('utf8')
    re_url = re.compile('<li>([^<]*?) <a href="(.*?)".*?>(.*?)</li>')
    ps = re_url.findall(content)

    res = []
    # t_re = re.compile('dth:50%;"><b>(.*?)</b>')
    # a_re = re.compile(u'作者：</span>.*?>(.*?)</a>')
    c_re = re.compile('poem">\s*?<p>([\W\w]*?)</p>')
    rm_re = re.compile('</*span.*?>|<small[\W\w]*?/small>|\s|</*a>|</*sub>')
    urlbase = "http://diy.fwg.hk/download/chi/learnandteach/software/poem300/"
    i = 0
    for pp in ps:
        i += 1
        if i % 10 == 0:
            print i
        url = "https://zh.wikisource.org" + pp[1]
        # print url
        try:
            content = urllib2.urlopen(url).read().decode('utf8')
            # t = t_re.findall(content)[0]
            # a = a_re.findall(content)[0]
            c = rm_re.sub('', c_re.findall(content)[0]).split('<br/>')
            res.append([url, rm_re.sub('', pp[2]), pp[0], c])
        except:
            print url

    f = open('./tang300.v0.json', 'w')
    s = json.dumps(res, ensure_ascii=False, indent=2)
    # print s
    print len(res)
    f.write(s.encode('utf-8'))
    f.close()


main()
