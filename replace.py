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

        pattern = f"{el_key}:"
        if pattern in js_content:
            idx = js_content.index(pattern)
            start_idx = js_content.index("'", idx) + 1
            end_idx = js_content.index("'", start_idx)
            old_el_value = js_content[start_idx:end_idx]

            if el_value is not None:
                print(f"Giá trị old_el_value là: {old_el_value} | {el_value}")
                js_content = js_content[:start_idx] + el_value + js_content[end_idx:]
            else:
                print(f"Lỗi: el_value là None. Không thể thực hiện thay thế tại dòng {item['stt']}.")

    with open(js_filename, 'w') as js_file:
        js_file.write(js_content)

excel_filename = 'output2.xlsx'
js_filename = 'el.js'

data_from_excel = read_excel_values(excel_filename)
update_el_values(data_from_excel, js_filename)
