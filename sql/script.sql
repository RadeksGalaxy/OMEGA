
create table auto
(
    id    int auto_increment
        primary key,
    model varchar(50) null
);

create table autoservisy
(
    id        int auto_increment
        primary key,
    global_id varchar(255) null,
    nazev     varchar(255) null,
    mesto     varchar(255) null,
    ulice     varchar(255) null,
    psc       varchar(50)  null,
    logo      varchar(255) null,
    prodejAut int          null,
    servisAut int          null
);

create table user
(
    id       int auto_increment
        primary key,
    jmeno    varchar(30)  null,
    prijmeni varchar(30)  null,
    usjmeno  varchar(30)  null,
    email    varchar(124) null,
    heslo    varchar(255) null
);

create table objednavky
(
    id            int auto_increment
        primary key,
    autoservis_id int           null,
    model_id      int           null,
    rok_vyroby    int           null,
    km            int           null,
    typ           int           null,
    datum         date          null,
    poz           varchar(1024) null,
    us_id         int           null,
    constraint autoservis_fk
        foreign key (autoservis_id) references autoservisy (id),
    constraint model_fk
        foreign key (model_id) references auto (id),
    constraint us_fk
        foreign key (us_id) references user (id)
);

create table zam
(
    id         int auto_increment
        primary key,
    autoser_id int          null,
    nazev      varchar(255) null,
    heslo      varchar(255) null,
    constraint autoser_fk
        foreign key (autoser_id) references autoservisy (id)
);


create table odpoved(
    id int primary key auto_increment,
    obj_id int,
    constraint obj_fk foreign key (obj_id) references objednavky(id),
    datum date,
    cas time,
    delka varchar(20),
    poz varchar(1024)
);