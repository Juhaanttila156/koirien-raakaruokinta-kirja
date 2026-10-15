from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "02_luvut_preview"
TARGET = ROOT / "04_julkaisuversio" / "kasikirjoitus"


CHAPTERS = [
    (6, "16_6_lihalajien_valinta.md", "21_06_lihalajien_ja_raaka_aineiden_valinta.md", "LIHALAJIEN JA RAAKA-AINEIDEN VALINTA", "Hyvä perusraaka-aine sopii koiralle, on koostumukseltaan riittävän tunnettu, turvallisesti hankittu ja arjessa saatavilla. Eläinlajin nimi ei yksin kerro tuotteen rasvaa, luuta, sisäelimiä tai ravintoarvoa."),
    (7, "17_7_luut_ja_kalsium.md", "22_07_luut_kalsium_ja_fosfori.md", "LUUT, KALSIUM JA FOSFORI", "Luu on sekä ravintoaineiden lähde että mekaaninen riski. Kalsium ja fosfori lasketaan koko annoksesta; luun turvallisuus arvioidaan erikseen koiran koon, purutavan ja luun ominaisuuksien perusteella."),
    (8, "18_8_sisaelimet.md", "23_08_sisaelimet.md", "SISÄELIMET", "Maksa, munuainen, perna, sydän ja pötsi eivät ole ravitsemuksellisesti sama raaka-aine. Sisäelimet punnitaan ja valitaan tehtävänsä mukaan; sydän on pääosin lihaskudosta eikä korvaa maksaa."),
    (10, "20_10_hiilihydraatit_kasvikset_ja_kuitu.md", "25_10_hiilihydraatit_kasvikset_ja_kuitu.md", "HIILIHYDRAATIT, KASVIKSET JA KUITU", "Koira ei tarvitse hiilihydraatteja samalla tavalla kuin välttämättömiä amino- ja rasvahappoja, mutta kypsennetty tärkkelys ja tarkoituksenmukainen kuitu voivat olla käyttökelpoisia. Raaka-aine valitaan tehtävän, ei maineen perusteella."),
    (11, "21_11_vitamiinit_kivennaiset_ja_lisaravinteet.md", "26_11_vitamiinit_kivennaisaineet_ja_lisaravinteet.md", "VITAMIINIT, KIVENNÄISAINEET JA LISÄRAVINTEET", "Lisäravinne ei korjaa epäselvää reseptiä. Ensin lasketaan koko annos, sitten täydennetään vain todettu tarve tuotteen todellisten pitoisuuksien ja koiran elämänvaiheen mukaan."),
    (12, "32_22_ruokintasuunnitelman_rakentaminen.md", "27_12_ruokintasuunnitelma_vaihe_vaiheelta.md", "RUOKINTASUUNNITELMA VAIHE VAIHEELTA", "Toimiva suunnitelma alkaa koirasta ja tavoitteesta, etenee energian ja ravintoaineiden laskentaan ja päätyy grammoiksi, valmistuseräksi, sallituiksi vaihdoiksi sekä ennalta sovituksi seurannaksi."),
    (13, "23_13_hygienia_ja_mikrobiologinen_turvallisuus.md", "31_13_hygienia_ja_mikrobiologinen_turvallisuus.md", "HYGIENIA JA MIKROBIOLOGINEN TURVALLISUUS", "Raaka ruoka ei ole steriiliä, eikä terveen koiran vahva ruoansulatuspuolustus poista kotitalouden ristikontaminaation riskiä. Tunnettu raaka-aine, katkeamaton kylmäketju, käsien ja välineiden pesu sekä riskiryhmien huomioiminen muodostavat turvallisen arjen."),
    (14, "33_23_ruokintarutiini.md", "32_14_ruokintarutiini_sailytys_ja_matkustaminen.md", "RUOKINTARUTIINI, SÄILYTYS JA MATKUSTAMINEN", "Hyvä resepti toimii vain, jos se voidaan toistaa arjessa. Punnitse, annostele, sulata ja tarjoa ruoka samalla selkeällä tavalla myös kiireessä ja matkalla."),
    (15, "34_24_koiran_seuraaminen.md", "33_15_seuraa_koiraa_ja_saada_yhta_asiaa_kerrallaan.md", "SEURAA KOIRAA JA SÄÄDÄ YHTÄ ASIAA KERRALLAAN", "Seuranta yhdistää painon, kehon kuntoluokan, lihaskunnon, ruoansulatuksen, ihon, turkin, juomisen, virtsaamisen, liikkeen ja palautumisen. Muutos tehdään hallitusti, jotta sen vaikutusta voidaan arvioida."),
    (16, "31_21_tavallisimmat_virheet.md", "34_16_tavallisimmat_virheet_ja_niiden_korjaaminen.md", "TAVALLISIMMAT VIRHEET JA NIIDEN KORJAAMINEN", "Useimmat ongelmat syntyvät toistuvista oletuksista, eivät yhdestä suuresta virheestä. Kirjoita toteutunut ruokinta näkyväksi, korjaa suurin riski ensin ja tee seuraavasta versiosta niin helppo, että sitä voidaan noudattaa."),
    (17, "25_15_pennut_tiineys_ja_imetys.md", "41_17_pennut_tiineys_ja_imetys.md", "PENNUT, TIINEYS JA IMETYS", "Kasvu ja lisääntyminen sietävät huonosti summittaisen reseptin. Energia, kalsium, fosfori, rasvahapot ja muut välttämättömät ravintoaineet on laskettava elämänvaiheen mukaan ja kasvua seurattava järjestelmällisesti."),
    (18, "26_16_seniorikoira.md", "42_18_seniorikoira.md", "SENIORIKOIRA", "Ikä ei yksin määrää ruokavaliota. Seniorin ruokinta rakennetaan lihasmassan, energiansaannin, suun terveyden, liikkumisen, sairauksien, lääkitysten ja yksilöllisen seurannan ympärille."),
    (19, "27_17_pieni_suuri_ja_aktiivinen_koira.md", "43_19_pieni_suuri_ja_aktiivinen_koira.md", "PIENI, SUURI JA AKTIIVINEN KOIRA", "Samat ravintoaineet koskevat kaikkia koiria, mutta mittakaava, energiatiheys, annostelutarkkuus ja käytännön toteutus muuttuvat koon ja aktiivisuuden mukaan."),
    (20, "28_18_allergiat_iho_korvat_ja_ruoansulatusoireet.md", "44_20_allergiaepailyt_iho_korvat_ja_ruoansulatusoireet.md", "ALLERGIAEPÄILYT, IHO, KORVAT JA RUOANSULATUSOIREET", "Oire ei yksin nimeä ruoka-ainetta eikä syytä. Ruokareaktio selvitetään eläinlääkärin arvion, tarkasti rajatun eliminaatioruokavalion ja hallitun altistuksen avulla."),
    (21, "29_19_raakaruokinta_sairauden_aikana.md", "45_21_sairaus_muuttaa_ruokinnan_tavoitteen.md", "SAIRAUS MUUTTAA RUOKINNAN TAVOITTEEN", "Sairaus voi muuttaa ruokinnan tavoitteen kokonaan. Diagnoosi, sairauden vaihe, lääkitys ja hoitavan eläinlääkärin suunnitelma menevät yleisen ruokintamallin edelle."),
    (22, "30_20_riista.md", "46_22_riista_turvallisena_ja_jaljitettavana_raaka_aineena.md", "RIISTA TURVALLISENA JA JÄLJITETTÄVÄNÄ RAAKA-AINEENA", "Riista voi olla erinomainen, vähärasvainen ja jäljitettävä perusraaka-aine. Turvallinen käyttö edellyttää lajin, alkuperän, käsittelyketjun, ampumajäämien, loisten ja todellisen ravintosisällön tuntemista."),
    (25, "24_14_mahahappo_ruoansulatus_ja_suolistomikrobisto.md", "53_25_mahahappo_ruoansulatus_ja_suolistomikrobisto.md", "MAHAHAPPO, RUOANSULATUS JA SUOLISTOMIKROBISTO", "Koiran mahalaukku voi olla hyvin hapan, mutta pH muuttuu aterian ja ajan mukana. Mahahappo on yksi puolustuskerros, ei takuu siitä, että pilaantunut tai vaarallisesti käsitelty ruoka olisi turvallista."),
    (26, "35_25_mita_tutkimus_voi_kertoa.md", "54_26_mita_tutkimus_voi_kertoa_ja_mita_ei.md", "MITÄ TUTKIMUS VOI KERTOA – JA MITÄ EI", "Tutkimuksen johtopäätös on aina sidottu kysymykseen, asetelmaan, vertailuun, aineistoon ja mitattuun lopputulokseen. Yhteys ei yksin osoita syytä, eikä yksittäinen biomarkkeri ratkaise koiran kokonaisterveyttä."),
    (27, "36_26_raakaruokinnan_tulevaisuus.md", "55_27_tulevaisuus_ja_elava_tietopohja.md", "TULEVAISUUS JA ELÄVÄ TIETOPOHJA", "Raakaruokinnan tulevaisuus rakentuu tarkemmasta ravintoainetiedosta, paremmasta jäljitettävyydestä, todennetuista turvallisuusprosesseista ja pitkäaikaisesta seurannasta. Siksi kirjan lähdepohjaa ylläpidetään elävänä aineistona."),
]


TERM_REPLACEMENTS = {
    "kivennäiset": "kivennäisaineet",
    "Kivennäiset": "Kivennäisaineet",
    "kivennäisten": "kivennäisaineiden",
    "Kivennäisten": "Kivennäisaineiden",
    "kivennäisiä": "kivennäisaineita",
    "Kivennäisiä": "Kivennäisaineita",
    "kivennäisissä": "kivennäisaineissa",
    "kivennäisistä": "kivennäisaineista",
    "kivennäisille": "kivennäisaineille",
    "Dogo Argentino": "dogo argentino",
    "Golden Retriever": "kultainennoutaja",
    "Labrador": "labradorinnoutaja",
    "German Shepherd": "saksanpaimenkoira",
}


def replace_terms(text: str) -> str:
    for old, new in TERM_REPLACEMENTS.items():
        text = re.sub(rf"\b{re.escape(old)}\b", new, text)
    return text


def clean_heading(line: str, old_number: int, new_number: int) -> str:
    match = re.match(r"^(#{1,6})\s+(.*)$", line)
    if not match:
        return line
    marks, title = match.groups()
    title = title.replace("\\*", "*").strip()
    title = re.sub(r"^\*{1,3}|\*{1,3}$", "", title).strip()
    title = re.sub(rf"^{old_number}\.(\d+)\b", rf"{new_number}.\1", title)
    title = re.sub(rf"^LUVUN\s+{old_number}\b", f"LUVUN {new_number}", title)
    return f"{marks} {title}"


def clean_source(text: str, old_number: int, new_number: int, title: str) -> str:
    # Publication files must not contain broken references to archived image assets.
    text = re.sub(
        r'<img[^>]+/>\s*\n\s*\*([^\n]+)\*',
        lambda m: f"> **Kuvapaikka:** {m.group(1).strip()}",
        text,
        flags=re.I,
    )
    text = re.sub(r"^<img[^>]+/>\s*$", "", text, flags=re.I | re.M)
    text = replace_terms(text)
    lines = text.splitlines()
    if not lines:
        return text
    lines[0] = f"# {new_number} {title}"
    lines = [clean_heading(line, old_number, new_number) for line in lines]
    text = "\n".join(lines).strip() + "\n"
    # Remove repeated blank lines introduced by image cleanup.
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text


def source_number(filename: str) -> int:
    match = re.search(r"_(\d+)_", filename)
    if not match:
        raise ValueError(filename)
    return int(match.group(1))


def write_chapter(new_number: int, source_name: str, target_name: str, title: str, summary: str) -> None:
    old_number = source_number(source_name)
    raw = (SOURCE / source_name).read_text(encoding="utf-8")

    # Two early source chapters contain an older essay followed by a newer concise chapter.
    if source_name == "18_8_sisaelimet.md":
        marker = "Sisäelimet ovat pieni mutta ravitsemuksellisesti voimakas osa raakaruokavaliota."
        raw = "# 8 SISÄELIMET\n\n" + raw[raw.index(marker):]

    body = clean_source(raw, old_number, new_number, title)
    provenance = (
        f"<!-- Lähde: 02_luvut_preview/{source_name}. "
        "Kielentarkistettu ja uudelleen numeroitu julkaisuversio 0.2, 16.10.2026. "
        "Alkuperäinen lähdetiedosto säilyy muuttamattomana. -->\n\n"
    )
    answer = f"> **Vastaus minuutissa:** {summary}\n\n"
    first_break = body.find("\n\n")
    if first_break == -1:
        finished = provenance + body + "\n" + answer
    else:
        finished = provenance + body[: first_break + 2] + answer + body[first_break + 2 :]
    (TARGET / target_name).write_text(finished, encoding="utf-8")


def build_fat_and_fish() -> None:
    fat = (SOURCE / "19_9_rasva_ja_rasvahapot.md").read_text(encoding="utf-8")
    concise = "Rasva on koiralle tiivis energianlähde"
    fat = "# 9 RASVA, KALA, EPA JA DHA\n\n" + fat[fat.index(concise):]
    fish = (SOURCE / "22_12_kala_ja_merenelavat.md").read_text(encoding="utf-8")
    fish = re.sub(r"^# 12 KALA JA MERENELÄVÄT\s*", "## Kala ja merenelävät\n\n", fish)
    merged = clean_source(fat, 9, 9, "RASVA, KALA, EPA JA DHA").rstrip()
    merged += "\n\n" + clean_source(fish, 12, 9, "RASVA, KALA, EPA JA DHA").split("\n", 1)[1].lstrip()
    # Remove the unsafe unverified historical dose from reader-facing copy while retaining it in the source.
    merged = re.sub(
        r"Diego sai valmistetta noin 50 millilitraa.*?toiseen tuotteeseen\.\s*",
        "Diego sai samaa valmistetta säännöllisesti koko elämänsä ajan. Alkuperäiseen muistiinpanoon kirjattu millilitramäärä on säilytetty lähdeaineistossa, mutta sitä ei julkaista annosteluohjeena ennen tuotteen ja pitoisuuksien varmistamista. Kokemus ei ole yleinen annossuositus. ",
        merged,
        flags=re.S,
    )
    provenance = (
        "<!-- Lähteet: 02_luvut_preview/19_9_rasva_ja_rasvahapot.md ja "
        "02_luvut_preview/22_12_kala_ja_merenelavat.md. Yhdistetty ja kielentarkistettu "
        "julkaisuversio 0.2, 16.10.2026. Alkuperäiset lähdetiedostot säilyvät muuttamattomina. -->\n\n"
    )
    answer = (
        "> **Vastaus minuutissa:** Rasvan määrä ratkaisee suuren osan annoksen energiasta, mutta rasvan laatu ratkaisee, mitä rasvahappoja koira saa. Kala ja kalaöljy eivät ole sama raaka-aine: tuotetta arvioidaan todellisen EPA- ja DHA-määrän, energian, hapettumissuojan ja koko reseptin perusteella.\n\n"
    )
    split = merged.find("\n\n")
    merged = provenance + merged[: split + 2] + answer + merged[split + 2 :]
    (TARGET / "24_09_rasva_kala_epa_ja_dha.md").write_text(merged, encoding="utf-8")


def main() -> None:
    TARGET.mkdir(parents=True, exist_ok=True)
    for args in CHAPTERS:
        write_chapter(*args)
    build_fat_and_fish()


if __name__ == "__main__":
    main()
