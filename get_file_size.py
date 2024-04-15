import json

import requests

url = 'https://github.com/radxa-build/rock-3c/releases/download/b36/rock-3c_debian_bullseye_cli_b36.img.xz'
date = '2023-08-03'

url = url.replace('github.com', 'gate.radxa.com')
ver = url[:-2] + 'sha512'
res = requests.head(url, allow_redirects=True)
length = res.headers.get('Content-Length')

name = url.split('/')[-1].split('.')[0]
_json = {
    'id': name,
    'name': name,
    'size': int(length),
    'pic_url': "https://imager.radxa.com/image/debian.svg",
    "desc": "This flavor is officially supported, tested, and recommended for all users." if 'cli' not in url else "This flavor is quite minimal and is intended for headless usage.",
    'time': date,
    'edit': True,
    'edit_version': 1,
    "hide": False,
    "checksum_method": "sha512",
    "checksum_file": "url",
    "checksum_url": ver,
    "extension": "xz",
    "download_url": url,
    'sort': '0'
}

print(json.dumps(_json, indent=4))
