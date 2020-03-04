import pandas as pd

ecom = pd.read_csv('Ecommerce Purchases')
# print(ecom.head())
# print(ecom['Purchase Price'].mean())
# print(ecom['Purchase Price'].max())
# print(ecom['Purchase Price'].min())

# print(ecom[ecom['Language'] == 'en']['Language'].count())

# print(ecom[ecom['Job'] == 'Lawyer'])


# print(ecom[(ecom['CC Provider'] == 'American Express')
#            & (ecom['Purchase Price'] > 95)])
print(ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25'))
