import requests
import csv

address = "http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=13"

response = requests.get(address)

if response.ok:
    print("Request successful")
else:
    print("Request failed")

print(response.text)
data = response.text.split("\n")

with open("C:/Koulu/Tvt22spl_syksy2023_projekti/python/data_from_http.csv", "w") as file:
    writer = csv.writer(file, lineterminator='\n')
    for line in data:
        line = line.replace(";", ",")
        values = line.split(",")
        writer.writerow(values)
    