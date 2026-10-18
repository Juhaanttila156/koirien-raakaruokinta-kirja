# Koevedoksen tekniset tarkistukset – 18.10.2026

## Vanhojen PDF-tiedostojen suora vertailu
- `JP_Anttila_Koirien_raakaruokinta_koko_kirja_v9-1.pdf`: **283 sivua**, PDF-tekstipoiminta **563 467 merkkiä**.
- `Koirien_raakaruokinta_koko_kirja_kuvitettu_tarkastusversio.pdf`: **283 sivua**, PDF-tekstipoiminta **563 467 merkkiä**.
- Poimittu teksti alkaa molemmissa samalla otsikolla ja päättyy samaan Diegolle omistettuun loppuun.
- Tiedostojen SHA-256-tiivisteet eroavat, joten PDF-tiedostot eivät ole bittitasolla identtiset. Pelkkä sama tekstimäärä ei yksin todista täydellistä sisältöidenttisyyttä.
- Sivukohtainen tekstivertailu ja kuvatason sisällön arviointi on tehtävä erikseen, jos vanhojen PDF-tiedostojen keskinäinen täydellinen identtisyys halutaan osoittaa.

## GitHubin nykyinen julkaisuvalmistelu
- `04_julkaisuversio/KOIRIEN_RAAKARUOKINTA_JULKAISUMASTER_v1.0.md`: noin 568 919 merkin Markdown-lähde.
- `04_julkaisuversio/DESIGNRR_TUONTI_v1.0.txt` on olemassa.
- `04_julkaisuversio/kasikirjoitus/` sisältää osiin jaetut lukutiedostot.
- `05_kuvat/Diego_01.jpg` … `Diego_06.jpg` ovat olemassa, ja `Diego_05.jpg` on aiemmin valittu kansikuvaehdokas.
- `04_julkaisuversio/KUVAVALINNAT_DIEGO_2026-10-16.md` ja `DIEGO_KUVIEN_TAITTOSUUNNITELMA_v0.1.md` dokumentoivat valinnat ja taittopaikat.

## Johtopäätös
Vanhan PDF:n **283 sivua ei ole uuden taiton sivumäärä**. Uusi PDF on rakennettava suoraan GitHubin nykyisestä julkaisumasterista ja kuudesta alkuperäiskuvasta. Tämän jälkeen sivumäärä, luvut, liitteet, lähteet ja tekstikattavuus täsmäytetään. Vanhan PDF:n kopiointia ei saa raportoida uudeksi koevedokseksi.

**Säilytys:** alkuperäisiin PDF-, Markdown- ja JPG-tiedostoihin ei tehdä poistavia muutoksia.
