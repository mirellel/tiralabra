## Viikko 2

### Mitä tein?
Tällä viikolla aloitin projektini käyttöliittymän sekä pelilogiikan koodauksen. Lisäksi tein yksikkötestausta erityisesti pelilogiikkaan liittyen.
En ehtinyt vielä aloittaa minimax-algoritmin koodausta, sillä käyttöliittymän tekemisessä kului paljon aikaa. Ohjelma avautuu nyt menuun, josta voi valita tällä hetkellä vain kahden pelaajan vaihtoehdon. Peliä ei voi vielä pelata edes kaveria vastaan, mutta pelin ydinalueesta sain paljon koodia kirjoitettua.
Projektini toimii poetrylla ja sain CI-palvelimen kautta toteutetun automaattisen testauksen toimimaan. Myös testikattavuus näkyy codecovin kautta repositorion etusivulla.

### Ongelmat
Ongelmia aiheutti tällä viikolla pygame ja testaus. Yritin ensin piirtää itse kuvat, joiden avulla pelilauta piirrettäisiin, mutta se kävi vähän työlääksi joten 
vaihdoin strategiaa ja aloin piirtämään pelilautaa pygamen avulla. En ollut käyttänyt pygamea aikoihin, joten sen muistelu ja kokeileminen vei paljon aikaa viikkotunneista. Sain kuitenkin lopulta piirrettyä pelilaudan pygamen avulla. Yksikkötestauksessa aiheutti ongelmia se, että testit eivät menneet poetrylla suoritettuna läpi import errorien takia. Ratkaisin lopulta sen ongelman, mutta seuraavaksi CI-palvelin ei saanut testejä suoritettua. StackOverFlowsta oli paljon apua ongelmien ratkaisussa, lopulta minun piti lisätä vain kaksi riviä koodia testitiedoston alkuun, jotta palvelin sain testit suoritettua. 

### Ajankäyttö
Koodasin tällä viikolla kolmena erillisenä päivänä ja aikaa käytin yhteensä 12h

### Mitä seuraavaksi
Ensi viikolla haluaisin keskittyä algoritmin koodaukseen, sekä pelin saamisen pelattavaksi edes kaveria vastaan. Katsoin jo materiaalista, että ensiviikolla pitäisi huolehtia koodin laadusta, joten sekin on asia mihin aion keskittyä. Lisään varmaankin Pylint tarkistuksen CI-palvelimelle.
