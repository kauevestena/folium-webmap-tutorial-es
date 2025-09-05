# 1. Importar las bibliotecas necesarias
import osmnx as ox
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster

# 2. Definir el área geográfica y las etiquetas de las características a descargar
place = "Curitiba, Brazil"
tags = {"highway": "bus_stop"}
description = "Bus Stop"
zoom_level = 13

# 3. Especificar qué campos mostrar dentro de las ventanas emergentes de los marcadores
popup_fields = ["name", "operator", "network", "ref"]

# 4. Descargar las características de las paradas de autobús de OpenStreetMap para el lugar elegido
gdf = ox.features_from_place(place, tags=tags)

# 5. Asegurarse de que el GeoDataFrame esté en el sistema de coordenadas de latitud/longitud
gdf = gdf.to_crs(epsg=4326)

# 6. Añadir las columnas que falten para que las ventanas emergentes no se rompan
for field in popup_fields:
    if field not in gdf.columns:
        gdf[field] = ""

# 7. Calcular el centroide de todas las paradas de autobús para centrar el mapa
centroid = gdf.union_all().centroid
center_latlon = [centroid.y, centroid.x]

# 8. Crear un mapa Folium y añadir algunas capas de teselas base
m = folium.Map(location=center_latlon, zoom_start=zoom_level, tiles=None)
folium.TileLayer("CartoDB positron", name="CartoDB Positron").add_to(m)
folium.TileLayer("OpenStreetMap", name="OpenStreetMap").add_to(m)
folium.TileLayer(
    "Stamen Terrain",
    name="Stamen Terrain",
    attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors",
).add_to(m)

# 9. Añadir marcadores de paradas de autobús al mapa utilizando un plugin MarkerCluster
marker_cluster = MarkerCluster(name="Bus Stops (Cluster)").add_to(m)
for _, row in gdf.iterrows():
    coords = row.geometry
    if coords.geom_type == "Point":
        folium.Marker(
            location=[coords.y, coords.x],
            popup=row.get("name", description),
        ).add_to(marker_cluster)

# 10. Añadir una capa GeoJSON simple con marcadores circulares interactivos
interactive_layer = folium.GeoJson(
    gdf,
    name="Bus Stops (Points)", show=False,
    marker=folium.CircleMarker(
        radius=5, color="blue", fill=True, fill_opacity=0.7
    ),
    highlight_function=lambda x: {"radius": 8},
    popup=folium.GeoJsonPopup(fields=popup_fields, labels=True),
).add_to(m)

# 11. Intentar obtener y mostrar el polígono del límite administrativo
#     OpenStreetMap utiliza la etiqueta "admin_level" para dichos límites:
#     https://wiki.openstreetmap.org/wiki/Key:admin_level
try:
    boundary_gdf = ox.geocode_to_gdf(place).to_crs(epsg=4326)
    folium.GeoJson(
        boundary_gdf,
        name="Boundary",
        style_function=lambda x: {"fillOpacity": 0, "color": "green"},
    ).add_to(m)
except Exception:
    pass

# 12. Permitir al usuario activar y desactivar las capas
folium.LayerControl().add_to(m)

# 13. Guardar el mapa en un archivo HTML
m.save("index.html")
