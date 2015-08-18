# -*- coding: utf-8 -*-
from config import APP_KEY, APP_SECRET, C_URL, ACCESS_TOKEN, EXPIRES_IN
import json
import os
import urllib
from weibo import APIClient


def main():
    client = APIClient(
        app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=C_URL)
    client.set_access_token(ACCESS_TOKEN, EXPIRES_IN)
    base_dir = os.path.split(os.path.realpath(__file__))[0]

    f = open(os.path.join(base_dir, 'tang300.v4.json'), 'r')
    ps = json.load(f)
    f.close()
    logfilename = os.path.join(base_dir, 'log.txt')
    logfile = open(logfilename, 'r')
    idx = int(logfile.read())
    logfile.close()

    p = ps[idx]
    q = urllib.quote_plus(p[1].encode('utf8'))
    s = u'《%s》%s %s https://www.google.com.hk/#q=%s' % (p[1], p[2], p[0], q)
    s = urllib.quote_plus(s.encode('utf8'))
    img = os.path.join(base_dir, 'poem_png/%03d.png' % idx)
    client.statuses.upload.post(
        status=s, pic=open(img, 'rb'))

    idx += 1
    logfile = open(logfilename, 'w')
    logfile.write(str(idx))
    logfile.close()


main()
