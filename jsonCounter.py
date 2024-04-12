import json

def count_entries(json_file_path):
    try:
        # 讀取 JSON 檔案
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 計算條目總數
        total_entries = len(data)
        return total_entries

    except FileNotFoundError:
        print(f"找不到檔案: {json_file_path}")
        return None
    except json.JSONDecodeError:
        print(f"JSON 解析錯誤: {json_file_path}")
        return None

file_path = 'data_dir/test_data.json'

total_entries = count_entries(file_path)

if total_entries is not None:
    print(f"總筆數: {total_entries}")
