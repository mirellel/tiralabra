# Testausdokumentti

## Testien suorittaminen
Projektissa käytössä GitHub Actions, joka suorittaa testit automaattisesti aina kun koodiin pushataan
muutoksia. 

Testit pääsee suorittamaan projektin juurihakemistossa komennolla ```pytest src``` 

tai poetryn kautta komennolla ```poetry run invoke test```

Testikattavuusraportin saa generoitua komennolla ```poetry run invoke coverage-report```

## Yksikkötestauksen kattavuusraportti
![image](https://github.com/mirellel/tiralabra/assets/101889891/753ee779-5334-4216-93c4-72ddf46881fe)


Testikattavuuden ulkopuolelle jää pelin ja menun UI:sta huolehtivat luokat, jotka ovat omassa kansiossaan UI. Kattavuudesta on jätetty pois myös files kansiossa olevat tiedostot multiplayer.py ja singleplayer.py, joissa olevat luokat huolehtivat yksin- ja kaksinpelin instansseista ja käsittelevät pygame tapahtumia seka menu.py, joka pääosin kutsuu ```MenuUI```-luokan funktioita. Jätin ne testikattavuudetsa pois, sillä luokissa ei ole kattavasti testattavaa. Pois on jätetty myös tiedosto load_image.py, joka lataa peliin käytettävät kuvat.

## Mitä on testattu
Testit ovat tehty Unittest-yksikkötesteillä ja ne testaavat pelilogiikkaa, pelin pyörimistä ja toimintaa (siirron tekeminen, uudelleen aloitus, voitontarkastus yms.) sekä minimax-algoritmin toimintaa.

#### Pelilogiikka
Pelilogiikan funktiot käyvät läpi taulukkoa, joka koostuu kuudesta seitsemän merkin pituisesta listasta. Pelilogiikan testeissä (sekä muissa testeissä) olen alustanut itse taulukot, jotta pelilauta olisi helpompi visualisoida. Pelilogiikan testit testaavat, että src/files/game_logic.py tiedoston luokan ```MainGame``` käyvät pelilautaa läpi tarkoitetulla tavalla, esimerkiksi testaamalla löytyykö vaaka- pysty- tai viistosuuntainen neljän suora toisille pelaajista.

#### Minimax
Tiedostossa minimax.py olevn luokan ```Minimax``` kaikkien funktioiden toimintaa on testattu. Pelitilanteen heuristisen arvon laskevaa funktiota score on testattu valmiilla pelilaudalla ja funktiota rate_possible_move valmiilla neljän riveillä. Minimax-algoritmin toimintaa on testattu valmiilla pelitilanteilla, joissa tietokone tulee joko häviämään seuraavalla siirrolla tai voittamaan varmasti x siirron jälkeen. Testeissä testataan, että algoritmi löytää parhaimman seuraavan liikeeen voiton kannalta.
Algoritmin toimintaa on testattu eri syvyyksillä ja eri tilanteissa, joissa voitto on väistämätön.

#### Pelin toiminta
Pelin toiminnasta vastaavaa luokkaa ```Game``` ollaan testattu samankaltaisesti kuin pelilogiikkaa. Osassa
testeissä on pelilaudat alustettu valmiiksi visuaalisesti. Testeissä ollaan testattu mm. siirron tekemistä, pelin totuusarvojen ja muiten muuttujien arvojen vaihtumista oikeisiin. Siirron tekemistä ollaan testattu myös tapauksessa, jossa kyseinen sarake johon siirtoa yritetään tehdä, on täynnä.






