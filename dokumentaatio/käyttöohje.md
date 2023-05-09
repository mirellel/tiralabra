# Käyttöohje

## Ohjelman lataaminen omalle tietokoneelle
Voit ladata Neljän suora -sovelluksen koneellesi joko kopioimalla git repositorion tai lataamalla repositorion 
zip-tiedostona.
##### Kloonaus
1. Paina repositorion etusivulla olevaa vihreää Code-nappia
2. Kopioi SSH-osoite leikepöydälle
3. Avaa tietokoneesi komentokehote ja siirry kansioon, johon haluat ladata sovelluksen
4. Syötä komento ```git clone git@github.com:mirellel/tiralabra.git``` ja sovelluksen pitäisi kloonautua koneellesi

##### Zip-tiedoston lataus
1. Paina repositorion etusivulla olevaa vihreää Code-nappia
2. Paina Download ZIP
3. Pura ladattu ZIP-kansio haluamaasi kansioon

## Ohjelman käynnistys
Kun olet saanut ladattua sovelluksen tietokoneellesi, siirry komentokehotteella sovelluksen juurihakemistoon.
Lataa riippuvuudet komennolla ```poetry install```
Saat tämän jälkeen sovelluksen käynnistettyä komennolla ```poetry run invoke start```

## Ohjelman käyttö
Sovellus aukeaa päävalikkoon, josta voit valita vastustajasi:


![image](https://user-images.githubusercontent.com/101889891/236881114-aa6a2839-866d-4eb1-a03f-54c7952533b7.png)

Kaverin kanssa voit pelata Neljän suoraa normaalisti vuorotellen. Vihreä pelaaja aloittaa aina, joten muistakaa
vuorotella värien kanssa!

Jos valitset vastustajaksi tietokoneen saat valita kolmesta eri tekoälyllä toimivasta pelaajasta. Pelaajat
ovat eri vaikeustasoilla, joka ilmoitetaan vastustajan nimen alapuolella.
Helppo vastustaja on aika hyvä pelissä, joten älä oleta voittavasi heti.


![image](https://user-images.githubusercontent.com/101889891/236881929-b9ef6154-9450-4835-a2bb-19e2490216e5.png)

Valittuasi vastustajan aukeaa pelinäkymä:


![image](https://user-images.githubusercontent.com/101889891/236882945-f25c27b7-1c01-47d2-8b1d-93893683d337.png)

Pelilaudan yläpuolella oleva nappula liikkuu hiiren mukana. Siirron tekeminen tapahtuu niin, että liikutat nappulaa haluamasi sarakkeen yläpuolelle.
Hiiren klikkauksen jälkeen nappula ilmestyy alimmalle vapaalle riville sarakkeessa.

Hyviä pelihetkiä!











