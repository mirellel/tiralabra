# Määrittelydokumentti

## Spesifikaatiot
Opinto-ohjelma: Tietojenkäsittelytieteen kandi

Ohjelmointikieli: Python

Dokumentaation kieli: Suomi (vertaisarviointi onnistuu myös englanniksi)

## Aihe
Projektin aihe on klassinen Connect Four peli, jossa on vastakkain kaksi pelaajaa 7x6 kokoisella pelilaudalla. 
Pelin voittaa yhdistämällä ensimmäisenä neljä oman värin nappulaa suoraan pystyyn, vaakaan tai viistoon.
Tavoitteenani on luoda pygamen avulla peli, jota voi pelata tekoälyä tai kaveria vastaan.

## Käytettävät algoritmit
Pelin tekoälyn luomiseen aion käyttää minimax-algoritmia, jota voidaan tehostaa alpha-beta karsinnalla. 
Näin saadaan binääripuun haaroja karsittua, jotta tekoälyn toiminta on nopeampaa.

## Aika- ja tilavaativuusarvio
Alpha-beta karsinnalla aika-arvio on O(sqrt(b^d)), missä d on minmaxin syvyys ja b lukuarvo, joka kuvaa kuinka moneen solmuun kukin puun solmu haarautuu.
