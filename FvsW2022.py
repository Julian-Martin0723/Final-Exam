import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
table_data = {
    'Metrics': ['Games Played', 'Passing Attempts', 'Completions', 
                'Passing Yards', 'First Down Passes', 'Rushing Yards', 'Touchdowns'],
    'Wilson Totals': [15, 447, 297, 3070, 135, 341, 3],
    'Fields Totals': [13, 370, 227, 2562, 121, 657, 4],
    'Leader': ['Wilson', 'Wilson', 'Wilson', 'Wilson', 'Wilson', 'Fields', 'Fields'],
}

# Convert to DataFrame
df = pd.DataFrame(table_data)

# Streamlit App
st.title("Russell Wilson vs. Justin Fields 2022 Statistics")

# Display Table
st.subheader("Career 2022 Table")
st.table(df)

# Bar Chart
st.subheader("Bar Chart of 2022 Statistics")

# Data for plotting
metrics = df['Metrics']
wilson_totals = df['Wilson Totals']
fields_totals = df['Fields Totals']

# Bar chart settings
x = np.arange(len(metrics))  # Position of groups on x-axis
width = 0.35  # Width of each bar

# Create plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars
bar1 = ax.bar(x - width / 2, wilson_totals, width, label='Wilson Totals', color='blue')
bar2 = ax.bar(x + width / 2, fields_totals, width, label='Fields Totals', color='orange')

# Add labels to bars
def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

add_labels(ax, bar1)
add_labels(ax, bar2)

# Add labels, title, and legend
ax.set_xlabel('Metrics', fontsize=12)
ax.set_ylabel('Values', fontsize=12)
ax.set_title('Comparison of Career Statistics', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(metrics, rotation=45, ha='right', fontsize=10)
ax.legend()

# Display plot
st.pyplot(fig)