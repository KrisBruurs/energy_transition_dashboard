import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import os

# Load in data
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "final_df.parquet")
df = pd.read_parquet(data_path)

st.title("Global Energy Transition Dashboard")
st.write("This dashboard provides insights into the global energy transition, including trends in renewable energy adoption, carbon emissions, and energy consumption patterns.")

# Table 1: lIne plot
st.markdown("### Table 1: Exploring Global Energy Transition Trends")

# Sidebars line plot
st.sidebar.markdown("## Select Metrics for Line Plot")
st.sidebar.markdown("*Note: Some metrics may not be available for all countries.*")
metric_choice = st.sidebar.selectbox(
    "Select metric to explore", 
    ["CO2 Emissions vs Renewable Energy",
    "Economic Growth vs Emissions",
    "Energy Mix Transition"])
selected_country = st.sidebar.selectbox("Select country", 
                                        df["country"].unique(),
                                        key="main_country")

df_country = df[df["country"] == selected_country].sort_values("year")

if metric_choice == "CO2 Emissions vs Renewable Energy":
    fig, ax1 = plt.subplots()

    ax1.plot(df_country["year"], df_country["co2"], color="red", label="CO2")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("CO2 Emissions")
    ax1.set_title(f"CO2 Emissions and Renewable Energy Share in {selected_country}")

    ax2 = ax1.twinx()
    ax2.plot(df_country["year"], df_country["renewables_share_energy"], color="green", label="Renewable Shares")
    ax2.set_ylabel("Renewable Share %")

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")


    st.pyplot(fig)

elif metric_choice == "Economic Growth vs Emissions":
    fig, ax1 = plt.subplots()

    ax1.plot(df_country["year"], df_country["gdp_per_capita"], color="blue", label="GDP per Capita")
    ax1.plot(df_country["year"], df_country["energy_per_capita"], color="green", label="Energy per Capita")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Economic and Energy Metrics")
    ax1.set_title(f"Economic Growth and Energy Consumption in {selected_country}")
    
    ax2 = ax1.twinx()
    ax2.plot(df_country["year"], df_country["co2_per_capita"], color="red", label="CO2 per Capita")
    ax2.set_ylabel("CO2 per Capita")

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()   
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

    st.pyplot(fig)

elif metric_choice == "Energy Mix Transition":
    fig, ax1 = plt.subplots()

    ax1.plot(df_country["year"], df_country["fossil_share_energy"], color="red", label="Fossil Fuels")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Energy Share %")
    ax1.set_title(f"Energy Mix Transition in {selected_country}")
    
    ax2 = ax1.twinx()
    ax2.plot(df_country["year"], df_country["solar_share_elec"], color="blue", label="Solar Energy")
    ax2.plot(df_country["year"], df_country["wind_share_elec"], color="green", label="Wind Energy")
    
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")


    st.pyplot(fig)


# Talbe 2 ranking
st.markdown("### Table 2: Comparing Countries on Key Energy Transition Metrics")

# Sidebar ranking
st.sidebar.markdown("## Select Metrics for Comparison")
metric_display_options = [c.replace("_", " ").title() for c in df.columns[3:]]
selected_metric_display = st.sidebar.selectbox(
    "Select metric for ranking",
    metric_display_options
)
# Transform back to original column name format
selected_metric = selected_metric_display.lower().replace(" ", "_")

comp_1 = st.sidebar.selectbox("Select first country", 
                              df["country"].unique(),
                              key="comp_1")    
comp_2 = st.sidebar.selectbox("Select second country", 
                              df["country"].unique(),
                              key="comp_2")          


fig, ax = plt.subplots()
ax.plot(df[df["country"] == comp_1]["year"], df[df["country"] == comp_1][selected_metric], label=comp_1)
ax.plot(df[df["country"] == comp_2]["year"], df[df["country"] == comp_2][selected_metric], label=comp_2)
ax.set_xlabel("Year")
ax.set_ylabel(selected_metric_display)
ax.legend()
ax.set_title(f"{selected_metric_display} Comparison: {comp_1} vs {comp_2}")
st.pyplot(fig)