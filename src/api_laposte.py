import requests 
from config import BASE_URL
from config import LANG
import logging


def api_tracking(tracking_number, headers):

    final_url = BASE_URL + tracking_number + "?lang=" + LANG

    response = requests.get(final_url, headers=headers)
    if response.status_code != 200:
        logging.warning(f"Tracking {tracking_number} failed with status {response.status_code}")
        return None
    
    response_json = response.json()

    delivery_id = response_json["shipment"]["idShip"]
    status = response_json["shipment"]["event"]
    last_status = status[0]
    code_delivery = last_status["code"]
    delivery_date = last_status["date"]
    delivery_label = last_status["label"]

    return {
        "Tracking_number" : delivery_id,
        "Code_Delivery" : code_delivery,
        "Date" : delivery_date,
        "Statut" : delivery_label
    }


