# Stichting Reeland voor Elkaar

Website van Stichting Reeland voor Elkaar, trekkingsgebied 15 van het Ondernemersfonds Dordrecht. Gewone HTML en CSS, zonder build-stap, CMS of database.

## Bestanden

| Bestand | Inhoud |
| --- | --- |
| `index.html` | Home: kern, geldstroom, straatzoeker, thema's, eerstvolgende vergadering |
| `gebied.html` | Vijf buurten, kaart, straatzoeker en stratenlijst |
| `aanvragen.html` | Vijf stappen, checklist, vergaderdata, mailknop |
| `over-ons.html` | Doel, bestuur, KvK en contact |
| `privacy.html`, `404.html` | Privacyverklaring en foutpagina |
| `tools/maak-paginas.py` | Bouwt alle pagina's; teksten staan hier |
| `assets/data.js` | Vergaderdata en stratenlijst |
| `assets/style.css` | Opmaak; palet en maten bovenaan als variabelen |
| `assets/script.js` | Straatzoeker, datums, stratenlijst |
| `assets/gate.js` | Tijdelijke toegangscode tijdens de opbouw |
| `assets/logo/` | Logo van Leen Oud: `logo-1` t/m `logo-5`, `logo-wit`, origineel |
| `assets/slinger.svg`, `assets/deelafbeelding.png` | Stijlelement (twee kolommen, naar het blad van Leen; opnieuw maken met `tools/maak-stijlelement.py`) en afbeelding voor delen |

Elke pagina gebruikt een eigen logovariant (home blauw/roze, gebied oranje/groen, aanvragen baksteen/lichtblauw, over ons groen/baksteen) en een lichte tint (`data-pair` op `<body>`). De slinger komt terug als stappenlijst (`ol.flow`), als bocht in de paginakop (`.kopband`) en als klein slingertje per thema in een eigen kleurpaar (`.list.tiles`), zoals Leen voorstelt: verschillende kleurcombinaties voor verschillende soorten aanvragen.

## Tekst aanpassen

Teksten staan in `tools/maak-paginas.py`. Pas ze daar aan en draai daarna vanuit de hoofdmap:

```
python3 tools/maak-paginas.py .
```

## Vergaderdatum of straat toevoegen

Alleen in `assets/data.js`. Datums als JJJJ-MM-DD; `indienen: null` toont "nader te bepalen". Zet `stratenCompleet` op `true` zodra de stratenlijst volledig is.

## Toegangscode tijdens de opbouw

`assets/gate.js` toont een codescherm en de pagina's hebben `noindex`. Dit is geen beveiliging: de bestanden staan openbaar op GitHub. Bij livegang: in `tools/maak-paginas.py` de regels met `gate.js` en `robots` weghalen, script draaien, `assets/gate.js` verwijderen.

## Lokaal bekijken

Draai `python3 -m http.server` in deze map en ga naar http://localhost:8000.

## Uitrol

Elke push naar `main` zet de site via GitHub Actions op GitHub Pages: https://reelandvoorelkaar.nl (www stuurt door).

Instellingen (Settings > Pages): Source "GitHub Actions", Custom domain `reelandvoorelkaar.nl`, Enforce HTTPS aan.

DNS bij mijn.host:

| Naam | Type | Waarde |
| --- | --- | --- |
| (leeg) | A | 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153 |
| www | CNAME | tollywollystudio.github.io |

Mail (MX, SPF, DKIM, DMARC, `mail`) blijft bij mijn.host.

Zet nooit wachtwoorden, tokens of sleutels in deze repository.

## Nog aan te leveren

- [ ] Stratenlijst en kaart van het trekkingsgebied (toegezegd door Peter ter Hark, kwartiermaker ONS, sept. 2025)
- [x] Eén regel per buurt (concept op basis van gemeentelijke beschrijving; laten checken)
- [x] Mailadres: voorzitter@reelandvoorelkaar.nl
- [ ] Vergaderdata 2027 en indientermijn
- [ ] Bestuur: foto en twee zinnen per persoon, eventueel telefoonnummer
- [ ] Checklist aanvraag en verantwoording laten vaststellen
- [ ] Zijn vergaderingen openbaar of op afspraak?
- [ ] ONS-logo in de footer (afgesproken in overleg 22 januari)
- [ ] Lettertype: Trade Gothic alleen met webfontlicentie; nu Helvetica
