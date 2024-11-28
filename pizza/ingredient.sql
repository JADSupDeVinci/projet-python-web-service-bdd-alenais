create table pizza.ingredient
(
    id                int auto_increment
        primary key,
    label             varchar(100) not null,
    label_commercial  varchar(100) null,
    id_typeingredient int          not null,
    constraint label
        unique (label),
    constraint label_commercial
        unique (label_commercial),
    constraint ingredient_ibfk_1
        foreign key (id_typeingredient) references pizza.typeingredient (id)
);

create index id_typeingredient
    on pizza.ingredient (id_typeingredient);

