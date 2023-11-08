import re
import json

def convert_to_flat_dict(data):
    flat_data = {}

    for category in data:
        for key in data[category]:
            flat_data[key] = data[category][key]

    return flat_data

# Đọc dữ liệu từ file export.js
with open('export.js', 'r') as file:
    content = file.read()

# Sử dụng regex để lấy nội dung từ export.js
# match = re.search(r'=\s*({.*?})\s*;', content, re.DOTALL)
# print(match)
if content:
    # Chuyển đổi dữ liệu thành từ điển Python
    data = json.loads(content.group(1))

    # Chuyển đổi thành từ điển phẳng
    flat_data = convert_to_flat_dict(data)
    print(flat_data)
else:
    print("Không tìm thấy dữ liệu phù hợp trong tệp export.js.")
