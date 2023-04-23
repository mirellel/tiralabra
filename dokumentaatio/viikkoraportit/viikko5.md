## Viikkoraportti 5

### Mitä tein?
Sain viimeviikolla palautetta, että algortimi toimii väärin, joten tällä viikolla korjasin
minimax-algoritmin niin, että voitontarkastus tapahtuu heti algoritmin alussa. Lisäksi muokkasin pelilaudan
heuristisen arvon laskentaa, niin että algoritmi toimi oikealla tavalla. Muokkasin luokkaa Minimax myös niin, että algoritmi palauttaa suoraan parhaimman sarakkeen ja 
poistin parhaan liikkeen palauttavan funktion best_move(). Tein algoritmin lisäksi muuhun koodiin
joitakin pieniä muutoksia, jonka syysta suurin osa testeistäni eivät toimineet. Käytin loput ajastani tällä
viikolla testien korjaukseen. Testit menevät nyt kaikki läpi. Muokkasin myös minimax-algoritmin testausta.
Lisäksi tein kurssin ensimmäisen vertaisarvioinnin.

### Ongelmat
Eniten aikaa tällä viikolla meni selvittäessä miksi algoritmi ei toiminut kunnolla. Tapasin kurssin ohjaajan
kanssa ja hänen neuvojensa jälkeen algoritmi ei vieläkään toiminut täysin oikein. Lopulta sain algoritmin
toimimaan halutulla tavalla, kun muokkasin Minimax luokkaan kuuluvia funktioita, jotka laskivat pelilaudalle 
heuristisen arvon. 

### Ajankäyttö
Aikaa käytin tällä viikolla yhteensä 10h

### Mitä seuraavaksi?
Seuraavaksi aion viimeistellä pelin toimintaa ja sovelluksen käyttöliittymää. Aion optimoida 
ohjelman laskentaa. Aion myös aloittaa käyttöliittymän viimeistelyn ja eri lisätä 
vaikeustasoilla pelaamisen.
