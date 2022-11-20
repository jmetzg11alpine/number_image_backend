from deta import Deta
import pandas as pd


deta = Deta('a0499p4s_aP4D8LBstFNj8tujRmuz6vGdVMYfBRB5')
numbers_db = deta.Base('numbers')


res = numbers_db.fetch()
data = res.items 

while res.last:
    res = numbers_db.fetch(last=res.last)
    data += res.items


X= []
y = []
for d in data:
    X.append(d['data'])
    y.append(d['number'])

training_data = pd.DataFrame(data={'y': y, 'X': X})

training_data.to_csv('training_data.csv', index=False)
