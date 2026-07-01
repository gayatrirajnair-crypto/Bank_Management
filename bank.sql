create database bank;
use bank;

create table staffdata(
SNo INT NOT NULL ,
fname VARCHAR(200) NOT NULL,
mname VARCHAR(200),
lname VARCHAR(200) NOT NULL,
staffid VARCHAR(80) PRIMARY KEY,
socialsecurity VARCHAR(100) NOT NULL,
DOB DATE,
DOJ DATE,
location varchar(200),
Branch varchar(200),
phone varchar(90),
email varchar(100),
emergencycont varchar(90),
designation varchar(200),
role varchar(200) NOT NULL,
username varchar(300) UNIQUE,
password varchar(300) NOT NULL,
securityqs varchar(255) NOT NULL,
securityans varchar(255) NOT NULL);

create table staffsalary(
staffid varchar(80) PRIMARY KEY,
name varchar(200),
salary int);

create table customerinfo(
sno int NOT NULL,
fname varchar(200),
mname VARCHAR(200),
lname VARCHAR(200) NOT NULL,
DOB DATE,
phoneno varchar(100) UNIQUE,
email varchar(300) UNIQUE,
ssno varchar(300),
incharge_staffid varchar(80),
creditscore int,
account_no varchar(80) NOT NULL UNIQUE,
address varchar(255),
profession varchar(200),
workplace varchar(200),
username varchar(300) PRIMARY KEY,
password varchar(300) NOT NULL,
age int );

create table nominee_info(
fname varchar(200) NOT NULL,
mname VARCHAR(200),
lname VARCHAR(200) NOT NULL,
location varchar(230) default "Dubai",
staffinchargeid VARCHAR(80),
nominee_account varchar(80),
customer_account varchar(80),
DOB DATE,
phoneno varchar(100) UNIQUE,
email varchar(230) UNIQUE,
ssno varchar(230),
relationship_with_customer varchar(200),
address varchar(255),
profession varchar(200),
workplace varchar(200),
creditscore int);



create table transfer(
sno varchar(100) NOT NULL PRIMARY KEY,
accountno varchar(80) NOT NULL,
handler_staff_id varchar(80) NOT NULL,
amt_transferred float,
Date_Of_request DATE,
Date_processed DATE,
status varchar(200),
account_no_of_sender varchar(80),
account_no_of_reciever varchar(80),
sender_branch varchar(200),
reciever_branch varchar(200),
reciever_bank_name varchar(200),
exchange_rate float default 0,
commission float);
create table balance(
sno varchar(100),
accountno varchar(80) PRIMARY KEY,
currentbalance float,
currency varchar(300));

create table salary(
staffid varchar(80) PRIMARY KEY,
salary float);


create table credit(
sno int PRIMARY KEY,
amount float,
accountno varchar(80),
interest_on_account float,
Date_Of_Credit DATE);

create table debit(
sno int PRIMARY KEY,
amount float,
accountno varchar(80),
interest float,
Date_of_deposit DATE);

create table fixed_deposit(
accountno varchar(80),
amount float,
interest float,
Date_deposited DATE,
End_date DATE);

create table loans(
accountno varchar(80),
staff_incharge varchar(80),
interest float,
amount float,
date_applied DATE,
status varchar(200),
collateral varchar(255),
branch varchar(230));

create table card_info(
accountno varchar(80),
cardno varchar(80),
card_type varchar(230),
status varchar(100),
issued_by varchar(230));

select * from staffdata
