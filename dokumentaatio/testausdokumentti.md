## Testausdokumentti

#### Yksikkötestauksen kattavuusraportti tällä hetkellä
![image](https://user-images.githubusercontent.com/101889891/232302689-cae63f9d-fc2c-495f-91b1-f17e0bf85c6f.png)

Testikattavuudesta on jätetty pois kokoaan UI:sta huolehtivat luokat, jotka ovat omassa kansiossaan UI.
Jätin myös pois tiedoston load_image.py.

### Mitä on testattu
Olen tähän mennessä testannut Unittest-yksikkötesteillä pelilogiikan, kaksinpelin toimintaa minimax-algorimin ja yksinpelin toimintaa.

Pelilogiikan funktiot käyvät läpi taulukkoa, joka koostuu siis kuudesta seitsemän merkin pituisesta listasta. Pelilogiikan testeissä (sekä muissa testeissä) olen alustanut itse taulukot, jotta pelilauta olisi helpompi visualisoida. Pelilogiikan testit testaavat, että src/files/game.py tiedoston luokan MainGame käyvät pelilautaa läpi tarkoitetulla tavalla. 

Minimax-algortimia ollaan testattu niin, että annetusta pelilaudasta algoritmi osaa laskea oikean heuristisen arvon, algorirmi osaa estää ihmispelaajan mahdollisen voiton sekä algoritmi osaa tehdä parhaimman siirron itsensä kannalta.

Pelin toiminnasta vastaavat luokat MultiPlayer ja SinglePlayer. Toimintaa olen testannut niin, että kun ihminen tai tietokone tekee siirron, luokat osaavat sijoittaa pelilaudalle nappulan tarkoitettuun kohtaan sekä tulktia pelilautaa ja asettaa luokkien boolean-muotoisille attribuuteille oikeat totuusarvot.


### Testien suorittaminen
Minulla on projektissa käytössä GitHub Actions, joka suorittaa testit automaattisesti aina kun koodiin pushataan
muutoksia. Testit voivat muuten suorittaa juurihakemistossa komennolla ```pytest src``` tai poetryn kautta komennolla ```poetry run invoke test```

Testikattavuusraportin saa generoitua komennolla ```poetry run invoke coverage-report```
