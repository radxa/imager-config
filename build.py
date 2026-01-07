import json
import os


def convert_bytes(bytes, decimals=2):
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    if bytes == 0:
        return '0 B'
    i = 0
    while bytes >= 1024 and i < len(units) - 1:
        bytes /= 1024
        i += 1
    return f'{bytes:.{decimals}f} {units[i]}'

def get_result():
    root = os.path.join(os.path.dirname(__file__), 'products')
    with open(os.path.join(root, 'config.json'), encoding='utf8') as f:
        imager_config = json.load(f)

    result = {
        "family": [],
        **imager_config
    }
    for serial in os.listdir(root):
        _path = os.path.join(root, serial)
        _config = os.path.join(_path, 'config.json')
        if not os.path.exists(_config):
            continue
        with open(_config, 'r', encoding='utf8') as f:
            serial_data = json.load(f)
        serial_data['devices'] = []
        for device in os.listdir(_path):
            if device != 'config.json':
                with open(os.path.join(_path, device, 'config.json'), encoding='utf8') as f:
                    device_data = json.load(f)
                device_data['images'] = []
                image_path = os.path.join(_path, device)
                for image in os.listdir(image_path):
                    if image != 'config.json':
                        with open(os.path.join(image_path, image), encoding='utf8') as f:
                            image_data = json.load(f)
                        device_data['images'].append(image_data)
                device_data['images'].sort(key=lambda x: x['sort'], reverse=True)
                serial_data['devices'].append(device_data)
        serial_data['devices'].sort(key=lambda x: x['sort'], reverse=True)
        result['family'].append(serial_data)

    result['family'].sort(key=lambda x: x['sort'], reverse=True)
    return result

if __name__ == '__main__':
    print(json.dumps(get_result(), indent=2, ensure_ascii=False))
