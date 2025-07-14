import pandas as pd
import os

def read_csv_to_dict(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None

    # Read CSV using pandas
    df = pd.read_csv(file_path)

    # Convert DataFrame to list of dictionaries (one dict per row)
    data_dict = df.to_dict(orient='records')

    return data_dict

if __name__ == "__main__":
    csv_file = r'C:\Users\ANGAD\Downloads\k.csv'  # Put your CSV path here

    data = read_csv_to_dict(csv_file)
    if data:
        for row in data:
            print(row)
