import streamlit as st
import math as math
import pandas as pd
import plotly.express as px
import requests
import json

#...app header and subheader......
st.write('''
# App to Calculate Vehicle Import Duty in Kenya
##### This web app uses calculation stipulated by [Kenya Revenue Authority](https://www.kra.go.ke/news-center/blog/1075-what-you-need-to-know-when-importing-a-motor-vehicle) on import of motor vehicle.
* ##### The app assumes that the vehicle has met the Kenya Bureau of Standards KS 1515:2000 – Code of Practice for Inspection of Road Vehicles before clearance.
* ##### The app uses real time exchange rates from [Exchange Rates API](https://exchangeratesapi.io/)
* ##### Also note, other charges like port charges and registration fee(NTSA) are not captured. Hence, calculations generated from the app can only be used as a guidleine but not as the exact costs of importing the vehicle
''')
('---')

#....sidebar and required calculations....
st.sidebar.header('Enter Details')
CIF_USD = st.sidebar.number_input ('Enter CIF in USD', value=0)
car = st.sidebar.number_input('Engine size in cc', value=0)

#..extracting exchange rate data from exchange rate api
url = 'https://v6.exchangerate-api.com/v6/25b9f38de08d7fedd64385d2/latest/USD'
response = requests.get(url)
data = response.json()

#..filtering data to get only KES row
st.write('USD to KES Conversion Rate')
df2 = pd.DataFrame(response.json())
df2 = df2.iloc[71:72 ,4:]
df2.drop('time_next_update_unix', axis=1,inplace=True)
df2['conversion_rates'] = df2['conversion_rates'].astype('float')
df2
('---')

#...converting USD to KES
CIF_KES = math.trunc(df2.iloc[0,3]) * CIF_USD

st.sidebar.write('CIF in KES:  ' + f'{CIF_KES:,}')


#...import duty @ 25%
import_duty = math.trunc(CIF_KES * 0.25)
st.sidebar.write('Import Duty :    ' + f'{import_duty:,}')

#...CIF + import duty
CIF_import = CIF_KES + import_duty

#..excise duty.....math.trunc is to drop decimal places
def excise_duty():
    if car <= 1500:
        excise_duty = math.trunc(CIF_import * 0.20)
    elif car > 1500:
        excise_duty = math.trunc(CIF_import * 0.25)
    return excise_duty
#excise_duty()
st.sidebar.write('Excise Duty :    ' + f'{excise_duty():,}')

#..CIF + import duty + excise duty
CIF_imex = CIF_KES + import_duty + excise_duty()

#...VAT @ 16%
vat = math.trunc(CIF_imex * 0.16)
st.sidebar.write('VAT  :     ' + f'{vat:,}')

#..IDF Payable
idf = math.trunc(CIF_KES * 0.035)
st.sidebar.write('IDF Payable  :   ' + f'{idf:,}')

#....Railway Levy
rail = math.trunc(CIF_KES * 0.02)
#rail = format(rail, ',d')
st.sidebar.write('Railway Levy  :  ' + f'{rail:,}')

#...Duties payable
duties = math.trunc(excise_duty() + import_duty + vat + idf + rail)
#duties = format(duties, ',d')
st.sidebar.write('Duties Payable  : ' + f'{duties:,}')

#....Duties + CIF
CIF_duties = CIF_KES + duties
st.sidebar.write('CIF+Duties  :  ' + f'{CIF_duties:,}')
#...display number without thousand comma f'{CIF_duties}'
#...display number with thousand comma f'{CIF_duties:,}'


#..creating pandas dataframe and plotting horizontal bar chart
#...creating pandas dataframe
df = pd.DataFrame({'Values': ['Duties Payable', 'CIF in KES','CIF+Duties'],
                   'Amount': [f'{duties:,}',f'{CIF_KES:,}',f'{CIF_duties:,}']})

#...plotting horizontal bar chart
fig = px.bar(df, x='Amount', y='Values', orientation='h', title='Chart Comparing Total Amount vs CIF and Duties Payable')
fig.update_layout(font_family='Times New Roman')
fig
('---')

st.write('''
Built with :heart: by Dennis Mutua
''')

