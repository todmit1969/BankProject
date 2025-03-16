'#-*- coding: utf-8 -*-'
import re

def get_trans_by_desc(dict_list, string):
    trans_by_desc = []
    pattern = re.compile(string, flags=re.IGNORECASE)
    for item in dict_list:
        if 'description' in item and pattern.findall(item['description']):
            trans_by_desc.append(item)
    return trans_by_desc



