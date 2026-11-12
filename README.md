```markdown
# Digiprojekti – RTS-peliprototyyppi

Tämä on digiprojektikurssia varten tehty pienimuotoinen reaaliaikaisen strategiapelin (RTS) prototyyppi, joka on toteutettu Pythonilla ja Pygame-kirjastolla.

## Nykyinen versio (v0.1)

Projektin ensimmäisessä toimivassa versiossa on toteutettu pelin perusohjausmekaniikka:

* **Yksikön valinta:** Pelaaja voi valita ruudulla olevan yksikön (sininen ympyrä) klikkaamalla sitä hiiren vasemmalla painikkeella. Valitun yksikön ympärille ilmestyy keltainen valintarengas.
* **Liikkuminen:** Kun yksikkö on valittuna, pelaaja voi osoittaa sille uuden määränpään klikkaamalla mihin tahansa pelikentällä (hiiren vasemmalla tai oikealla painikkeella).
* **Visuaalinen palaute:** Liikkuessa määränpäähän piirtyy punainen kohdemerkki, ja yksikkö liikkuu tasaisella nopeudella kohti pistettä.

## Käyttöönotto ja ajaminen

### Esivaatimukset
* Python 3 asennettuna
* Pygame-kirjasto

### Asennus ja käynnistys

1. Asenna tarvittava Pygame-kirjasto komentorivillä:
   ```bash
   pip install pygame

```

2. Siirry projektikansioon ja käynnistä peli:
```bash
python Projekti.py

```



```

### Näin tallennat muutoksen GitHubiin:
1. Avaa `README.md` koneellasi (esim. Muistiolla tai VS Codella), liitä teksti sinne ja tallenna tiedosto.
2. Aja tutut kolme komentoa komentorivillä:
   ```bash
   git add README.md
   git commit -m "Päivitetty README-kuvaus"
   git push origin main

```
