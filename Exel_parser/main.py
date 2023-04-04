import re
import pandas as pd

exel_data = pd.read_excel('asmetal.xlsx')
data = pd.DataFrame(exel_data, columns=['Անվանում'])
ptern = r'(?:\d{2}\w{2}\d+)'      #r'/s[0-9]+[A-Z]+[a-z]*/sAS/M'
new_data = pd.DataFrame({'Կոդ':[]})
codes = []
for i in data['Անվանում']:
    if re.findall(ptern, i):
        codes.append((re.findall(ptern, i)))
    else:
        codes.append(None)
for i in codes:
    if i == None:
        continue
    else:
        print(''.join(i[0]))