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


root = 'products'

with open(os.path.join(root, 'config.json')) as f:
    imager_config = json.load(f)

result = {
    "devices": [],
    "device_images": {},
    "images": {},
    **imager_config
}

for serial in os.listdir(root):
    _path = os.path.join(root, serial)
    _config = os.path.join(_path, 'config.json')
    if not os.path.exists(_config):
        continue
    with open(_config, 'r') as f:
        serial_data = json.load(f)
    serial_data['data'] = []
    result['devices'].append(serial_data)
    for device in os.listdir(_path):
        if device != 'config.json':
            with open(os.path.join(_path, device, 'config.json')) as f:
                device_data = json.load(f)
            serial_data['data'].append(device_data)
            image_path = os.path.join(_path, device)
            _image_result = []
            for image in os.listdir(image_path):
                if image != 'config.json':
                    with open(os.path.join(image_path, image)) as f:
                        image_data = json.load(f)
                        _image_result.append(
                            {
                                'id': image_data['id'],
                                'pic_url': image_data.get('pic_url', ''),
                                'name': image_data['name'],
                                'desc': image_data.get('desc', ''),
                                'time': image_data.get('time', ''),
                                'size': convert_bytes(image_data['size']),
                                'edit': image_data['edit'],
                                'edit_version': image_data.get('edit_version', 0),
                                'hide': image_data['hide'],
                            }
                        )
                        result['images'][image_data['id']] = {
                            "checksum_method": image_data['checksum_method'],
                            "checksum_file": image_data['checksum_file'],
                            "checksum_url": image_data['checksum_url'],
                            "extension": image_data['extension'],
                            "download_url": image_data['download_url'],
                            "size": image_data['size'],
                        }
            result['device_images'][device_data['id']] = _image_result
print(json.dumps(result, indent=4))
