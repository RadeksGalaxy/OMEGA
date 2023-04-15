create table odpoved
(
    id      int auto_increment
        primary key,
    obj_id  int           null,
    datum   date          null,
    cas     time          null,
    delka   varchar(20)   null,
    poz     varchar(1024) null,
    odpoved int           null comment '1=potvrzene || 2=zruseno',
    casPred time          null comment 'cas zacatku servisu',
    constraint obj_fk
        foreign key (obj_id) references objednavky (id)
)
    auto_increment = 6;

INSERT INTO db_autoservis.odpoved (id, obj_id, datum, cas, delka, poz, odpoved, casPred) VALUES (1, 4, '2023-04-20', '10:00:00', '1', 'je potreba podrobnejsi informace. Vytvorte novou objednavku s lepsimm popisem nebo telefonicky dle id objednavky.
dekuji', 1, '08:00:00');
INSERT INTO db_autoservis.odpoved (id, obj_id, datum, cas, delka, poz, odpoved, casPred) VALUES (2, 6, '2023-04-27', '11:00:00', '1', 'oprava predniho narazniku.', 2, '09:00:00');
INSERT INTO db_autoservis.odpoved (id, obj_id, datum, cas, delka, poz, odpoved, casPred) VALUES (3, 13, '2023-04-27', '09:00:00', '1', null, 2, '07:00:00');
INSERT INTO db_autoservis.odpoved (id, obj_id, datum, cas, delka, poz, odpoved, casPred) VALUES (4, 14, '2023-04-27', '10:00:00', '1', 'ok', null, '08:00:00');
INSERT INTO db_autoservis.odpoved (id, obj_id, datum, cas, delka, poz, odpoved, casPred) VALUES (5, 15, '2023-04-25', '10:00:00', '0', 'ani sem nejezdete. :}', 1, '09:00:00');
