import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from backend.data_loader import load_titanic_data

df = load_titanic_data()

def generate_visualization(chart_type, column_name):
    """Generates visualization dynamically based on user request."""
    plt.figure(figsize=(8, 5))

    if chart_type == "histogram":
        sns.histplot(df[column_name].dropna(), bins=30, kde=True)
        plt.title(f"Histogram of {column_name}")

    elif chart_type == "bar":
        df[column_name].value_counts().plot(kind="bar", color="skyblue")
        plt.title(f"Bar Chart of {column_name}")

    elif chart_type == "pie":
        df[column_name].value_counts().plot(kind="pie", autopct='%1.1f%%')
        plt.title(f"Pie Chart of {column_name}")

    elif chart_type == "scatter":
        sns.scatterplot(x=df[column_name], y=df["Age"], hue=df["Survived"])
        plt.title(f"Scatter Plot: {column_name} vs Age")

    image_path = f"data/{chart_type}_{column_name}.png"
    plt.savefig(image_path)
    return image_path
