create table zam
(
    id         int auto_increment
        primary key,
    autoser_id int          null,
    nazev      varchar(255) null,
    heslo      varchar(255) null,
    constraint autoser_fk
        foreign key (autoser_id) references autoservisy (id)
)
    auto_increment = 7;

INSERT INTO db_autoservis.zam (id, autoser_id, nazev, heslo) VALUES (1, 1, 'novak', '64118260ecb916c23621d8f2768d8dc75d1f5710b1b7e4f2c41ad41e6bc4d688');
INSERT INTO db_autoservis.zam (id, autoser_id, nazev, heslo) VALUES (2, 1, 'koblic', '3753909314524a923b907ad20fcd7a99c606070460ccf60aa2ca4ce821998f9c');
INSERT INTO db_autoservis.zam (id, autoser_id, nazev, heslo) VALUES (3, 2, 'stajny', '728c0d217646a0f13d4ede301f8a83b063cea6df37a5bb15a71116fc8e113fa4');
INSERT INTO db_autoservis.zam (id, autoser_id, nazev, heslo) VALUES (4, 1, 'sroub', '774f7e6bd8bbfb4ae94553fe91d79f97427f2d71cf159abd9af33f7fd51ad255');
INSERT INTO db_autoservis.zam (id, autoser_id, nazev, heslo) VALUES (5, 2, 'koblic', '01d668cad5609aa2c85bb58b93e190349f5d5446a79842c87d897d9e14e5d25c');
INSERT INTO db_autoservis.zam (id, autoser_id, nazev, heslo) VALUES (6, 1, 'hrouza', 'fa2c936e2d1efdedec1698aeaf1cfbf2263bb12743941331a8746e9acea8f577');
