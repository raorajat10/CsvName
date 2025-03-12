import pandas as pd

def process_query(df, user_query):
    """Processes user queries related to CSV data."""
    try:
        query_parts = user_query.lower().split()
        
        if "average" in query_parts:
            column = query_parts[-1]
            if column in df.select_dtypes(include=['number']).columns:
                return f"Average {column}: {df[column].mean()}"
        elif "max" in query_parts:
            column = query_parts[-1]
            if column in df.select_dtypes(include=['number']).columns:
                return f"Max {column}: {df[column].max()}"
        elif "min" in query_parts:
            column = query_parts[-1]
            if column in df.select_dtypes(include=['number']).columns:
                return f"Min {column}: {df[column].min()}"
        elif "sum" in query_parts:
            column = query_parts[-1]
            if column in df.select_dtypes(include=['number']).columns:
                return f"Sum {column}: {df[column].sum()}"
        elif "count" in query_parts:
            column = query_parts[-1]
            return f"Count of {column}: {df[column].count()}"

        return "Query type not supported."
    except Exception as e:
        return f"Error processing query: {str(e)}"
