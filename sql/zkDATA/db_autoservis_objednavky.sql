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
)
    auto_increment = 18;

INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (1, 1, 1, 2000, 7, 1, '2023-03-31', null, 1);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (2, 1, 1, 2000, 5, 1, '2023-03-31', null, 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (3, 2, 9, 2000, 13, 1, '2023-03-31', null, 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (4, 1, 1, 2008, 24, 2, '2023-04-20', null, 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (5, 1, 9, 2020, 100, 2, '2023-04-25', null, 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (6, 1, 7, 2019, 100, 3, '2023-04-23', null, 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (7, 1, 7, 2018, 50000, 1, '2023-04-22', null, 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (8, 1, 6, 2015, 100, 2, '2023-04-15', 'Dobry den,
potreboval bych opravit odrene dvere na prave strane auta.
dekuji', 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (9, 1, 12, 2022, 40000, 2, '2023-04-14', null, 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (10, 1, 9, 2017, 15000, 3, '2023-04-17', null, 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (11, 2, 2, 2013, 36, 1, '2023-04-23', 'Potrebuju celkovy servis.', 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (12, 2, 4, 2016, 65, 2, '2023-04-23', null, 4);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (13, 1, 11, 2023, 5000, 1, '2023-04-27', 'Dobry den,
potrebovala bych kontrolni servis po koupi auta.
dekuji. ', 8);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (14, 1, 11, 2023, 5000, 1, '2023-04-27', 'Dobry den,
potrebovala bych kontrolni servis po koupi meho auta.
dekuji', 8);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (15, 1, 3, 2021, 40, 2, '2023-04-25', 'Dobry den,
auto je bohuzel ve strome nevim co stim mam delat.
dekuji', 9);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (16, 1, 6, 2013, 19000, 1, '2023-04-24', 'dobry den,
potreboval bych udelat pravidelny servis oleju.
dekuji', 9);
INSERT INTO db_autoservis.objednavky (id, autoservis_id, model_id, rok_vyroby, km, typ, datum, poz, us_id) VALUES (17, 1, 6, 2023, 50000, 3, '2023-04-22', 'leve predni dvere jsou odrene = vymena', 9);
