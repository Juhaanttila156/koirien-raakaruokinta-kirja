# Koirien raakaruokinta

Tämä kansio kokoaa koirien raakaruokinta -kirjan löydetyt Google Drive- ja ChatGPT Library -aineistot yhteen Git-versionhallittavaan muotoon.

## Aloita tästä

- [MASTER.md](MASTER.md) on suora Markdown-muunnos uusimmasta selvästi versionumerolla nimetystä kokonaisesta Library-masterista: `JP_Anttila_Koirien_raakaruokinta_koko_kirja_v9.docx`.
- `01_markdown/` sisältää jokaiselle löydetylle lähdetiedostolle oman Markdown-version. Alkuperäinen tiedostopääte säilyy nimessä, esimerkiksi `nimi.pdf.md` ja `nimi.docx.md`.
- `90_alkuperaiset/` sisältää alkuperäiset PDF-, DOCX-, ZIP-, XLSX-, kuva- ja tekstitiedostot.
- [MANIFEST.csv](00_hallinta/MANIFEST.csv) sisältää tiedostokoot ja SHA-256-tarkisteet.
- [Google Drive -lähdeluettelo](00_hallinta/GOOGLE_DRIVE_LAHDELUETTELO.md) sisältää kaikki 58 löydettyä Drive-lähdettä ja niiden tunnukset.

## Aineistomäärä

- Google Drive: **58** lähdetiedostoa
- ChatGPT Library: **34** lähdetiedostoa
- alkuperäisiä tiedostoja: **92**
- Markdown-pari jokaiselle alkuperäiselle tiedostolle
- v9-masterin kuvat on erotettu `01_markdown/library-paakansio/assets/`-kansioon ja linkitetty `MASTER.md`-tiedostosta

Täydellinen 62 153 290 tavun ZIP-varmuuskopio on GitHub-yhteyden siirtokehyksen vuoksi tallennettu kahteen häviöttömään osaan. [Palautusohje ja tarkistussummat](00_hallinta/SUUREN_ZIPIN_PALAUTUS.md) osoittavat, miten alkuperäinen ZIP kootaan täsmälleen takaisin.

Täsmälleen samanlaisia versioita ei ole poistettu. Manifesti ryhmittelee ne tarkistussumman perusteella, jotta myöhempi siivous voidaan tehdä hallitusti.

`MASTER.md` on tekninen työskentelyn aloituspiste, ei vielä vakuutus sisällön lääketieteellisestä tai ravitsemustieteellisestä oikeellisuudesta. Sisällön faktantarkistus ja lopullisen julkaisu-masterin valinta ovat erillisiä vaiheita.
