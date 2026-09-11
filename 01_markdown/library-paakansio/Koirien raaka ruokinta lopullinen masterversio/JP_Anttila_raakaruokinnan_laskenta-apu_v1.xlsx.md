# JP_Anttila_raakaruokinnan_laskenta-apu_v1

> Excel-työkirjan sisältö tekstimuodossa. Alkuperäinen XLSX on arkistossa.

## Aloitus

| Sarake 1 | Sarake 2 | Sarake 3 | Sarake 4 | Sarake 5 | Sarake 6 | Sarake 7 | Sarake 8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KOIRIEN RAAKARUOKINNAN LASKENTA-APU | KOIRIEN RAAKARUOKINNAN LASKENTA-APU | KOIRIEN RAAKARUOKINNAN LASKENTA-APU | KOIRIEN RAAKARUOKINNAN LASKENTA-APU | KOIRIEN RAAKARUOKINNAN LASKENTA-APU | KOIRIEN RAAKARUOKINNAN LASKENTA-APU | KOIRIEN RAAKARUOKINNAN LASKENTA-APU | KOIRIEN RAAKARUOKINNAN LASKENTA-APU |
| Terveen aikuisen koiran lähtölaskuri. Ei pennulle, tiineelle tai imettävälle nartulle eikä sairauden hoitoon. Laskurin tulos on aloitusarvio: koiran paino-, kehon- ja lihaskuntotrendi ratkaisevat annoksen tarkistuksen. |  |  |  |  |  |  |  |
| SYÖTÄ KELTAISIIN SOLUIHIN |  |  | LASKETUT TULOKSET |  |  |  |  |
| Koiran paino | 20 | kg | Metabolinen paino | =IF(B7>0,B7^0.75,0) | kg⁰·⁷⁵ |  |  |
| Vuorokausienergia käsin (0 = käytä kerrointa) | 0 | kcal/vrk | Käytetty vuorokausienergia | =IF(B8>0,B8,E7*B9) | kcal/vrk |  |  |
| Energiakerroin | 95 | kcal/kg⁰·⁷⁵/vrk | Perusruoalle jäävä energia | =MAX(0,E8-B11) | kcal/vrk |  |  |
| Ruoan energiapitoisuus | 180 | kcal/100 g | Perusruokaa päivässä | =IF(B10>0,E9/(B10/100),0) | g/vrk |  |  |
| Herkut ja muut lisäenergiat | 0 | kcal/vrk | Perusruokaa aterialla | =IF(B12>0,E10/B12,0) | g/ateria |  |  |
| Aterioita vuorokaudessa | 2 | kpl | Perusruokaa viikossa | =E10*7 | g/viikko |  |  |
| Käyttötilanne | Terve aikuinen |  | Herkkujen energiaosuus | =IF(E8>0,B11/E8,0) | % |  |  |
|  |  |  | Energiatiheys | =B10/100 | kcal/g |  |  |
|  |  |  | Laskurin tila | =IF(B13<>"Terve aikuinen","PYSÄYTÄ: käyttötilanne vaatii yksilöarvion",IF(OR(B7<=0,B9<=0,B10<=0,B12<1),"TARKISTA SYÖTTEET",IF(E13>0.1,"HUOMIO: lisäenergia yli 10 %","LÄHTÖLASKU VALMIS"))) |  |  |  |
| NÄIN LUET TULOSTA |  |  |  |  |  |  |  |
| 1. Jos tiedät koiran toteutuneen ylläpitoenergian luotettavasta seurannasta, syötä se kohtaan Vuorokausienergia käsin. |  |  |  |  |  |  |  |
| 2. Muuten laskuri käyttää painoa ja säädettävää energiakerrointa. Kerroin ei ole kaikille koirille sama. |  |  |  |  |  |  |  |
| 3. Ruoan energiapitoisuus otetaan tuotteen tiedosta tai reseptin analyysistä. Älä päättele sitä lihan nimestä. |  |  |  |  |  |  |  |
| 4. Herkut, öljyt, purutuotteet ja energiapitoiset lääkkeenantojakeet lasketaan mukaan. |  |  |  |  |  |  |  |
| 5. Punnitse koira ja arvioi BCS sekä MCS. Muuta energiaa maltillisesti trendin, ei yhden päivän vaihtelun perusteella. |  |  |  |  |  |  |  |
| 6. Tämä laskuri ei tarkista vitamiineja, kivennäisiä, aminohappoja tai rasvahappoja. Käytä Reseptierä-välilehteä vain energia- ja Ca:P-esitarkistukseen. |  |  |  |  |  |  |  |

## Viikkosuunnitelma

| Sarake 1 | Sarake 2 | Sarake 3 | Sarake 4 | Sarake 5 | Sarake 6 | Sarake 7 | Sarake 8 | Sarake 9 | Sarake 10 | Sarake 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VIIKKOSUUNNITELMA | VIIKKOSUUNNITELMA | VIIKKOSUUNNITELMA | VIIKKOSUUNNITELMA | VIIKKOSUUNNITELMA | VIIKKOSUUNNITELMA | VIIKKOSUUNNITELMA | VIIKKOSUUNNITELMA | VIIKKOSUUNNITELMA | VIIKKOSUUNNITELMA | VIIKKOSUUNNITELMA |
| Suunnitellut ateriamäärät tulevat Aloitus-välilehdeltä. Keltaiset toteuma- ja seurantakentät täytetään päivän aikana. Jos käytät eri ruokia, laske kunkin energiapitoisuus erikseen äläkä korvaa grammoja grammoilla. |  |  |  |  |  |  |  |  |  |  |
| Päivä | Päivämäärä | Ruoka / reseptiversio | Ateria 1 g | Ateria 2 g | Ateria 3 g | Suunniteltu yht. g | Toteutunut g | Herkut kcal | Uloste 1–7 | Huomiot |
| Maanantai |  | Perusannos P | =IF('Aloitus'!$B$12>=1,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=2,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=3,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =SUM(D7:F7) |  |  |  |  |
| Tiistai |  | Perusannos P | =IF('Aloitus'!$B$12>=1,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=2,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=3,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =SUM(D8:F8) |  |  |  |  |
| Keskiviikko |  | Perusannos P | =IF('Aloitus'!$B$12>=1,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=2,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=3,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =SUM(D9:F9) |  |  |  |  |
| Torstai |  | Perusannos P | =IF('Aloitus'!$B$12>=1,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=2,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=3,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =SUM(D10:F10) |  |  |  |  |
| Perjantai |  | Perusannos P | =IF('Aloitus'!$B$12>=1,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=2,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=3,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =SUM(D11:F11) |  |  |  |  |
| Lauantai |  | Perusannos P | =IF('Aloitus'!$B$12>=1,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=2,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=3,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =SUM(D12:F12) |  |  |  |  |
| Sunnuntai |  | Perusannos P | =IF('Aloitus'!$B$12>=1,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=2,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =IF('Aloitus'!$B$12>=3,'Aloitus'!$E$10/'Aloitus'!$B$12,0) | =SUM(D13:F13) |  |  |  |  |
| VIIKON YHTEENSÄ |  |  |  |  |  | =SUM(G7:G13) | =SUM(H7:H13) | =SUM(I7:I13) |  |  |
| VIIKKOYHTEENVETO |  |  |  |  |  |  |  |  |  |  |
| Ruokahalu |  |  |  |  |  |  |  |  |  |  |
| Uloste ja vatsan toiminta |  |  |  |  |  |  |  |  |  |  |
| Iho, korvat, aktiivisuus ja muu muutos |  |  |  |  |  |  |  |  |  |  |

## Reseptierä

| Sarake 1 | Sarake 2 | Sarake 3 | Sarake 4 | Sarake 5 | Sarake 6 | Sarake 7 | Sarake 8 | Sarake 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RESEPTIERÄN ENERGIA- JA Ca:P-ESITARKISTUS | RESEPTIERÄN ENERGIA- JA Ca:P-ESITARKISTUS | RESEPTIERÄN ENERGIA- JA Ca:P-ESITARKISTUS | RESEPTIERÄN ENERGIA- JA Ca:P-ESITARKISTUS | RESEPTIERÄN ENERGIA- JA Ca:P-ESITARKISTUS | RESEPTIERÄN ENERGIA- JA Ca:P-ESITARKISTUS | RESEPTIERÄN ENERGIA- JA Ca:P-ESITARKISTUS | RESEPTIERÄN ENERGIA- JA Ca:P-ESITARKISTUS | RESEPTIERÄN ENERGIA- JA Ca:P-ESITARKISTUS |
| Syötä keltaisiin soluihin jokaisen raaka-aineen määrä ja koostumustieto samasta luotettavasta lähteestä. Tämä välilehti laskee vain energian, kalsiumin ja fosforin. Hyvä Ca:P-suhde ei todista reseptiä täysipainoiseksi. |  |  |  |  |  |  |  |  |
| Raaka-aine / tuote | Määrä g/erä | kcal/100 g | Ca mg/100 g | P mg/100 g | Energia kcal | Ca mg | P mg | Tietolähde / URL |
| Liharaaka-aine 1 |  |  |  |  | =IFERROR(B7*C7/100,0) | =IFERROR(B7*D7/100,0) | =IFERROR(B7*E7/100,0) |  |
| Liharaaka-aine 2 |  |  |  |  | =IFERROR(B8*C8/100,0) | =IFERROR(B8*D8/100,0) | =IFERROR(B8*E8/100,0) |  |
| Maksa |  |  |  |  | =IFERROR(B9*C9/100,0) | =IFERROR(B9*D9/100,0) | =IFERROR(B9*E9/100,0) |  |
| Muu erittävä elin |  |  |  |  | =IFERROR(B10*C10/100,0) | =IFERROR(B10*D10/100,0) | =IFERROR(B10*E10/100,0) |  |
| Kuitulähde |  |  |  |  | =IFERROR(B11*C11/100,0) | =IFERROR(B11*D11/100,0) | =IFERROR(B11*E11/100,0) |  |
| Kalsiumlähde |  |  |  |  | =IFERROR(B12*C12/100,0) | =IFERROR(B12*D12/100,0) | =IFERROR(B12*E12/100,0) |  |
| Öljy / rasva |  |  |  |  | =IFERROR(B13*C13/100,0) | =IFERROR(B13*D13/100,0) | =IFERROR(B13*E13/100,0) |  |
| Täydennys 1 |  |  |  |  | =IFERROR(B14*C14/100,0) | =IFERROR(B14*D14/100,0) | =IFERROR(B14*E14/100,0) |  |
| Täydennys 2 |  |  |  |  | =IFERROR(B15*C15/100,0) | =IFERROR(B15*D15/100,0) | =IFERROR(B15*E15/100,0) |  |
| Muu |  |  |  |  | =IFERROR(B16*C16/100,0) | =IFERROR(B16*D16/100,0) | =IFERROR(B16*E16/100,0) |  |
| ERÄN YHTEENVETO |  |  |  |  |  |  |  |  |
| Erän paino | =SUM(B7:B16) | g |  | TARKISTUSRAJAT EIVÄT OLE TÄYDELLISYYSTODISTUS |  |  |  |  |
| Erän energia | =SUM(F7:F16) | kcal |  | Ca:P-suhteen tulkinta tehdään koiran elämänvaiheen ja käytetyn suosituksen mukaan. |  |  |  |  |
| Energiatiheys | =IF(B19>0,B20/B19*100,0) | kcal/100 g |  | Pennun kivennäistarpeita ei arvioida tällä laskurilla. |  |  |  |  |
| Kalsium yhteensä | =SUM(G7:G16) | mg |  | Luu, luujauho, munankuori ja kalsiumkarbonaatti eivät ole grammoina vaihtokelpoisia. |  |  |  |  |
| Fosfori yhteensä | =SUM(H7:H16) | mg |  | FEDIAF-vaatimukset ilmaistaan suhteessa energiaan ja elämänvaiheeseen; tarkista koko ravintoaineprofiili erikseen. |  |  |  |  |
| Ca:P-suhde | =IF(B23>0,B22/B23,0) | suhde |  | Jos koostumustieto puuttuu, nolla tarkoittaa tässä vain puuttuvaa syötettä – ei sitä, ettei aineessa olisi ravintoainetta. |  |  |  |  |
| Erästä päiviä | =IF('Aloitus'!$E$8>0,B20/'Aloitus'!$E$8,0) | vrk |  | Säilytä tietolähde ja reseptiversio, jotta lasku voidaan myöhemmin tarkistaa. |  |  |  |  |
| Erän laskennallinen päiväannos | =IF(B21>0,'Aloitus'!$E$9/(B21/100),0) | g/vrk |  |  |  |  |  |  |

## Seuranta

| Sarake 1 | Sarake 2 | Sarake 3 | Sarake 4 | Sarake 5 | Sarake 6 | Sarake 7 | Sarake 8 | Sarake 9 | Sarake 10 | Sarake 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA | PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA | PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA | PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA | PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA | PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA | PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA | PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA | PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA | PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA | PAINON, KEHONKUNNON JA RUOKINNAN SEURANTA |
| Täytä lähtötilanne ja sen jälkeen samalla menetelmällä sovituin välein. BCS arvioidaan asteikolla 1–9 ja uloste tässä työkalussa asteikolla 1–7. Älä tee diagnoosia yhdestä numerosta; seuraa trendiä ja koiran yleistilaa. |  |  |  |  |  |  |  |  |  |  |
| Päivämäärä | Paino kg | Muutos alusta % | BCS 1–9 | MCS | Päiväannos g | Energia kcal | Uloste 1–7 | Ruokahalu | Aktiivisuus | Huomiot / muutos |
|  |  | =IF(OR(B7="",$B$7=""),"",B7/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B8="",$B$7=""),"",B8/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B9="",$B$7=""),"",B9/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B10="",$B$7=""),"",B10/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B11="",$B$7=""),"",B11/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B12="",$B$7=""),"",B12/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B13="",$B$7=""),"",B13/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B14="",$B$7=""),"",B14/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B15="",$B$7=""),"",B15/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B16="",$B$7=""),"",B16/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B17="",$B$7=""),"",B17/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B18="",$B$7=""),"",B18/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B19="",$B$7=""),"",B19/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B20="",$B$7=""),"",B20/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B21="",$B$7=""),"",B21/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B22="",$B$7=""),"",B22/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B23="",$B$7=""),"",B23/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B24="",$B$7=""),"",B24/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B25="",$B$7=""),"",B25/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B26="",$B$7=""),"",B26/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B27="",$B$7=""),"",B27/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B28="",$B$7=""),"",B28/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B29="",$B$7=""),"",B29/$B$7-1) |  |  |  |  |  |  |  |  |
|  |  | =IF(OR(B30="",$B$7=""),"",B30/$B$7-1) |  |  |  |  |  |  |  |  |
| Hakeudu arvioon, jos koira laihtuu tahattomasti, menettää lihasta, kieltäytyy ruoasta, oksentaa tai ripuloi toistuvasti, juo tai virtsaa selvästi enemmän, on kivulias tai sen yleistila heikkenee. |  |  |  |  |  |  |  |  |  |  |

## Ohjeet ja lähteet

| Sarake 1 | Sarake 2 | Sarake 3 | Sarake 4 | Sarake 5 | Sarake 6 | Sarake 7 | Sarake 8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OHJEET, RAJAUKSET JA LÄHTEET | OHJEET, RAJAUKSET JA LÄHTEET | OHJEET, RAJAUKSET JA LÄHTEET | OHJEET, RAJAUKSET JA LÄHTEET | OHJEET, RAJAUKSET JA LÄHTEET | OHJEET, RAJAUKSET JA LÄHTEET | OHJEET, RAJAUKSET JA LÄHTEET | OHJEET, RAJAUKSET JA LÄHTEET |
| MITÄ TYÖKIRJA LASKEE |  |  |  |  |  |  |  |
| • metabolisen painon kg⁰·⁷⁵ |  |  |  |  |  |  |  |
| • käyttäjän syöttämään energia-arvioon perustuvan päivä- ja ateria-annoksen |  |  |  |  |  |  |  |
| • viikkosuunnitelman suunnitellut grammamäärät |  |  |  |  |  |  |  |
| • reseptierän energian sekä kalsium- ja fosforisumman käyttäjän syöttämistä koostumustiedoista |  |  |  |  |  |  |  |
| • painon muutoksen ensimmäiseen seurantamerkintään verrattuna. |  |  |  |  |  |  |  |
| MITÄ TYÖKIRJA EI LASKE |  |  |  |  |  |  |  |
| • se ei todista reseptiä täysipainoiseksi eikä tarkista kaikkia aminohappoja, rasvahappoja, vitamiineja ja hivenaineita |  |  |  |  |  |  |  |
| • se ei määritä pennun, tiineen tai imettävän nartun eikä sairaan koiran tarvetta |  |  |  |  |  |  |  |
| • se ei arvioi luiden mekaanista turvallisuutta tai tuotteen mikrobiologista riskiä |  |  |  |  |  |  |  |
| • se ei korvaa eläinlääkärin diagnoosia, ravitsemussuunnittelua tai koiran seurantaa |  |  |  |  |  |  |  |
| • se ei tee puuttuvasta koostumustiedosta nollaa ravintoainetta – nolla syötteessä tarkoittaa puuttuvaa tietoa. |  |  |  |  |  |  |  |
| LÄHTEET JA TARKISTUSPISTEET |  |  |  |  |  |  |  |
| Lähde | Käyttö | URL |  |  |  |  |  |
| FEDIAF 2025 | Eurooppalaiset koirien ja kissojen ravintosuositukset | https://www.fediaf.org/self-regulation/nutritional-guidelines/ |  |  |  |  |  |
| WSAVA 2025 | Koiran kehon kuntoluokitus BCS 1–9 | https://wsava.org/wp-content/uploads/2025/06/WSAVA_BCSCat_BCSDog_Nutrition_250612.pdf |  |  |  |  |  |
| WSAVA 2024 | Herkkujen ja muun lisäenergian ohje | https://wsava.org/wp-content/uploads/2024/06/Feeding-treats-to-your-dog-v2.pdf |  |  |  |  |  |
| AAHA 2021 | Ravitsemuksen ja painonhallinnan kliiniset periaatteet | https://www.aaha.org/resources/2021-aaha-nutrition-and-weight-management-guidelines/home/ |  |  |  |  |  |
| VERSIO JA KÄYTTÖ |  |  |  |  |  |  |  |
| Työkirjan versio: 1.0 / 9.8.2026 |  |  |  |  |  |  |  |
| Kirjaprojekti: JP Anttila – Koirien raakaruokinta |  |  |  |  |  |  |  |
| Syöttösolut ovat keltaisia, kaavasolut vihertäviä ja turvallisuusvaroitukset punaisia. |  |  |  |  |  |  |  |
| Säilytä jokaisesta käytetystä koostumustiedosta lähde, päivämäärä ja tuote- tai erätieto. |  |  |  |  |  |  |  |
| Tarkista suositusten uusin versio ennen julkaisua tai kliinistä käyttöä. |  |  |  |  |  |  |  |
