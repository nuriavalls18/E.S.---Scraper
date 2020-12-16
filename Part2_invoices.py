from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver_path = '/home/nuria/chromedriver' 
url = 'file:///home/nuria/Descargas/Scraper/Scrapper/nuri.html'

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

driver.get(url)

###################    Create an array from invoice data and items    ###################

table_xpath = ('//fieldset[@id="fs_detalhe"]/table[@class="detalhe tablesorter tb2 tablesorter-default"]/tbody')
table_element = driver.find_element_by_xpath(table_xpath)

invoices = table_element.find_elements_by_xpath('.//tr')
    
results = []
for index, item in enumerate(invoices):
    datetime = item.find_element_by_xpath('.//td[@class="periodo_val detalhe"]').text
    amount = item.find_element_by_xpath('.//td[@class="val_pagar_val detalhe"]').text
    invoice_dict = {
        'Invoice': index,
        'Datetime': datetime,
        'Amount': amount
    }
    results.append(invoice_dict)
    print(f'Theese are the features of the invoice: {invoice_dict}')


###################    Click EXTRAVIO to view the invoice    ###################

position = int(input('Enter the invoice number you want to view: '))
invoice = invoices[position]

link = invoice.find_element_by_xpath('.//td[@class="2avia"]/a[@href]').click()

extravio = link.find_elements_by_xpath('//tr[@class="neotd"]/td/input[@value="Extravio"]')
extravio.click()
