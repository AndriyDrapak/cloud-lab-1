use lab5;

drop trigger if exists delete_fk;
drop trigger if exists update_fk;
drop trigger if exists insert_fk;
drop procedure if exists insert_into_owners;
drop procedure if exists insert_into_da;
drop procedure if exists insert_owners;
drop procedure if exists get_calculate_price;
drop function if exists calculate_price;
drop trigger if exists forbid_updating;
drop trigger if exists allowed_license_insert;
drop trigger if exists allowed_license_update;
drop trigger if exists allowed_manufactures_insert;
drop trigger if exists allowed_manufactures_update;

delimiter //

create trigger insert_fk
before insert on owner_city
for each row
begin
    declare owner_exists int;
    select count(*) into owner_exists from owners where id = new.owner_id;
    if owner_exists = 0 then
        signal sqlstate '45000' set message_text = 'Owner does not exist';
    end if;
end //

create trigger update_fk
before update on owner_city
for each row
begin
    declare owner_exists int;
    select count(*) into owner_exists from owners where id = new.owner_id;
    if owner_exists = 0 then
         signal sqlstate '45000' set message_text = 'Owner does not exist.';
    end if;
end //

create trigger delete_fk
before delete on owners
for each row
begin
    declare owner_count int;
    select count(*) into owner_count from owner_city where owner_id = old.id;
    if owner_count > 0 then
        signal sqlstate '45000' set message_text = 'Cannot delete fk.';
    end if;
end //


create procedure insert_into_owners(
	name varchar(50),
    contact varchar(15))
begin
	insert into owners (name, contact) values
    (name, contact);
end //


create procedure insert_into_da(
	driver_id int,
    bus_route_id int,
    start_date date,
    end_date date)
begin
	insert into driver_assignments (driver_id, bus_route_id, start_date, end_date) values
	(driver_id, bus_route_id, start_date, end_date);
end //

create procedure insert_owners()
begin
    declare num int default 1;
    while num <= 10 do
        insert into owners (name, contact) value (concat('Noname', num), "a");
        set num = num + 1;
    end while;
end //

create function calculate_price(type varchar(10))
returns decimal(10, 2)
deterministic
begin
    declare result decimal(10, 2);

    if type = 'max' then
        select max(price) into result from tickets;
    elseif type = 'min' then
        select min(price) into result from tickets;
    elseif type = 'sum' then
        select sum(price) into result from tickets;
    elseif type = 'avg' then
        select avg(price) into result from tickets;
	else
		signal sqlstate '45000' set message_text = 'This type does not exist.';
    end if;

    return result;
end //

create procedure get_calculate_price(type varchar(10))
begin
    select calculate_price(type) as result;
end //

create trigger forbid_updating
before update on bus_routes
for each row
begin
	signal sqlstate '45000' set message_text = 'Updates are not allowed';
end //


create trigger allowed_license_insert
before insert on drivers
for each row
begin
    if new.license_number not regexp '^[A-LN-Z]{2}-[0-9]{3}-[0-9]{2}$' then
		signal sqlstate "45000" set message_text = "license_number must be in ^[A-LN-Z]{2}-[0-9]{3}-[0-9]{2}$";
	end if;
end //

create trigger allowed_license_update
before update on drivers
for each row
begin
    if new.license_number not regexp '^[A-LN-Z]{2}-[0-9]{3}-[0-9]{2}$' then
		signal sqlstate "45000" set message_text = "license_number must be in ^[A-LN-Z]{2}-[0-9]{3}-[0-9]{2}$";
	end if;
end //

create trigger allowed_manufactures_insert
before insert on buses
for each row
begin
	if new.manufacturer not in ('Mercedes', 'Opel', 'LAZ') then
        signal sqlstate '45000' set message_text =  'Invalid manufacturer name. Only Mersedes, Opel, and LAZ are allowed.';
    end if;
end //

create trigger allowed_manufactures_update
before update on buses
for each row
begin
	if new.manufacturer not in ('Mercedes', 'Opel', 'LAZ') then
        signal sqlstate '45000' set message_text =  'Invalid manufacturer name. Only Mersedes, Opel, and LAZ are allowed.';
    end if;
end //


delimiter ;