import re


number_create = [{'parts_name': ['主桁'], 'symbol': ['Mg'], 'number': ['0401'], 'material': ['コンクリート'], 'main_frame': ['〇']}, 
                 {'parts_name': ['主桁'], 'symbol': ['Mg'], 'number': ['0701'], 'material': ['コンクリート'], 'main_frame': ['✕']}]

flattened_join = [{'parts_name': ['主桁 Mg0101'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0102'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0103'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0104'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0201'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0202'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, 
                  {'parts_name': ['主桁 Mg0203'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0204'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0302'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0304'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0401'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0402'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, 
                  {'parts_name': ['主桁 Mg0403'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['主桁 Mg0901'], 'damage_name': ['⑦剥離・鉄筋露出-c'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070537.JPG']}, {'parts_name': ['主桁 Mg0901'], 'damage_name': ['⑰その他(分類6:異物混入)-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070404.JPG']}, {'parts_name': ['横桁 Cr0101'], 'damage_name': ['⑰その他(分類6:施工不良)-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070496.JPG']}, 
                  {'parts_name': ['横桁 Cr0102'], 'damage_name': ['⑰その他(分類6:施工不良)-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070424.JPG', 'infra/img\\9月7日\u3000佐藤\u3000地上\\P9070430.JPG']}, {'parts_name': ['横桁 Cr0103'], 'damage_name': ['⑦剥離・鉄筋露出-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070433.JPG']}, {'parts_name': ['横桁 Cr0201'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['横桁 Cr0301'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['横桁 Cr0402'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None},
                  {'parts_name': ['横桁 Cr0403'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['横桁 Cr0602'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['横桁 Cr0604'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['横桁 Cr0704'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['横桁 Cr0204'], 'damage_name': ['⑦剥離・鉄筋露出-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070478.JPG']}, {'parts_name': ['横桁 Cr0304'], 'damage_name': ['⑦剥離・鉄筋露出-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070476.JPG']}, 
                  {'parts_name': ['横桁 Cr0401'], 'damage_name': ['⑦剥離・鉄筋露出-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070523.JPG']}, {'parts_name': ['横桁 Cr0503'], 'damage_name': ['⑦剥離・鉄筋露出-d', '⑰その他(分類6:施工不良)-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070450.JPG', 'infra/img\\9月7日\u3000佐藤\u3000地上\\P9070452.JPG']}, {'parts_name': ['横桁 Cr0801'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070525.JPG']}, {'parts_name': ['横桁 Cr0802'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070396.JPG', 'infra/img\\9月7日\u3000佐藤\u3000地上\\P9070412.JPG']}, 
                  {'parts_name': ['横桁 Cr0803'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070458.JPG']}, {'parts_name': ['床版 Ds0101'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070497.JPG']}, {'parts_name': ['床版 Ds0201'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['床版 Ds0203'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': None}, {'parts_name': ['床版 Ds0803'], 'damage_name': ['⑦剥離・鉄筋露出-d'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070465.JPG']}, 
                  {'parts_name': ['PC定着部 Cn1203'], 'damage_name': ['NON-a'], 'this_time_picture': None}, {'parts_name': ['橋台[胸壁] Ap0101'], 'damage_name': ['⑳漏水・滞水-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070438.JPG']}, {'parts_name': ['橋台[竪壁] Ac0101'], 'damage_name': ['⑳漏水・滞水-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070438.JPG']}, {'parts_name': ['伸縮装置 Ej0101'], 'damage_name': ['⑳漏水・滞水-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070438.JPG']}, {'parts_name': ['橋台[胸壁] Ap0102'], 'damage_name': ['⑳漏水・滞水-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070443.JPG']}, 
                  {'parts_name': ['橋台[竪壁] Ac0102'], 'damage_name': ['⑳漏水・滞水-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070443.JPG']}, {'parts_name': ['伸縮装置 Ej0102'], 'damage_name': ['⑳漏水・滞水-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070443.JPG']}, {'parts_name': ['支承本体 Bh0102'], 'damage_name': ['NON-a'], 'this_time_picture': None}, {'parts_name': ['沓座モルタル Bm0102'], 'damage_name': ['NON-a'], 'this_time_picture': None}, {'parts_name': ['地覆 Fg0201'], 'damage_name': ['⑫うき-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070535.JPG']}, 
                  {'parts_name': ['排水管 Dp0101'], 'damage_name': ['①腐食(大大)-e', '⑤防食機能の劣化(分類1)-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070422.JPG']}, {'parts_name': ['排水管 Dp0102'], 'damage_name': ['①腐食(小大)-c', '⑤防食機能の劣化(分類1)-e'], 'this_time_picture': ['infra/img\\9月7日\u3000佐藤\u3000地上\\P9070486.JPG']}, {'parts_name': ['排水管 Dp0201'], 'damage_name': ['①腐食(小大)-c', '⑤防食機能の劣化(分類1)-e'], 'this_time_picture': None}, {'parts_name': ['排水管 Dp0202'], 'damage_name': ['①腐食(小大)-c', '⑤防食機能の劣化(分類1)-e'], 'this_time_picture': None}]

# << 材料の置換 >>
""""""
# 置換マッピング
replace_dict = {
    '鋼': 'S',
    'コンクリート': 'C',
    'その他': 'X'
}

# 置換処理
for part in number_create:
    part['material'] = [replace_dict.get(mat, mat) for mat in part['material']]
    # parts_name と symbol の各要素を結合して新しいリストを作成
    combined = [p + ' ' + s for p, s in zip(part['parts_name'], part['symbol'])]
    # 新しいリストを parts_name に設定（symbol は削除）
    part['parts_name'] = combined
    del part['symbol']

""""""

# << parts_nameを部材名と番号に分割 >>
""""""
split_parts_and_damage = []

# 各要素に対して処理を行う
for item in flattened_join:
    combined_string = item['parts_name'][0]
    
    # 正規表現を使って、記号と数字の部分で分割する
    match = re.match(r'(.+ [A-Za-z]+)(\d+)', combined_string)
    
    if match:
        parts_name = match.group(1)
        number = match.group(2)
        
        for damage in item['damage_name']:
            if "-" in damage:
                damage_name, damage_lank = damage.split("-")
            
            parts_dict = {
                'parts_name': [parts_name],
                'number': [number],
                'damage_name': [damage_name],
                'damage_lank': [damage_lank],
                'this_time_picture': item['this_time_picture']  # this_time_pictureを追加
            }
            split_parts_and_damage.append(parts_dict)
            
# 分解
# print(f"split_parts_and_damage：{split_parts_and_damage}")
""""""

# << 2つのリストを合体 >>
def sort_and_merge_list(ordered_result, order_dict, material_dict, order_number, order_lank):
    # ソートキーの設定
    def sort_key(item):
        # parts_nameのソートキー
        parts_name_key = order_dict.get(item['parts_name'][0].split()[0], 0)
        
        # numberのソートキー
        number_key = int(item['number'][0]) if item['number'] and item['number'][0].isdigit() else 0
        
        # damage_nameのソートキー (最初の1文字を使用)
        damage_name_initial = item['damage_name'][0][0] if item['damage_name'] else "None"
        damage_name_key = order_number.get(damage_name_initial, 0)
        
        # damage_lankのソートキー
        damage_lank_key = order_lank.get(item['damage_lank'][0], 0) if item['damage_lank'] else 0
        
        return parts_name_key, number_key, damage_name_key, damage_lank_key

    # リストをソート
    ordered_result = sorted(ordered_result, key=sort_key)

    # 重複および合体の処理
    merged_result = []
    for item in ordered_result:
        # 重複をチェックしてマージするか新規追加するか決定
        if not merged_result:
            merged_result.append(item)
        else:
            last_item = merged_result[-1]
            if (last_item['parts_name'] == item['parts_name'] and 
                last_item['number'] == item['number'] and 
                last_item['damage_name'] == item['damage_name'] and
                last_item['main_frame'] == item['main_frame']):
                
                # materialの合体
                if last_item['material'] and item['material']:
                    last_item['material'] = list(set(last_item['material'] + item['material']))
                elif item['material']:
                    last_item['material'] = item['material']
                
                # damage_lankの合体
                if last_item['damage_lank'] and item['damage_lank']:
                    last_item['damage_lank'] = list(set(last_item['damage_lank'] + item['damage_lank']))
                elif item['damage_lank']:
                    last_item['damage_lank'] = item['damage_lank']
            else:
                merged_result.append(item)

    return merged_result

# 結果格納用のリスト
result = []

# sorted_splitをループし、number_createと比較
for item in split_parts_and_damage:
    found = False
    for nc_item in number_create:
        if item['parts_name'] == nc_item['parts_name'] and item['number'] == nc_item['number']:
            item.update({'material': nc_item['material'], 'main_frame': nc_item['main_frame']})
            found = True
            break
    if 'material' not in item:
        item['material'] = None
    if 'main_frame' not in item:
        item['main_frame'] = None
    result.append(item)

# number_createの項目を結果に追加
for nc_item in number_create:
    # sorted_splitに存在しない場合のチェック
    exists = any(item['parts_name'] == nc_item['parts_name'] and item['number'] == nc_item['number'] for item in split_parts_and_damage)
    if not exists:
        result.append({'parts_name': nc_item['parts_name'], 'number': nc_item['number'], 'material': nc_item['material'], 'main_frame': nc_item['main_frame'], 'this_time_picture': None})

# 指定した順番でキーを整列
ordered_result = []
ordered_keys = ['parts_name', 'number', 'material', 'damage_lank', 'damage_name', 'main_frame', 'this_time_picture']

for item in result:
    ordered_item = {key: item.get(key) for key in ordered_keys}
    ordered_result.append(ordered_item)

# 入力データ

order_dict = {"主桁": 1, "横桁": 2, "床版": 3, "PC定着部": 4, "橋台[胸壁]": 5, "橋台[竪壁]": 6, "支承本体": 7, "沓座モルタル": 8, "防護柵": 9, "地覆": 10, "伸縮装置": 11, "舗装": 12, "排水ます": 13, "排水管": 14}
material_dict = {"S": 1, "C": 2, "X": 3}
order_number = {"None": 0, "①": 1, "②": 2, "③": 3, "④": 4, "⑤": 5, "⑥": 6, "⑦": 7, "⑧": 8, "⑨": 9, "⑩": 10, "⑪": 11, "⑫": 12, "⑬": 13, "⑭": 14, "⑮": 15, "⑯": 16, "⑰": 17, "⑱": 18, "⑲": 19, "⑳": 20, "㉑": 21, "㉒": 22, "㉓": 23, "㉔": 24, "㉕": 25, "㉖": 26}
order_lank = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# ソートとマージ
flattened_join_result = sort_and_merge_list(ordered_result, order_dict, material_dict, order_number, order_lank)

# 結果の表示
for item in flattened_join_result:
    combined = [p_n  + num for p_n, num in zip(item['parts_name'], item['number'])]
    # 新しいリストを parts_name に設定（symbol は削除）
    item['parts_name'] = combined
    del item['number']
    print(item)