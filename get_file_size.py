import requests

url = 'https://gate.radxa.com/radxa-build/radxa-zero3/releases/download/b6/radxa-zero3_debian_bullseye_xfce_b6.img.xz'

res = requests.head(url, allow_redirects=True)
length = res.headers.get('Content-Length')

name = url.split('/')[-1].split('.')[0]
_json = {
    'name': name,
    'size': length
}

print(_json)
