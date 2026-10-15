from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "02_luvut_preview"
TARGET = ROOT / "04_julkaisuversio" / "kasikirjoitus"


FILES = [
    ("44_omistuskirjoitus.md", "00a_omistuskirjoitus.md"),
    ("41_loppusanat.md", "61_mita_diego_opetti_minulle.md"),
    ("37_liite_a_usein_kysytyt_kysymykset.md", "62_liite_a_usein_kysytyt_kysymykset.md"),
    ("38_liite_b_malliviikot.md", "63_liite_b_malliviikot.md"),
    ("39_liite_c_laskenta_ja_seurantalomakkeet.md", "64_liite_c_laskenta_ja_seurantalomakkeet.md"),
    ("40_liite_d_sanasto.md", "65_liite_d_sanasto.md"),
    ("48_lahteiden_kaytto.md", "66_lahteiden_kaytto.md"),
    ("42_lahteet.md", "67_lahteet.md"),
    ("43_asiahakemisto.md", "68_asiahakemisto.md"),
    ("45_kiitokset.md", "69_kiitokset.md"),
    ("46_kirjoittajasta.md", "70_kirjoittajasta.md"),
    ("47_tietoa_tasta_kirjasta.md", "71_tietoa_tasta_kirjasta.md"),
    ("49_tekijanoikeussivu.md", "72_tekijanoikeussivu.md"),
    ("50_takakansiteksti_pitka_versio.md", "80_takakansiteksti_pitka_versio.md"),
    ("51_takakansiteksti_lyhyt_versio.md", "81_takakansiteksti_lyhyt_versio.md"),
    ("52_viimeinen_sivu.md", "82_viimeinen_sivu.md"),
]


TERMS = {
    "kivennäiset": "kivennäisaineet",
    "Kivennäiset": "Kivennäisaineet",
    "kivennäisten": "kivennäisaineiden",
    "kivennäisiä": "kivennäisaineita",
    "kivennäisissä": "kivennäisaineissa",
    "Dogo Argentino": "dogo argentino",
}


CHAPTER_MAP = {
    1: 23,
    2: 24,
    3: 5,
    4: 3,
    5: 4,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 9,
    13: 13,
    14: 25,
    15: 17,
    16: 18,
    17: 19,
    18: 20,
    19: 21,
    20: 22,
    21: 16,
    22: 12,
    23: 14,
    24: 15,
    25: 26,
    26: 27,
}


def normalize(text: str) -> str:
    for old, new in TERMS.items():
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    text = re.sub(r"^#\s{2,}", "# ", text, flags=re.M)
    text = text.replace("lähes 14 vuoden elämä", "yli 13 vuoden elämä")
    return text.strip() + "\n"


def update_faq(text: str) -> str:
    old = (
        "Voi, jos koira sietää yhdistelmän ja koko päivän energia sekä ravintoaineet huomioidaan. "
        "Ruoat eivät vaadi erillisiä mahalaukkuja. Käytännön ongelma syntyy useammin siitä, että "
        "täysravinnon rinnalle lisätään niin paljon epätasapainoisia aineksia, että kokonaisuus laimenee."
    )
    new = (
        "Voi käyttää samassa ruokavaliossa, jos koira sietää molemmat ja koko päivän energia sekä ravintoaineet huomioidaan. "
        "JP:n käytännössä raaka ja kuivaruoka tarjotaan eri aterioilla tai eri päivinä, ei samassa kulhossa. "
        "Tämä tekee annoksista ja koiran vasteesta helpommin seurattavia. Käytäntöä ei perustella väitteellä, "
        "ettei koiran ruoansulatus pystyisi käsittelemään ruokia yhdessä. Tavallisin ravitsemuksellinen ongelma syntyy siitä, "
        "että täysravinnon rinnalle lisätään niin paljon epätasapainoisia aineksia, että kokonaisuus laimenee."
    )
    text = text.replace(old, new)
    text = text.replace("(WSAVA 2011; katso luku 23.)", "(WSAVA 2011; katso luku 4.)")
    text = text.replace("(FEDIAF 2025; Ruokavirasto 2024–2026; katso luku 20.)", "(FEDIAF 2025; Ruokavirasto 2024–2026; katso luku 22.)")
    text = text.replace("(DogRisk 2021–2025; katso luku 25.)", "(DogRisk 2021–2025; katso luku 26.)")
    return text


def remap_index_reference(token: str) -> str:
    match = re.fullmatch(r"(\d+)(\.\d+)?(–\d+(?:\.\d+)?)?", token)
    if not match:
        return token
    chapter = int(match.group(1))
    if chapter not in CHAPTER_MAP:
        return token
    return str(CHAPTER_MAP[chapter]) + (match.group(2) or "") + (match.group(3) or "")


def update_index(text: str) -> str:
    out = []
    for line in text.splitlines():
        if line.startswith("**") and "**" in line[2:]:
            head, refs = line.rsplit("**", 1)
            refs = re.sub(
                r"(?<![A-Za-zÅÄÖåäö])\d+(?:\.\d+)?(?:–\d+(?:\.\d+)?)?",
                lambda m: remap_index_reference(m.group(0)),
                refs,
            )
            line = head + "**" + refs
        out.append(line)
    joined = "\n".join(out)
    joined = joined.replace(
        "## A\n",
        "## A\n\n**aloittamisen edellytykset** 1\n\n**arjen soveltuvuus raakaruokintaan** 1\n",
    )
    joined = joined.replace(
        "## T\n",
        "## T\n\n**turvallisen raakaruokinnan perussäännöt** 2\n\n**turvallisuus- ja eläinlääkärirajaus** alkuosa\n",
    )
    return joined


def main() -> None:
    for source_name, target_name in FILES:
        text = normalize((SOURCE / source_name).read_text(encoding="utf-8"))
        if source_name.startswith("37_"):
            text = update_faq(text)
        if source_name.startswith("43_"):
            text = update_index(text)
        provenance = (
            f"<!-- Lähde: 02_luvut_preview/{source_name}. Kielentarkistettu julkaisuversio 0.2, "
            "16.10.2026. Alkuperäinen lähdetiedosto säilyy muuttamattomana. -->\n\n"
        )
        (TARGET / target_name).write_text(provenance + text, encoding="utf-8")


if __name__ == "__main__":
    main()
