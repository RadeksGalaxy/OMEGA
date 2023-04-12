
CREATE TABLE auto (
  id int NOT NULL AUTO_INCREMENT,
  model varchar(50) DEFAULT NULL,
  PRIMARY KEY (id)
);

INSERT INTO auto VALUES (1,'Fabia'),
                          (2,'Fabia Combi'),
                          (3,'Scala'),
                          (4,'Kamiq'),
                          (5,'Octavia'),
                          (6,'Octavia Combi'),
                          (7,'Karoq'),
                          (8,'Kodiaq'),
                          (9,'Superb'),
                          (10,'Superb Combi'),
                          (11,'Enyaq Coupe'),
                          (12,'Enyaq');


CREATE TABLE user (
  id int NOT NULL AUTO_INCREMENT,
  jmeno varchar(30) DEFAULT NULL,
  prijmeni varchar(30) DEFAULT NULL,
  usjmeno varchar(30) DEFAULT NULL,
  email varchar(124) DEFAULT NULL,
  heslo varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
);


INSERT INTO user VALUES (1,'Radek','Koblic','radekBorec12','koblic@spsejecna.cz','08e795977b1fbd776f9f27ac44884c40471987df13ade40d90b922efb0c06c6a'),
                          (2,'Honza','Karel','honzakarlik','karel@spsejecna.cz','d0f33413465cdef5f979ae170f6df775dbbdcafbee63ad5dc646eb41a0550a22'),
                          (3,'Pavel','Velky','pavelVelky','velky@spsejecna.cz','e103446a4069a87a124940388f3886c85beae189fb44b553f4451ac1840c68ab'),
                          (4,'Student','Student','zsStudent','student@spsejecna.cz','b13712428800d6a2b03aa8d5edf49dd343f6ab75beb1ca759b2a3af9ca666679');


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


create table objednavky
(
    id        int auto_increment primary key,
    autoservis_id int,
    model_id int,
    constraint model_fk foreign key (model_id) references auto(id),
    constraint autoservis_fk foreign key (autoservis_id) references autoservisy(id),
    rok_vyroby int,
    km int,
    typ int,
    datum date,
    poz varchar(555)

);


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


create or replace table odpoved
(
	id int auto_increment
		primary key,
	obj_id int null,
	datum date null,
	cas time null,
	delka varchar(20) null,
	poz varchar(1024) null,
	odpoved int null comment '1=potvrzene || 2=zruseno',
	casPred time null comment 'cas zacatku servisu',
	constraint obj_fk
		foreign key (obj_id) references db_autoservis.objednavky (id)
);