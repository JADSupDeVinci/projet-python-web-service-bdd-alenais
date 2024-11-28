create table pizza.habitante
(
    id    int auto_increment
        primary key,
    label varchar(100) not null,
    constraint label
        unique (label)
);

