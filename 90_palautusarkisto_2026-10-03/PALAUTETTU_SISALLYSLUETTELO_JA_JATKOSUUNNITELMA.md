# Palautettu sisällysluettelo ja turvallinen jatkosuunnitelma

Päiväys: 3.10.2026

Tämä tiedosto on kartta tulevaa uudelleenrakentamista varten. Se ei korvaa `MASTER.md`-tiedostoa eikä muuta mitään alkuperäistä lähdettä.

## Keskeinen havainto

Palautetun kokonaisen v9-version ja GitHubin nykyisen `main`-haaran `MASTER.md`-tiedoston päälukurakenne on sama: molemmissa ovat luvut 1–26, liitteet A–D ja kirjan loppuosat. Mahdollinen katoaminen tai suunnan muuttuminen on siksi tutkittava lukujen sisältä kappale- ja tekstijaksotasolla. Pelkkä sisällysluettelon vertailu ei riitä.

## Palautettu sisällysluettelo

### Alkuosa

1. Lukijalle
2. Alkusanat
3. Johdanto
4. Raakaruokinnan eri suuntaukset
5. Mitä raakaruokinta tässä kirjassa tarkoittaa

### Biologinen perusta

1. Koira on petoeläintaustainen, ravitsemuksellisesti joustava eläin
2. Raaka, kypsennetty ja ekstrudoitu ruoka – mitä käsittely muuttaa?

### Ruokavalion rakentaminen ja raaka-aineet

3. Pelkkä liha ei riitä
4. Kuinka paljon koiralle annetaan ruokaa?
5. Siirtyminen raakaruokintaan
6. Lihalajien valinta
7. Luut ja kalsium
8. Sisäelimet
9. Rasva ja rasvahapot
10. Hiilihydraatit, kasvikset ja kuitu
11. Vitamiinit, kivennäiset ja lisäravinteet
12. Kala ja merenelävät
13. Hygienia ja mikrobiologinen turvallisuus
14. Mahahappo, ruoansulatus ja suolistomikrobisto

### Elämänvaiheet, oireet ja erityistilanteet

15. Pennut, tiineys ja imetys
16. Seniorikoira
17. Pieni, suuri ja aktiivinen koira
18. Allergiat, iho, korvat ja ruoansulatusoireet
19. Raakaruokinta sairauden aikana
20. Riista
21. Tavallisimmat virheet

### Käytännön toteutus ja tulevaisuus

22. Ruokintasuunnitelman rakentaminen
23. Ruokintarutiini
24. Koiran seuraaminen
25. Mitä tutkimus voi kertoa?
26. Raakaruokinnan tulevaisuus

### Liitteet ja loppuosa

- Liite A: Usein kysytyt kysymykset
- Liite B: Malliviikot
- Liite C: Laskenta- ja seurantalomakkeet
- Liite D: Sanasto
- Loppusanat
- Lähteet
- Asiahakemisto
- Omistuskirjoitus
- Kiitokset
- Kirjoittajasta
- Tietoa tästä kirjasta
- Lähteiden käyttö
- Tekijänoikeussivu
- Takakansiteksti, pitkä versio
- Takakansiteksti, lyhyt versio
- Viimeinen sivu

## Lähdekerrokset, joita ei saa korvata

### A. Alkuperäiset kokonaiset kirjaversiot

- työmaster 8.8.2026
- kokonaiset versiot v4, v5, v6, v7, v8 ja v9
- Drive-varmuuskopiot 001–012 sekä niiden PDF- ja DOCX-kumppanit
- vanha lukukopio, vaikka sen nimessä lukee ”ÄLÄ JATKA TÄSTÄ”

### B. Erilliset ja mahdollisesti vanhempaa sanamuotoa säilyttävät osat

- Osa 2
- Osa 3
- Osa 6
- Osa 8
- korjatut alkusanat
- kirjaprojektin erilliset tekstit
- loppuosien versiot v1, v4 ja v5

### C. Lukukohtaiset palautuslähteet

TURBOTALLENNE sisältää erilliset tekstiversiot luvuista 17–26 sekä liitteistä ja loppusanoista. Näitä verrataan vastaaviin v9- ja nykyisen masterin lukuihin, eikä niitä liitetä automaattisesti toistensa päälle.

### D. Keskusteluista palautettu sisältö

- kirjoittajan raakaruokintamyönteinen lähtökohta
- Diegon kokemukset ja 13 vuoden arki
- silmien rähmiminen, kasvojen hankaaminen ja eläinlääkärin hoitoa vaatineet tulehdukset
- eri lihalajien, herkkujen ja reissuruoan yhteydessä tehdyt havainnot
- jäisten luiden käyttö ja niiden rauhoittava merkitys
- kalaöljy sekä EPA- ja DHA-ajattelu
- riistalihaan siirtyminen
- naudan lääkitystä ja mahdollisia jäämiä koskeva kirjoittajan pohdinta, joka erotetaan tutkimusnäytöstä mutta säilytetään kokemuksena

## Suositeltu uudelleenrakennustapa

### 1. Lähteet jäädytetään

`90_palautusarkisto_2026-10-03` pidetään muuttumattomana. Sinne ei tehdä kielellisiä korjauksia, yhdistämisiä tai poistoja.

### 2. Jokaiselle luvulle tehdään oma vertailukansio

Esimerkiksi luvulle 2 luodaan myöhemmin kansio:

`uudelleenrakennus/luku_02/`

Sen sisällä pidetään erillään:

- nykyisen masterin teksti
- v9-version teksti
- vanhempien versioiden lisäkappaleet
- keskusteluista palautettu aineisto
- hyväksytty uusi työversio
- muutosloki, jossa kerrotaan jokainen lisäys, siirto ja poisto

### 3. Vertailu tehdään kappaleittain, ei koko kirjaa kerralla

Jokainen tekstijakso merkitään yhdellä tilalla:

- `SÄILYTÄ` – kuuluu varmasti tulevaan kirjaan
- `PALAUTA` – puuttuu nykyisestä masterista
- `RINNAKKAINEN` – sama aihe eri sanamuodolla, päätetään myöhemmin
- `DUPLIKAATTI` – säilytetään lähteissä, mutta sitä ei tarvitse julkaista kahdesti
- `TARKISTA` – sisältö, tutkimusväite tai sanamuoto vaatii erillisen päätöksen
- `HYVÄKSYTTY` – käyttäjä on hyväksynyt julkaistavaan versioon

### 4. Kirjoittajan ääni palautetaan ensin

Ennen tutkimus- ja kielentarkistusta palautetaan kirjoittajan omat kokemukset, Diegon tarina ja raakaruokintamyönteinen peruslinja. Tutkimusviitteet lisätään tukemaan ja rajaamaan väitteitä, ei muuttamaan kirjaa kokonaan toisen kirjoittajan näkökulmaksi.

### 5. Uusi master syntyy vasta hyväksytyistä luvuista

Uutta masteria ei rakenneta kopioimalla automaattisesti yhtä vanhaa versiota nykyisen päälle. Jokainen luku hyväksytään erikseen. Vasta hyväksytyt luvut kootaan uuteen tiedostoon, esimerkiksi `MASTER_PALAUTETTU.md`.

### 6. Mitään lähdettä ei poisteta uuden masterin valmistuessa

Vanha `MASTER.md`, palautusarkisto, keskustelumuistiot ja kaikki väliversiot jäävät Git-historiaan. Uusi master on uusi tiedosto ja uusi kehityshaara, ei vanhojen aineistojen korvaaminen.

## Suositeltu tarkistusjärjestys

1. Lukijalle, alkusanat ja johdanto
2. Luku 2: biologinen perusta ja ruoansulatus
3. Luku 18: oireet, iho, silmät, korvat ja ruoansulatus
4. Luku 20: riista ja Diegon ruokavalio
5. Luvut 6–9: lihalajit, luut, sisäelimet ja rasvat
6. Loppusanat: mitä Diego opetti
7. Muut luvut numerojärjestyksessä

Tällä järjestyksellä kirjan alkuperäinen ääni ja keskeinen raakaruokintamyönteinen ajatus saadaan näkyviin ennen koko käsikirjoituksen teknistä viimeistelyä.

