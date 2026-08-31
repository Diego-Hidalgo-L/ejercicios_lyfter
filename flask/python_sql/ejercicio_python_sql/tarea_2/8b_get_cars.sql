SET search_path TO lyfter_car_rental;

SELECT *
FROM cars
WHERE status = 'available';