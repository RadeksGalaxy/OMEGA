
create database db_autoservis;
use db_autoservis;

create table auto
(
    id    int auto_increment
        primary key,
    model varchar(50) null
)
    auto_increment = 13;

INSERT INTO db_autoservis.auto (id, model) VALUES (1, 'Fabia');
INSERT INTO db_autoservis.auto (id, model) VALUES (2, 'Fabia Combi');
INSERT INTO db_autoservis.auto (id, model) VALUES (3, 'Scala');
INSERT INTO db_autoservis.auto (id, model) VALUES (4, 'Kamiq');
INSERT INTO db_autoservis.auto (id, model) VALUES (5, 'Octavia');
INSERT INTO db_autoservis.auto (id, model) VALUES (6, 'Octavia Combi');
INSERT INTO db_autoservis.auto (id, model) VALUES (7, 'Karoq');
INSERT INTO db_autoservis.auto (id, model) VALUES (8, 'Kodiaq');
INSERT INTO db_autoservis.auto (id, model) VALUES (9, 'Superb');
INSERT INTO db_autoservis.auto (id, model) VALUES (10, 'Superb Combi');
INSERT INTO db_autoservis.auto (id, model) VALUES (11, 'Enyaq Coupe');
INSERT INTO db_autoservis.auto (id, model) VALUES (12, 'Enyaq');


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
)
    auto_increment = 226;

INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (1, '260-27561', 'AB AUTO BREJLA s.r.o.', 'Vestec u Prahy', 'Automobilová 585', '25242', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/2L3S6YR7YSQJMDDVPPZNNDMMIE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (2, '260-2756A', 'AB AUTO BREJLA s.r.o.', 'Vlašim', 'Vlasákova 1800', '25801', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/2L3S6YR7YSQJMDDVPPZNNDMMIE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (3, '260-30090', 'AD AUTO Praha s.r.o.', 'Praha 4', 'Hornokrčská 2/1947', '14000', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/KELGNVCJZGPNRZDXWJQ6AHXTDQ======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (4, '260-27782', 'ADIV, spol. s r.o.', 'Opava', 'Těšínská 3007/91', '74601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/LZEUCWHEK7PDGJREJWVQHB4OGE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (5, '260-2778B', 'ADIV, spol. s r.o.', 'Ostrava', 'Ruská 2880', '70300', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/LZEUCWHEK7PDGJREJWVQHB4OGE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (6, '260-2742C', 'AGROTEC  a.s.', 'Břeclav', 'Lidická 123', '69002', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/7ZXKN2K2XQH4RYHYZUDWA7J5P4======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (7, '260-27421', 'AGROTEC  a.s.', 'Hustopeče', 'Brněnská 74', '69301', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/7ZXKN2K2XQH4RYHYZUDWA7J5P4======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (8, '260-2742D', 'AGROTEC  a.s.', 'Brno, Modřice', 'Chrlická 1153', '66442', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/7ZXKN2K2XQH4RYHYZUDWA7J5P4======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (9, '260-22128', 'AK auto Kostelec,s.r.o.', 'Kostelec nad Černými Lesy', 'Pražská 1110', '28163', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (10, '260-28860', 'AMOND,  spol. s r.o.', 'Kladno', 'Smečenská 889', '27204', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/RMN6HTSXEFMELATKFS5JPSQNCI======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (11, '260-24139', 'AR SERVIS s.r.o.', 'Jindřichův Hradec', 'Jarošovská 869/II', '37701', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (12, '260-24210', 'ARAVER CZ, s.r.o.', 'Staré Město', 'Zerzavice 2144', '68603', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MKD6IWPTYKKEJN64YVSYV3BB2A======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (13, '260-2421C', 'ARAVER CZ, s.r.o.', 'Vlčnov', 'J. Plesla 556', '68761', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MKD6IWPTYKKEJN64YVSYV3BB2A======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (14, '260-28649', 'AUTO - BAYER, s.r.o.', 'Slavkov u Brna', 'Bučovická 299', '68401', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/TJS2GO255YJ234NCPBJL23KAWY======.PNG', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (15, '260-22951', 'AUTO  DUBINA, a. s.', 'Ostrava - Dubina', 'Horní  3023/122', '70030', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/6S5HO3HGCOAPJQZJHODVNRVBPI======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (16, '260-2303A', 'AUTO - Evžen Myslivec s.r.o.', 'Slaný', 'Pražská 314', '27401', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/33OVYDPAV2KV334FNHHVFEPKMQ======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (17, '260-23035', 'AUTO - Evžen Myslivec s.r.o.', 'Louny', 'Václava Majera 2666', '44001', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/33OVYDPAV2KV334FNHHVFEPKMQ======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (18, '260-2408A', 'Auto - Poly spol. s r.o.', 'Příbram', 'Novohospodská 148', '26101', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/6Y7BNTKTR3YGG7AHX2SWUNSFSQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (19, '260-24082', 'Auto - Poly spol. s r.o.', 'Praha 9', 'Pod Harfou 904/1', '19000', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/6Y7BNTKTR3YGG7AHX2SWUNSFSQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (20, '260-20389', 'AUTO . . .   s.r.o.', 'Žďár nad Sázavou', 'Nádražní 2118/67', '59101', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OQGVLT2S4CFYGNHT2BZCVSZWQ4======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (21, '260-21342', 'Auto Anex s.r.o.', 'Děčín III', 'Žerotínova 378', '40501', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (22, '260-22840', 'AUTO Brandýs n/L. s.r.o.', 'Brandýs nad Labem – Stará Boleslav', 'Rolnická 1928', '25001', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (23, '260-2205B', 'AUTO BRANKA Mělník', 'Mělník', 'Mladoboleslavská 2862', '27601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MEN7JWBPN3AAB6IG3YXR5OBYZA======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (24, '260-2205A', 'AUTO BRANKA Náchod', 'Náchod', 'Českoskalická 1743/I', '54701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MEN7JWBPN3AAB6IG3YXR5OBYZA======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (25, '260-22055', 'AUTO BRANKA Praha', 'Praha 9', 'Prosecká 817/82', '19000', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MEN7JWBPN3AAB6IG3YXR5OBYZA======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (26, '260-20397', 'AUTO CB, spol. s r.o.', 'Plzeň', 'Nepomucká 487/119', '32600', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/6HG6GWHW6ACU6WHK3VG5IPZVMA======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (27, '260-2039A', 'AUTO CB, spol. s r.o.', 'Přeštice', 'Tř. 1. máje 849', '33401', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/6HG6GWHW6ACU6WHK3VG5IPZVMA======.png', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (28, '260-28754', 'AUTO Červený s.r.o.', 'Mariánské Lázně', 'Hlavní 384/142', '35301', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/I2IUIWW7D3MG6N7O2YLRN3QMXQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (29, '260-23671', 'Auto color Design s.r.o.', 'Bruntál', 'Staroměstská 3', '79201', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (30, '260-21407', 'AUTO DOBROVOLNÝ V.M.', 'Jihlava', 'Okružní 4720/3', '58601', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (31, '260-25526', 'AUTO DRYML a.s.', 'Pardubice - Rosice', 'gen. Svobody 658', '53351', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/C3DF55F7SKF47RT3YJIWZZVYCM======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (32, '260-24481', 'AUTO ELSO  s.r.o.', 'Praha 9', 'Cukrovarská 900/10', '19600', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MSZDNTIYWHUWPHKF23CMZEGQLI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (33, '260-2362A', 'Auto Enge a.s.', 'Praha 10', 'U Seřadiště 65/7', '101 00', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/KPDDYERLGNHDDM7QHRRNHVAW7Q======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (34, '260-23621', 'Auto Enge a.s.', 'Liberec 6', 'Hodkovická 747/29', '460 06', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/KPDDYERLGNHDDM7QHRRNHVAW7Q======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (35, '260-22705', 'AUTO GOLDCAR a.s.', 'Praha 10', 'Bohdalecká 1416/12', '10100', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/ZFOFEWFULZWJ4LF2UN7DEW6MKQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (36, '260-20095', 'AUTO GREMOS, spol. s r.o.', 'Liberec 11', 'Zahradní 300', '46001', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/J7SRG34LXW3QSVYCVNRP3PGI24======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (37, '260-29904', 'Auto Hégr, a. s., provozovna Olomouc', 'Olomouc', 'Hněvotínská 658/54a', '77900', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/XSCN3D7G2DGUU334RHKTRGJNNM======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (38, '260-2990A', 'Auto Hégr, a. s., provozovna Šternberk', 'Šternberk', 'Olomoucká 2318/110', '78501', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/XSCN3D7G2DGUU334RHKTRGJNNM======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (39, '260-2990B', 'Auto Hégr, a. s., provozovna Šumperk', 'Šumperk', 'Jesenická 2839/1b', '78701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/XSCN3D7G2DGUU334RHKTRGJNNM======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (40, '260-20575', 'AUTO Hlaváček a.s.', 'Olomouc - Holice', 'Týnecká 669/5', '77900', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/22C2WVAU56LOLGW2MKZBHKGRG4======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (41, '260-2057C', 'AUTO Hlaváček a.s.', 'Litomyšl', 'Nedošín 125', '57001', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/22C2WVAU56LOLGW2MKZBHKGRG4======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (42, '260-24031', 'Auto Hybeš s.r.o.', 'Dřenice', 'Dřenice 122', '53701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/XIGXMRKIK7WCZCYTUQTAUW5MLY======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (43, '260-25910', 'AUTO IN s.r.o.', 'Hradec Králové', 'Kutnohorská 217/3', '50004', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (44, '260-22209', 'Auto Janák s.r.o.', 'Ústí nad Orlicí', 'Královéhradecká 1545', '56201', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (45, '260-2923A', 'AUTO JAROV Kunratice', 'Praha 4', 'Vídeňská 126', '14800', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/HXJHQZTIU7EEPJXYMGZDQRMWEY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (46, '260-29238', 'AUTO JAROV, s.r.o.', 'Praha 3 - Jarov', 'Osiková 2 čp. 2688', '13000', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/LVLCFE4TUXUYQRSQPE45KN4BTE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (47, '260-24589', 'AUTO KÁPL s.r.o.', 'Písek', 'Malé Nepodřice 41', '39701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/WMBTX2RJU5TTQANUIQFXGR6I2Y======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (48, '260-21580', 'AUTO KOUTEK s.r.o.', 'Liberec', 'Tanvaldská 1141', '46311', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/FQV7KPECLVIKJO374E3TI72ARI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (49, '260-24864', 'AUTO KRALUPY a.s.', 'Kralupy nad Vltavou', 'V Růžovém údolí 554', '27801', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/FTEJ2PJMPCHUAYQIGRG3PDIZDM======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (50, '260-20761', 'Auto MERCIA a.s.', 'Chrudim', 'Dašická 1228', '53701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/NRS5ITJSIIOZW3RRVJKOOYSGBQ======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (51, '260-24261', 'AUTO MYSLIVEC  s.r.o.', 'Podbořany', 'Hlubanská 741', '44101', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/3VJELITDEANR4ORVME5KRGKZKM======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (52, '260-25920', 'Auto Palace Spořilov s.r.o.', 'Praha 4', 'Na Chodovci 2457/1', '14100', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/ZA4EIX3GEPDO7IS5CAV3D7BNO4======.JPG', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (53, '260-3020A', 'Auto Palace Západ s.r.o.', 'Praha -Tuchoměřice', 'Ke Kopanině 529', '25267', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/TUFWKQ6NFH2B3CCAHDTRBIGC4A======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (54, '260-30200', 'Auto Palace Západ s.r.o.', 'Karlovy Vary - Dvory', 'Chebská 361/55', '36006', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/TUFWKQ6NFH2B3CCAHDTRBIGC4A======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (55, '260-24279', 'AUTO RACEK  a. s.', 'Havlíčkův Brod', 'Jihlavská 1917', '58001', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/PPFVUTVBSEJFSFEGVYPCBKUPVU======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (56, '260-2427B', 'AUTO RACEK a. s.', 'Pelhřimov', 'Humpolecká 1911', '39301', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/PPFVUTVBSEJFSFEGVYPCBKUPVU======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (57, '260-2427A', 'AUTO RACEK a. s.', 'Humpolec', 'Masarykova 757', '39601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/PPFVUTVBSEJFSFEGVYPCBKUPVU======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (58, '260-22411', 'Auto Sael s.r.o.', 'Chodov', 'Karlovarská 140', '35735', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/R2NH2KBOVGKZQAMWTBX73RM2KM======.png', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (59, '260-2024D', 'AUTO ŠEVČÍK c.z., spol. s r.o.', 'Vodňany', 'Vinařického 961/II', '38901', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OT76WRX7T2PO45QIHX4O5Q475Y======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (60, '260-20249', 'AUTO ŠEVČÍK c.z., spol. s r.o.', 'České Budějovice', 'České Vrbné 2379', '37011', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OT76WRX7T2PO45QIHX4O5Q475Y======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (61, '260-2024A', 'AUTO ŠEVČÍK c.z., spol. s r.o.', 'Prachatice', 'Rožmberská 1219', '38301', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OT76WRX7T2PO45QIHX4O5Q475Y======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (62, '260-2024B', 'AUTO ŠEVČÍK c.z., spol. s r.o.', 'Vimperk', 'Špidrova 119', '385 01', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OT76WRX7T2PO45QIHX4O5Q475Y======.png', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (63, '260-2024E', 'AUTO ŠEVČÍK c.z., spol. s r.o.', 'Strakonice', 'Dopravní 35', '38601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OT76WRX7T2PO45QIHX4O5Q475Y======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (64, '260-25992', 'AUTO ŠÍDLO s.r.o.', 'Horoměřice', 'Únětická 20', '25262', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/4LBZ5CQCCZCQJ4P6BYDQDXGF2M======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (65, '260-28011', 'Auto Štěpánek, a.s.', 'Praha 15 - Hostivař', 'Dolnoměcholupská 1654/10b', '10200', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/XWAXITT4MAHRTWV6ZWCUQP2JJU======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (66, '260-30280', 'Auto Strž CZ a.s.', 'Praha 4', 'Na Strži 35', '14000', 'https://skodak2ngddm.blob.core.windows.net/images/dealer', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (67, '260-25208', 'AUTO STYL  a.s.', 'Praha 5 - Stodůlky', 'Jeremiášova 3/1115', '15000', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/HXWGDK4BSRIPAFODQ6FH5D6ZSY======.JPG', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (68, '260-2431A', 'AUTO TOMAN, s.r.o.', 'Třinec', 'Lidická 166', '73961', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/ESDWNBTUDSG66W446QB3J3GVTQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (69, '260-24317', 'AUTO TOMAN, s.r.o.', 'Havířov', 'Dlouhá třída 1026/65', '73601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/VXVUIUC547TKL6QBK44KA6ABUQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (70, '260-21083', 'AUTO UL a.s.', 'Ústí nad Labem', 'Havířská 373/25', '40010', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/TEB72MZEHONQDXRTDEY73MKEWM======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (71, '260-2025C', 'AUTO VOLF spol. s r.o.', 'Holýšov', 'Jiráskova 646', '34562', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/XYP44JQP2YIJEZP2GVPCUYCOKQ======.PNG', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (72, '260-2025B', 'AUTO VOLF spol. s r.o.', 'Stříbro', 'Plzeňská 1444', '34901', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/XYP44JQP2YIJEZP2GVPCUYCOKQ======.PNG', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (73, '260-20257', 'AUTO VOLF spol. s r.o.', 'Plzeň- Bory', 'Folmavská 2828/6', '30100', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/XYP44JQP2YIJEZP2GVPCUYCOKQ======.PNG', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (74, '260-2004B', 'AUTOCENTRÁLA  s.r.o.', 'Karviná, Fryštát', 'Ostravská 1946/12', '73301', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/6AXYW3VQNZQWKQWYIWLCVTSLF4======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (75, '260-2004A', 'AUTOCENTRÁLA  s.r.o.', 'Ostrava - Třebovice', 'Třebovická 5534', '72200', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/6AXYW3VQNZQWKQWYIWLCVTSLF4======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (76, '260-20044', 'AUTOCENTRÁLA  s.r.o.', 'Hlučín', 'Markvartovická 1906/7', '74801', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/6AXYW3VQNZQWKQWYIWLCVTSLF4======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (77, '260-20176', 'AUTOCENTRUM  TA  a.s.', 'Plzeň', 'Tylova 70', '30100', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/IFUOH2F7XXKWISJ3M522R5KHTY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (78, '260-23299', 'Autocentrum BARTH', 'Pardubice - Dubina', 'Hůrka 1798', '53012', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/YJGF6MAPP3I3EDWEW4TTEIF5VY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (79, '260-2329C', 'Autocentrum BARTH - Hradec Králové', 'Hradec Králové', 'Brněnská 2004', '50006', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/YJGF6MAPP3I3EDWEW4TTEIF5VY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (80, '260-29203', 'AUTOCENTRUM BOURA  spol. s r.o.', 'Činěves  p. Dymokury', 'Činěves 143', '28901', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (81, '260-23361', 'AUTOCENTRUM JAN ŠMUCLER s.r.o.', 'Horšovský Týn', 'Dvořákova 304', '34601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/4C5MKLQQW4WGRQPIGE57WNHV4Q======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (82, '260-2336D', 'AUTOCENTRUM JAN ŠMUCLER s.r.o.', 'Klatovy III', 'Domažlické předměstí 610', '33901', 'https://skodak2ngddm.blob.core.windows.net/images/4c5mklqqw4wgrqpige57wnhv4q%3D%3D%3D%3D%3D%3D', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (83, '260-2336A', 'AUTOCENTRUM JAN ŠMUCLER s.r.o.', 'Plzeň', 'Borská 59', '30100', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/4C5MKLQQW4WGRQPIGE57WNHV4Q======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (84, '260-22850', 'AUTOCENTRUM Jičín s.r.o.', 'Jičín', 'Hradecká 1101', '50601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/UAWUHIDKPCYJMNEJMDZXMTDYNY======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (85, '260-2084A', 'Autocentrum Lukáš s.r.o.', 'Rožnov pod Radhoštěm', 'Meziříčská 2607', '75661', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/IN4Z7GMHSXT7N7WZGMK47Y4ALE======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (86, '260-2084C', 'Autocentrum Lukáš s.r.o.', 'Šenov u Nového Jičína', 'Jeremenkovu 9', '74242', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/IN4Z7GMHSXT7N7WZGMK47Y4ALE======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (87, '260-20842', 'Autocentrum Lukáš s.r.o.', 'Valašské Meziříčí', 'Masarykova 752', '75701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/IN4Z7GMHSXT7N7WZGMK47Y4ALE======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (88, '260-22268', 'AUTOCENTRUM OLOMOUC s.r.o.', 'Olomouc', 'Horní Lán čp. 445/1', '77900', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/HZTIZFHNQQIG3PB67T7ZIN4ACQ======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (89, '260-22713', 'Autocentrum Přerov CZ  s.r.o.', 'Přerov - Předmostí', 'Olomoucká 440/44', '75124', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/YBHJ2J2YNKQYEYIXXGJUXYRCQ4======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (90, '260-24198', 'Autocentrum ROS, a. s', 'Brno', 'Poříčí 1c', '60300', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/3D5HPJ5T25NPV4AB236C26D3PE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (91, '260-22781', 'AUTOCENTRUM VOTICE, s.r.o.', 'Votice', 'Na Bělické louce 756', '25901', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (92, '260-22896', 'AUTODRUŽSTVO  PODBABSKÁ', 'Praha 6', 'Pod Paťankou 217/1', '16000', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/K72YY7CSNQGNCEHA6PQEG6QH2I======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (93, '260-28924', 'Autodružstvo Frýdek - Místek', 'Frýdek - Místek', 'Beskydská 704', '73802', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/N2HE3ER3CNSC7OWSXWBRSM4UXI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (94, '260-2892B', 'Autodružstvo Frýdek - Místek', 'Ostrava - Moravská Ostrava', 'Brandlova 5', '70200', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/N2HE3ER3CNSC7OWSXWBRSM4UXI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (95, '260-2892A', 'Autodružstvo Frýdek - Místek', 'Český Těšín', 'Frýdecká ul.', '73701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/N2HE3ER3CNSC7OWSXWBRSM4UXI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (96, '260-2892C', 'Autodružstvo Frýdek - Místek', 'Ostrava - Přívoz', 'Hlučínská 60', '70200', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/N2HE3ER3CNSC7OWSXWBRSM4UXI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (97, '260-29513', 'AUTODRUŽSTVO ZNOJMO', 'Znojmo', 'Vídeňská třída  2573/43', '66902', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/V2RJDPTTGVFVRCZT4GPDOXK7NA======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (98, '260-28657', 'AutoDům Chomutov  spol. s r.o.', 'Chomutov', 'Spořická 4522', '43000', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (99, '260-27049', 'Autodům Vrána s.r.o.', 'Havířov - Město', 'Železničářů 1492/3', '73601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/TUWYSRE5SRLPVWRDXOBKXVQKHE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (100, '260-24392', 'AUTOKLEVER, spol. s r.o.', 'Nový Jičín', 'Hřbitovní 5', '74101', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MRF57PSOGQ3I35JMMDYN36UTCI======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (101, '260-24180', 'Autokomplex Menčík a.s.', 'Praha 8', 'Korybutova 686/4', '18600', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/WZCZFSGV45PGKDIW2HAOSCHNSU======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (102, '260-2418A', 'Autokomplex Menčík a.s.', 'Benátky nad Jizerou', 'Mladská 713', '29471', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/WZCZFSGV45PGKDIW2HAOSCHNSU======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (103, '260-25429', 'Automechanika, a.s.', 'Prostějov', 'Letecká 3753/2', '79601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/SGJBKR3HP63FXVQQEBUXMU5XDY======.PNG', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (104, '260-30070', 'AUTONORTH VDF s.r.o.', 'Varnsdorf', 'Karlínská 1839', '40747', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/QEFPFO32QSJHWWJ4SKADNRC77Q======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (105, '260-28266', 'AUTONOVA BRNO s.r.o.', 'Brno', 'Masná 418/20, Trnitá', '60200', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/ZFEFIDEERPPA2O6RH5D4GW3GBM======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (106, '260-24066', 'AUTOPLUS II, s.r.o.', 'Most', 'Rudolická 1730', '43401', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/SJLC23HFVUQ3N6CO33A7ONCZGE======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (107, '260-21016', 'AUTOPROFIT s.r.o.', 'Svitavy', 'Mýtní 2', '56802', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (108, '260-27693', 'AUTOS, spol. s r.o.', 'Kunštát', 'Palackého 154', '67972', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/T6BXTZGUJFU27EH2RVJBATW3RU======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (109, '260-28886', 'Autosalon ASTRA a.s.', 'Jablonec nad Nisou', 'Jarní 28', '46601', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (110, '260-20168', 'AUTOSALON F3K, s.r.o.', 'Třebíč', 'Spojovací 1338', '67401', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/SZWRWI2BAB3NTIUIVUECUCCTLE======.PNG', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (111, '260-20826', 'AUTOSALON HORA CZ  a .s.', 'Brno', 'Šťouračova 1b', '63500', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/T7S4F275IHSJTHJKL3FTOYX5HQ======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (112, '260-24503', 'Autosalon Klokočka Centrum a.s.', 'Praha 6', 'Karlovarská 660/117', '16300', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OVHM72IUVSZ4MZ23WAUPECBOHU======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (113, '260-2450B', 'Autosalon Klokočka Centrum a.s.', 'Praha 5 - Barrandov', 'Borského 1/989', '15200', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (114, '260-29327', 'AUTOSALON KUDRNA s.r.o.', 'Orlová- Poruba', 'Příčná 1215', '73514', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/I6CD5SSLYWVYX7MH25J2U7SVO4======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (115, '260-29971', 'AUTOSERVIS JINDRA s.r.o.', 'Soběslav', 'Mrázkova 801/III', '39201', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/NIF7UXF5N6OJK7KSBLJQ6UWWGI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (116, '260-29181', 'AUTOSERVIS NEDVĚD, s.r.o.', 'Plzeň - Černice', 'Štefanikova 104', '32600', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/GMOTOT5JSF3OWSVA6YPWJ5KHLQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (117, '260-26379', 'AUTOSERVIS NOVOTNÝ spol. s r.o.', 'Týn nad Vltavou', 'Táborská 568', '37501', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/7X34WORSWYIEBCWMY3WJEZP25E======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (118, '260-27707', 'AUTOSERVIS spol. s r.o.', 'Vysoké Mýto', 'Slunečná 76/II', '56601', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (119, '260-29149', 'Autoservis Šrachta s.r.o.', 'Strakonice', 'Písecká 513', '38601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/6FMSGIWR2DPBC6HPTQVSSC4HXM======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (120, '260-27260', 'AUTOSHOP PAULUS, spol. s r.o.', 'Kroměříž', 'Hulínská 3221', '76701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/VGVH75LETACLWLETNUOV3QV5FU======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (121, '260-28029', 'AUTOspektrum 2000 - Mariánské Lázně', 'Mariánské Lázně', 'Plzeňská 608/17', '35301', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/N4H4SEVU35LRYR36HYA7YYK3KA======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (122, '260-24601', 'AUTO-SPEKTRUM -ACC, spol. s r.o.', 'Brno- Slatina', 'Hviezdoslavova 3', '62700', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/EJORFBM3WTBN7NMKBOLKESBQ4Y======.png', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (123, '260-2802A', 'AUTOspektrum2000 - Cheb', 'Cheb', 'Truhlářská 2061/11', '35002', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/N4H4SEVU35LRYR36HYA7YYK3KA======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (124, '260-27081', 'AUTOSPOL PLUS spol. s r.o.', 'Horažďovice', 'Strakonická 366', '34101', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (125, '260-28606', 'AUTOSPOL, s.r.o.', 'Boskovice', 'nám.9.května 1', '68001', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/4PGTNS7UK3XB2ZH7GA4B2MKWAE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (126, '260-30180', 'AUTOSPORT KUČERA s.r.o.', 'Liberec', 'Kunratická 1145', '46015', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/422NDGNZMJJNR62TXOKGG372YI======.JPG', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (127, '260-28673', 'Autostop, spol. s r.o.', 'Rakovník', 'Luženská 1992', '26901', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/GQNSJ7UDEC3DKAWJADOFFJSRJE======.JPG', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (128, '260-28231', 'AUTOSTYL a.s.', 'Trutnov', 'Horská 579', '54101', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/BUSMTSJ6F5332ZEOZ43W3F5POU======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (129, '260-28380', 'AUTOTREND, spol. s r.o.', 'Liberec 25', 'ul. České mládeže 1101', '46312', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (130, '260-20834', 'AUTOTRIO Praha, s.r.o.', 'Praha 4', 'Vzpoury 3', '14300', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/IIRQDHPE6K5TYKZEQ6XN2NNYMA======.jpeg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (131, '260-28975', 'AUTOZÍTKA s.r.o.', 'Sukorady', 'Martinovice 31', '29406', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/D2WZKJGUJW6KLWWKNVULDFAR3E======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (132, '260-25518', 'AZ SERVIS, a.s.', 'Brno', 'Pražákova 1008/69', '63900', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/KLRBAPXAWNOHNJ2THE52TMGZHY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (133, '260-28291', 'BENO ŘÍČANY, s.r.o.', 'Říčany u Prahy', 'Říčanská 1818', '25101', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (134, '260-2235C', 'CAR POINT s.r.o.', 'Domažlice', 'Masarykova 570', '34401', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (135, '260-2264A', 'CB Auto a.s.', 'Český Krumlov', 'Budějovická 166', '38101', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OKC7RI2IZHC3FGXXNHYFLJ23PE======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (136, '260-2264B', 'CB Auto a.s.', 'Tábor', 'Soběslavská 2985', '39005', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OKC7RI2IZHC3FGXXNHYFLJ23PE======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (137, '260-22641', 'CB Auto a.s.', 'České Budějovice', 'Dr. Milady Horákové 1477', '37005', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OKC7RI2IZHC3FGXXNHYFLJ23PE======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (138, '260-21415', 'Daníček, s.r.o.', 'Zlín', 'Vizovická 423', '76001', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (139, '260-20150', 'DOBE CAR  s.r.o.', 'Holešov', 'Tovární 1250', '76901', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/Z7YDLS37AIJKAWQHRRMAZI42WE======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (140, '260-3019B', 'DRUPOL autodružstvo', 'Beroun', 'Na Parkáně 367/14', '26601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/CLD2Z2B4E34XX3QVVU2G6OJJBI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (141, '260-3019A', 'DRUPOL autodružstvo', 'Příbram', 'Milínská 30', '26101', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/QWH6CI3ILSCUYMDVZIFZW4BJZQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (142, '260-30190', 'DRUPOL autodružstvo', 'Zdice', 'Komenského 947', '26751', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/QWH6CI3ILSCUYMDVZIFZW4BJZQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (143, '260-23965', 'EURO CAR Zlín s.r.o.', 'Zlín', 'VIZOVICKÁ 4097', '76001', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (144, '260-24571', 'FEMAT Radotín s.r.o.', 'Praha 5 - Radotín - Autosalon ', 'Výpadová 2313', '153 00', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/ROJ4YJZJSXLDP4SVPQLJT7GOQ4======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (145, '260-22535', 'FORTEX - AGS a.s.', 'Šumperk', 'Jílová 1550/1', '78792', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (146, '260-2885A', 'Gerhard Horejsek a spol., s.r.o.', 'Česká Lípa - Česká ul.', 'Česká 2725', '47001', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (147, '260-2885C', 'Gerhard Horejsek a spol., s.r.o.', 'Litoměřice', 'U terezínské křižovatky 164', '41201', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (148, '260-2885E', 'Gerhard Horejsek a spol., s.r.o.', 'Česká Lípa - Sluneční ul.', 'Sluneční 3115', '47001', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (149, '260-2885F', 'Gerhard Horejsek a spol., s.r.o.', 'Jablonec nad Nisou', 'Palackého čp. 4530/94', '46604', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (150, '260-2885B', 'Gerhard Horejsek a spol., s.r.o.', 'Roudnice nad Labem', 'Žižkova ul.2492', '41301', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (151, '260-28851', 'Gerhard Horejsek a spol., s.r.o.', 'Děčín I. - St- Město', 'Oblouková 1416/19', '40502', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (152, '260-29459', 'HAVEX-auto s.r.o.', 'Vrchlabí', 'Na Bělidle 503', '54301', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/EZHEUGMA7QKBAFRO2MO2TCBAFY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (153, '260-2945F', 'HAVEX-auto s.r.o.', 'Chlumec nad Cidlinou', 'Pražská 792/IV', '50351', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/EZHEUGMA7QKBAFRO2MO2TCBAFY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (154, '260-2945H', 'HAVEX-auto s.r.o.', 'Praha 8 ', 'Lodžská 814/24a', '181 00', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/EZHEUGMA7QKBAFRO2MO2TCBAFY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (155, '260-2945G', 'HAVEX-auto s.r.o.', 'Praha 7 - Holešovice', 'Jateční 41', '17000', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/EZHEUGMA7QKBAFRO2MO2TCBAFY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (156, '260-2945D', 'HAVEX-auto s.r.o.', 'Nová Paka', 'Pražská 1825', '50901', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/EZHEUGMA7QKBAFRO2MO2TCBAFY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (157, '260-2945E', 'HAVEX-auto s.r.o.', 'Kosmonosy', 'Průmyslová 909', '29306', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/EZHEUGMA7QKBAFRO2MO2TCBAFY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (158, '260-27189', 'Horácké autodružstvo', 'Třebíč', 'Brněnská 123', '67401', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/QTCHROHS73EWC56IQZZCTPFOTA======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (159, '260-25232', 'Horácké autodružstvo', 'Velké Meziříčí', 'K novému nádraží 1345', '59401', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (160, '260-21482', 'INPRO Čáslav, s.r.o.', 'Čáslav', 'Jeníkovská 1815', '28601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/ZENRAS2QUYAKWP4U6O7GOM7CFY======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (161, '260-24538', 'IVACAR 2000, a.s.', 'Ivančice', 'Krumlovská 30', '66491', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/LY7GOKYMF77F2ZU777LKVPJSZE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (162, '260-20265', 'Jaroslav Tichý - AUTO TICHÝ', 'Lysá nad Labem', 'Ke Vrutici 1730', '28922', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/7TIWWKBRSOTYLFAMM2QOKVVBSM======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (163, '260-29688', 'JE & NE, spol. s r.o.', 'Brno - Komín', 'Branka 36', '62400', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/SUEL5YNPR7XKZ7PQAKBIOK57DU======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (164, '260-20583', 'K.E.I. GROUP, s.r.o.', 'Brno', 'Žarošická 21', '62800', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/W62IG2HSQQ6BIV6KFAZR4NWEM4======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (165, '260-28592', 'Karel Frolík - AUTOSERVIS', 'Písek', 'Táborská 2400', '39701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OIT6XHOUQFETSXPNIV4MQHVAVA======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (166, '260-21997', 'KARIREAL a.s.', 'Třinec', 'Frýdecká 272', '73961', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/IYHZDDJVFCEEVS5VSF76G6PMVI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (167, '260-2199A', 'KARIREAL a.s.', 'Oldřichovice', 'Oldřichovice 793', '73961', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/IYHZDDJVFCEEVS5VSF76G6PMVI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (168, '260-21059', 'KONTAKT - služby motoristům, spol. s r.o.', 'Turnov', 'Svobodova 2050', '51101', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (169, '260-29050', 'LAURETA AUTO  a.s.', 'Mladá Boleslav', 'Nádražní 307', '29301', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/KDTLWU5V4ZUDSOAZ3DZUXSE7VY======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (170, '260-27316', 'Libor Suchý, autoprodejna', 'Nový Šaldorf-Sedlešovice', 'Dlouhá 81', '67181', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/QUFBKPK6FWJNGKPNUPS3EO54A4======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (171, '260-2594A', 'Louda Auto a.s.', 'Pardubice - Hradecká', 'Hradecká 555', '53009', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/USHXCSYRZWAYLFXSZWYZOOTVQA======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (172, '260-2594G', 'Louda Auto a.s.', 'Teplice', 'Dvořákova 83', '41510', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (173, '260-2594I', 'Louda Auto a.s.', 'Svitavy', 'Dimitrovova 2', '56802', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/USHXCSYRZWAYLFXSZWYZOOTVQA======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (174, '260-2594E', 'Louda Auto a.s.', 'Kolín IV.', 'Havlíčkova ul. 158', '28002', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/USHXCSYRZWAYLFXSZWYZOOTVQA======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (175, '260-2594M', 'Louda Auto a.s.', 'Jihlava', 'Znojemská 4461/86a', '58601', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (176, '260-2594J', 'Louda Auto a.s.', 'Brno', 'Hněvkovského 603/81', '61700', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/4MW3Z7VGW5AT7MFDM7LUDFB76E======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (177, '260-2594H', 'Louda Auto a.s.', 'Praha 9', 'Kolbenova 898/37a', '19800', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/USHXCSYRZWAYLFXSZWYZOOTVQA======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (178, '260-2594C', 'Louda Auto a.s.', 'Pardubice - Teplého', 'Teplého', '53002', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/USHXCSYRZWAYLFXSZWYZOOTVQA======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (179, '260-25941', 'Louda Auto a.s.', 'Poděbrady', 'Choťánky 166', '29001', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/USHXCSYRZWAYLFXSZWYZOOTVQA======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (180, '260-31050', 'Lumír  Tvarůžka AUTOMOTOR s.r.o.', 'Čavisov', 'Chrudimská 92', '74766', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (181, '260-24767', 'MAGNUM CAR, a.s.', 'Vyškov', 'Brněnská 37/444', '68201', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/XEBMD2NWLODBUS4JXNYFEPJPSM======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (182, '260-2896C', 'Manfred Schöner - AUTOSERVIS', 'Karlovy Vary', 'Jáchymovská 53', '36004', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/CXAT6MJDRWMR7UAA2XJYMHVU3A======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (183, '260-2896A', 'Manfred Schöner - AUTOSERVIS', 'Karlovy Vary - Tašovice', 'Česká 225', '36018', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/CXAT6MJDRWMR7UAA2XJYMHVU3A======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (184, '260-28967', 'Manfred Schöner - AUTOSERVIS', 'Sokolov', 'Křižíkova 1624', '35605', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/CXAT6MJDRWMR7UAA2XJYMHVU3A======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (185, '260-2896B', 'Manfred Schöner - AUTOSERVIS', 'Cheb', 'Pražská 159/50', '35002', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/CXAT6MJDRWMR7UAA2XJYMHVU3A======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (186, '260-21881', 'MATRIX a.s.', 'Rychnov nad Kněžnou', 'Lipovka 142', '51601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/YDUH43I2URCQTJM65CDRKQRBFA======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (187, '260-21768', 'Mototechna Servis s.r.o.', 'Praha 8 - Kobylisy', 'Dopraváků 723', '18400', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (188, '260-28932', 'NH Car, s.r.o. ', 'Praha 9 - Černý Most', 'Broumarská čp. 1503', '19800', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/365WXPDHJ25SVE3IKPDWATY3DY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (189, '260-2893A', 'NH Car, s.r.o. ', 'Praha 6 - Strahov', 'Chodecká 2341/2', '16900', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/365WXPDHJ25SVE3IKPDWATY3DY======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (190, '260-2286B', 'OKIM spol. s r.o.', 'Louny', 'ul. 5. Května 2645', '44001', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MVZAQDYYXCDTU7MLF5BKU6LKJQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (191, '260-2286A', 'OKIM spol. s r.o.', 'Lovosice', 'Terezínská 1119', '41002', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MVZAQDYYXCDTU7MLF5BKU6LKJQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (192, '260-22861', 'OKIM spol. s r.o.', 'Ústí nad Labem', 'Masarykova 1028', '40001', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MVZAQDYYXCDTU7MLF5BKU6LKJQ======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (193, '260-20273', 'Olfin Car Palace, s.r.o.', 'Hradec Králové', 'Na Rybárně 203/5', '50002', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/WE7TIHNLBB3DCXI52LCGQSCZRA======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (194, '260-30240', 'OLFIN Car s.r.o.', 'Hradec Králové', 'Na Rybárně 1670', '50002', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/AJLGL3Y7SJTQ6PHXE3CCI7O7XM======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (195, '260-27898', 'Porsche Inter Auto CZ spol.  s.r.o., o.z. Auto Heller Ostrava', 'Ostrava  - Moravská Ostrava', 'Cihelní 3160/49b', '70200', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/GFFCFKXCDNJXJGAKLHKA3QSYCE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (196, '260-21636', 'Porsche Inter Auto CZ spol. s r. o. - Porsche Olomouc ', 'Olomouc', 'Kafkova 474/1', '77900', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/2JONQHE7CZLZJTBTNCNBAXPY2U======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (197, '260-22675', 'Porsche Inter Auto CZ spol. s r.o.', 'Praha 8', 'Liberecká 12', '18200', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/XU3V6HHLOWOJHZN45WOQ62JXCA======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (198, '260-22756', 'Porsche Inter Auto CZ spol. s r.o.', 'Plzeň - Borská pole', 'Podnikatelská 1', '30100', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/WHRDIRQS4S42U7KRI225ES5DV4======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (199, '260-21270', 'Porsche Inter Auto CZ spol. s r.o.', 'Hradec Králové', 'Na Okrouhlíku 1708/25b', '50002', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/VF5HZNHQ4YNCON2CZXULNSBR7A======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (200, '260-23841', 'Porsche Inter Auto CZ spol. s r.o.', 'České Budějovice 3', 'Okružní ulice 2557', '370 04', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/SUCKYMEOC4WSE54MLYGCAKFRLE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (201, '260-29440', 'Porsche Inter Auto CZ spol. s r.o., o.z. Auto Heller Opava', 'Opava - Jaktař', 'Bruntálská 7', '74707', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/GFFCFKXCDNJXJGAKLHKA3QSYCE======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (202, '260-23256', 'Porsche Inter Auto CZ, spol. s r.o. - Porsche Brno', 'Brno', 'Řipská 13a', '62700', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/BMFZ3NOPAD4BZ3MOPVRBHPGYXI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (203, '260-20745', 'Porsche Inter Auto CZ, spol. s r.o. - Porsche Praha-Smíchov', 'Praha 5', 'Vrchlického 31/18', '15000', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (204, '260-24376', 'PP AUTOCENTRUM s.r.o.', 'Hranice 1 - Město', 'Tř. 1. máje 328', '75301', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/UUG2MKKRVME4KPOLNGB652UWBU======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (205, '260-27570', 'Přerost a Švorc - auto, s.r.o.', 'Praha 6', 'Veleslavínská 39', '16200', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/UY3BEBQ5JCRGGW4ZZYCUQ2UCMI======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (206, '260-20711', 'Prima, komanditní společnost', 'Kroměříž', 'Velehradská 4260', '76701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/TGQVKREKCQUYGAL32F2KPXWCXQ======.png', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (207, '260-21121', 'PROFI AUTO SERVIS s.r.o.', 'Praha 4', 'Holušická 2253/1', '148 00', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (208, '260-23167', 'PV-AUTO spol. s r.o.', 'Prostějov', 'Brněnská 108', '79601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/MM2EWKIW625T3YI3PWK3GPRT5E======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (209, '260-22021', 'RT TORAX,  s.r.o.', 'Ostrava - Svinov', ' Sjízdná 2', '721 00', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (210, '260-2768A', 'SAMOHÝL MOTOR a.s.', 'Vsetín', 'Štěpánská 383', '75501', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/ON4ZLZPCPXZ4XONOXWYSB4AQ2Y======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (211, '260-27685', 'SAMOHÝL MOTOR a.s.', 'Zlín', 'tř. T. Bati 642', '76302', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/ON4ZLZPCPXZ4XONOXWYSB4AQ2Y======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (212, '260-2768B', 'SAMOHÝL MOTOR a.s.', 'Olomouc', 'Kosmonautů  846/2', '77900', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/ON4ZLZPCPXZ4XONOXWYSB4AQ2Y======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (213, '260-21610', 'Servis AUTO OPAT s.r.o.', 'Nupaky', 'Komerční zóna Nupaky č.p. 467', '25101', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/4E2ND5IQEPVAQDGV37WLABATBE======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (214, '260-2161A', 'Servis AUTO OPAT s.r.o.', 'Praha 2', 'Legerova 1853/24', '12000', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/4E2ND5IQEPVAQDGV37WLABATBE======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (215, '260-25216', 'ŠKODA Servisní centrum', 'Kosmonosy', 'Boleslavská 366', '29306', null, 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (216, '260-22616', 'TOP AUTOSALON BLANSKO s.r.o.', 'Blansko', 'Svitavská 2329', '67801', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/OXXIZXIXVNDL2SMG2GY5BVCVUM======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (217, '260-27073', 'TUkas ČSAO a.s.', 'Praha 10', 'Černokostelecká 144/565', '10834', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/QSPN7ALLYBEZZBPY32LJHAHXRM======.jpg', 0, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (218, '260-27162', 'TUkas, a.s.', 'Praha 10', 'K Hrušovu 344/6', '10200', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/QSPN7ALLYBEZZBPY32LJHAHXRM======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (219, '260-2716B', 'TUkas, a.s.', 'Praha 4', 'K Vltavě 1911/33', '143 00', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/QSPN7ALLYBEZZBPY32LJHAHXRM======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (220, '260-25178', 'UNICAR, spol. s r.o.', 'Ostrava', 'Vítkovická 2744/36', '70200', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/PONK7ZGKD5VMZAGFKGSR5ZXPT4======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (221, '260-21172', 'UNIKOM, a.s.', 'Kutná Hora', 'Hrnčířská 214', '28401', null, 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (222, '260-30000', 'V-Auto Žebrák s.r.o.', 'Žebrák', 'Tovární 502', '26753', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/JEUYRD7Y3YTBVGDGP54XNELS7A======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (223, '260-24074', 'Verold Benešov, spol. s r.o.', 'Benešov', 'Červené Vršky 1490', '25601', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/L7Y3CGMAEXSJ6JTEBLTERSUC4Y======.png', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (224, '260-22969', 'VISTA car', 'Hodonín', 'Brněnská 3955', '69501', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/QCWRUV2U7YNQ76LKBWDQTJUDUU======.jpg', 1, 1);
INSERT INTO db_autoservis.autoservisy (id, global_id, nazev, mesto, ulice, psc, logo, prodejAut, servisAut) VALUES (225, '260-2296A', 'VISTA car', 'Kyjov', 'Strážovská 958', '69701', 'https://downloadportal.blob.core.windows.net/k2ngtools/Images/QCWRUV2U7YNQ76LKBWDQTJUDUU======.jpg', 0, 1);


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
INSERT INTO db_autoservis.odpoved (id, obj_id, datum, cas, delka, poz, odpoved, casPred) VALUES (5, 15, '2023-04-25', '10:00:00', '0', 'ani sem nejezdete. :)', 1, '09:00:00');


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

