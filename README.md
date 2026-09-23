# Koirien raakaruokinta

Tämä repositorio on koirien raakaruokinta -kirjan itsenäinen GitHub-päärepo. SOTE-koulutus ja raakaruokintakirja pidetään eri repositorioissa.

## Ensisijainen tallennusmuoto

- Kaikki jatkossa laadittava ja hyväksytty tekstiaineisto tallennetaan Markdown-muodossa (`.md`).
- [MASTER.md](MASTER.md) on kirjan tekninen työskentelyn aloituspiste.
- `01_markdown/` sisältää lähdeaineistoista tehdyt Markdown-versiot.
- `90_alkuperaiset/` säilyttää alkuperäisten lähteiden hakemistorakennetta Markdown-esityksinä. Binaariset Word-, PDF-, ZIP-, XLSX- ja kuvatiedostot eivät ole aktiivisen jatkotyön ensisijaisia versioita.
- [MANIFEST.csv](00_hallinta/MANIFEST.csv) sisältää aineiston tiedostotietoja ja tarkisteita.
- [Google Drive -lähdeluettelo](00_hallinta/GOOGLE_DRIVE_LAHDELUETTELO.md) kuvaa migraatiossa löydetyt Drive-lähteet.

## Repositorion erottaminen SOTE-koulutuksesta

SOTE-repossa ollut `09_koirien_raakaruokinta`-kansion Markdown-aineisto tarkistettiin tätä repoa vasten. Kaikki 116 tekstitiedostoa olivat täällä samoilla poluilla ja samoilla Git-blob-tarkisteilla. Raakaruokinta-aineiston aktiivinen kopio poistettiin SOTE-reposta 23.9.2026.

Vanhojen Word-, PDF-, ZIP-, XLSX- ja kuvatiedostojen alkuperäiset versiot säilyvät tarvittaessa palautettavina Git-historiassa. Jatkotyö tehdään Markdown-tiedostoilla.

Tarkempi siirtotarkastus: [SIIRRON_TILA_2026-09-11.md](00_hallinta/SIIRRON_TILA_2026-09-11.md).

`MASTER.md` on tekninen työskentelyn aloituspiste, ei vielä vakuutus sisällön lääketieteellisestä tai ravitsemustieteellisestä oikeellisuudesta. Sisällön faktantarkistus ja lopullisen julkaisu-masterin valinta ovat erillisiä vaiheita.
