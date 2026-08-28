SET search_path TO lyfter_car_rental;

DROP TABLE lyfter_car_rental.users;

SELECT id, status FROM cars WHERE status = 'available' OR status = 'rental ongoing';

SELECT rentals.id, rentals.user_id, rentals.car_id, rentals.rental_date, rentals.status
FROM rentals
LEFT JOIN users
ON rentals.user_id = users.id
WHERE rentals.status = 'ongoing'
ORDER BY rentals.id ASC;


SET search_path TO lyfter_car_rental;

SELECT rentals.car_id, rentals.user_id, rentals.return_date, cars.status AS car_status, rentals.status AS rental_status
FROM rentals
LEFT JOIN cars
ON cars.id = rentals.car_id
WHERE cars.status = 'rental ongoing';


DELETE FROM lyfter_car_rental.rentals WHERE id > 7;

ALTER TABLE lyfter_car_rental.rentals
ALTER COLUMN id RESTART WITH 8;

SELECT * FROM lyfter_car_rental.users ORDER BY id ASC;

SELECT id, rental_date FROM lyfter_car_rental.cars WHERE status = 'rental ongoing';

SELECT * FROM lyfter_car_rental.cars WHERE id = 68;