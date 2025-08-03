# Ruokareseptit

## Sovelluksen toiminnot

- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen
- Käyttäjä pystyy lisäämään reseptejä ja muokkaamaan ja poistamaan niitä
- Käyttäjä näkee sovellukseen lisätyt reseptit
- Käyttäjä pystyy etsimään reseptejä hakusanalla
- Käyttäjäsivu näyttää, montako reseptiä käyttäjä on lisännyt ja listan käyttäjän lisäämistä resepteistä
- Käyttäjä pystyy valitsemaan reseptille yhden tai useamman luokittelun
- Käyttäjä pystyy antamaan reseptille kommentin

## Sovelluksen asennus

1. Asenna `flask`-kirjasto:
```bash
$ pip install flask
```

2. Luo tietokannan taulut:
```bash
$ sqlite3 database.db < sql/schema.sql
```

3. Sovelluksen käynnistys:
```bash
$ flask run
```
