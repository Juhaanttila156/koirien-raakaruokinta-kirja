# Täydellisen ZIP-varmuuskopion palautus

Alkuperäinen tiedosto:

`JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip`

Alkuperäinen koko: **62 153 290 tavua**  
Alkuperäinen SHA-256: `63f4f5769068f3d4191793b32f6d543c0025b26f174c3efe7fbe691cfb0f1de3`

GitHub-yhteyden 64 MiB viestikehys ei voinut siirtää tämän tiedoston base64-esitystä yhtenä blobina. Tiedosto on siksi jaettu tavurajoilta kahteen osaan ilman pakkausta tai sisällön muuttamista:

| Osa | Koko | SHA-256 |
| --- | ---: | --- |
| `JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip.part-001` | 31 457 280 | `5fc8f1ec7b34564625f9d96444117b27b23930d3d61eac8d0ad11ed4109322b2` |
| `JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip.part-002` | 30 696 010 | `315463d9381a963b44041185ea8d2e0d729ec6ea1cb6ad8df077509da55d9620` |

Osat sijaitsevat kansiossa:

`90_alkuperaiset/library-paakansio/Koirien raaka ruokinta lopullinen masterversio/`

## Yhdistä Linuxissa tai macOS:ssä

```bash
cat JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip.part-001 \
    JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip.part-002 \
    > JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip
sha256sum JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip
```

## Yhdistä Windowsissa

```powershell
cmd /c copy /b "JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip.part-001"+"JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip.part-002" "JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip"
Get-FileHash -Algorithm SHA256 "JP_Anttila_Koirien_raakaruokinta_TAYDELLINEN_VARMUUSKOPIO_2026-08-09.zip"
```

Palautetun tiedoston SHA-256:n pitää olla täsmälleen `63f4f5769068f3d4191793b32f6d543c0025b26f174c3efe7fbe691cfb0f1de3`.
