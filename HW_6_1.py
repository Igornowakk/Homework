dict_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750 }]
result_dict = {}

for element in dict_list:
    key = element['item']
    value = element['amount']
    if key in result_dict:
        result_dict[key] += value
    else:
        result_dict[key] = value

print(result_dict)