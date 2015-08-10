# -*- coding: utf-8 -*-
import json


def main():
    f = open('tang300.v3.json', 'r')
    ps = json.load(f)
    np = []
    for p in ps:
        b = False
        if p[3][0][-1] == u'，':
            t = []
            for i in xrange(len(p[3])/2):
                t.append(p[3][2*i]+p[3][2*i+1])
            p[3] = t
        np.append(p)
    f2 = open('tang300.v4.json', 'w')
    s = json.dumps(np, ensure_ascii=False, indent=2)
    f2.write(s.encode('utf-8'))
    f.close()
    f2.close()


main()
