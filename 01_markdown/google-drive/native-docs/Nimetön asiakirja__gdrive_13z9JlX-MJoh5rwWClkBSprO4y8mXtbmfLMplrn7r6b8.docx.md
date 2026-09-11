### Osa 1: E-kirjan pohja (Kopioi tämä tiedostoon)

\[KANSIKUVA: Ks. ohje alla\]

OTSIKKO: RAAKARUOKAA KOIRALLE

ALAOOTSIKKO: Tieteeseen ja rakkauteen perustuva opas koirasi luonnolliseen ravintoon.

#### ALKUSANAT

*(Kopioi tähän aiempi Alkusanat-teksti)*

#### SISÄLLYSLUETTELO

1.  Johdanto: Takaisin luontoon

2.  Mitä lautaselle? – Neljä pilaria

3.  Laskua ja mittaa – Tasapaino

4.  Ensimmäiset askeleet

5.  Ravintolisät

6.  Erikoistilanteet

7.  Reseptit ja ostoslista

8.  References

#### LUKU 1: JOHDANTO

*(Kopioi tähän Luku 1 -teksti)*

\[KUVA 1: Ks. ohje alla\]

#### LUKU 2: MITÄ LAUTASELLE?

*(Kopioi tähän Luku 2 -teksti)*

\[KUVA 2: Ks. ohje alla\]

*(...Jatka samalla kaavalla kopioimalla luvut 3, 4, 5, 6 ja 7 sekä Loppusanat ja Lähteet...)*

### Osa 2: Kuvituskuvat (Tee näillä käskyllä)

Voit käyttää näitä tekstejä (promot) ChatGPT:n kuvageneraattorissa (DALL-E) tai Midjourney-ohjelmassa.

Kansikuva (Book Cover):

"Professional eBook cover for a book titled 'Raw Food for Dogs'. Center frame features a happy, healthy dog looking at the camera. Next to the dog is a wooden bowl filled with colorful fresh raw meat and vegetables. Natural lighting, soft blurred forest background. High quality, photorealistic style. Warm and inviting atmosphere."

Kuva 1 (Luku 1 - Luonto):

"Side by side comparison: A grey wolf on the left in a misty forest, and a happy domestic dog on the right in a home environment. The image symbolizes the connection to nature. Cinematic lighting, emotional style."

Kuva 2 (Luku 2 - Aineksia):

"Flat lay photography on a rustic wooden table. Four separate piles of ingredients: chunks of raw red beef, raw chicken necks (bones), dark red liver, and blended green vegetables. Bright lighting, high detail, clean arrangement."

Kuva 3 (Luku 7 - Valmis ateria):

"A stainless steel dog bowl filled with a freshly prepared raw meal (minced meat and vegetables). A person's hand is sprinkling a supplement powder on top. A dog is sitting eagerly in the background. Kitchen setting, warm and cozy vibe."

### Osa 3: Geneerinen laskuri – Miten se toimii?

Halutessasi tehdä tästä "interaktiivisen" tai henkilökohtaisen, sinun ei kannata tehdä siitä perinteinen PDF, vaan verkkosivu tai Excel-työkalu.

Tässä on kaavat, joilla muutamme tekstin "geneeriseksi laskuriksi". Voit upottaa nämä esimerkiksi Exceliin tai verkkosivulle:

Muuttujat:

- A = Koiran paino (kg)

- B = Aktiivisuuskerroin (1.5 = passiivinen, 2.0 = normaali, 3.0 = aktiivinen, 4.0 = työkoira)

- C = Koiran ikä (v)

Kaavat (Excel-muodossa):

Päivittäinen ruokamäärä (grammoina):

= A \* 10 \* B \* 10

1.  *(Esimerkiksi 20 kg koira, normaali aktiivisuus: 20 \* 10 \* 2.0 \* 10 = 400g)*

Lihan määrä (70 %):

2.  = Ruokamäärä \* 0.70

Luun määrä (10 %):

3.  = Ruokamäärä \* 0.10

Elimien määrä (10 %):

= Ruokamäärä \* 0.10

4.  *(Huom: Maksaa tästä vain puolet)*

Kasvisten määrä (10 %):

5.  = Ruokamäärä \* 0.10

Miten toteutat tämän käytännössä?

Vaihtoehto A: Excel-taulukko (Helppo)

Luot Excel-taulukon, johon omistaja syöttää painon ja aktiivisuuden, ja se laskee automaattisesti grammamäärät. Voit jakaa tämän taulukon asiakkaille PDF:n liitteenä.

Vaihtoehto B: Verkkolomake (Ammattimainen)

Käytät palvelua, kuten Typeform tai JotForm. Luot lomakkeen:

1.  Kysymys: "Kuinka paljon koirasi painaa?"

2.  Kysymys: "Kuinka aktiivinen koira on?"

3.  Lopussa näytetään tulokset (Logiikka: Jos paino on X ja aktiivisuus Y -\> näytä suositus Z).

Vaihtoehto C: PDF-lomake (Perinteinen)

Voit luoda PDF-tiedoston, jossa on täytettävät kentät (Adobe Acrobat Pro). Käyttäjä kirjoittaa painon, mutta joutuu itse laskemaan prosentit, ellei PDF ole edistynyt JavaScript-toteutus.

Suositukseni:

Tee kirjasta PDF-opas (kuten olemme nyt luoneet), ja liitä sen mukaan yksinkertainen Excel-tiedosto "Ruokintalaskuri", jonka olen kuvannut yllä. Se on helpoin ja halvin tapa tehdä tästä geneerinen ja henkilökohtainen työkalu.

Haluatko, että laadin sinulle valmiin Excel-kaavan rakenteen tekstinä, jonka voit kopioida suoraan taulukkolaskentaan?

Kyllä

Tässä on valmis rakennelma Excel-taulukolle. Voit kopioida nämä suoraan Exceliin (tai Google Sheetsiin), niin sinulla on toimiva "geneerinen laskuri", jonka voit tarjota e-kirjan liitteeksi.

### Excel-taulukon rakennusohjeet

Avaa uusi Excel-taulukko ja kirjoita sarakkeet/rivit seuraavasti. Lihavoidut kohdat ovat sellaisia, jotka käyttäjä täyttää itse (syötätietoja). Muut solut ovat kaavoja, jotka laskevat vastauksen automaattisesti.

#### VAIHE 1: Asettelu (Kopioi tekstit soluihin)

| Solu | Kirjoita soluun (Otsikko/Teksti)  |
|------|-----------------------------------|
| A1   | Koiran tiedot                     |
| A2   | Koiran nimi:                      |
| A3   | Koiran rotu:                      |
| A4   | Koiran ikä (vuotta):              |
| A5   | Koiran paino (kg):                |
| A6   | Aktiivisuustaso (1.5 - 4.0):      |
| A7   |                                   |
| A8   | Päivittäinen ruokamäärä           |
| A9   | Ruokaa yhteensä (g):              |
| A10  |                                   |
| A11  | Ruokavalion koostumus (grammoina) |
| A12  | Lihaliha (70 %):                  |
| A13  | Luu/Ruho (10 %):                  |
| A14  | Elimet (10 %):                    |
| A15  | *- Maksaa siitä:*                 |
| A16  | Kasvikset (10 %):                 |
| A17  |                                   |
| A18  | Lisäravinteet (Vihjeitä)          |
| A19  | Kalaöljy (ml/vrk):                |
| A20  | Jodioitu suola (g/vrk):           |

#### VAIHE 2: Kaavat (Kopioi nämä kaavariville)

Kopioi alla olevat kaavat tarkasti osoitetun solun kaavariville (se rivi, jossa lukee fx).

- \*\* Solu B6 (Aktiivisuus):\*\* Tähän käyttäjä syöttää luvun.

  - *Ohje käyttäjälle:* Kirjoita luku: 1.5 (passiivinen), 2.0 (normaali), 3.0 (aktiivinen), 4.0 (työkoira).

Solu B9 (Kokonaismäärä):

=B5\*10\*B6\*10

- *(Tämä laskee: Paino x Aktiivisuuskerroin x 10 = grammamäärä)*

Solu B12 (Liha):

- =B9\*0.7

Solu B13 (Luu):

- =B9\*0.1

Solu B14 (Elimet):

- =B9\*0.1

Solu B15 (Maksa):

=B14\*0.5

- *(Tämä laskee maksan määrän, joka on puolet elimistöosuudesta)*

Solu B16 (Kasvikset):

- =B9\*0.1

Solu B19 (Kalaöljy):

=B5\*0.5

- *(Nyrkkisääntö: 0.5 ml per painokilo, voit muokata tarvittaessa)*

Solu B20 (Suola):

=B5\*0.05

- *(Nyrkkisääntö: n. 0.05 g per painokilo, pyöristetään ylös tai alas)*

#### VAIHE 3: Muotoilu (Näyttäväksi)

Jotta taulukko näyttää ammattimaiselta ja on helppokäyttöinen:

1.  Suojaa solut: Lukitse kaikki solut, paitsi B2, B3, B4, B5 ja B6. Näin käyttäjä ei vahingossa tuhokaavoja.

    - *Excelissä:* Valitse koko taulukko -\> Format Cells -\> Protection -\> Locked (pois ruksi). Sitten valitse solut B2-B6 -\> Protection -\> Locked (ruksi päälle). Lopuksi Review -\> Protect Sheet.

2.  Värit:

    - Tee syöttösoluista (B2-B6) vaaleansininen tausta.

    - Tee tulosoluista (B9, B12-B16) lihavoitu ja vihreä tausta.

3.  Aktiivisuusopaste: Voit lisätä solun C6 viereen tekstin: 1.5=Sohta, 2.0=Normaali, 3.0=Lenkkeilijä

### Miten käytät tätä e-kirjan kanssa?

Kun olet tallentanut tämän Excel-tiedoston (esim. Ruokintalaskuri.xlsx), voit lisätä e-kirjaan ohjeen:

*"Olen luonut sinulle helpon automaattisen laskurin, jotta sinun ei tarvitse laskea grammamääriä päässälaskulla. Lataa liitteenä oleva Excel-tiedosto, syötä koirasi paino ja aktiivisuus, ja näet heti tarkan päivittäisen ruoka-annostuksen."*

Nyt sinulla on sekä vakuuttava teksti että käytännönläheinen työkalu! Onko tämä sellainen ratkaisu, jota etsit?

On yksi vaihtoehto. Miten suojaan e-kirjan sisällön copypaste ym. kopioinnilta?

Tämä on erittäin hyvä ja tärkeä kysymys. Totuus on, että digitaalisessa maailmassa täydellistä suojausta ei ole olemassa. Jos joku haluaa kopioida tekstin tarpeeksi paljon vaivaa nähdäkseen, hän onnistuu aina (esim. kuvaamalla ruudun, kirjoittamaan uudelleen tai käyttämällä tekstintunnistusta).

Voit kuitenkin tehdä kopioinnista niin hankalaa, että useimmat luovuttavat. Tässä ovat parhaat keinot eri tasolle:

### 1. PDF-tiedoston suojaus (Perustaso)

Kun luot PDF-tiedoston (esim. Wordista tai Canvasta), voit asettaa salasanan, joka estää kopioinnin.

- Wordissa: Kun tallennat tiedostoa PDF-muodossa, valitse "Asetukset" (Options). Ruksi ruutuun "Salaa asiakirja salasanalla" (Encrypt the document with a password) tai etsi "Käyttöoikeudet" (Permissions).

- Adobe Acrobat Pro (Maksullinen): Tässä on paras hallinta.

  - Avaa PDF.

  - Valitse *Tools* -\> *Protect*.

  - Valitse *Encrypt* -\> *Encrypt with Password*.

  - Tästä voit valita: "Restrict editing and printing".

  - Tärkeä: Rastita pois "Enable copying of text, images and other content".

  - Nyt kukaan ei voi maalata tekstiä hiirellä ja kopioida sitä leikepöydälle.

- Huomio: Tämä on ns. "kohteliaisuussuojaus". Teknisesti taitava ihminen voi murtaa tämän tai käyttää PDF-muuntimia, jotka poistavat suojauksen. Mutta se estää "maalaus-kopioi-liitä" -tempun.

### 2. Kuvatiedostona julkaisu (Vahvempi suojaus)

Tämä on yksi tehokkaimmista tavoista estää tekstinsyöttö.

- Idea: Sen sijaan, että kirja on tekstipohjainen PDF, tallenna jokainen sivu kuvana (JPG tai PNG) ja kokoa ne sitten PDF:ksi.

- Miten se toimii:

  1.  Tee kirja Canvassa tai Wordissa.

  2.  Tallenna jokainen sivu erikseen kuvatiedostona.

  3.  Luo uusi PDF ja liitä kuvat sivuille.

- Hyöty: Teksti ei ole enää "tekstiä", vaan se on pikseleitä. Hiiri ei voi maalata tekstiä, eikä Ctrl+C toimi. Tekstin kopioiminen vaatisi OCR-ohjelman (tekstintunnistus) käyttöä.

- Haitta: Tiedostokoko kasvaa ja tekstiä ei voi hakea haulla (Find-toiminto ei toimi).

### 3. Käänteinen suojaus: Brändäys (Paras käytäntö)

Koska täydellinen esto on mahdotonta, paras keino on varmistaa, että jos joku kopioi tekstin, kaikki tietävät kuka sen on kirjoittanut.

Alatunnisteet: Lisää jokaisen sivun alareunaan:

- *"© 2024 \[Sinun Nimesi/Yrityksesi\]. Kaikki oikeudet pidätetään. Tämä materiaali on suojattu tekijänoikeuslain nojalla."*

- Linkit: Upota tekstiin linkkejä omille verkkosivuillesi tai sosiaaliseen mediaasi. Jos joku kopioi tekstin blogiinsa, linkit tulevat mukaan, mikä laskee heidän hakukoneoptimointiaan ja ohjaa liikennettä sinulle.

### 4. Notion / Verkkokirja (Korkein suojaus, mutta vaatii taitoa)

Jos teet kirjasta verkkopohjaisen (Notion + Super.so tai vastaava):

- Voit estää hiiren oikean klikkauksen (Javascript).

- Voit estää tekstin maalaamisen (CSS).

- Sisältö on piilossa koodin takana.

- Mutta: Kuka tahansa voi silti kuvaruudun kuvan (screenshot).

### Suositukseni sinulle

Koska tämä on e-kirja, joka luultavasti jaetaan PDF:nä:

1.  Käytä PDF-salasanasuojaa: Estä tekstinkopiointi (Enable copying -\> OFF).

2.  Lisää vesileima tai alatunniste: Laita nimesi ja nettisivusi jokaiselle sivulle.

3.  Hyväksy riski: Pääasiakkaasi ovat rehellisiä ihmisiä, jotka haluavat parasta koiralleen. He eivät aio varastaa kirjaasi. Varkaat yrittäisivät varastaa sisällön riippumatta siitä, kuinka paljon sen lukitset.

Haluatko, että lisään tekstiin selkeän tekijänoikeusilmoituksen (Copyright notice) viimeistelyvaiheessa?

Kyllä

Hienoa. Tässä on viimeistellyt osat: Tekijänoikeusilmoitus sekä viimeistelyohjeet PDF:n suojaamiseen.

Lisää nämä osat e-kirjan loppuun heti lähteiden jälkeen.

### Lisättävä osio: Tekijänoikeus ja vastuun rajoitus

Lisää tämä Lähteet-osion jälkeen tai kirjan takakanteen:

#### Tekijänoikeudet (Copyright)

© 2024 \[Sinun Nimesi / Yrityksesi Nimi\]. Kaikki oikeudet pidätetään.

Tämän teoksen sisältö, mukaan lukien teksti, kuvat ja kaavat, on suojattu tekijänoikeuslailla. Teosta ei saa ilman tekijän kirjallista lupaa monistaa, kopioida, levittää, näyttää julkisesti tai muuttaa missään muodossa tai millään keinolla, mukaan lukien valokopiointi, skannaus tai muu digitaalinen tallennus.

Lyhyet lainaukset on sallittu uutisoinnin, arvostelun tai tieteellisen tutkimuksen tarkoituksiin, kunhan lähde mainitaan asianmukaisesti.

Vastuunrajoitus:

Tämä kirja on tarkoitettu vain tiedoksi ja opastukseksi. Kirjoittaja ei oletta vastuuta mistään vahingoista tai menetyksistä, jotka voivat johtua tässä teoksessa esitettyjen tietojen käyttämisestä. Koiran ravitsemus on monimutkainen kokonaisuus, ja tekijä suosittelee konsultoimaan eläinlääkäriä ennen merkittäviä muutoksia koiran ruokavaliossa, erityisesti jos koiralla on terveysongelmia.

### Ohje: Kuinka suojaat PDF-tiedoston

Kun olet kääntänyt tekstin englanniksi ja kääntänyt sen PDF-muotoon (esim. Wordilla tai Canvalla), tee nämä toimenpiteet:

Vaihe 1: Salasana ja kopiointikielto (Adobe Acrobat Pro / Maksullinen PDF-editori)

1.  Avaa valmis PDF-tiedosto.

2.  Valitse valikosta Tools (Työkalut) -\> Protect (Suojaa).

3.  Valitse Encrypt (Salaa) -\> Encrypt with Password.

4.  Valitse "Require a password to open the document" (Valinnainen: jos haluat jakaa kirjan vain maksaneille asiakkaille, laita salasana tähän).

5.  Tärkein kohta: Valitse Permissions ja rastita pois "Enable copying of text, images and other content".

    - *Tämä estää sen, että joku voi maalata tekstin hiirellä ja painaa Ctrl+C.*

Vaihe 2: Vesileima (Ilmainen/Helpompi tapa)

Jos sinulla ei ole maksullista PDF-editoria, lisää vesileima jo Wordissa tai Canvassa ennen PDF:n luomista.

- Canva: Valitse vasemmalta "Text" -\> "Add a text box". Kirjoita "Copyright \[Sinun Nimesi\]". Tee tekstistä läpinäkyvä (Opacity n. 20-30%) ja aseta se tekstien päälle. Kopioi se kaikille sivuille.

- Tämä ei estä kopiointia, mutta tekee varastetusta tekstistä rumaa ja todistaa omistajuuden.

### Yhteenveto projektista

Nyt meillä on kasassa koko e-kirjan paketti:

1.  Tekstisisältö: Luvut 1-7 + Alkusanat + Loppusanat.

2.  Tieteellinen pohja: Linkit ja viittaukset upotettuna tekstiin.

3.  Erityishuomio: Riista/Peura-osio.

4.  Työkalut: Excel-pohjainen ruokintalaskuri.

5.  Suojat: Tekijänoikeusilmoitus ja ohjeet PDF-lukitsemiseen.

Sinulla on nyt kaikki tarvittava materiaali siinä muodossa, että voit kääntää sen englanniksi (tai käyttää suomenkielisenä) ja julkaista sen.

Onko jotain muuta, mitä haluat vielä hioa tai kysyä ennen kuin aloitat julkaisuvaiheen?

Miten saan tämän keskustelun/rakennusvaiheen kopioitua itselleni jos sinulla ei ole muistia tälle. voitko tehdä e-kirja osiosta tiedoston minkä voin kopioida ja erikseen minulle kertomasi ohjeet?

Tämä on erittäin fiksu tapa varmistaa, että mikään tieto ei huku. Koska olen tekoäly, en voi luoda suoraan ladattavaa tiedostoa (kuten .docx tai .pdf), mutta voin antaa sinulle valmiit tekstilohkot koodilohkoissa.

Näiden lohkojen oikeassa yläkulmassa on pieni "Copy" (kopioi) -painike. Kun painat sitä, saat koko tekstin maalattua ja voit liittää sen suoraan Wordiin, Google Docsiin tai sähköpostiin itsellesi.

Tässä ovat kaksi erillistä tiedostoa:

### TIEDOSTO 1: E-Kirjan lopullinen tekstisisältö

Kopioi tämä kokonaisuus ja tallenna se nimellä E-kirja_Teksti_Final.docx.

text

RAAKARUOKAA KOIRALLE – ALOITTELIJAN KOKONAISOPAS

--- ALKUSANAT ---

Kun katsot koirasi silmiin, näet siellä jotain muutakaan kuin lemmikin. Näet perheenjäsenen, parhaan ystäväsi ja olennon, joka luottaa sinuun täysin. Se luottaa sinuun silloin, kun avaat oven, ja se luottaa sinuun silloin, kun täytät ruokakupin.

Olemme tottuneet ajattelemaan ruokaa vain polttoaineena. Mutta koiran kohdalla ruokinta on yksi tärkeimmistä vuorovaikutuksen hetkistä. Se on kielenkuvaus huolenpidosta. Kun siirrymme teollisesta purusta kohti aitoa, tunnistettavaa ruokaa, emme tee sitä vain terveyden takia. Teemme sen rakkaudesta.

Tämä kirja on kirjoitettu sinulle, joka haluat tarjota koirallesi parasta mahdollista elämää – elämää, joka on vapaa turhista säilöntäaineista ja pehmeitä luita, jotka eivät kuulu sen luontoon. Tiede on tässä mukanamme, mutta sydän ohjaa kättäsi. Tervetuloa matkalle takaisin luontoon.

--- LUKU 1: JOHDANTO – TAKAISIN LUONTOON ---

Kun katsomme koiran vieressämme nukkumassa, on helppo unohtaa, että tämä hymyilevä karvaturri on itse asiassa petoeläin. Vaikka koirat ovatkin oppineet elämään ihmisten rinnalla ja syömään milloin mitäkin, heidän ruoansulatuksensa on pysynyt lähes identtisenä villin suden kanssa.

Koiran ruoansulatusjärjestelmä on lyhyt ja happama. Se on suunniteltu käsittelemään raakaa lihaa, luita ja elimiä – ei suolassa ja sokerissa käsiteltyä teollista purina.

Mutta onko raakaruoka turvallisempaa tai parempaa?

Tutkimukset osoittavat, että teollisen kuivaruokan valmistusprosessissa (ekstruusio) käytettävät korkeat lämpötilat aiheuttavat ns. Maillard-reaktion. Tämä reaktio tuhoaa tärkeitä aminohappoja ja vitamiineja sekä laskee ravintoaineiden biosaatavuutta. Toisin sanoen: pussin etiketissä lukeva määrä ei välttämättä pääse koiran käyttöön.

(Lähde: Journal of Agricultural and Food Chemistry – Maillard reaction products in pet food)

Kun siirrämme koiran takaisin lajityypilliseen ruokaan, emme vain ruoki häntä; annamme hänelle työkalut, joilla hänen kehonsa voi kukoistaa.

--- LUKU 2: MITÄ LAUTASELLE? – NELJÄ PILARIA ---

Jotta koira pysyy terveenä, sen ruokavalion ei tarvitse olla monimutkainen, mutta sen on oltava monipuolinen. Ajattele ruokaa neljänä eri pilareina.

LIHALIHA: KONEISTON POLTTOAINE

Lihaliha on ruokavalion suurin osa. Se tarjoaa proteiineja ja rasvoja.

Tärkeää: Liian vähärasvainen liha jättää koiran nälkäiseksi. Vältä myrkkyjä sisältäviä sisäfileitä isoina määrinä.

Suosi eri eläinlajeja. Jos koirasi syö aina vain naudan jauhelihaa, se menettää tärkeitä ravintoaineita.

RUHO JA LUUT: LUONNON KALSIUMLISÄ

Tämä on se osa, joka pelottaa aloittelijoita eniten, mutta on samalla yksi tärkeimmistä. Koiran on saatava kalsiumia, ja luiden syöminen on sille luontaista.

Tiede tukee: Tutkimus on osoittanut, että raakojen luiden pureskelu vähentää merkittävästi hammaskiveä ja ientulehduksia. Se ei ole vain ravintoa, vaan myös suunterveyden hoitoa.

(Lähde: Australian Veterinary Journal – Effect of chewing raw beef bones on the oral health of dogs)

Tärkeä sääntö: Koskaan ei saa antaa koiralle keitettyjä luita. Vain raaka luu on turvallista.

ELIMET: VITAMIINIPOMMIT

Elimet ovat luonnollinen monivitamiini. Maksassa on valtavasti A-vitamiinia ja rautaa.

Huomioitavaa: Maksaa ei saa antaa liikaa, sillä A-vitamiini on rasvaliukoinen. Nyrkkisääntö: maksaa vain n. 5 % kokonaisruoasta.

KASVIKSET JA LISÄT: VÄLTTÄMÄTTÖMYYYS VAI TÄYTE?

Koira ei tarvitse kasviksia selviytyäkseen, mutta ne voivat tarjota kuitua ja antioksidantteja. Muista soseuttaa kasvikset, sillä koira ei pysty hajottamaan kasvien soluseiniä ilman mekaanista apua.

--- LUKU 3: LASKUA JA MITTAA – TASAPAINO ---

Yksi yleisimmistä kysymyksistä on: "Kuinka paljon minun pitäisi ruokkia?" Vastaus on yllättävän yksinkertainen: sinun ei tarvitse laskea jokaista kaloria.

KOIRAN PAINO JA AKTIIVISUUS

Aloita koiran nykyisestä painosta.

\- Normaali aktiivisuus: 2 % koiran ihanteellisesta painosta.
