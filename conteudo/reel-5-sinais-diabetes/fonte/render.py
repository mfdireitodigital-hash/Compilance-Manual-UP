#!/usr/bin/env python3
"""Renderiza reel.html em frames JPEG deterministicos via __seek(t)."""
import os, sys, glob
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = 'file://' + os.path.join(BASE, 'reel.html')
OUT = os.path.join(BASE, 'frames')
FPS = int(sys.argv[1]) if len(sys.argv) > 1 else 24
ONLY = sys.argv[2] if len(sys.argv) > 2 else None  # ex: "0,120,400" p/ teste

os.makedirs(OUT, exist_ok=True)

def launch(p):
    try:
        return p.chromium.launch(headless=True)
    except Exception as e:
        print('default launch failed:', e)
        return p.chromium.launch(headless=True, executable_path='/opt/pw-browsers/chromium')

with sync_playwright() as p:
    browser = launch(p)
    page = browser.new_page(viewport={'width': 1080, 'height': 1920})
    page.goto(HTML)
    page.wait_for_timeout(400)
    dur = page.evaluate('window.__DURATION')
    total = int(dur / 1000 * FPS)
    print(f'duration={dur}ms fps={FPS} frames={total}')
    idxs = [int(i) for i in ONLY.split(',')] if ONLY else range(total)
    for i in idxs:
        t = i * 1000.0 / FPS
        page.evaluate(f'__seek({t})')
        page.screenshot(path=os.path.join(OUT, f'f_{i:04d}.jpg'), type='jpeg', quality=90)
        if not ONLY and i % 100 == 0:
            print('frame', i, flush=True)
    browser.close()
print('done:', len(glob.glob(os.path.join(OUT, "*.jpg"))), 'frames')
