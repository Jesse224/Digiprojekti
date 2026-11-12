# Digiprojekti – RTS-peliprototyyppi ("Kasvatus ja puolustus")

Tämä on digiprojektikurssia varten tehty pienimuotoinen reaaliaikaisen strategiapelin (RTS) prototyyppi. Pelin tavoitteena on tarjota matalan kynnyksen, nopeatempoinen ja helppokäyttöinen strategiapelikokemus ilman monimutkaisia valikoita tai raskasta mikromanagerointia.

## Nykyinen versio (v0.2)

Projektin tämänhetkisessä versiossa on toteutettu seuraavat ydinmekaniikat:

* **Yksikön valinta:** Pelaaja voi valita ruudulla olevan unitin (sininen ympyrä) klikkaamalla sitä hiiren vasemmalla painikkeella. Valitun unitin ympärille ilmestyy keltainen valintarengas.
* **Liikkuminen ja ohjaus:** Valittua unittia voi liikuttaa klikkaamalla mihin tahansa kentälle hiiren vasemmalla tai oikealla painikkeella. Punainen kohdemerkki näyttää määränpään.
* **Valinnan poisto (ESC):** Valitun unitin valinnan voi purkaa milloin tahansa painamalla näppäimistön **ESC**-näppäintä, jolloin unitti pysähtyy paikoilleen.
* **Resurssien kerääminen:** Pelikentällä on vihreitä mineraaleja. Kun unitti liikkuu ja astuu mineraalin päältä, se kerää sen automaattisesti, ja kerättyjen mineraalien määrä kasvaa ruudun yläkulmassa näkyvässä laskurissa.

---

## Käyttöönotto ja ajaminen

### Esivaatimukset
* Python 3 asennettuna
* Pygame-kirjasto

### Asennus ja käynnistys

1. Asenna Pygame komentorivillä, jos sitä ei ole vielä asennettu:
   ```bash
   pip install pygame

## Käynnistä peli:

   python Projekti.py
