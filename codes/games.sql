 create table customers (
    firstName varchar(20) not null,
    lastName varchar(50) not null,
    customer_ID int not null,
    address varchar(200) not null,
    email varchar(50) not null,
    password varchar(20) not null,
    unique(customer_ID),
    PRIMARY KEY (customer_ID)
    );


create table orders (
    order_id int not null auto_increment,
    customer_id int NOT NULL,
    placed date,
    total dec(7,2),
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_ID) REFERENCES customers (customer_ID)
    );

create table games (
    product_ID int not null,
    game_title varchar(20) not null,
    stock int default '0',
    price dec(7,2) not null,
    unique(product_ID),
    PRIMARY KEY (product_ID)
     );

