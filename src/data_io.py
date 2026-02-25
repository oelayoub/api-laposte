import pandas as pd 

def read_file(file_path): 
    df = pd.read_csv(file_path, sep=";")
    return df["tracking_numbers"].tolist()

def export_file(data):
    final_data = pd.DataFrame(data)
    final_data.to_csv("final data2502.csv", index=False)


