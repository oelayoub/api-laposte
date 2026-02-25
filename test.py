response = {
    "status": "success",
    "data": [
        {"tracking": "AB123", "status": "DELIVERED", "timestamp": "2026-02-14T10:32:00"},
        {"tracking": "CD456", "status": "IN_TRANSIT", "timestamp": "2026-02-14T08:15:00"},
        {"tracking": "EF789", "status": "DELIVERED", "timestamp": "2026-02-13T18:05:00"}
    ]
}

def get_delivered_tracking(response: dict) -> list: # -> list veut dire transfomer en liste
    delivered = []

    if response.get("status") != "success":
        return delivered

    for item in response.get("data", []): # si data existe on récupère sa valeur, sinon on récupère une liste vide []
        if item.get("status") == "DELIVERED":
            delivered.append(item.get("tracking"))

    return delivered

result = get_delivered_tracking(response)
print(result)
