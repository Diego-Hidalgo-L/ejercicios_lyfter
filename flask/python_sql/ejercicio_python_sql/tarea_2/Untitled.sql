SET search_path TO lyfter_car_rental;

SELECT * FROM lyfter_car_rentals.rentals ORDER BY id ASC;

ALTER TABLE lyfter_car_rentals.rentals
ALTER COLUMN id RESTART WITH 8;