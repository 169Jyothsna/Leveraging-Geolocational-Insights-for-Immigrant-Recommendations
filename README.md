# Leveraging-Geolocational-Insights-for-Immigrant-Recommendations

**Leveraging Geolocational Insights for Immigrant  Recommendations through Advanced Analytics and K  Means Clustering**

This project aims to use geolocational data analysis to enhance the immigrant settlement processes.

This study attempts to find patterns and trends within cities or regions that are significant to immigrant settlement by examining geolocational data. Advanced analytics approaches such as K Means Clustering enable the categorization of locations based on different criteria, including amenities, price, and proximity to various services.

**Steps**
  1. **Data Collection:** Gather data from Kaggle or other resources.
  2. **Data Cleaning:** Clean data by removing null and unnecessary values, improving productivity and decision-making quality, and removing errors from multiple data sources.
  3. **Data Visualization:** Data visualization aids in understanding data by presenting it graphically through graphs, tables, and maps, enabling easy identification of patterns, trends, and communication to non-technical audiences.
  4. **Data Pre-processing:** The project uses the K-means clustering method to partition data points into k clusters with minimal variance. The Elbow methodology determines the ideal number of clusters using the internal cluster sum of squares (WCSS) value.
  5. **Collecting Geographical Information:** GeoPy initializes city coordinates, which are sent to FourSquare API for location lists. JSON-formatted data is translated into a data frame for further processing.
  6. **Displaying the results on a map:** The Folium library visualizes data by displaying recommendations in a spatial representation, providing users with insights into popular areas and facilitating investigation or travel to these regions.

**Libraries Used:**
  1. Matplotlib
  2. Numpy
  3. Pandas
  4. Seaborn
  5. Sklearn
  6. SciPy
  7. Geopy
  8. Folium
  9. Pandas io.json
  10. Geopy.geocoders
  11. WebView
  12. WebBrowser
  13. Nomination
  14. Json_normalize

**How should this project be executed?**
  1. Open project_code.py file in VS Code or in any other IDE.
  2. Install Live Server extension by Ritwick Dey.
  3. Click on Go Live in VSC window.
  4. Run .py file.
  5. Select a city from available options.
  6. Click Go to open city map with various plots.

**Incorporate New City into Exploratory Data Analysis:**
  1. Go to the project_code2.py file.
  2. Enter the city name into the variable named city.
  3. Update the city name in map_.save("Destination/Mumbai.html").
  4. Execute the .py file.
  5. City map is stored in the Cities folder.
  6. Open the project_code.py file.
  7. Add the city name to the cities tuple.
  8. Execute the project_code.py file.

As part of this project, a website has been built that assists individuals who are in different cities or those who are planning to relocate to another city in finding the best accommodation based on their budget and distance from the desired location. The K-means clustering algorithm, a machine learning approach, was suggested to be used in this study to determine the optimum locations for lodging. The resulting solution offers an intuitive user interface that prioritizes usability.
