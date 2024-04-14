import json

import requests

url = 'https://github.com/radxa-build/radxa-zero3/releases/download/b6/radxa-zero3_debian_bullseye_xfce_b6.img.xz'
date = '2024-01-10'

url = url.replace('github.com', 'gate.radxa.com')
ver = url[:-2] + 'sha512'
res = requests.head(url, allow_redirects=True)
length = res.headers.get('Content-Length')

name = url.split('/')[-1].split('.')[0]
_json = {
    'name': name,
    'size': int(length),
    'pic_url': "https://imager.radxa.com/image/debian.svg",
    "desc": "This flavor is officially supported, tested, and recommended for all users.",
    'time': date,
    'edit': True,
    'edit_version': 1,
    "hide": False,
    "checksum_method": "sha512",
    "checksum_file": "url",
    "checksum_url": ver,
    "extension": "xz",
    "download_url": url
}

print(json.dumps(_json, indent=4))
