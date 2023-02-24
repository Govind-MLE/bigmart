import requests
url='http://localhost:8080/request'
r=requests.post(url,json={'Item_Weight':23.6,'Item_MRP':453.5,'Outlet_Location_Type':1})
print(r.json())