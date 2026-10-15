# Julkaisuversion laadunvarmistus

**Päivä:** 16.10.2026  
**Versio:** 1.0  
**Tulos:** hyväksytty taiton lähtöaineistoksi

## Automaattinen tarkistus

Tarkistus suoritetaan komennolla:

```bash
python scripts/check_release.py
```

Hyväksytyn ajon tulos:

```text
JULKAISUTARKISTUS: HYVÄKSYTTY
Luvut: 27 (1–27)
Julkaisumasterin sanat: 70294
Käsikirjoitustiedostot: 58
Tekstiviitteiden avaimet: 205
Mahdollisesti puuttuvat lähdeavaimet: 0
Sovitut henkilökertomukset ja turvallisuusrajaukset: mukana
```

Sanamäärässä on 15 sanan ero manifestiin, koska tarkistus laskee myös masterin teknisen muodostuskommentin; lukijatekstin sanamäärä manifestissa on 70 279.

## Tarkistettu rakenne

- Lukunumerot 1–27 esiintyvät kerran ja oikeassa järjestyksessä.
- Viisi osaa, alkutekstit, loppusanat, neljä liitettä, lähteet, hakemisto ja julkaisutiedot ovat mukana.
- Pitkä ja lyhyt takakansiteksti on pidetty erillään leipätekstin masterista.
- Julkaisumasteri päättyy sovittuun viimeiseen sivuun ja sanaan `Diegolle.`

## Turvallisuus- ja lähdeauditointi

- FEDIAF 2025 -ravitsemusohje varmistettiin FEDIAFin virallisesta julkaisusta.
- WSAVA:n raakaruokaa koskeva riskilausuma ja Global Nutrition Toolkit tarkistettiin WSAVA:n virallisista aineistoista.
- Ruokaviraston raakaruoan, ekinokokin, villisian ja trikiinin ajantasaiset ohjeet tarkistettiin viranomaislähteistä.
- Mikrobiologisia riskejä, ravitsemuksellista epätasapainoa, eliminaatioruokavaliota, kroonista enteropatiaa sekä eläinlääkejäämiä koskevat ydinkohdat tarkistettiin alkuperäisistä vertaisarvioiduista julkaisuista tai PubMed-tietueista.
- Havainnoivat DogRisk-tulokset on kuvattu yhteyksinä, ei syy-yhteyden todisteina.

## Tarkistetut sovitut kertomukset

- Diego ja peura pääraaka-aineena
- Diego ja kalaöljy ilman varmistamatonta annostusohjetta
- Diego-puuro henkilökohtaisena muistona
- matkaruoka ja Diegon silmäoireet
- Diegon luupäivä turvallisuusrajauksineen
- Diegon pentueen demodikoosi
- Diegon virtsakivitapaus ilman yleistä hoitopäätelmää
- Jutta pienen koiran annostarkkuuden esimerkkinä
- Vekun luukätkö käyttäytymismuistona, ei hygieniaohjeena

## Jäljelle jäävät tuotantoportit

Julkaisuversio 1.0 on toimituksellisesti valmis. Kaupallisen julkaisemisen portteja ovat vielä ISBN- ja kustantajatiedot, kuvien käyttöoikeudet, taitto sekä nimetty riippumaton eläinlääketieteellinen ja juridinen loppulukeminen.

