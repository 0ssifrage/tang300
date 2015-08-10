# -*- coding: utf-8 -*-
import json


def main():
    f = open('tang300.v1.json', 'r')
    ps = json.load(f)
    np = []
    for p in ps:
        b = False
        for l in p[3]:
            if u'。' in l or u'，' in l:
                b = True
                break
        if not b:
            t = []
            for i in xrange(len(p[3])/2):
                t.append(p[3][2*i]+u'，'+p[3][2*i+1]+u'。')
            p[3] = t
        np.append(p)
    f2 = open('tang300.v2.json', 'w')
    s = json.dumps(np, ensure_ascii=False, indent=2)
    f2.write(s.encode('utf-8'))
    f.close()
    f2.close()


main()
