import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint

col_names1=["Osservazione", "Ristorante", "Prezzo", "Cibo", "Decoro", "Servizio", "East", "Latitudine", "Longitudine", "Tipo"]
data=pd.read_csv("NYC_resturants_clean.csv", names=col_names1, on_bad_lines="skip", sep=";")
data["Latitudine"]= data["Latitudine"].str.replace(',', '.').astype(float)
data["Longitudine"]= data["Longitudine"].str.replace(',', '.').astype(float)

for i in range(len(data["Prezzo"])):
    data["Prezzo"][i]=((data["Prezzo"][i]-min(data["Prezzo"]))/(max(data["Prezzo"])-min(data["Prezzo"])))
    data["Cibo"][i]=((data["Cibo"][i]-min(data["Cibo"]))/(max(data["Cibo"])-min(data["Cibo"])))
    data["Decoro"][i]=((data["Decoro"][i]-min(data["Decoro"]))/(max(data["Decoro"])-min(data["Decoro"])))
    data["Servizio"][i]=((data["Servizio"][i]-min(data["Servizio"]))/(max(data["Servizio"])-min(data["Servizio"])))
    
center_lat = data["Latitudine"].mean()
center_lng = data["Longitudine"].mean()
center_lat_east = data.loc[data["East"]==1, "Latitudine"].mean()
center_lng_east = data.loc[data["East"]==1, "Longitudine"].mean()
center_lat_rest = data.loc[data["Tipo"]==("Pizzeria" or "Resturant"), "Latitudine"].mean()
center_lng_rest = data.loc[data["Tipo"]==("Pizzeria" or "Resturant"), "Longitudine"].mean()
center_lat_takeaway = data.loc[data["Tipo"]==("Street Food" or "Panini"), "Latitudine"].mean()
center_lng_takeaway = data.loc[data["Tipo"]==("Street Food" or "Panini"), "Longitudine"].mean()

plt.figure(figsize=(8, 8))
plt.scatter(data["Longitudine"], data["Latitudine"], c='blue', label='Points')
plt.scatter(center_lng, center_lat, c='red', marker='X', s=100, label='Center')
plt.scatter(center_lng_east, center_lat_east, c='green', marker='X', s=100, label='Center east')
plt.scatter(center_lng_rest, center_lat_rest, c='purple', marker='X', s=100, label='Center of resturants')
plt.scatter(center_lng_takeaway, center_lat_takeaway, c='brown', marker='X', s=100, label='Center of takeaways')
plt.title('Scatter Plot of Coordinates')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.grid(False)
plt.show()