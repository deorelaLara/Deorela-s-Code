create database apod;
use apod;

CREATE TABLE pictures(
    date varchar(20) primary key,
    name varchar(50),
    media_type varchar(50),
    url varchar(450)
);