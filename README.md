# Tutorial de Webmap con Folium

Este repositorio es un tutorial y una plantilla básica para crear y publicar fácilmente un mapa web interactivo. Utiliza Python con las bibliotecas Folium, GeoPandas y OSMnx para generar el mapa, y se despliega automáticamente en GitHub Pages a través de GitHub Actions.

## ¿Cómo usar esta plantilla?

El objetivo de este proyecto es que puedas crear tu propio mapa con mínimos cambios. Simplemente sigue estos pasos:

0.  Activa GitHub Pages en las configuraciones. (mira la imágen abajo, no te olvider de hacer un click en "save")  

1.  Utiliza ese repositorio como template (no un fork): Esto creará una copia en tu propia cuenta de GitHub.

2.  Modifica el archivo `make_map.py`:

    *   Cambia el valor de la variable `place` para definir la ubicación geográfica de tu mapa (por ejemplo, `"Medellin, Colombia"`).

    *   Ajusta las `tags` de OpenStreetMap para seleccionar las características que quieres mostrar en el mapa (por ejemplo, `{"amenity": "restaurant"}` para restaurantes).

3.  Guarda los cambios (commit): Una vez que guardes los cambios en tu repositorio, una acción de GitHub se ejecutará automáticamente.

4.  ¡Listo! La acción generará un archivo `index.html` y lo publicará en GitHub Pages. Podrás ver tu mapa en una URL como `https://<tu-usuario>.github.io/<nombre-del-repositorio>/`.

¡Este proyecto es una manera sencilla de crear proyectos customizables para visualización y compartimiento de datos de OSM!

<img width="2871" height="1704" alt="image" src="https://github.com/user-attachments/assets/79b25903-1e89-49f2-8d9d-f65489d45570" />

Bonus: Intenta expandir las funcionalidades; puedes utilizar agentes de código como Google Jules o Copilot.
