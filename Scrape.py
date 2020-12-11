import requests
from bs4 import BeautifulSoup
import pandas as pd

input = pd.read_csv('search_results.csv')
df = pd.DataFrame(columns=['Parcel Number',
                           'Name',
                           'Address',
                           'Sale Date',
                           'Sale Price',
                           "Year Built",
                           "Total Rooms",
                           "# Bedrooms",
                           "# Full Bathrooms",
                           "# Half Bathrooms",
                           "Last Sale Date",
                           "Last Sale Amount",
                           "Conveyance Number",
                           "Deed Type",
                           "Deed Number",
                           "# of Parcels Sold",
                           "Acreage",
                           "Board of Revision",
                           "Rental Registration",
                           "Homestead",
                           "Owner Occupancy Credit",
                           "Foreclosure",
                           "Special Assessments",
                           "Market Land Value",
                           "CAUV Value",
                           "Market Improvement Value",
                           "Market Total Value",
                           "TIF Value",
                           "Abated Value",
                           "Exempt Value",
                           "Taxes Paid",
                           "Tax as % of Total Value"])
entry = 0
for index, row in input.iterrows():
    row_list = []
    row_list.append(row['Parcel Number'])
    row_list.append(row['Name'])
    row_list.append(row['Address'])
    row_list.append(row['Sale Date'])
    row_list.append(row['Sale Price'])


    #URL = 'https://wedge1.hcauditor.org/view/re/5920001000100/2019/summary'
    URL = f'https://wedge1.hcauditor.org/view/re/{row["Parcel Number"].replace("-","")}/2019/summary'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())
    results = soup.find_all('table', class_="datagrid ui-widget summary")
    x = 0


    for result in results:
        rows = result.find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            for cell in cells:
                x += 1
                # print(x)
                if x % 2 == 0:
                    row_list.append(cell.text)
    df.loc[entry] = row_list
    entry += 1
    print(entry)
    x = 1
df.to_csv('result.csv')

