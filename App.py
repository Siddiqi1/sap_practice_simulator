import streamlit as st
# import openai (Commented out as it's not currently used)
import pandas as pd
import folium
from streamlit_folium import folium_static
import time

# Initialize Streamlit app
st.set_page_config(layout="wide", page_title="What Happened - Roadside Assistance")

# Display cartoon image of a person with a roadside issue
st.image("roadside_issue_cartoon.png", use_column_width=True)

# Title and search bar
st.title("What Happened? - AI Roadside Assistance")
issue = st.text_input("Describe your issue:", placeholder="E.g., My tire is flat and I'm stuck on the highway")

# Example pretend services database
dummy_services = pd.DataFrame({
    "Service Name": ["Joe's Towing", "Rapid Response Auto", "24/7 Tire Fix", "Emergency Gas Delivery"],
    "Distance (miles)": [2.5, 5.0, 3.2, 4.7],
    "Cost ($)": [75, 100, 50, 40],
    "Provider": ["Joe Thompson", "Amy Rogers", "Mark Daniels", "Lisa Tran"],
    "Latitude": [37.7749, 37.7840, 37.7640, 37.7520],
    "Longitude": [-122.4194, -122.4090, -122.4290, -122.4390]
})

# Simulate AI response to categorize issue and find the best match
if issue:
    st.subheader("Analyzing your situation... 🔍")
    time.sleep(2)  # Simulating AI processing time
    
    best_match = dummy_services.iloc[0]  # Simulating AI choosing the closest service
    
    st.success("We found the best roadside assistance for you! 🚗")
    st.write(f"✅ **Service Name:** {best_match['Service Name']}")
    st.write(f"📍 **Distance:** {best_match['Distance (miles)']} miles")
    st.write(f"💰 **Cost Estimate:** ${best_match['Cost ($)']}")
    st.write(f"👨‍🔧 **Provider:** {best_match['Provider']}")
    
    # Display map with service locations
    st.subheader("Live Service Locations")
    map_center = [best_match["Latitude"], best_match["Longitude"]]
    service_map = folium.Map(location=map_center, zoom_start=13)
    for _, row in dummy_services.iterrows():
        folium.Marker([row["Latitude"], row["Longitude"]], 
                      popup=f"{row['Service Name']} ({row['Distance (miles)']} mi)",
                      icon=folium.Icon(color='blue')).add_to(service_map)
    folium_static(service_map)
    
    # Simulated live tracking of service vehicle
    st.subheader("Live Service Tracking")
    progress_bar = st.progress(0)
    for percent in range(0, 101, 10):
        time.sleep(0.5)
        progress_bar.progress(percent)
    st.success("Your service provider has arrived! 🚙💨")
    
    st.button("Request Assistance 🚗")

