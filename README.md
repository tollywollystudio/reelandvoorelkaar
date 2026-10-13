# Stichting Reeland voor Elkaar

Onepager voor Stichting Reeland voor Elkaar, trekkingsgebied 15 van het Ondernemersfonds Dordrecht. Gewone HTML en CSS, zonder build-stap, CMS of database.

## Bestanden

| Bestand | Inhoud |
| --- | --- |
| `index.html` | Alle teksten en de zes blokken van de pagina |
| `assets/style.css` | Opmaak; kleuren en lettertype bovenaan als variabelen |
| `assets/script.js` | Streept verlopen vergaderdata door |
| `assets/kaart.svg` | Kaart van het gebied (nu nog placeholder) |
| `assets/favicon.svg` | Tabblad-icoon (nu nog placeholder) |
| `.github/workflows/pages.yml` | Automatische uitrol naar GitHub Pages |

## Lokaal bekijken

Open `index.html` in een browser, of draai `python3 -m http.server` in deze map en ga naar http://localhost:8000.

## Tekst aanpassen

Zoek in `index.html` de tekst op en vervang hem. Elk blok staat in een eigen `<section>` met een id (`wat-we-doen`, `gebied`, `aanvragen`, `vergaderdata`, `contact`).

## Vergaderdatum toevoegen

Voeg in `index.html` onder `<tbody>` een rij toe:

```html
<tr data-date="2027-05-01"><td>1 mei 2027</td><td>15 mei 2027</td></tr>
```

`data-date` is de uiterste indiendatum als JJJJ-MM-DD. Na die datum wordt de rij automatisch doorgestreept.

## Uitrol

Elke push naar `main` zet de site via GitHub Actions op GitHub Pages. Eenmalig instellen: Settings > Pages > Source: GitHub Actions. Voor een eigen domein vul je daar het domein in en zet je bij de registrar een CNAME naar `<account>.github.io`.

Zet nooit wachtwoorden, tokens of sleutels in deze repository.

## Nog te vervangen

Alle placeholders staan tussen blokhaken. Zoek op `[` om ze te vinden.

- [ ] `[LOGO]` logo als SVG van Leen Oud in `assets/logo.svg`, plus favicon en og:image
- [ ] `[KLEUR]` kleuren uit het logo in `assets/style.css`
- [ ] `[KAART]` kaart van het trekkingsgebied als SVG met straatnamen
- [ ] `[BUURT 1]` t/m `[BUURT 5]` namen van de vijf buurten
- [ ] `[STRAAT]` straatnamenlijst
- [ ] `[THEMA 1]` t/m `[THEMA 4]` thema's waarvoor je kunt aanvragen
- [ ] `[AANVULLEN]` checklist aanvraag en verantwoording
- [ ] `[DATUM]` vergaderdata en indientermijnen
- [ ] `[MAILADRES]` mailadres van de stichting (komt 4 keer voor)
- [ ] `[KVK-NUMMER]`
- [ ] `[FUNCTIE]` functie van Wouter Sieuwerts; bestuursnamen laten bevestigen
- [ ] `[CHECKEN]` via welke belasting ondernemers meebetalen
- [ ] `[CONCEPT]` alle concepttekst laten goedkeuren door het bestuur
- [ ] Lettertype: Trade Gothic alleen met webfontlicentie; nu Helvetica
