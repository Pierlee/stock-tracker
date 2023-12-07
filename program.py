import pyodbc 
import requests
import time
cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for PostgreSQL};Server=localhost;Port=5432;Database=StockMonitor;User ID=postgres;Password=admin;String Types=Unicode')
cursor = cnxn.cursor()
while True:
  rows = cursor.execute("SELECT stockname FROM public.TrackedStocks;")
  rows = rows.fetchall()
  if rows is None: 
    time.sleep(5*60)
    continue
  symbols = []
  for row in rows:
      # words.append(row['unites_lexicales'])
      symbols.append(row[0])
  print(symbols)

  url = f'https://api.hgbrasil.com/finance/stock_price?key=5348bce0&symbol={",".join(symbols)}'
  print (url)
  result = requests.get(url)
  print(result.text)
  time.sleep(5*60)
# cursor.execute("INSERT INTO public.trackedstocks(stockname, creationdate, minvalue, maxvalue) VALUES ('petr1', CURRENT_TIMESTAMP, 10, 20);")