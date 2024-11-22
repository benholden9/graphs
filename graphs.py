import plotly.express as px
import pandas as pd

# Data
data = {
    "Product": ["A", "B", "C", "D"],
    "Direct Sales": [83, 54, 89, 90],
    "Indirect Sales": [145, 131, 122, 129],
    "Total Sales": [128, 127, 107, 118]
}
df = pd.DataFrame(data)

# Reshape the data for Plotly
df_melted = pd.melt(df, id_vars=["Product"], var_name="Sales Type", value_name="Average Time")

# Create the plot
fig = px.bar(
    df_melted,
    x="Product",
    y="Average Time",
    color="Sales Type",
    barmode="group",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    title="Average Time to Close Deals by Product and Sales Type"
)

# Customize layout
fig.update_layout(
    xaxis_title="Product",
    yaxis_title="Average Time (days)",
    title_font=dict(size=18, family="Arial", color="black"),
    legend_title="Sales Type",
    legend=dict(font=dict(size=12)),
    bargap=0.2,  # Adjust spacing between bars in each group
)

# Add annotations
for data in fig.data:
    for x, y in zip(data["x"], data["y"]):
        fig.add_annotation(
            x=x,
            y=y + 5,  # Position the annotation slightly above the bar
            text=str(y),
            showarrow=False,
            font=dict(size=12, color="black"),
        )

# Show plot
fig.show()

