SELECT 
 a.City, 
 a.Total_Population, 
 AVG(b.CO) AS Average_CO, 
 AVG(b.NO2) AS Average_NO2, 
 AVG(b.O3) AS Average_O3, 
 AVG(b.SO2) AS Average_SO2, 
 AVG(b.PM2_5) AS Average_PM2_5, 
 AVG(b.PM10) AS Average_PM10 
FROM 
 (
    SELECT 
      c.City, 
      c.Total_Population, 
      ROW_NUMBER() OVER(PARTITION BY c.Country ORDER BY c.Total_Population DESC) AS Rank 
    FROM 
      Cities c
 ) a 
INNER JOIN 
 AirQuality b 
ON 
 a.Country = b.Country AND a.City = b.City 
WHERE 
 a.Rank <= 10 
GROUP BY 
 a.City, 
 a.Total_Population 
ORDER BY 
 a.Total_Population DESC;


 ##Explicación
 #Primero, utilicé una subconsulta para obtener el total de población de cada ciudad y asignar 
 #un rango según la población y el país. 
 #Luego, en la consulta principal, uní las tablas 'Cities' y 'AirQuality'.
 #Utilicé la función AVG para calcular el promedio de los valores de las columnas 
 #'CO', 'NO2', 'O3', 'SO2', 'PM2_5' y 'PM10' de la tabla 'AirQuality'.
 #Finalmente, seleccioné las columnas 'City', 'Total_Population' y las columnas de promedio 
 #calculadas previamente, para posteriormente ordenar los resultados de la columna 'Total_Population' 
 #de forma descendente.

 #Intepretación
 #Al analizar los resultados de la consulta, se observa que las ciudades con las peores
 #calidades del aire tienen una mayor población. 
 #Se presenta una relación directa entre ambos aspectos, sin embargo no se descarta que haya otros 
 #factores que también influyan en dicho resultado y que no se incluyeron en este análisis.