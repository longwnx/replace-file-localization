import openpyxl
import re

def read_excel_values(excel_filename):
    wb = openpyxl.load_workbook(excel_filename)
    ws = wb.active
    data = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        stt, key, el_value = row[0], row[1], row[3]  # Lấy giá trị từ cột A, B và D (EL)
        data.append({'stt': stt, 'key': key, 'el': el_value})

    return data

def update_el_values(data, js_filename):
    with open(js_filename, 'r') as js_file:
        js_content = js_file.read()

    for item in data:
        el_key = item['key']
        el_value = item['el']

        pattern = rf'{el_key}\s*:\s*\'([^\']+)\''
        match = re.search(pattern, js_content)

        if match:
            old_el_value = match.group(1)
            js_content = js_content.replace(old_el_value, el_value)

    with open(js_filename, 'w') as js_file:
        js_file.write(js_content)

excel_filename = 'output.xlsx'
js_filename = 'el.js'

data_from_excel = read_excel_values(excel_filename)
update_el_values(data_from_excel, js_filename)
