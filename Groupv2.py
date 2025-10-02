import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint

col_names1=["Osservazione", "Ristorante", "Prezzo", "Cibo", "Decoro", "Servizio", "East", "Latitudine", "Longitudine", "Tipo"]
data=pd.read_csv("NYC_resturants_clean.csv", names=col_names1, on_bad_lines="skip", sep=";")
data["Latitudine"]= data["Latitudine"].str.replace(',', '.').astype(float)
data["Longitudine"]= data["Longitudine"].str.replace(',', '.').astype(float)
data["Prezzo"]= data["Prezzo"].astype(float)
data["Cibo"]=data["Cibo"].astype(float)
data["Decoro"]=data["Decoro"].astype(float)
data["Servizio"]=data["Servizio"].astype(float)

for i in range(len(data["Prezzo"])):
    data.loc[i, "Prezzo"]=((data.loc[i, "Prezzo"]-min(data["Prezzo"]))/(max(data["Prezzo"])-min(data["Prezzo"])))
    data.loc[i, "Cibo"]=((data.loc[i, "Cibo"]-min(data["Cibo"]))/(max(data["Cibo"])-min(data["Cibo"])))
    data.loc[i, "Decoro"]=((data.loc[i, "Decoro"]-min(data["Decoro"]))/(max(data["Decoro"])-min(data["Decoro"])))
    data.loc[i, "Servizio"]=((data.loc[i, "Servizio"]-min(data["Servizio"]))/(max(data["Servizio"])-min(data["Servizio"])))
    
center_lat = data["Latitudine"].mean()
center_lng = data["Longitudine"].mean()
center_lat_east = data.loc[data["East"]==1, "Latitudine"].mean()
center_lng_east = data.loc[data["East"]==1, "Longitudine"].mean()
center_lat_rest = data.loc[data["Tipo"]==("Pizzeria" or "Resturant"), "Latitudine"].mean()
center_lng_rest = data.loc[data["Tipo"]==("Pizzeria" or "Resturant"), "Longitudine"].mean()
center_lat_takeaway = data.loc[data["Tipo"]==("Street Food" or "Panini"), "Latitudine"].mean()
center_lng_takeaway = data.loc[data["Tipo"]==("Street Food" or "Panini"), "Longitudine"].mean()
weighted_center_lat_price = 0
weighted_center_lng_price = 0
weighted_center_lat_food = 0
weighted_center_lng_food = 0
weighted_center_lat_decoration = 0
weighted_center_lng_decoration = 0
weighted_center_lat_service = 0
weighted_center_lng_service = 0
sum_weights_price = sum(data["Prezzo"])
sum_weights_food = sum(data["Cibo"])
sum_weights_decoration = sum(data["Decoro"])
sum_weights_service = sum(data["Servizio"])

for i in range(len(data["Prezzo"])):
    weighted_center_lat_price = (data.loc[i, "Latitudine"]*data.loc[i, "Prezzo"])+weighted_center_lat_price
    weighted_center_lng_price = (data.loc[i, "Longitudine"]*data.loc[i, "Prezzo"])+weighted_center_lng_price
    weighted_center_lat_food = (data.loc[i, "Latitudine"]*data.loc[i, "Cibo"])+weighted_center_lat_food
    weighted_center_lng_food = (data.loc[i, "Longitudine"]*data.loc[i, "Cibo"])+weighted_center_lng_food
    weighted_center_lat_decoration = (data.loc[i, "Latitudine"]*data.loc[i, "Decoro"])+weighted_center_lat_decoration
    weighted_center_lng_decoration = (data.loc[i, "Longitudine"]*data.loc[i, "Decoro"])+weighted_center_lng_decoration
    weighted_center_lat_service = (data.loc[i, "Latitudine"]*data.loc[i, "Servizio"])+weighted_center_lat_service
    weighted_center_lng_service = (data.loc[i, "Longitudine"]*data.loc[i, "Servizio"])+weighted_center_lng_service

weighted_center_lat_price = weighted_center_lat_price/sum_weights_price
weighted_center_lng_price = weighted_center_lng_price/sum_weights_price
weighted_center_lat_food = weighted_center_lat_food/sum_weights_food
weighted_center_lng_food = weighted_center_lng_food/sum_weights_food
weighted_center_lat_decoration = weighted_center_lat_decoration/sum_weights_decoration
weighted_center_lng_decoration = weighted_center_lng_decoration/sum_weights_decoration
weighted_center_lat_service = weighted_center_lat_service/sum_weights_service
weighted_center_lng_service = weighted_center_lng_service/sum_weights_service

plt.figure(figsize=(8, 8))
plt.scatter(data["Longitudine"], data["Latitudine"], c='blue', label='Points')
plt.scatter(center_lng, center_lat, c='red', marker='X', s=100, label='Center')
plt.scatter(center_lng_east, center_lat_east, c='green', marker='X', s=100, label='Center east')
plt.scatter(center_lng_rest, center_lat_rest, c='purple', marker='X', s=100, label='Center of resturants')
plt.scatter(center_lng_takeaway, center_lat_takeaway, c='brown', marker='X', s=100, label='Center of takeaways')
plt.scatter(weighted_center_lng_price, weighted_center_lat_price, c='orange', marker='*', s=100, label='Center of weighted price')
plt.scatter(weighted_center_lng_food, weighted_center_lat_food, c='purple', marker='*', s=100, label='Center of weighted food')
plt.scatter(weighted_center_lng_decoration, weighted_center_lat_decoration, c='green', marker='*', s=100, label='Center of weighted decoration')
plt.scatter(weighted_center_lng_service, weighted_center_lat_service, c='gray', marker='*', s=100, label='Center of weighted service')
plt.title('Scatter Plot of Coordinates')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.grid(False)
plt.show()
