use rasse;
create table product (
 id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
         data VARCHAR(100) 
);

insert into product (data) values ('Hink');
insert into product (data) values ('Spade');
insert into product (data) values ('Kanna');
commit;
