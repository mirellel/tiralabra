# Toteutusdokumentti

## Ohjelman tarkoitus
Ohjelmalla voi pelata Neljän suora -peliä tietokonetta tai kaveria vastaan. Pelin tarkoitus on saada neljä omaa pelinappulaa suoraan
joko vaaka- pysty- tai viistosuunnassa 7x6 kokoisella pelilaudalla. Tietokonetta vastaan pelatessa on kolme eri vaikeustasoa (helppo,
keskitaso, vaikea).

## Ohjelman rakenne

Ohjelma on koodattu kokonaan Pythonilla. Käyttöliittymään on käytetty Pythonin pygame-kirjastoa.

Tietokonepelaaja on toteutettu minimax-algoritmilla, jota on tehostettu alfa-beta-karsinnalla. Pelin eri vaikeustasot kutsuvat minimaxia eri syvyyksillä
eli vaikeampi vastustaja laskee pelitilanteita pidemmälle kuin helpompi vastustaja. 

Ohjelma on jaettu sovelluslogiikkaan ja käyttöliittymään, jotka sijaitsevat omissa kansioissaan files ja UI koko lähdekoodin sisältävän kansion src sisällä.

**Sovelluslogiikasta vastaavat luokat**:
- GameLogic: vastaa pelilaudasta ja sen läpikäymisen logiikasta
- Game: vastaa pelin kulusta ja pelilaudan päivittämisestä siirtojen jälkeen
- Minimax: sisältää minimax-algoritmin ja sen apufunktiot

**Käyttöliittymästä vastaavat luokat**:
- GameUI: määrittää pelinäkymän ruudun ja piirtää pelilaudan
- MenuUI: piirtää ohjelman aloitusmenun

**Muut luokat**:
- Menu: käsittelee MenuUI-luokan pygame-tapahtumia ja kutsuu sen funktioita
- MultiPlayer: pyörittää kahden ihmispelaajan välisen pelin pygame-tapahtumia
- SinglePlayer: pyörittää ihmispelaajan ja tietokoneen välisen pelin pygame-tapahtumia

Ohjelma käynnistyy tiedoston main.py avulla. Ohjelmaan tarvittavat kuvat ladataan tiedoston load_image.py avulla.


## Aika- ja tilavaativuudet

Minimaxalgoritmin, joka hyödyntää alpha-beta-karsintaa, aikavaativuus on O($\sqrt{b^d}$), jossa b on haarautumien määrä ja
d haun syvyys. Pelissä on 7 saraketta, johon pelinappulan voi laittaa ja kolme eri syvyysversiota, 2, 4 ja 6.
Toteutuva aikavaativuus on parhaimmillaan siis O($\sqrt{(7²)}$) ja huonoimmillaan O($\sqrt{(7⁶)}$). Neljän suorassa paras siirto löytyy useimmiten keskimmäisestä sarakkeesta, joten siirrot käydään läpi aloittaen keskisarakkeesta ja vuorotellen sen ympäriltä. Näin alfa-beta-karsinta on mahdollisimman tehokas, koska parhaat siirrot käsitellään aluksi.

Toisaalta jos paras siirto ei löydykkään keskeltä koko puu pitää käydä läpi eli alpha-beta-karsintaa ei voitu hyödyntää, on aikavaativuus O($b^d$) eli  O($7^d$).

Minimax-algortimin tilavaativuus on O(b * d), jossa b on haarautumien määrä ja d haun syvyys.

## Puutteet ja parannusehdotukset
- Minimaxin toimintaa olisi voinut nopeuttaa tehostamalla pelilogiikan funktioita
- Vihjeen antaminen kahden ihmispelaajalle parhaasta siirrotsa voisi olla hyvä lisä, jota en ehtinyt toteuttaa
- Voittotiedot olisi voinut tallentaa, jotta pelaaja näkee pelihistoriansa.

## Lähteet
[Minimax-pelit](https://tiralabra.github.io/2023_p4/fi/aiheet/minimax.pdf) pdf kurssisivulta 

Wikipedia (FI), [Neljän suora](https://fi.wikipedia.org/wiki/Nelj%C3%A4n_suora)

Wikipedia (ENG), [Minimax](https://en.wikipedia.org/wiki/Minimax)

Wikipedia (ENG), [Alpha-beta-karsinta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)

GeeksForGeeks, [Minmax algorithm in game theory](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/)
