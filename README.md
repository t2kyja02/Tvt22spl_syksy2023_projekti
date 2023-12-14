# Tvt22spl_syksy2023_projekti

Käyttäen nRF5340 Development Kittiä mittaamme kiihtyvyysanturin dataa ja välitämme tiedon langattomasti Raspberry Pi:lle. Raspberry välittää dataa Oamkin MySQL-palvelimelle.

Tietokantaan tallentuvaan dataan on TCP-sokettirajapinta ja yksinkertainen HTTP API. Kerättyä dataa haetaan HTTP-rajapinnasta omaan kannettavaan koodatulla ohjelmalla ja käsitellään koneoppimistarkoituksiin.

# Käytetyt/tehdyt ohjelmat
1) nRF5340 ohjelma, joka lukee kiihtyvyysanturin dataa ja lähettää sen serial terminaaliin ja bluetoothin yli. (Bluetooth kansio)
2) Python ohjelma, joka lukee tietokannasta dataa ja kirjoittaa sen tiedostoon. (Kolme eri toteutusta löytyy python kansiosta ja yksi toteutus on kmeans kansiossa.)
3) Python ohjelma, johon on toteutettu K-means algoritmi. (kmeans kansio)
4) nRF5340 ohjelma, johon on toteutettu konfuusiomatriisi mittaamaan kmeans algoritmin suorituskykyä. (kansio TL_Project_Week6)

## Arkkitehtuurikuva
![image](https://github.com/t2kyja02/Tvt22spl_syksy2023_projekti/assets/123270538/c3011663-6fa1-4914-803f-0ec7d58638c5 "Arkkitehtuurikuva")

## Kmeans algoritmi
Kmeans algoritmin tarkoitus on opettaa satunnaisesti valittuja pisteitä liikkumaan kuuden data klusterin keskiarvon sijaintiin (ks. kuva alla). Vasemalla näkyy vihreinä palloina mitatun datan sijainti ja mustina palloina satunnaisesti valittujen pisteiden viimeinen sijainti (klusterien sisällä) ja oikealla pisteiden etäisyyden virheen suppeneminen.
![Figure_1](https://github.com/t2kyja02/Tvt22spl_syksy2023_projekti/assets/123270538/8558bf2c-75f1-4281-828a-6f7fff6686e4 "Kmeans plot")

## Konfuusiomatriisi
Konfuusiomatriisin tarkoitus on kuvata koneoppimisen tarkkuutta/suorituskykyä (kuinka moni sadasta keksitystä datapisteestä on lähimpänä opetettuja pisteitä). Tässä tapauksessa pitäisi näkyä viistossa kuusi "100" numeroa (ks. kuva alla).

![confusion](https://github.com/t2kyja02/Tvt22spl_syksy2023_projekti/assets/123270538/ee2bdd88-7764-429b-ab7b-2fca3cf907e0 "Konfuusiomatriisi")

Linux-kokeilut/nettisivu asiat löytyy linux-kokeilut haarasta.
