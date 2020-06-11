import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#Scraping the data from tcmb.gov.tr
url = "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Para+Politikasi/Merkez+Bankasi+Faiz+Oranlari/1+Hafta+Repo"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'lxml')
table = soup.find_all('table')[0]

#Creating DataFrame
df_tcmb = pd.read_html(str(table))[0]
df_tcmb.columns = df_tcmb.iloc[0] #set first row as columns name
df_tcmb = df_tcmb[1:] #drop first row
df_tcmb=df_tcmb.reset_index(drop=True) #reset index
df_tcmb['Tarih']= pd.to_datetime(df_tcmb['Tarih']) #Set column type
df_tcmb['Borç Verme']= df_tcmb['Borç Verme'].astype('float64')  #Set column type
df_tcmb.head()
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#Scraping the data from tcmb.gov.tr
url = "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Temel+Faaliyetler/Para+Politikasi/Merkez+Bankasi+Faiz+Oranlari/1+Hafta+Repo"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'lxml')
table = soup.find_all('table')[0]

#Creating DataFrame
df_tcmb = pd.read_html(str(table))[0]
df_tcmb.columns = df_tcmb.iloc[0] #set first row as columns name
df_tcmb = df_tcmb[1:] #drop first row
df_tcmb=df_tcmb.reset_index(drop=True) #reset index
df_tcmb['Tarih']= pd.to_datetime(df_tcmb['Tarih']) #Set column type
df_tcmb['Borç Verme']= df_tcmb['Borç Verme'].astype('float64')  #Set column type
df_tcmb.head()
