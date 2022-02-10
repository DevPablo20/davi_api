import json
from string_simplified_functions import full_name_to_first,full_to_full,full_name_to_last,security_code_formatation
from string_simplified_functions import year_formatation, month_formatation, cpf_formatation, card_formatation
from string_simplified_functions import card_brand_formatation

with open('input_card.json') as json_file:
    brute_data = json.load(json_file)
    json_file.close()

new_dict_2 = {}
for key in brute_data.keys(): # The problem is in the loop for estruturation
    for n in brute_data.values():
        new_dict = {}
        full_name = full_to_full(n['full_name'])
        cpf = cpf_formatation(n['cpf'])
        card_number = card_formatation(n['card_number'])
        expiration_mm = month_formatation(n['expiration_mm'])
        expiration_yyyy = year_formatation(n['expiration_yyyy'])
        card_brand =  card_brand_formatation(n['card_brand'])
        security_code = security_code_formatation(n['security_code'])
        new_dict['full_name'] = full_name
        new_dict['cpf'] = cpf
        new_dict['card_number'] = card_number
        new_dict['expiration__mm'] = expiration_mm
        new_dict['expiration_yyyy']  =  expiration_yyyy
        new_dict['card_brand'] = card_brand
        new_dict['security_code'] = security_code
        new_dict_2.update({key: new_dict})
        print(new_dict_2)
new_json_dict = json.dumps(new_dict_2)
print(new_json_dict)

"""
with open('output_json.json', 'w') as output_json:
    output_json.write(new_json_dict)
"""




"""
new_json = {
    'full_name': None,
    'cpf': None,
    'card_number': None,
    'expiration_mm': None,
    'expiration_yyyy': None,
    'card_brand': None,
    'security_code' : None
}
"""