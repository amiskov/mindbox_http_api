--
-- PostgreSQL database dump
--

-- Dumped from database version 13.8
-- Dumped by pg_dump version 13.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: andreymiskov
--

COPY public.category (id, name) FROM stdin;
1	Мелкая бытовая техника
2	Компьютерная техника
3	Офис и канцелярия
\.


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: andreymiskov
--

COPY public.product (id, name) FROM stdin;
1	Ноутбук Lenovo ThinkPad X270 [X270 20HN0012RT]
2	Материнская плата MSI B250M BAZOOKA PLUS
3	Электрочайник Oursson \t EK1763M
4	Фен Sinbo SHD-7034
5	Ноутбук HP 250 G6 [250G6 1WY51EA]
6	Ноутбук HP 15-bs000 [15-BS019UR 1ZJ85EA]
7	Видеокарта Gigabyte GeForce GTX 1050 GV-N1050WF2OC-2GD
8	Массажер для тела GEZAtone AMG114
9	Ноутбук Dell Inspiron 15 5570 [5570-0054]
10	Ноутбук Dell Latitude 3480 [3480-6126]
11	Монитор Acer G237HLAwi
12	Электродуховка Artel MD 4212 E
13	Электрическая зубная щетка CS Medica Sonic Pulsar CS-131
14	Материнская плата MSI H81M-E33
15	Ноутбук MSI GS70 6QE Stealth Pro [GS70 6QE-265]
16	Швейная машина, оверлок Singer 14SH754
17	Пылесос Samsung SC-432A
18	Микроволновая печь Candy CMXW 22 DS
19	Ноутбук HP 15-bw000 [15-BW071UR 2CN98EA]
20	Антенна для Wi-Fi и 3G Ubiquiti AirMax Sector M-V5G-Ti
21	Швейная машина, оверлок BERNINA B580
22	Пылесос Agressor AGR 140
23	Весы Kromax KS-519
24	Кофемолка Saturn ST-CM1033
25	Весы Tanita HD-394
26	Сумка для ноутбуков Sumdex Impulse Fashion Place Portfolio Brief [Impulse Fashion Place Portfolio Brief 15.4]
27	Антенна для Wi-Fi и 3G Antex PETRA Broad Band 75
28	Фен Redmond RF-524
29	Оперативная память Transcend DDR2 [JM800QLU-2G]
30	Фен Beurer HS80
31	Фен Gamma Piu Rainbow
32	Машинка для стрижки волос Moser 1245-0066
33	Жесткий диск WD RE [WD2004FBYZ]
34	Монитор Sharp PN-80SC5
35	Микроволновая печь LG MS-23M38GIH
36	Ноутбук MSI GP72M 7RDX Leopard [GP72M 7RDX-1239]
37	Блок питания Thermaltake Toughpower DPS [TPG-0850D]
38	Коммутатор Dell X4012
39	Оперативная память Corsair Vengeance RGB DDR4 [CMR32GX4M4A2666C16]
40	Фен Moser 4445-0050
41	Блинница Kromax CM-24
42	Коммутатор Cisco WS-C2960X-48TD-L
43	Электрочайник Tefal KI 760
44	Весы Scarlett SC-KS57P20
45	Система охлаждения Thermaltake CLW0222
46	Кофемолка De'Longhi KG 49
47	Коммутатор HP JG221A
48	Ноутбук Lenovo Ideapad 710S 13 [710S-13ISK 80SW0063RK]
49	Швейная машина, оверлок Toyota ART 20
50	Сумка для ноутбуков Sumdex Passage Computer Brief PON-328 [Passage Computer Brief PON-328 15.6]
\.


--
-- Data for Name: category_product; Type: TABLE DATA; Schema: public; Owner: andreymiskov
--

COPY public.category_product (category_id, product_id) FROM stdin;
2	1
2	2
1	3
1	4
2	5
2	6
2	7
1	8
2	9
2	10
2	11
1	12
1	13
2	14
2	15
1	16
1	17
1	18
2	19
2	20
1	21
1	22
1	23
1	24
1	25
2	26
2	27
1	28
2	29
1	30
1	31
1	32
2	33
2	34
1	35
2	36
2	37
2	38
2	39
1	40
1	41
2	42
1	43
1	44
2	45
1	46
2	47
2	48
1	49
2	50
\.


--
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: andreymiskov
--

SELECT pg_catalog.setval('public.category_id_seq', 6, true);


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: andreymiskov
--

SELECT pg_catalog.setval('public.product_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

