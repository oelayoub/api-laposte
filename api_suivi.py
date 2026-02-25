import requests 
import pandas as pd
import time

headers = {
"X-Okapi-Key" : "", #TOKEN
"accept" : "application/json" # accepte format json 
}

all_data = [] #créer une liste vite ou on va stocker le dictionnaire de chaque boucle 
df = pd.read_csv("Suivi_livraison_V3.csv", sep=";")
tracking_number = df["COLIS_TRANSPORTEUR"].tolist() #récupérer toutes les lignes de la première colonne sous forme de liste 

#tracking_number = [
#    "4M00533946516",
#    "XX062633073JB"
#]

for tracking in tracking_number: # créer la boucle 
    url = f"https://api.laposte.fr/suivi/v2/idships/{tracking}?lang=fr_FR" # reconstruire l'url pour chaque ligne 
    response = requests.get(url, headers = headers) 
    if response.status_code != 200:
        print(f"Erreur de {tracking}")
        continue
    data = response.json() #transformer en json 
    id_ship = data["shipment"]["idShip"] #affecter l'idship du json à une variable
    event = data["shipment"]["event"] #affecter la liste event à une variable 
    last_event = event[0] # récupérer le premier éveénement de la liste
    all_data.append({ #pour chaque ligne stocker les éléments sous forme de dictionnaire
        "Id_ship" : id_ship,
        "Code" : last_event["code"],
        "Statut" : last_event["label"],
        "Date" : last_event["date"]
        })
    #print("id :", id_ship)
    #print("Code : ", last_event["code"])
    #print("Statut :", last_event["label"])
    #print("Date : ", last_event["date"])
    #print()   
    time.sleep(0.05)

final_df = pd.DataFrame(all_data) # tranforme les dictionnaire en dataframe
final_df.to_csv("Livraison_V3.csv", index=False) # export vers un csv 
print("All Done! ")