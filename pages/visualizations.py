import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)
blue = '#51C4D3' # To mark drinkable water
green = '#74C365' # To mark undrinkable water
red = '#CD6155' # For further markings
orange = '#DC7633' # For further markings
st.set_page_config(page_title="Water Potability Visualization Dashboard", 
                   page_icon=":bar_chart:", 
                   layout="wide")
st.title("Water Potability Visualization Dashboard:bar_chart:")
df =  df = pd.read_csv('water_potability.csv')

st.sidebar.header("Select filter")
potability = st.sidebar.multiselect(
    "Select Water Type:",
    options=df["Potability"].unique(),
    default=df["Potability"].unique()
)
df_selection = df.query(
    "Potability == @potability"
)
st.markdown("##")
#top bar '
total_number_of_rows = int(len(df_selection))
number_of_rows_clean = int(len(df_selection[df_selection["Potability"]== 0 ]))
number_of_rows_dirty = int(len(df_selection[df_selection["Potability"]== 1]))
number_of_null = df_selection.isna().sum().sum()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total rows:")
    st.subheader(f"{total_number_of_rows:,}")
with middle_column:
    st.subheader("clean water:")
    st.subheader(f"{number_of_rows_clean} ")
with right_column:
    st.subheader("null values:")
    st.subheader(f" {number_of_null}")
st.markdown("##")
# SALES BY PRODUCT LINE [BAR CHART]

st.markdown("***")
top_row1, top_row2 = st.columns(2)
group_by_portability = (
    df_selection.groupby(by=["Potability"]).sum()
)
fig_potability = px.bar(
    group_by_portability,
    x="ph",
    y=group_by_portability.index,
    orientation="h",
    title="<b>Water type barchart</b>",
    color_discrete_sequence=["#0083B8"] * len(group_by_portability),
    template="plotly_white",
)
fig_potability.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

plt.clf()
plt.style.use('ggplot')

# Create subplot and pie chart
plt.clf()
plt.style.use('ggplot')

# Create subplot and pie chart
fig1, ax1 = plt.subplots()
ax1.pie(df['Potability'].value_counts(),labels=['Not drinkable', 'Drinkable'], autopct='%1.1f%%', startangle=0, rotatelabels=False)

centre_circle = plt.Circle((0,0),0.80, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')  


top_row1.pyplot(fig1)
#st.dataframe(df_selection.head(111))
#st.dataframe(df_selection.describe())
def mask_plotter(column, mask1, mask2, label1, label2, color2, title):
    # Set size and stlye
    plt.figure(figsize=(5, 5))
    plt.style.use('ggplot')

    # Create to histplots
    sns.histplot(data=df_selection[mask1], x=column, multiple='stack', color=blue, label=label1) # Save
    sns.histplot(data=df_selection[mask2], x=column, multiple='stack', color=color2, label=label2)

    # Add title, legend and show plot
    plt.title(title)
    plt.legend()
    plt.show()
red = '#CD6155'
soft_mask = (df['Hardness'] < 150)
hard_mask = (df['Hardness'] > 150) 

top_row2.pyplot(mask_plotter('Hardness', soft_mask, hard_mask, 'Soft - moderate water', 'Hard water', red, 'Hardness'))
second_row1, second_row2 = st.columns(2)
drinkable_ph_mask = (df['ph'] > 6.5) & (df['ph'] < 9)
undrinkable_ph_mask = (df['ph'] < 6.5) | (df['ph'] > 9)
second_row1.pyplot(mask_plotter('ph', drinkable_ph_mask, undrinkable_ph_mask, 'Safe ph value', 'Unsafe ph-value', red, 'ph-values'))

  # Equal aspect ratio ensures that pie is drawn as a circle.

# Plot Sulfate
who_recommendation = (df['Sulfate'] > 250) & (df['Sulfate'] < 500)
not_recommended= (df['Sulfate'] < 250)
second_row2.pyplot(mask_plotter('Sulfate',who_recommendation,not_recommended ,'Within WHO limits', 'Outside WHO limits',orange, 'Sulfate'))