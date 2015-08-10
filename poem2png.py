import json
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps


width = 1080
min_height = width
margin_min = 72

max_tfz = 72
max_afz = 32
max_cfz = 48


def get_fontsize_and_margin(l, maxfs):
    fs = min(maxfs, (width - margin_min*2) / l)
    return [fs, (width - fs*l) / 2]


def render_poem(p, idx):
    lt = len(p[1])
    la = len(p[2])
    lc = max(map(lambda x: len(x), p[3]))

    tfz, tmar = get_fontsize_and_margin(lt, max_tfz)
    afz, amar = get_fontsize_and_margin(la, max_afz)
    cfz, cmar = get_fontsize_and_margin(lc, max_cfz)

    tfnt = ImageFont.truetype('Wyue-GutiFangsong-NC_deliverable.otf', tfz)
    afnt = ImageFont.truetype('Wyue-GutiFangsong-NC_deliverable.otf', afz)
    cfnt = ImageFont.truetype('Wyue-GutiFangsong-NC_deliverable.otf', cfz)

    height = margin_min*2 + tfz*1.5 + afz*2.5 + cfz*len(p[3])*1.6
    height = max(min_height, int(height))

    img = Image.new("RGB", (width, height), "#FFF")
    drw = ImageDraw.Draw(img)
    y = margin_min

    drw.text((tmar, y), p[1], font=tfnt, fill='#000')
    y += tfz*1.5

    drw.text((amar, y), p[2], font=afnt, fill='#000')
    y += afz*2.5

    for l in p[3]:
        drw.text((cmar, y), l, font=cfnt, fill='#000')
        y += cfz*1.6

    f = open('poem_png/%03d.png' % idx, 'wb')
    img.save(f, 'PNG')


def main():
    f = open('./tang300.v4.json', 'r')
    ps = json.load(f)
    if not os.path.exists('poem_png'):
        os.makedirs('poem_png')
    i = 0
    for p in ps:
        render_poem(p, i)
        i += 1


main()
