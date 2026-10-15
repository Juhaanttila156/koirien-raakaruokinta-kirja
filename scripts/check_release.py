from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "04_julkaisuversio"
MANUSCRIPT = PUBLICATION / "kasikirjoitus"
MASTER = PUBLICATION / "KOIRIEN_RAAKARUOKINTA_JULKAISUMASTER_v1.0.md"


def citation_keys(text: str) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    for parenthesis in re.findall(r"\(([^()]*?(?:19|20)\d{2}[a-z]?[^()]*)\)", text):
        for item in re.split(r";\s*", parenthesis):
            match = re.match(
                r"(.+?)\s+((?:19|20)\d{2}[a-z]?(?:[–-](?:19|20)?\d{2})?)\.?$",
                item.strip(),
            )
            if not match:
                continue
            author = re.sub(r"\s+ym\.$", "", match.group(1).strip(), flags=re.I)
            keys.add((author.lower(), match.group(2).lower()))
    return keys


def main() -> None:
    text = MASTER.read_text(encoding="utf-8")
    all_chapters = [int(number) for number in re.findall(r"^# (\d+)\s", text, flags=re.M)]
    if all_chapters != list(range(1, 28)):
        raise SystemExit(f"Lukunumerointi ei ole 1–27: {all_chapters}")

    banned = {
        "rikkinäinen img-elementti": r"<img",
        "kenoviiva numeroidussa listassa": r"^\d+\\\.",
        "lähdelinkki otsikkona": r"^## \[",
        "vanha rotunimen kirjoitusasu": r"Dogo Argentino",
        "vanha kivennäiset-termi": r"\bkivennäiset\b",
        "epätarkka ikäilmaus": r"lähes 14",
        "varmistamaton kalaöljyn millilitramäärä": r"(?:50\s*millilitra|50\s*ml\s+kalaöljyä)",
    }
    for label, pattern in banned.items():
        if re.search(pattern, text, flags=re.M | re.I if label == "vanha kivennäiset-termi" else re.M):
            raise SystemExit(f"Laatuvirhe: {label}")

    required = {
        "Vekun luukätkö": "Vekun luukätkö",
        "Jutan esimerkki": "Jutta – kahden kilon tarkkuustyö",
        "Diegon matkaruokakokemus": "matkaruoka ja Diegon silmät",
        "eri aterioiden käytäntö": "eri aterioilla tai eri päivinä",
        "Diegon ikä": "yli 13-vuotiaaksi",
        "eläinlääkärirajaus": "TURVALLISUUS- JA ELÄINLÄÄKÄRIRAJAUS",
    }
    missing_required = [label for label, phrase in required.items() if phrase not in text]
    if missing_required:
        raise SystemExit("Sovitusta sisällöstä puuttuu: " + ", ".join(missing_required))

    references = (MANUSCRIPT / "67_lahteet.md").read_text(encoding="utf-8").lower()
    body_citations: set[tuple[str, str]] = set()
    for path in MANUSCRIPT.glob("*.md"):
        if path.name in {"67_lahteet.md", "68_asiahakemisto.md"}:
            continue
        body_citations |= citation_keys(path.read_text(encoding="utf-8"))

    aliases = {"nrc": "national research council"}
    missing_references = []
    for author, year in sorted(body_citations):
        first = re.split(r"[,& ]", author)[0].strip(".,")
        needle = aliases.get(first, first)
        base_year = re.match(r"\d{4}", year)
        if first and base_year and not (needle in references and base_year.group() in references):
            missing_references.append(f"{author} {year}")
    if missing_references:
        raise SystemExit("Lähdeluettelosta mahdollisesti puuttuu: " + ", ".join(missing_references))

    if not text.rstrip().endswith("Diegolle."):
        raise SystemExit("Julkaisumasterin viimeinen sivu ei pääty sovitusti.")

    words = len(re.findall(r"\b[\wÅÄÖåäöŠšŽž-]+\b", text, flags=re.UNICODE))
    chapter_files = len(list(MANUSCRIPT.glob("*.md")))
    print("JULKAISUTARKISTUS: HYVÄKSYTTY")
    print(f"Luvut: {len(all_chapters)} (1–27)")
    print(f"Julkaisumasterin sanat: {words}")
    print(f"Käsikirjoitustiedostot: {chapter_files}")
    print(f"Tekstiviitteiden avaimet: {len(body_citations)}")
    print("Mahdollisesti puuttuvat lähdeavaimet: 0")
    print("Sovitut henkilökertomukset ja turvallisuusrajaukset: mukana")


if __name__ == "__main__":
    main()
