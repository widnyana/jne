#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    DEPRECATED :p
"""
from lxml import etree


def chunk(l, num):
    """Yield num-sized chunk from l"""
    for i in xrange(0, len(l), num):
        yield l[i:i+num]


def tariff(content):
    """Parse Content and create response"""
    stack = {}
    data = etree.HTML(content)
    tujuan = data.xpath("//td[@class='tarif_post_70']//text()")
    tarif = data.xpath("//tr[not(@class)]//td[@class='list_tarif_33']//text()")

    stack['dari'] = tujuan[0]
    stack['menuju'] = tujuan[1]
    stack['berat'] = tujuan[2]

    if tarif:
        tarif_stack = []
        tarif = list(chunk(tarif, 3))
        for item in tarif:
            entry = {
                "paket": item[0],
                "jenis": item[1],
                "harga": item[2]
            }
            tarif_stack.append(entry)
    else:
        tarif_stack = []

    stack['tarif'] = tarif_stack

    return stack

if __name__ == '__main__':
    fh = open("result.html", mode="r")
    content = fh.read()
    fh.close()

    tariff(content)
