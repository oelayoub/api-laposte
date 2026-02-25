from data_io import read_file 
from data_io import export_file
from config import get_headers
from api_laposte import api_tracking
import pandas as pd
import time
import logging

logging.basicConfig(
    level= logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

tracking_numbers = read_file("test.csv")
logging.info(f"{len(tracking_numbers)} tracking numbers loaded")
headers = get_headers()
data = []
for tracking in tracking_numbers:
    api_call = api_tracking(tracking, headers=headers)
    if api_call is None:
        continue
    data.append(api_call)
    
    time.sleep(0.05)

export_file(data)
logging.info("Export completed successfuly")
#final_data = pd.DataFrame(data)
#final_data.to_csv("final data.csv", index=False)


