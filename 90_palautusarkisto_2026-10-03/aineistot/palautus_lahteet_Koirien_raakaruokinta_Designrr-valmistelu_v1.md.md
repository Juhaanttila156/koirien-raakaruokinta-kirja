# Palautettu lähdeaineisto

- Alkuperäinen tiedosto: `Koirien_raakaruokinta_Designrr-valmistelu_v1.md`
- Lähdepolku koontivaiheessa: `palautus_lahteet/Koirien_raakaruokinta_Designrr-valmistelu_v1.md`
- SHA-256: `0294357f2f169e5155db11b3a300b449688f123e83fbcd97af2ca01b97269436`
- Huomautus: Tämä on automaattisesti purettu lukukopio. Alkuperäistiedosto säilytetään erillisessä lähdearkistossa.

---

# KOIRIEN RAAKARUOKINTA

## Designrr-valmistelu ja taittoon viennin työohje — v1

**Tekijä:** JP Anttila  
**Julkaisija / imprint:** Nature Borealis  
**Lähdemaster:** `JP_Anttila_Koirien_raakaruokinta_koko_kirja_v6.docx`  
**Periaate:** lähdemasteria ei muuteta eikä sisältöä ohenneta. Designrr-tuontia varten tehdään aina erillinen kopio.

## 1. Tavoite

Valmistaa pitkästä hyväksytystä v6-masterista rakenteellisesti puhdas DOCX, jonka Designrr pystyy lukemaan mahdollisimman ennustettavasti. Varsinainen visuaalinen ilme, kansi, sisällysluettelo, sivunumerot, ylä- ja alatunnisteet sekä lopullinen sivutaitto rakennetaan Designrrissa.

Kirjasta tuotetaan myöhemmin vähintään kaksi erillistä lopputuotetta:

1. kiinteätaittoinen PDF-versio;
2. uudelleenjuoksutettava EPUB/Kindle-versio.

Niitä ei pidä käsitellä yhtenä ja samana taittona, koska PDF:n sivuasettelu ja EPUBin mukautuva lukutapa vaativat eri ratkaisuja.

## 2. Lähdemasterin alustava tekninen tarkastus

| Kohde | Havainto |
|---|---:|
| Kappaleita yhteensä | 4 417 |
| Tyhjiä kappaleita | 1 380 |
| Heading 1 | 53 |
| Heading 2 | 451 |
| Heading 3 | 65 |
| Otsikkotyylisiä kappaleita yhteensä | 569 |
| Lähdeluettelotyylisiä kappaleita | 229 |
| Luettelokappaleita | 138 |
| Tekstissä olevia kuvia | 8 |
| Taulukoita | 0 |
| Word-osioita | 1 |

Tarkastus osoittaa, että sisältöä on runsaasti ja pitkä master on oikea lähtökohta. Rakenne tarvitsee kuitenkin puhdistuksen ennen tuontia. Otsikkotasoja on paljon, osa väliotsikoista on tavallista leipätekstiä ja alussa on päällekkäiseltä vaikuttavia johdanto- ja osaotsikoita. Näitä ei poisteta mekaanisesti, vaan ne verrataan sisällysluetteloon ja kirjan hyväksyttyyn rakenteeseen.

## 3. Designrr-tuontiversion rakenne

Tuontitiedoston työnimi:

`JP_Anttila_Koirien_raakaruokinta_DESIGNRR_IMPORT_v1.docx`

Tuontiversioon sisällytetään:

- lopullinen kirjan teksti oikeassa lukujärjestyksessä;
- luvut selkeästi Word-otsikkotyyleillä;
- väliotsikot yhtenäisillä otsikkotyyleillä;
- aidot Word-luettelot;
- kuvat tai yksiselitteiset kuvapaikkamerkinnät;
- kuvatekstit ja kuvalähteet;
- lähdeviitteet ja toimivat linkit;
- taulukkomuotoinen tieto yksinkertaisessa, saavutettavassa rakenteessa;
- laskuria koskevat tekstiosat ja selkeä linkitys erilliseen interaktiiviseen laskuriin.

Tuontiversiosta poistetaan tai jätetään Designrrissa rakennettavaksi:

- Wordissa tehty kansi ja takakansi;
- käsin kirjoitettu tai Wordissa generoitu sivunumerollinen sisällysluettelo;
- ylä- ja alatunnisteet;
- Word-sivunumerot;
- turhat tyhjät kappaleet ja manuaaliset tyhjät sivut;
- päällekkäiset tai vanhat rakenneversiot;
- työohjeet, metatekstit ja toimitukselliset muistiinpanot;
- sellainen Word-tyylittely, jonka Designrrin valittu mallipohja kuitenkin korvaa.

## 4. Otsikkotasojen lukittu periaate

Designrr-tuontiversiossa käytetään seuraavaa rakennetta:

| Sisällön tehtävä | Word-tyyli | Käyttö |
|---|---|---|
| Kirjan osan nimi | Heading 1 tai erillinen osamerkintä | OSA I–VII |
| Varsinainen numeroitu luku | Heading 2 | Luvut 1–26 sekä liitteet |
| Luvun pääasiallinen väliotsikko | Heading 3 | Luvun sisäinen navigointi |
| Pieni väliotsikko | Heading 4 tai lihavoitu aloituskappale | Käytetään säästeliäästi |
| Leipäteksti | Normal | Varsinainen kerronta |
| Lähdemerkintä | yhtenäinen lähdetyyli | Ei otsikkotyyliä |

Ennen lopullista muunnosta tehdään otsikkokartta, jotta nykyisiä 569 otsikoksi merkittyä kappaletta ei muuteta sokkona.

## 5. Sisällön puhdistuksen tarkistuslista

### Ensimmäinen kierros — rakenne

- verrataan kaikki osat ja luvut hyväksyttyyn sisällysluetteloon;
- tunnistetaan päällekkäiset johdannot, osat ja luvut;
- erotetaan tarkoituksellinen syventävä sisältö aidosta kaksoiskappaleesta;
- säilytetään hyväksytyt alkusanat täsmälleen ennallaan;
- varmistetaan, että Diego-kerronta kulkee mukana eikä muutu irrallisiksi laatikoiksi;
- tarkistetaan liitteiden, UKK:n, malliviikkojen, laskennan, sanaston ja hakemiston sijainti.

### Toinen kierros — tekninen muoto

- normalisoidaan otsikkotasot;
- muutetaan käsin kirjoitetut luettelomerkit aidoiksi Word-luetteloiksi;
- poistetaan ylimääräiset tyhjät kappaleet hallitusti;
- poistetaan vanhat manuaaliset sivunvaihdot, jos ne eivät palvele tuontia;
- säilytetään kursivoinnit, lihavoinnit, ala- ja yläindeksit sekä hyperlinkit;
- tarkistetaan erikoismerkit, mittayksiköt ja desimaalit.

### Kolmas kierros — julkaisuvalmius

- lähdeviitteiden yhtenäisyys ja linkkien toimivuus;
- väitteiden ja lähteiden vastaavuus;
- kuvien käyttöoikeudet, kuvalähteet ja vaihtoehtoiset tekstit;
- taulukoiden luettavuus puhelimella;
- varoitusten ja eläinlääketieteellisten rajausten näkyvyys;
- Yhdysvaltain markkinoille myöhemmin vaihdettavien yksiköiden, standardien ja termien merkintä;
- PDF- ja EPUB-versioiden erillinen laadunvarmistus.

## 6. Kuvakartta

Jokaiselle kuvalle annetaan yksilöllinen tunnus:

`KUVA-OSA-LUKU-NUMERO`

Esimerkiksi `KUVA-II-07-01` tarkoittaa osan II luvun 7 ensimmäistä kuvaa.

Kuvakarttaan merkitään vähintään:

- kuvatunnus;
- tiedostonimi;
- luku ja sijoituskohta;
- kuvan aihe;
- kuvateksti;
- kuvalähde ja käyttöoikeus;
- tekijänoikeusmerkintä;
- vaihtoehtoinen teksti;
- rajausohje;
- soveltuuko kuva PDF:ään, EPUBiin vai molempiin.

Diegon kuvista valitaan erikseen tarinaa kantavat pääkuvat ja täydentävät kuvat. Kaikkia satoja kuvia ei viedä taittoon, vaan ensin rakennetaan kuvakertomus.

## 7. Laskuri

Interaktiivista ruokinta-, vitamiini- ja lisäravinnelaskuria ei rakenneta staattiseksi Word-taulukoksi. Kirjaan tehdään:

- selkeä laskentaperiaatteen kuvaus;
- muutama läpinäkyvä esimerkkilasku;
- turvallisuusrajat ja varoitukset;
- QR-koodi ja tavallinen verkkolinkki erilliseen laskuriin;
- versionumero ja viimeisin tarkistuspäivä.

Näin kirjan teksti säilyy luettavana ja laskuri voidaan päivittää ilman, että koko e-kirja täytyy taittaa uudelleen.

## 8. Designrrissa tehtävät asiat

- kirjan koon ja mallipohjan valinta;
- kannen ja takakannen suunnittelu;
- väripaletti, fontit ja graafiset elementit;
- sisällysluettelon luonti;
- sivunumeroiden sekä ylä- ja alatunnisteiden määrittely PDF-versioon;
- kuva-asettelut ja nostot;
- PDF-vientiprofiilin tarkistus;
- erillisen Kindle/EPUB-projektin luonti ja tarkistus.

## 9. Suositeltu etenemisjärjestys

1. Lukitaan hyväksytty v6 lähdemasteriksi.
2. Tehdään täydellinen rakenne- ja kaksoissisältöauditointi.
3. Luodaan puhdas Designrr-import-DOCX.
4. Tehdään ensimmäinen koetuonti Designrriin ilman lopullisia kuvia.
5. Korjataan otsikot, luettelot, kappalejaot ja kuvapaikat koetuonnin perusteella.
6. Rakennetaan kuvakartta ja valitaan kuvat.
7. Valitaan PDF:n visuaalinen tyyli ja taitetaan PDF-versio.
8. Tehdään erillinen EPUB/Kindle-versio.
9. Tarkistetaan molemmat puhelimella, tabletilla ja tietokoneella.
10. Vasta hyväksytyn laaduntarkastuksen jälkeen julkaistaan.

## 10. Seuraava konkreettinen työvaihe

Seuraavaksi muodostetaan v6-masterista otsikko- ja lukukartta, jossa jokainen nykyinen pääotsikko luokitellaan johonkin seuraavista:

- säilytä osan otsikkona;
- säilytä luvun otsikkona;
- säilytä väliotsikkona;
- muuta leipätekstiksi;
- mahdollinen päällekkäinen sisältö — tarkista;
- työmerkintä — poista vain varmistuksen jälkeen.

Kun otsikkokartta on hyväksytty tai tarkistettu, puhdas Designrr-import-DOCX voidaan tehdä hallitusti ilman sisällön ohentamista.
