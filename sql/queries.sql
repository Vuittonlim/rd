-- Get busiest stations by total volume, peak hour by day type, weekday vs weekend comparison.
SELECT pt_code, SUM(total_volume) FROM station_volumes GROUP BY pt_code ORDER BY SUM(total_volume) DESC LIMIT 10;
SELECT day_type, time_per_hour, sum(total_volume)  FROM station_volumes GROUP BY(day_type, time_per_hour) ORDER BY sum
(total_volume) DESC LIMIT 10;
SELECT day_type, SUM(total_volume) AS total_volume FROM station_volumes GROUP BY day_type ORDER BY total_volume DESC;