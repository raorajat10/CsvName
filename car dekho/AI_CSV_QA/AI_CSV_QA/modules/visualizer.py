import matplotlib.pyplot as plt

def generate_plot(df, column_x, column_y, plot_type="line"):
    """Generates a graph based on the specified columns and plot type."""
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

        return fig  # Return the figure to be displayed in Gradio
    except Exception as e:
        return f"Error generating plot: {str(e)}"
