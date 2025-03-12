import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from modules.file_handler import load_csv
from modules.query_processor import process_query
from modules.visualizer import generate_plot

def load_csv(csv_file):
    try:
        df = pd.read_csv(csv_file.name)
        return df
    except Exception as e:
        return f"Error loading CSV: {str(e)}"

def process_query(df, user_query):
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

def generate_plot(df, column_x, column_y, plot_type="line"):
    try:
        if column_x not in df.columns or column_y not in df.columns:
            return "Invalid column names."
        
        fig, ax = plt.subplots()
        if plot_type == "line":
            ax.plot(df[column_x], df[column_y], marker='o', linestyle='-')
        elif plot_type == "bar":
            ax.bar(df[column_x], df[column_y])
        elif plot_type == "scatter":
            ax.scatter(df[column_x], df[column_y])
        
        ax.set_xlabel(column_x)
        ax.set_ylabel(column_y)
        ax.set_title(f"{plot_type.capitalize()} Plot of {column_y} vs {column_x}")
        return fig
    except Exception as e:
        return f"Error generating plot: {str(e)}"

def handle_query(csv_file, user_query):
    if csv_file is None:
        return "Please upload a CSV file."
    
    df = load_csv(csv_file)
    if isinstance(df, str):
        return df  # Return error message
    
    response = process_query(df, user_query)
    return response

def handle_plot(csv_file, column_x, column_y, plot_type):
    if csv_file is None:
        return "Please upload a CSV file.", None
    
    df = load_csv(csv_file)
    if isinstance(df, str):
        return df, None  # Return error message
    
    fig = generate_plot(df, column_x, column_y, plot_type)
    return "Graph Generated Successfully!", fig

with gr.Blocks() as app:
    gr.Markdown("# CSV Question Answering and Visualization App")
    csv_file = gr.File(label="Upload CSV File")
    
    with gr.Row():
        user_query = gr.Textbox(label="Ask a question about the CSV data")
        query_output = gr.Textbox(label="Answer", interactive=False)
        gr.Button("Submit").click(handle_query, inputs=[csv_file, user_query], outputs=query_output)
    
    with gr.Row():
        column_x = gr.Textbox(label="X-axis Column")
        column_y = gr.Textbox(label="Y-axis Column")
        plot_type = gr.Dropdown(choices=["line", "bar", "scatter"], label="Select Plot Type", value="line")
        plot_output = gr.Plot()
        gr.Button("Generate Graph").click(handle_plot, inputs=[csv_file, column_x, column_y, plot_type], outputs=[query_output, plot_output])

app.launch(share=True)

