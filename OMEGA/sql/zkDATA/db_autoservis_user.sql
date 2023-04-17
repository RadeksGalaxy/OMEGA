create table user
(
    id       int auto_increment
        primary key,
    jmeno    varchar(30)  null,
    prijmeni varchar(30)  null,
    usjmeno  varchar(30)  null,
    email    varchar(124) null,
    heslo    varchar(255) null
)
    auto_increment = 10;

INSERT INTO db_autoservis.user (id, jmeno, prijmeni, usjmeno, email, heslo) VALUES (1, 'Radek', 'Koblic', 'radekBorec12', 'koblic@spsejecna.cz', '08e795977b1fbd776f9f27ac44884c40471987df13ade40d90b922efb0c06c6a');
INSERT INTO db_autoservis.user (id, jmeno, prijmeni, usjmeno, email, heslo) VALUES (2, 'Honza', 'Karel', 'honzakarlik', 'karel@spsejecna.cz', 'd0f33413465cdef5f979ae170f6df775dbbdcafbee63ad5dc646eb41a0550a22');
INSERT INTO db_autoservis.user (id, jmeno, prijmeni, usjmeno, email, heslo) VALUES (3, 'Pavel', 'Velky', 'pavelVelky', 'velky@spsejecna.cz', 'e103446a4069a87a124940388f3886c85beae189fb44b553f4451ac1840c68ab');
INSERT INTO db_autoservis.user (id, jmeno, prijmeni, usjmeno, email, heslo) VALUES (4, 'Student', 'Student', 'zsStudent', 'student@spsejecna.cz', 'b13712428800d6a2b03aa8d5edf49dd343f6ab75beb1ca759b2a3af9ca666679');
INSERT INTO db_autoservis.user (id, jmeno, prijmeni, usjmeno, email, heslo) VALUES (5, 'Petr', 'Holada', 'ahojjakjj', 'petr@spsejecna.cz', 'd8b404762e2b50aafaf78acd58284896ff5ffc89834f80e376529637e46553f3');
INSERT INTO db_autoservis.user (id, jmeno, prijmeni, usjmeno, email, heslo) VALUES (6, 'Matej', 'Kolar', 'zkurvysyn', 'kolar@spsejecna.cz', 'bec06f453fda703a16a4f5f5b9bc5f5cdb6479e65248e8b91e806a8e2048608c');
INSERT INTO db_autoservis.user (id, jmeno, prijmeni, usjmeno, email, heslo) VALUES (7, 'Kolar', 'Kolarovic', 'radegast', 'kolar3@spsejecna.cz', 'b7fd817eb80c6f351be98413c88941a1dfac7babce99afa6d24ccdedf2685f5b');
INSERT INTO db_autoservis.user (id, jmeno, prijmeni, usjmeno, email, heslo) VALUES (8, 'Eliska', 'Horska', 'EliskaHorska32', 'eliska@gmail.com', 'c3dda77ad9d4da71c6f8de9cf5fcd91b0ed2db188045d3c7e48d010cd5b15ce8');
INSERT INTO db_autoservis.user (id, jmeno, prijmeni, usjmeno, email, heslo) VALUES (9, 'Karel', 'Ondrka', 'karalOnrka25', 'ondrka@gmail.com', 'b86a11d882f3067c4ddb03b601396902e2e1ec2d8f79e5ec89ffa72afbf0be7a');
