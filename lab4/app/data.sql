use drapak;

INSERT INTO owners (name, contact) VALUES
('LeasingCorp', 'leasing@corp.com'),
('AutoRental LLC', 'info@autorental.com'),
('BusFleet Inc.', 'contact@busfleet.com'),
('RoadWay Rentals', 'info@roadwayrentals.com'),
('DriveNow Ltd.', 'support@drivenow.com'),
('Highway Haulers', 'service@highwayhaulers.com'),
('Urban Mobility', 'info@urbanmobility.com'),
('FastTrack Co.', 'support@fasttrack.com'),
('RouteMasters', 'contact@routemasters.com'),
('National Transit', 'support@nationaltransit.com');

INSERT INTO buses (registration_number, manufacturer, model, capacity, mileage, age, ownership_type, owner_id) VALUES
('AA1234BB', 'Mercedes', 'Sprinter', 50, 120000, 5, 'owned', 2),
('CC5678DD', 'Volvo', '9700', 60, 300000, 8, 'rented', 4),
('EE9012FF', 'Scania', 'Citywide', 70, 50000, 2, 'owned', 5),
('FF3456GG', 'MAN', 'Lion’s Coach', 55, 200000, 6, 'rented', 5),
('GG7890HH', 'Iveco', 'Evadys', 65, 250000, 7, 'owned', 9),
('HH1234II', 'Mercedes', 'Citaro', 40, 80000, 3, 'owned', 4),
('II5678JJ', 'Setra', 'ComfortClass', 70, 150000, 4, 'rented', 8),
('JJ9012KK', 'Ford', 'Transit', 20, 60000, 1, 'owned', 10),
('KK3456LL', 'Volvo', '7900', 30, 220000, 10, 'rented', 7),
('LL7890MM', 'Mercedes', 'Tourismo', 50, 180000, 5, 'owned', 2);

-- Маршрути
INSERT INTO routes (start_address, end_address, total_distance, total_price) VALUES
('Kyiv', 'Lviv', 540, 800),
('Odesa', 'Kharkiv', 700, 1000),
('Dnipro', 'Poltava', 200, 300),
('Chernihiv', 'Sumy', 300, 400),
('Zhytomyr', 'Rivne', 250, 350),
('Lviv', 'Uzhhorod', 250, 350),
('Khmelnytskyi', 'Ternopil', 150, 200),
('Kyiv', 'Vinnytsia', 270, 400),
('Poltava', 'Kharkiv', 150, 250),
('Ivano-Frankivsk', 'Chernivtsi', 120, 200);

-- Зупинки
INSERT INTO stops (route_id, stop_order, stop_name, distance_to_next, price_to_next) VALUES
(1, 1, 'Kyiv', 100, 150),
(1, 2, 'Zhytomyr', 150, 200),
(1, 3, 'Rivne', 290, 450),
(2, 1, 'Odesa', 200, 300),
(2, 2, 'Dnipro', 500, 700),
(3, 1, 'Dnipro', 100, 150),
(3, 2, 'Kremenchuk', 100, 150),
(4, 1, 'Chernihiv', 150, 200),
(4, 2, 'Krolevets', 150, 200),
(5, 1, 'Zhytomyr', 125, 175);

-- Водії
INSERT INTO drivers (first_name, last_name, license_number, phone_number, hire_date) VALUES
('Ivan', 'Petrenko', 'A12345', '380501234567', '2020-01-15'),
('Olga', 'Shevchenko', 'B67890', '380671234567', '2018-06-10'),
('Taras', 'Bondarenko', 'C23456', '380931234567', '2019-11-20'),
('Nadiya', 'Tkachuk', 'D34567', '380501234123', '2021-03-25'),
('Andriy', 'Kovalchuk', 'E45678', '380671111222', '2022-07-30'),
('Svitlana', 'Lytvyn', 'F56789', '380931223344', '2023-01-15'),
('Yaroslav', 'Melnyk', 'G67890', '380501112233', '2017-04-10'),
('Dmytro', 'Ostapchuk', 'H78901', '380671334455', '2016-08-22'),
('Kateryna', 'Hrytsenko', 'I89012', '380931445566', '2020-11-30'),
('Oleksandr', 'Voronov', 'J90123', '380501556677', '2019-02-18');

-- Призначення автобусів на маршрути
INSERT INTO bus_routes (bus_id, route_id, assignment_date) VALUES
(1, 1, '2024-01-01'),
(2, 2, '2024-02-01'),
(3, 3, '2024-03-01'),
(4, 4, '2024-04-01'),
(5, 5, '2024-05-01'),
(6, 6, '2024-06-01'),
(7, 7, '2024-07-01'),
(8, 8, '2024-08-01'),
(9, 9, '2024-09-01'),
(10, 10, '2024-10-01');

-- Призначення водіїв на автобуси
INSERT INTO driver_assignments (driver_id, bus_route_id, start_date, end_date) VALUES
(1, 1, '2024-01-01', '2024-01-31'),
(2, 2, '2024-02-01', '2024-02-28'),
(3, 3, '2024-03-01', NULL),
(4, 4, '2024-04-01', NULL),
(5, 5, '2024-05-01', NULL),
(1, 6, '2024-06-01', NULL),
(2, 7, '2024-07-01', NULL),
(3, 8, '2024-08-01', NULL),
(4, 9, '2024-09-01', NULL),
(5, 10, '2024-10-01', NULL);

-- Таблиця квитків
INSERT INTO tickets (route_id, stop_from_id, price, purchase_date) VALUES
(1, 1, 800, '2024-11-01'),
(2, 1, 1000, '2024-11-10'),
(3, 1, 300, '2024-11-11'),
(4, 1, 400, '2024-11-12'),
(5, 1, 350, '2024-11-13'),
(6, 1, 350, '2024-11-14'),
(7, 1, 200, '2024-11-15'),
(8, 1, 400, '2024-11-16'),
(9, 1, 250, '2024-11-17'),
(10, 1, 200, '2024-11-18');

-- Технічне обслуговування автобусів
INSERT INTO bus_maintenance (bus_id, maintenance_date, description, cost) VALUES
(1, '2024-10-01', 'Engine repair', 15000),
(2, '2024-09-15', 'Oil change', 2000),
(3, '2024-08-10', 'Brake replacement', 8000),
(4, '2024-07-05', 'Transmission repair', 12000),
(5, '2024-06-20', 'Tire replacement', 5000),
(6, '2024-05-15', 'Air conditioning service', 3000),
(7, '2024-04-01', 'Battery replacement', 4000),
(8, '2024-03-15', 'Suspension repair', 9000),
(9, '2024-02-10', 'Interior cleaning', 1500),
(10, '2024-01-05', 'General inspection', 1000);

-- Таблиця власників автобусів


-- Таблиця розкладів
INSERT INTO schedules (route_id, departure_time, arrival_time) VALUES
(1, '2024-10-01 08:00:00', '2024-10-01 14:00:00'),
(2, '2024-10-01 10:00:00', '2024-10-01 20:00:00'),
(3, '2024-10-01 09:00:00', '2024-10-01 12:00:00'),
(4, '2024-10-01 15:00:00', '2024-10-01 18:30:00'),
(5, '2024-10-01 07:00:00', '2024-10-01 10:00:00'),
(6, '2024-10-01 06:00:00', '2024-10-01 09:00:00'),
(7, '2024-10-01 11:00:00', '2024-10-01 13:30:00'),
(8, '2024-10-01 16:00:00', '2024-10-01 19:30:00'),
(9, '2024-10-01 14:00:00', '2024-10-01 16:00:00'),
(10, '2024-10-01 17:00:00', '2024-10-01 19:00:00');


drop procedure if exists get_buses_by_owner;
drop procedure if exists get_stops_by_route;
drop procedure if exists get_routes_by_stop;
drop procedure if exists get_bus_routes_by_driver;
drop procedure if exists get_drivers_by_bus_route;
drop procedure if exists get_routes_by_bus;
drop procedure if exists get_busses_by_route;
drop procedure if exists get_schedules_by_route;
drop procedure if exists get_bus_maintenances_by_bus;
drop procedure if exists get_stops_by_route1;


delimiter //

create procedure get_buses_by_owner(owner_id int)
begin
	select o.id, b.*
	from buses b
	join owners o on o.id = b.owner_id
	where b.owner_id = owner_id;
end //


create procedure get_stops_by_route(route_id int)
begin
	select r.id, s.*
	from stops s
	join routes r on r.id = s.route_id
	where s.route_id = route_id;
end //

create procedure get_bus_maintenances_by_bus(bus_id int)
begin
	select b.id, bm.*
	from bus_maintenance bm
	join buses b on b.id = bm.bus_id
	where bm.bus_id = bus_id;
end //

create procedure get_schedules_by_route(route_id int)
begin
	select r.id, s.*
	from schedules s
	join routes r on r.id = s.route_id
	where s.route_id = route_id;
end //

create procedure get_busses_by_route(route_id int)
begin
	select bs.*, b.*
	from buses b
	join bus_routes bs on bs.bus_id = b.id
	where bs.route_id = route_id;
end //

create procedure get_routes_by_bus(bus_id int)
begin
	select bs.*, r.*
	from routes r
	join bus_routes bs on bs.route_id = r.id
	where bs.bus_id = bus_id;
end //

create procedure get_drivers_by_bus_route(bus_route_id int)
begin
	select da.*, d.*
	from drivers d
	join driver_assignments da on da.driver_id = d.id
	where da.bus_route_id = bus_route_id;
end //

create procedure get_bus_routes_by_driver(driver_id int)
begin
	select da.*, b.*
	from bus_routes b
	join driver_assignments da on da.bus_route_id = b.id
	where da.driver_id = driver_id;
end //

create procedure get_routes_by_stop(stop_id int)
begin
	select t.*, r.*
	from routes r
	join tickets t on t.route_id = r.id
	where t.stop_from_id = stop_id;
end //


create procedure get_stops_by_route1(route_id int)
begin
	select t.*, s.*
	from stops s
	join tickets t on t.stop_from_id = s.id
	where t.route_id = route_id;
end //


delimiter ;