#!/usr/bin/env python3
# rewrite index.html and index.en.html

de_html = open('index.html', 'rb').read()
en_html = open('index.en.html', 'rb').read()
print("DE size:", len(de_html), "EN size:", len(en_html))
print("OK")
