import pandas as pd

def load_csv(csv_file):
    """Loads a CSV file into a Pandas DataFrame."""
    try:
        df = pd.read_csv(csv_file.name)
        return df
    except Exception as e:
        return f"Error loading CSV: {str(e)}"
