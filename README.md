# XTILO - Semestrální práce

## Popis
Předmětem semestrální práce je Turingův stroj pro násobení binárních čísel
(které jsem si popravdě řečeno musel připomenout <sup>[1]</sup>).
Kromě tohoto popisu ji tvoří tři soubory - soubor `turing_machine.py`, `tape.py` 
a `run.py`. Při tvorbě jsem vyšel z již existující implementace pythonového
Turingova stroje pro tvorbu komplementu binárního čísla <sup>[2]</sup>.
V souboru `turing_machine.py` je Turingův stroj reprezentován objektem, resp. třídou,
jejíž součástí je objekt `Tape` (což není nic jiného než string převedený na
dictionary, kde jsou jednotlivé znaky očíslovány pomocí funkce `enumerate`)
a dále proměnné, jejichž názvy jsou, myslím, samopopisné - `head_position`,
`blank_symbol`, `current_state`, `transition_functions` a `final_states`.
Má také metody `next_step()`, která zvětšuje nebo zmenšuje index reprezentující
vzdálenost čtecí hlavy od počáteční pozice o jedna na základě instrukce v přechodové funkci a přepisuje znak na daném poli, `should_finish()`, která
kontroluje, zda je stroj v konečném stavu, pomocnou metodu `get_head()`, která
vypisuje pozici čtecí hlavy (spíše pro účely debuggingu) a `get_tape()`, která volá getter třídy `Tape`.

Hlavní slabinou implementace, ze které jsem vycházel, bylo, že pro své účely počítala pouze s pevně daným počtem
znaků na pásce. Avšak protože Turingův stroj má být schopný pracovat s páskou,
která je nekonečně dlouhá, bylo potřeba getter třídy `Tape` upravit tak,
aby si sám "dotvářel" pásku, pokud se čtecí hlavice dostane mimo (konečný) uživatelem definovaný string, reprezentující relevantní část pásky.
Původní implementace pracovala s indexy pythonovsky, tedy index `-1` znamenal přesun
odkaz na nejvyšší index (smyčka ze začátku na konec). V mé implementaci přesun
na neexistující index vytvoří nový dictionary s vyšším, resp. nižší indexem a prázdným znakem
a připojí ho k již existující pásce, což stroji umožňuje posouvat hlavu neomezeně daleko od počáteční pozice.

Soubor `run.py` obsahuje konkrétní definici počátečního stavu, množiny konečných stavů
a množiny přechodových funkcí, která je reprezentována jako dictionary, kde
klíčem je tuple (stav, znak) a hodnotou je tuple (následující stav, znak k zapsání, směr pohybu hlavy).
Klíč tedy definuje, v jakém stavu musí stroj být a jaký znak musí číst, aby se vykonaly instrukce v druhém tuplu.
Následuje samotné vytvoření stroje, přidělení hodnot a smyčka, která volá jednotlivé kroky, dokud
stroj nedojde do konečného stavu, přičemž vypisuje momentální stav, pásku a pozici hlavy na ní.

Největší problém byla samotná definice přechodových funkcí. Tu jsem ani po mnoha pokusech nemohl vyřešit
a až při hledání inspirace v již existujícím řešení <sup>[3]</sup> jsem si uvědomil možnost
využít abecedu větší než jen 0 a 1. I tak se jedná o poměrně komplexní řešení, které problém
řeší v cca 90 krocích.

![Diagram](https://t4tutorials.com/wp-content/uploads/Turing-machine-to-Multiply-two-binary-numbers.gif)

## Zdroje:

[1] http://fyzika.jreichl.com/main.article/view/1559-soucin-dvou-cisel-ve-dvojkove-soustave

[2] https://python-course.eu/applications-python/turing-machine.php

[3] https://t4tutorials.com/turing-machine-to-multiply-two-binary-numbers/