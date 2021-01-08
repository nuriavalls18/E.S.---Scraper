from selenium import webdriver

chromedriver_path = '/home/nuria/chromedriver' 
url = 'file:///home/nuria/Descargas/factura.html'

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

driver.get(url)

###### Auxiliar function

def add_element_to_list(element_class,item,elements_list):
    element = item.find_elements_by_xpath(element_class)
    if element:
        elements_list.append(element)

invoice_table = driver.find_element_by_xpath('//tr[5]/td/table/tbody/tr/td/table/tbody')
top_head_table = invoice_table.find_elements_by_xpath('.//tr')

total_invoice_value = invoice_table.find_elements_by_xpath('.//tr[11]/td[@class="caixaTxtDinheiroBold"]')
total_invoice_value_list = [] 
for i in total_invoice_value:
    total_invoice_value_list.append(i.text)

description = []
description_values = []
for index, item in enumerate(top_head_table):
    add_element_to_list('.//td[@class="caixaItensDescB"]', item, description)

for i in description:
    for e in i:
        if e.text != "":
            description_values.append(e.text)

quantity = []
quantity_values = []
for index, item in enumerate(top_head_table):
    add_element_to_list('.//td[@class="caixaItensQuant"]', item, quantity)

for i in quantity:
    for e in i:
        if e.text != "":
            quantity_values.append(e.text)

price = []
price_values = []
for index, item in enumerate(top_head_table):
    add_element_to_list('.//td[@class="caixaItensPreco"]', item, price)

for i in price:
    for e in i:
        if e.text != "":
            price_values.append(e.text)

value = []
total_invoice_value_list =[] 
for i in total_invoice_value:
    total_invoice_value_list.append(i.text)
value_values = []
for index, item in enumerate(top_head_table):
    add_element_to_list('.//td[@class="caixaTxtDinheiro"]', item, value)

for i in value:
    for e in i:
        if e.text != "":
            value_values.append(e.text)
        
items = {}
for index, value in enumerate(description_values):
    items[description_values[index]] = {
        "Quantity": quantity_values[index],
        "Price": price_values[index],
        "Value": value_values[index],
    }


invoice_taxes_table = driver.find_element_by_xpath('//tr[5]/td/table/tbody/tr/td/table[2]/tbody')
taxes_information_table_tr2 = invoice_taxes_table.find_elements_by_xpath('.//tr[2]')
taxes_information_table_tr3 = invoice_taxes_table.find_elements_by_xpath('.//tr[3]')
taxes_information_table_tr4 = invoice_taxes_table.find_elements_by_xpath('.//tr[4]')

values_ICMS = []
values_PIS = []
values_COFINS = []
for index, item in enumerate(taxes_information_table_tr4):
    add_element_to_list('.//td[@class="caixaTxt2"][1]', item, values_ICMS)
    add_element_to_list('.//td[@class="caixaTxt2"][2]', item, values_ICMS)
    add_element_to_list('.//td[@class="caixaTxt2"][3]', item, values_ICMS)
    add_element_to_list('.//td[@class="caixaTxt2"][4]', item, values_PIS)
    add_element_to_list('.//td[@class="caixaTxt2"][5]', item, values_PIS)
    add_element_to_list('.//td[@class="caixaTxt2"][6]', item, values_PIS)
    add_element_to_list('.//td[@class="caixaTxt2"][7]', item, values_COFINS)
    add_element_to_list('.//td[@class="caixaTxt2"][8]', item, values_COFINS)
    add_element_to_list('.//td[@class="caixaTxt2"][9]', item, values_COFINS)



values_ICMS_texto = []
for i in values_ICMS:
    for e in i:
        if e.text != "":
            values_ICMS_texto.append(e.text)

values_PIS_texto = []
for i in values_PIS:
    for e in i:
        if e.text != "":
            values_PIS_texto.append(e.text)

values_COFINS_texto = []
for i in values_COFINS:
    for e in i:
        if e.text != "":
            values_COFINS_texto.append(e.text)

response = {
    "items": items,
    "Total invoice value": total_invoice_value_list[0],
    "Taxes": {
        "ICMS": {
            "Base of calculation" : values_ICMS_texto[0],
            "%" : values_ICMS_texto[1],
            "Value" : values_ICMS_texto[2]
        },
        "PIS": {
            "Base of calculation" : values_PIS_texto[0],
            "%" : values_PIS_texto[1],
            "Value" : values_PIS_texto[2]
        },
        "COFINS": {
            "Base of calculation" : values_COFINS_texto[0],
            "%" : values_COFINS_texto[1],
            "Value" : values_COFINS_texto[2]
        }
    }
}

print(response)