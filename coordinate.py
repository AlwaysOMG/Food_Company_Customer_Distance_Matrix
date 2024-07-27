# pip install pandas
# pip install openpyxl
# pip install googlemaps
import pandas as pd
import googlemaps

# API setting
API_KEY = None
gmaps = googlemaps.Client(key=API_KEY)

# load the data
DATA_PATH = './data/2月9日(上午)送貨單.xlsx'
df = pd.read_excel(DATA_PATH, usecols=['市', '區', '地址'], dtype=str)
df['address'] = df['市'] + df['區'] + df['地址']
small_df = df.iloc[:, 3]

# output the info of latitude and longitude
coordinate = []
for i in range(len(small_df)):
    # remove the contents after left parentheses
    index = small_df.iloc[i].find('(')
    if index != -1:
        small_df.iloc[i] = small_df.iloc[i][:index]
    # find the latitude and longitude with Geocoding API
    geocode_result = gmaps.geocode(small_df.iloc[i])
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lng = geocode_result[0]["geometry"]["location"]["lng"]
    coordinate.append([lat, lng])

coordinate['address'] = df['address']
output = pd.DataFrame(coordinate, columns =['latitude', 'longitude', 'address'])
output.to_csv('./data/info2.csv')