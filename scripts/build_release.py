from __future__ import annotations

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "04_julkaisuversio"
MANUSCRIPT = PUBLICATION / "kasikirjoitus"
MASTER = PUBLICATION / "KOIRIEN_RAAKARUOKINTA_JULKAISUMASTER_v1.0.md"
MANIFEST = PUBLICATION / "02_julkaisuversio_manifesti.md"


ORDER = [
    "00_nimiotiedot.md",
    "00a_omistuskirjoitus.md",
    "00b_sisallysluettelo.md",
    "01_lukijalle.md",
    "02_alkusanat.md",
    "03_jp_ja_diego.md",
    "04_raakaruokinnan_eri_suuntaukset.md",
    "05_mita_raakaruokinta_tassa_kirjassa_tarkoittaa.md",
    "06_nain_kaytat_tata_kirjaa.md",
    "07_turvallisuus_ja_elainlaakarirajaus.md",
    "10_osa_i_aloita_turvallisesti.md",
    "11_01_sopiiko_raakaruokinta_meidan_arkeemme.md",
    "12_02_kymmenen_turvallisen_raakaruokinnan_perussaantoa.md",
    "13_03_kuinka_paljon_koira_tarvitsee_ruokaa.md",
    "14_04_hallittu_siirtyminen_raakaruokintaan.md",
    "15_05_pelkka_liha_ei_riita.md",
    "20_osa_ii_rakenna_tasapainoinen_annos.md",
    "21_06_lihalajien_ja_raaka_aineiden_valinta.md",
    "22_07_luut_kalsium_ja_fosfori.md",
    "23_08_sisaelimet.md",
    "24_09_rasva_kala_epa_ja_dha.md",
    "25_10_hiilihydraatit_kasvikset_ja_kuitu.md",
    "26_11_vitamiinit_kivennaisaineet_ja_lisaravinteet.md",
    "27_12_ruokintasuunnitelma_vaihe_vaiheelta.md",
    "30_osa_iii_tee_suunnitelmasta_toimiva_arki.md",
    "31_13_hygienia_ja_mikrobiologinen_turvallisuus.md",
    "32_14_ruokintarutiini_sailytys_ja_matkustaminen.md",
    "33_15_seuraa_koiraa_ja_saada_yhta_asiaa_kerrallaan.md",
    "34_16_tavallisimmat_virheet_ja_niiden_korjaaminen.md",
    "40_osa_iv_sovita_ruokinta_koiraan.md",
    "41_17_pennut_tiineys_ja_imetys.md",
    "42_18_seniorikoira.md",
    "43_19_pieni_suuri_ja_aktiivinen_koira.md",
    "44_20_allergiaepailyt_iho_korvat_ja_ruoansulatusoireet.md",
    "45_21_sairaus_muuttaa_ruokinnan_tavoitteen.md",
    "46_22_riista_turvallisena_ja_jaljitettavana_raaka_aineena.md",
    "50_osa_v_ymmarra_tausta_ja_nayton_rajat.md",
    "51_23_koira_petoelaintaustaisena_ja_ravitsemuksellisesti_joustavana_elaimena.md",
    "52_24_raaka_kypsennetty_ja_ekstrudoitu_ruoka.md",
    "53_25_mahahappo_ruoansulatus_ja_suolistomikrobisto.md",
    "54_26_mita_tutkimus_voi_kertoa_ja_mita_ei.md",
    "55_27_tulevaisuus_ja_elava_tietopohja.md",
    "60_loppuosa.md",
    "60a_koiran_ja_ihmisen_kiintymys_ja_menetys.md",
    "61_mita_diego_opetti_minulle.md",
    "62_liite_a_usein_kysytyt_kysymykset.md",
    "63_liite_b_malliviikot.md",
    "64_liite_c_laskenta_ja_seurantalomakkeet.md",
    "65_liite_d_sanasto.md",
    "66_lahteiden_kaytto.md",
    "67_lahteet.md",
    "68_asiahakemisto.md",
    "69_kiitokset.md",
    "70_kirjoittajasta.md",
    "71_tietoa_tasta_kirjasta.md",
    "72_tekijanoikeussivu.md",
    "82_viimeinen_sivu.md",
]


PRODUCTION_ONLY = [
    "80_takakansiteksti_pitka_versio.md",
    "81_takakansiteksti_lyhyt_versio.md",
]


def words(text: str) -> int:
    return len(re.findall(r"\b[\wÅÄÖåäöŠšŽž-]+\b", text, flags=re.UNICODE))


def provenance(text: str) -> str:
    match = re.match(r"<!--\s*(.*?)\s*-->\s*", text, flags=re.S)
    if not match:
        return "Julkaisuversiossa kirjoitettu tai koottu"
    return " ".join(match.group(1).split())


def reader_copy(text: str) -> str:
    return re.sub(r"^<!--.*?-->\s*", "", text, count=1, flags=re.S).strip()


def validate() -> None:
    missing = [name for name in ORDER + PRODUCTION_ONLY if not (MANUSCRIPT / name).is_file()]
    if missing:
        raise SystemExit("Puuttuvat julkaisutiedostot: " + ", ".join(missing))

    problems: list[str] = []
    for name in ORDER + PRODUCTION_ONLY:
        text = (MANUSCRIPT / name).read_text(encoding="utf-8")
        if not re.search(r"^#\s+\S", text, flags=re.M):
            problems.append(f"{name}: pääotsikko puuttuu")
        if "<img" in text:
            problems.append(f"{name}: rikkinäiseksi jäävä img-elementti")
        if re.search(r"^\d+\\\.", text, flags=re.M):
            problems.append(f"{name}: numeroidussa listassa on kenoviiva")
        if re.search(r"^## \[", text, flags=re.M):
            problems.append(f"{name}: lähdelinkki on virheellisesti otsikko")
    if problems:
        raise SystemExit("Julkaisun laadunvarmistus epäonnistui:\n- " + "\n- ".join(problems))


def build_master() -> None:
    sections = [
        "<!-- Julkaisumasteri 1.0, muodostettu tiedostosta scripts/build_release.py. "
        "Lukukohtaiset lähde- ja muokkaustiedot ovat 02_julkaisuversio_manifesti.md-tiedostossa. -->"
    ]
    for name in ORDER:
        text = (MANUSCRIPT / name).read_text(encoding="utf-8")
        sections.append(reader_copy(text))
    MASTER.write_text("\n\n---\n\n".join(sections).rstrip() + "\n", encoding="utf-8")


def build_manifest() -> None:
    rows = []
    total_words = 0
    for index, name in enumerate(ORDER, start=1):
        data = (MANUSCRIPT / name).read_bytes()
        text = data.decode("utf-8")
        word_count = words(reader_copy(text))
        total_words += word_count
        digest = hashlib.sha256(data).hexdigest()[:12]
        source = provenance(text).replace("|", "\\|")
        rows.append(f"| {index} | `{name}` | {word_count} | `{digest}` | {source} |")

    production_rows = []
    for name in PRODUCTION_ONLY:
        data = (MANUSCRIPT / name).read_bytes()
        production_rows.append(
            f"| `{name}` | {words(reader_copy(data.decode('utf-8')))} | `{hashlib.sha256(data).hexdigest()[:12]}` |"
        )

    content = f"""# Julkaisuversio 1.0 – manifesti

**Koontipäivä:** 19.10.2026  
**Julkaisumasteri:** `KOIRIEN_RAAKARUOKINTA_JULKAISUMASTER_v1.0.md`  
**Masterin sanamäärä:** {total_words}  
**Lukuja:** 27  
**Loppuosan lisäys:** JP Anttilan 19.10.2026 hyväksymä ja lukitsema kiintymys- ja menetysosuus sekä henkilökohtainen Diego-päätösteksti.

Julkaisumasteri muodostetaan alla olevista tiedostoista tässä järjestyksessä komennolla `python scripts/build_release.py`. Lukukohtaiset HTML-kommentit säilyttävät yhteyden muuttamattomaan lähdeaineistoon, mutta ne poistetaan lukijalle tarkoitetusta koontitiedostosta.

## Julkaisumasterin tiedostot

| Järjestys | Tiedosto | Sanoja | SHA-256 (12) | Jäljitettävyys |
|---:|---|---:|---|---|
{chr(10).join(rows)}

## Erillinen tuotantoaineisto

Takakansiteksteistä valitaan taitossa vain toinen. Ne eivät kuulu kirjan leipätekstin julkaisumasteriin.

| Tiedosto | Sanoja | SHA-256 (12) |
|---|---:|---|
{chr(10).join(production_rows)}

## Versiorajaus

- `MASTER.md`, `02_luvut_preview/` ja `90_alkuperaiset/` ovat lähde- ja arkistoaineistoa, eikä niitä korvata julkaisumasterilla.
- Julkaisumasteri 1.0 on toimitettu lukijaversio. Se on valmis taiton, ISBN-tietojen, kuvituksen, riippumattoman eläinlääketieteellisen asiatarkistuksen ja juridisen loppulukemisen lähtöaineistoksi.
- Hakasulkeisiin jätetyt kustannus-, ISBN-, kansi-, kuva-, taitto-, kielenhuolto-, asiatarkistus- ja verkkotiedot täytetään tuotantopäätösten jälkeen.
"""
    MANIFEST.write_text(content, encoding="utf-8")


def main() -> None:
    validate()
    build_master()
    build_manifest()
    print(f"Valmis: {MASTER.relative_to(ROOT)}")
    print(f"Valmis: {MANIFEST.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
