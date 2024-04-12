import json

def split_json(input_file, output_prefix, skip_records, num_records):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    start_index = skip_records
    end_index = start_index + num_records
    chunk_data = data[start_index:end_index]

    output_file = f"{output_prefix}_{start_index + 1}_{end_index}.json"
    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(chunk_data, out_file, ensure_ascii=False, indent=2)

input_file = "data_dir/train_data.json"  # 輸入的JSON檔案
output_prefix = "output_chunk"  # 輸出檔案的前綴名稱
num_records = 20000  # 要匯出的記錄數
skip_records = 0  # 要跳過的記錄數

split_json(input_file, output_prefix, skip_records, num_records)
