### mysql queries

-- query for creating new database
    mysql> create database database_name;
eg:
    mysql> create database movie_db_june;

-- mysql query for listing databases
mysql> show databases;

-- mysql query for switch into a database
    mysql> use database_name;
eg:
    mysql> use movie_db_june;
-- mysql query for creating table

    mysql > create table table_name(

    column_name data_type constraint,
    column_name data_type constraint,
    column_name data_type constraint,
);

eg: movie [id,title,year,run_time,rating genre]
    mysql> create table movie(

        id int auto_increment primary key,
        title varchar(200) not null,
        year varchar(10) not null,
        run_time int not null,
        rating float not null,
        genre enum("action","comedy","drama","triller","horror") default "action"
    );

-- query for describing table

    mysql> desc table_name;

eg:
    mysql> desc movie;

-- query for inserting records into table

    mysql > insert into table_name (col1,col2,col3,,) values(val1, val2,val3,,);

 eg:

    mysql> insert into movie(title,year,run_time,rating,gener)
    values('abcd',2002,120,8.5,'action');

-- query for listing all records

    mysql> select * from table_name;

eg:

    mysql> select * from movie;

-- filtering records

-- selecting record with id =2

    mysql>select * from table_name where condition
eg:
    mysql> select * from movie where id = 2;

-- query for updating records
    mysql > update table_name set col1=value,col12=val2 col3=val3 where condition
eg:
    mysql>update movie set title = "balan the boy", run_time=150 where id = 3;
