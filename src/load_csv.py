# CSV Data Loader
import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)
    return df

def parse_csv(csv, name):
    if name == "summary":
        return parse_summary(csv)
    else :
        return parse_metadata(csv)
    
def parse_summary(csv):
    # Parse into the summary class model
    return csv

def parse_metadata(csv):
    # Parse into the metadata class model
    return csv