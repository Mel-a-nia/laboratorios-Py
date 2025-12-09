from src.lab05.json_csv import json_to_csv, csv_to_json

json_to_csv("prueba.json", "prueba.csv")
csv_to_json("prueba.csv", "prueba2.json")

print("Conversión completada")
