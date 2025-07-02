create database hmbank;
use hmbank;

create table customers (
    customerid int primary key auto_increment,
    firstname varchar(50) not null,
    lastname varchar(50) not null,
    dob date not null,
    email varchar(100) unique not null,
    phone varchar(15) unique not null,
    address text not null
);

create table accounts (
    accountid int primary key auto_increment,
    customerid int,
    type enum('savings', 'current', 'zero_balance') not null,
    balance decimal(12,2) not null default 0.00,
    foreign key (customerid) references customers(customerid)
);

create table transactions (
    transactionid int primary key auto_increment,
    accountid int,
    type enum('deposit', 'withdrawal', 'transfer') not null,
    amount decimal(12,2) not null,
    date timestamp default current_timestamp,
    foreign key (accountid) references accounts(accountid)
);
