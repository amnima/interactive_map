# This file is the first attempt to create a series of the interactive maps for Afg.
# The goal of this project is to create a full interactive map of afghanistan showcasing the mineral resource and drainage regions
# of Afgh. 
# The primary author is: Amin Mirzai
import folium
import mysql.connector

# Connect to the MySQL database
db_config = {
    'host': 'localhost',
    'user': 'Amin',
    'password': 'Tomorrow',
    'database': 'mineral_db'
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Retrieve mineral data from the database
query = "SELECT name, latitude, longitude FROM minerals"
cursor.execute(query)
mineral_data = cursor.fetchall()

# Create a Folium map centered around Afghanistan
afghanistan_map = folium.Map(location=[34.5553, 69.2075], zoom_start=6)

# Add markers for each mineral location
for mineral in mineral_data:
    name, lat, lon = mineral
    folium.Marker(location=[lat, lon], popup=name).add_to(afghanistan_map)

# Save the map to an HTML file
afghanistan_map.save('mineral_map.html')

# Close the database connection
cursor.close()
conn.close()
