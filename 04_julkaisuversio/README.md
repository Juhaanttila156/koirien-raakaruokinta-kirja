# Koirien raakaruokinta – julkaisuversio 1.0

Tämä kansio sisältää 16.10.2026 lukitun, lukijalle toimitetun julkaisuversion. Lähde- ja arkistokerrokset säilyvät muualla repositoriossa muuttamattomina.

## Aloita tästä

- [Yhtenäinen julkaisumasteri](KOIRIEN_RAAKARUOKINTA_JULKAISUMASTER_v1.0.md)
- [Julkaisuversion manifesti ja jäljitettävyys](02_julkaisuversio_manifesti.md)
- [Lukittu sisällysluettelo](01_ehdotettu_sisallysluettelo.md)
- [Käsikirjoituksen osat](kasikirjoitus/)
- [Kielen ja toimitustyön tarkistusloki](../00_hallinta/SUOMEN_KIELEN_TARKISTUSLOKI_2026-10-16.md)
- [Laadunvarmistusraportti](../00_hallinta/JULKAISUVERSION_LAADUNVARMISTUS_2026-10-16.md)

## Sisältö

Julkaisumasterissa on:

- alkutekstit ja kolme lukupolkua;
- 27 numeroitua lukua viidessä osassa;
- JP:n, Diegon, Jutan ja Vekun henkilökohtaiset kertomukset, jotka on erotettu tutkimusväitteistä;
- usein kysytyt kysymykset, malliviikot, laskenta- ja seurantalomakkeet sekä sanasto;
- lukukohtaiset lähteet, koottu lähdeluettelo ja asiahakemisto;
- kiitokset, kirjoittaja- ja julkaisutiedot sekä viimeinen sivu.

Pitkä ja lyhyt takakansiteksti ovat erillistä tuotantoaineistoa eivätkä sisälly leipätekstin masteriin.

## Suojaussääntö

- `MASTER.md`, `02_luvut_preview/` ja `90_alkuperaiset/` ovat lähde- ja arkistoversioita.
- Julkaisuversion toimitustyö on tehty vain `04_julkaisuversio/`-kansioon.
- Lähdepolut ja tiedostokohtaiset tarkisteet ovat manifestissa.
- ISBN-, kustantaja-, kansi-, kuvitus-, taitto- ja tarkastajatiedot täytetään vasta, kun tuotantopäätökset on tehty.

## Toistettava koonti ja tarkistus

```bash
python scripts/build_release.py
python scripts/check_release.py
```

Ensimmäinen komento muodostaa masterin ja manifestin käsikirjoituksen osista. Toinen tarkistaa muun muassa lukujen järjestyksen, sovitut henkilökertomukset, turvallisuusrajaukset, tekniset Markdown-virheet ja lähdeavainten kattavuuden.

## Julkaisukynnys

Tekstitoimitus 1.0 on valmis taiton lähtöaineistoksi. Ennen kaupallista julkaisua täytetään tuotantotiedot, varmistetaan kaikkien valokuvien käyttöoikeudet sekä teetetään riippumaton eläinlääketieteellinen asiatarkistus ja juridinen loppulukeminen.

