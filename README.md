# Stichting Reeland voor Elkaar

Onepager voor Stichting Reeland voor Elkaar, trekkingsgebied 15 van het Ondernemersfonds Dordrecht. Gewone HTML en CSS, zonder build-stap, CMS of database.

## Bestanden

| Bestand | Inhoud |
| --- | --- |
| `index.html` | Home: zo werkt het, straatzoeker, thema's, eerstvolgende indiendatum |
| `gebied.html` | Kaart, vijf buurten, straatzoeker en stratenlijst |
| `aanvragen.html` | Route, checklist, vergaderdata, mailknop |
| `over-ons.html` | Bestuur en contactgegevens |
| `assets/data.js` | Vergaderdata en stratenlijst; verschijnen automatisch op alle pagina's |
| `assets/style.css` | Opmaak; palet en maten bovenaan als variabelen |
| `assets/script.js` | Straatzoeker, datums, stratenlijst |
| `assets/logo/` | Logo van Leen Oud: `logo-1` t/m `logo-5` (kleurvarianten), `logo-wit` (footer), origineel |
| `assets/slinger.svg` | Stijlelement voor de homepage |
| `.github/workflows/pages.yml` | Automatische uitrol naar GitHub Pages |

Elke pagina gebruikt een eigen logovariant en kleurpaar (`data-pair` op `<body>`): home blauw/roze, gebied oranje/groen, aanvragen baksteen/lichtblauw, over ons groen/baksteen.

De slinger tussen de blokken bestaat uit `<section class="lane lane--r">` of `lane--l` met `--c1` (bovenste helft) en `--c2` (onderste helft). Laat elke volgende sectie beginnen met de `--c2` van de vorige, dan loopt de band door.

## Lokaal bekijken

Draai `python3 -m http.server` in deze map en ga naar http://localhost:8000.

## Vergaderdatum of straat toevoegen

Alleen in `assets/data.js`. Datums als JJJJ-MM-DD. Verlopen data worden doorgestreept, de eerstvolgende krijgt een label en staat ook op de homepage.

## Tekst aanpassen

Zoek de tekst op in de HTML-pagina en vervang hem. Header en footer staan op elke pagina; wijzig ze op alle vier.

## Uitrol

Elke push naar `main` zet de site via GitHub Actions op GitHub Pages. Eenmalig instellen: Settings > Pages > Source: GitHub Actions. Voor een eigen domein vul je daar het domein in en zet je bij de registrar een CNAME naar `<account>.github.io`.

Zet nooit wachtwoorden, tokens of sleutels in deze repository.

## Nog te vervangen

Alle placeholders staan tussen blokhaken. Zoek op `[` om ze te vinden.

- [ ] og:image (deelafbeelding) maken van het logo
- [ ] `[KAART]` kaart van het trekkingsgebied als SVG met straatnamen
- [ ] `[BUURT 1]` t/m `[BUURT 5]` namen van de vijf buurten
- [ ] `[STRATEN]` volledige straatnamenlijst met buurt in `assets/data.js`
- [ ] `[THEMA 1]` t/m `[THEMA 4]` thema's waarvoor je kunt aanvragen
- [ ] `[CHECKLIST]` checklist aanvraag en verantwoording definitief maken
- [ ] `[X]` reactietermijnen invullen
- [ ] `[VOORBEELDDATA]` echte vergaderdata in `assets/data.js`
- [ ] `[MAILADRES]` mailadres van de stichting (komt 4 keer voor)
- [ ] `[KVK-NUMMER]`
- [ ] `[FUNCTIE]` functie van Wouter Sieuwerts; bestuursnamen laten bevestigen
- [ ] `[CHECKEN]` via welke belasting ondernemers meebetalen
- [ ] `[CONCEPT]` alle concepttekst laten goedkeuren door het bestuur
- [ ] Lettertype: Trade Gothic alleen met webfontlicentie; nu Helvetica
