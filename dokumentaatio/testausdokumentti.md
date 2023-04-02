## Testausdokumentti

#### Yksikkötestauksen kattavuusraportti tällä hetkellä
![image](https://user-images.githubusercontent.com/101889891/229354727-a633396a-36af-4355-bbd1-1d7a8e581c4b.png)

Testikattavuudesta on jätetty pois kokoaan UI:sta huolehtivat luokat, jotka ovat omassa kansiossaan UI.
Jätin myös pois tiedoston load_image.py sekä toistaiseksi minimax-algoritmin sisältävän tiedoston. Jätin algoritmin
toistaiseski testikattavuuden ulkopuolelle, koska en ole vielä käynyt algoritmien testausta koskevalla
luennolla, joten en tiedä miten sitä pitäisi testata järkevästi.

### Mitä on testattu
Olen tähän mennessä testannut Unittest-yksikkötesteillä pelilogiikan ja kaksinpelin toimintaa.
Pelilogiikan funktiot käyvät läpi taulukkoa, joka koostuu siis kuudesta seitsemän merkin pituisesta listasta.
Olen testeissä alustanut itse taulukot selkeäsi, jotta niiden sisällön näkee selkeämmin. 


### Testien suorittaminen
Minulla on projektissa käytössä GitHub Actions, joka suorittaa testit automaattisesti aina kun koodiin pushataan
muutoksia. Testit voivat muuten suorittaa juurihakemistossa komennolla ```pytest src``` tai poetryn kautta komennolla ```poetry run invoke test```

Testikattavuusraportin saa generoitua komennolla ```poetry run invoke coverage-report```
