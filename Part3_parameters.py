from selenium import webdriver

chromedriver_path = '/home/nuria/chromedriver' 
url = 'file:///home/nuria/Descargas/factura.html'

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

driver.get(url)


###### Auxiliar function

def add_element_to_list(element_class,item,elements_list):
    element = item.find_elements_by_xpath(element_class).text
    if element:
        elements_list.append(element)

### Get parameters function

invoice_table = driver.find_element_by_xpath('//tr[5]/td/table/tbody/tr/td/table/tbody')
top_head_table = invoice_table.find_elements_by_xpath('.//tr')

titles_list =[]
table_content_list = []
for index, item in enumerate(top_head_table):
    #Titulo descripcion, cantidad, precio, valor, valor total
    add_element_to_list('.//td[@class="caixaTxt2"]', item, titles_list)
    #consumo TUSD, TE, Contrib
    add_element_to_list('.//td[@class="caixaItensDescB"]', item, table_content_list)
    #lista de cantidades
    add_element_to_list('.//td[@class="caixaItensQuant"]', item, table_content_list)
    #lista de precios
    add_element_to_list('.//td[@class="caixaItensPreco"]', item, table_content_list)
    #lista de valores
    add_element_to_list('.//td[@class="caixaTxtDinheiro"]', item, table_content_list)

""" for i in titles_list:
    for e in i:
        print(e.text)    
for i in table_content_list:
    for e in i:
        print(e.text) """
       
invoice_taxes_table = driver.find_element_by_xpath('//tr[5]/td/table/tbody/tr/td/table[2]/tbody')
taxes_information_table_tr2 = invoice_taxes_table.find_elements_by_xpath('.//tr[2]')
taxes_information_table_tr3 = invoice_taxes_table.find_elements_by_xpath('.//tr[3]')
taxes_information_table_tr4 = invoice_taxes_table.find_elements_by_xpath('.//tr[4]')

information_titles = []
for index, item in enumerate(taxes_information_table_tr2):
    add_element_to_list('.//td[@class="caixaTxt2"][1]', item, information_titles)
    add_element_to_list('.//td[@class="caixaTxt2"][2]', item, information_titles)
    add_element_to_list('.//td[@class="caixaTxt2"][3]', item, information_titles)

""" for i in information_titles:
    for e in i:
        print(e.text) """


information_subtitles = []
for index, item in enumerate(taxes_information_table_tr3):
    add_element_to_list('.//td[@class="caixaTxt2"][1]', item, information_subtitles)
    add_element_to_list('.//td[@class="caixaTxt2"][2]', item, information_subtitles)
    add_element_to_list('.//td[@class="caixaTxt2"][3]', item, information_subtitles)
    add_element_to_list('.//td[@class="caixaTxt2"][4]', item, information_subtitles)
    add_element_to_list('.//td[@class="caixaTxt2"][5]', item, information_subtitles)
    add_element_to_list('.//td[@class="caixaTxt2"][6]', item, information_subtitles)
    add_element_to_list('.//td[@class="caixaTxt2"][7]', item, information_subtitles)
    add_element_to_list('.//td[@class="caixaTxt2"][8]', item, information_subtitles)
    add_element_to_list('.//td[@class="caixaTxt2"][9]', item, information_subtitles)

""" for i in information_subtitles:
    for e in i:
        print(e.text) """

information_values = []
for index, item in enumerate(taxes_information_table_tr4):
    add_element_to_list('.//td[@class="caixaTxt2"][1]', item, information_values)
    add_element_to_list('.//td[@class="caixaTxt2"][2]', item, information_values)
    add_element_to_list('.//td[@class="caixaTxt2"][3]', item, information_values)
    add_element_to_list('.//td[@class="caixaTxt2"][4]', item, information_values)
    add_element_to_list('.//td[@class="caixaTxt2"][5]', item, information_values)
    add_element_to_list('.//td[@class="caixaTxt2"][6]', item, information_values)
    add_element_to_list('.//td[@class="caixaTxt2"][7]', item, information_values)
    add_element_to_list('.//td[@class="caixaTxt2"][8]', item, information_values)
    add_element_to_list('.//td[@class="caixaTxt2"][9]', item, information_values)

""" for i in information_values:
    for e in i:
        print(e.text) """


""" parameters_dict = {
    'Description': table_content_list[0]
} """

 
parameters_dict = {
    "Descripción": {
        "cantidad": table_content_list[1],
        "precio": table_content_list[2],
        "valor": table_content_list[3]
    },
}
    
print(parameters_dict)