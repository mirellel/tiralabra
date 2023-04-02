## Testausdokumentti

#### Yksikkötestauksen kattavuusraportti tällä hetkellä
![image](https://user-images.githubusercontent.com/101889891/229357012-fa21bcfc-58c6-4508-befb-08ab829b62fa.png)

Testikattavuudesta on jätetty pois kokoaan UI:sta huolehtivat luokat, jotka ovat omassa kansiossaan UI.
Jätin myös pois tiedoston load_image.py. Testikattavuus jäi pieneksi, koska en vielä ole testannut minimax-algoritmia.

### Mitä on testattu
Olen tähän mennessä testannut Unittest-yksikkötesteillä pelilogiikan ja kaksinpelin toimintaa.
Pelilogiikan funktiot käyvät läpi taulukkoa, joka koostuu siis kuudesta seitsemän merkin pituisesta listasta.
Olen testeissä alustanut itse taulukot selkeäsi, jotta niiden sisällön näkee selkeämmin. 


### Testien suorittaminen
Minulla on projektissa käytössä GitHub Actions, joka suorittaa testit automaattisesti aina kun koodiin pushataan
muutoksia. Testit voivat muuten suorittaa juurihakemistossa komennolla ```pytest src``` tai poetryn kautta komennolla ```poetry run invoke test```

Testikattavuusraportin saa generoitua komennolla ```poetry run invoke coverage-report```
