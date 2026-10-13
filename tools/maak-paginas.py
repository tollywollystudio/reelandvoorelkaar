# Bouwt alle HTML-pagina's (gedeelde kop, menu en footer + inhoud per pagina).
# Gebruik: python3 tools/maak-paginas.py .   (vanuit de hoofdmap)
# Pas teksten hier aan en draai het script opnieuw, anders gaan handmatige wijzigingen in de HTML verloren.
import sys, os
root = sys.argv[1]
slinger = open(os.path.join(root, 'assets/slinger.svg')).read().replace('<svg ', '<svg class="hero__art" ', 1)

NAV = [('gebied.html', 'Het gebied'), ('aanvragen.html', 'Aanvragen'), ('over-ons.html', 'Over ons')]
MAIL = 'voorzitter@reelandvoorelkaar.nl'

def page(fn, title, desc, pair, logo, body):
    nav = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == fn else ""}>{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="nl">
<head>
  <meta charset="utf-8">{'<base href="/">' if fn == '404.html' else ''}
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="nl_NL">
  <meta property="og:image" content="https://reelandvoorelkaar.nl/assets/deelafbeelding.png">
  <meta property="og:url" content="https://reelandvoorelkaar.nl/{fn}">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <meta name="robots" content="noindex, nofollow">
  <link rel="stylesheet" href="assets/style.css?v=202610132159">
  <script src="assets/gate.js?v=202610132159"></script>
</head>
<body data-pair="{pair}">
  <a class="skip" href="#inhoud">Naar de inhoud</a>

  <header class="top">
    <div class="wrap top__bar">
      <a class="logo" href="index.html"><img src="assets/logo/logo-{logo}.svg" alt="Stichting Reeland voor Elkaar" width="249" height="94"></a>
      <nav class="nav" aria-label="Hoofdmenu">
        {nav}
        <a class="btn" href="aanvragen.html#indienen">Aanvraag indienen</a>
      </nav>
    </div>
  </header>

  <main id="inhoud">
{body}
  </main>

  <footer class="foot">
    <div class="wrap foot__grid">
      <div>
        <img src="assets/logo/logo-{logo}.svg" alt="Stichting Reeland voor Elkaar" width="249" height="94">
        <p>Trekkingsgebied 15 van <a href="https://www.ondernemersfondsdordrecht.nl/">ONS Dordrecht</a>, het Ondernemersfonds Dordrecht.</p>
      </div>
      <div>
        <h2>Contact</h2>
        <p><a href="mailto:{MAIL}">{MAIL}</a></p>
        <p>KvK 98417975</p>
      </div>
      <div>
        <h2>Pagina's</h2>
        <ul>
          <li><a href="index.html">Home</a></li>
          {''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)}
          <li><a href="privacy.html">Privacy</a></li>
        </ul>
      </div>
    </div>
  </footer>

  <script src="assets/data.js?v=202610132159"></script>
  <script src="assets/script.js?v=202610132159" defer></script>
</body>
</html>
'''

def lane(side, c1, c2, inner, id_=None, label=None):
    a = f' id="{id_}"' if id_ else ''
    l = f' aria-labelledby="{label}"' if label else ''
    return f'''    <section class="block"{a}{l}>
      <div class="wrap">
{inner}
      </div>
    </section>
'''

checker = '''        <div class="panel">
          <div>
            <h2 id="h-check">Hoor ik erbij?</h2>
            <p>Heb je een onderneming, school, vereniging of organisatie met een pand in het Reeland? Dan betaal je mee aan het fonds en kun je een aanvraag doen.</p>
          </div>
          <div>
            <form class="streetform" data-straatcheck>
              <label for="straat-{k}">Typ je straatnaam</label>
              <input id="straat-{k}" name="straat" list="straten-lijst" autocomplete="off" placeholder="Bijvoorbeeld Vogelplein">
              <button class="btn" type="submit">Check</button>
            </form>
            <p class="result" role="status" aria-live="polite"></p>
            <datalist id="straten-lijst"></datalist>
          </div>
        </div>'''

# ---------- Home ----------
home = f'''    <section class="hero" aria-labelledby="kop">
      <div class="wrap hero__grid">
        <div>
          <h1 id="kop">Geld uit het Reeland, <span>voor het Reeland.</span></h1>
          <p class="lead">Iedereen met een bedrijfspand in het Reeland betaalt mee aan het Ondernemersfonds Dordrecht. Het deel dat voor het Reeland bestemd is, beheren wij. Zo komt dat geld terug bij plannen die het gebied sterker maken.</p>
          <div class="actions">
            <a class="btn" href="aanvragen.html">Zo doe je een aanvraag</a>
            <a href="#hoor-ik-erbij">Hoor ik erbij?</a>
          </div>
        </div>
        {slinger}
      </div>
    </section>

''' + lane('r', 'baksteen', 'groen', '''        <h2 id="h-werkt">Een fonds van en voor het Reeland</h2>
        <p class="intro">Het is geen subsidie van buiten. Het is jullie eigen geld, dat wij op aanvraag teruggeven aan plannen die het gebied ten goede komen. Wij bepalen niet wat er moet gebeuren; dat doen de ondernemers, verenigingen en organisaties uit het Reeland samen.</p>
        <ol class="flow">
          <li><span class="flow__label">Stap 1</span><h3>Je betaalt mee</h3><p>Eigenaren en gebruikers van panden die geen woning zijn, betalen een kleine opslag op de onroerendezaakbelasting (OZB). De gemeente Dordrecht draagt dat af aan het Ondernemersfonds Dordrecht, ONS Dordrecht.</p></li>
          <li><span class="flow__label">Stap 2</span><h3>Het blijft in het Reeland</h3><p>Dordrecht is verdeeld in 24 trekkingsgebieden. Het fonds houdt het geld per gebied bij elkaar. Het Reeland is trekkingsgebied 15, en Stichting Reeland voor Elkaar beheert het geld voor dit gebied.</p></li>
          <li><span class="flow__label">Stap 3</span><h3>Het komt terug</h3><p>Ondernemers, organisaties en bewoners uit het Reeland dienen een plan in. Het bestuur beoordeelt de aanvraag en ziet erop toe dat het geld goed wordt besteed.</p></li>
        </ol>''', label='h-werkt') + lane('l', 'groen', 'oranje', checker.format(k='home') + '''
        <p class="small mt-s">Of bekijk <a href="gebied.html">de vijf buurten en de kaart</a>.</p>''', id_='hoor-ik-erbij', label='h-check') + lane('r', 'oranje', 'oker', '''        <h2 id="h-thema">Waarvoor kun je aanvragen?</h2>
        <p class="intro">Voor plannen die het gezamenlijk belang van ondernemers dienen en ook goed zijn voor het gebied. Bijvoorbeeld op deze terreinen:</p>
        <ul class="list list--2 tiles">
          <li><h3>Samen organiseren</h3><p>Ondernemers in het Reeland beter met elkaar verbinden en organiseren.</p></li>
          <li><h3>Gezamenlijke activiteiten</h3><p>Activiteiten die ondernemers samen opzetten, voor het hele gebied.</p></li>
          <li><h3>Schoon, heel en veilig</h3><p>De leefbaarheid van straten, pleinen en bedrijfsomgeving.</p></li>
          <li><h3>Duurzaamheid en innovatie</h3><p>Plannen die het Reeland duurzamer of vernieuwender maken.</p></li>
          <li><h3>Promotie en marketing</h3><p>Het Reeland en zijn ondernemers zichtbaar maken.</p></li>
          <li><h3>Overleg en vertegenwoordiging</h3><p>Een stem voor het gebied in relevante overleggen.</p></li>
          <li><h3>Onderzoek en data</h3><p>Weten wat er speelt, zodat plannen beter aansluiten.</p></li>
        </ul>
        <div class="deadline">
          <div><small>Eerstvolgende indiendatum</small><strong data-next="indienen">&nbsp;</strong></div>
          <div><small>Besproken in de vergadering van</small><strong data-next="vergadering">&nbsp;</strong></div>
          <a class="btn" href="aanvragen.html">Aanvraag indienen</a>
        </div>''', label='h-thema') + lane('l', 'oker', 'blauw', '''        <h2 id="h-gesteund">Al gesteund</h2>
        <ul class="list list--2">
          <li><h3>Muziek rond de Reeweg 2026</h3><p>Ons eerste gesteunde initiatief: muziek in de wijk, georganiseerd vanuit het Reeland zelf.</p></li>
        </ul>
        <h2 id="h-meer" class="mt">Meer weten</h2>
        <ul class="list list--3">
          <li><a class="linkcard" href="gebied.html"><h3>Het gebied</h3><p>Wantijbuurt, Transvaalbuurt, Vogelbuurt, Indische Buurt en Land van Valk.</p></a></li>
          <li><a class="linkcard" href="aanvragen.html"><h3>Aanvragen</h3><p>Wat erin moet, wanneer we vergaderen en wat we achteraf vragen.</p></a></li>
          <li><a class="linkcard" href="over-ons.html"><h3>Over ons</h3><p>Wie in het bestuur zitten en hoe je ons bereikt.</p></a></li>
        </ul>''', label='h-meer')

# ---------- Gebied ----------
gebied = '''    <section class="pagehead" aria-labelledby="kop">
      <div class="kopband" aria-hidden="true"></div>
      <div class="wrap">
        <h1 id="kop">Het gebied</h1>
        <p class="lead">Trekkingsgebied 15, het Reeland, bestaat uit vijf buurten. Samen tellen ze ongeveer 175 adressen van ondernemers, scholen, verenigingen en organisaties.</p>
      </div>
    </section>

''' + lane('r', 'oranje', 'groen', '''        <h2 id="h-buurten">Vijf buurten</h2>
        <p class="intro">Heb je een pand in een van deze buurten dat geen woning is? Dan betaal je mee aan het fonds en kun je een aanvraag doen.</p>
        <ul class="list list--3">
          <li><h3>Wantijbuurt</h3><p>[Eén regel over wat de buurt kenmerkt.]</p></li>
          <li><h3>Transvaalbuurt</h3><p>[Eén regel over wat de buurt kenmerkt.]</p></li>
          <li><h3>Vogelbuurt</h3><p>Met het Vogelplein als winkelhart. [Aanvullen.]</p></li>
          <li><h3>Indische Buurt</h3><p>[Eén regel over wat de buurt kenmerkt.]</p></li>
          <li><h3>Land van Valk</h3><p>[Eén regel over wat de buurt kenmerkt.]</p></li>
        </ul>''', label='h-buurten') + lane('l', 'groen', 'baksteen', '''        <h2 id="h-kaart">Kaart</h2>
        <figure class="map">
          <!-- [KAART] vervangen door assets/kaart.svg met straatnamen en de buurten in de paletkleuren -->
          <a href="assets/kaart.svg"><img src="assets/kaart.svg" alt="Kaart van trekkingsgebied 15 Reeland met de vijf buurten. Alle straten staan ook in de lijst verderop." width="800" height="600"></a>
          <figcaption>De grenzen van het trekkingsgebied zoals vastgelegd met het Ondernemersfonds Dordrecht. Tik op de kaart om in te zoomen.</figcaption>
        </figure>''', label='h-kaart') + lane('r', 'baksteen', 'oker', checker.format(k='gebied') + '''
        <h3 class="mt">Alle straten</h3>
        <ul class="streets" data-stratenlijst></ul>''', id_='hoor-ik-erbij', label='h-check')

# ---------- Aanvragen ----------
aanvragen = f'''    <section class="pagehead" aria-labelledby="kop">
      <div class="kopband" aria-hidden="true"></div>
      <div class="wrap">
        <h1 id="kop">Aanvraag indienen</h1>
        <p class="lead">Ondernemers, maatschappelijke organisaties en bewoners uit het Reeland kunnen een aanvraag doen. Je stuurt je plan met een begroting per mail. Het bestuur beoordeelt het in de eerstvolgende vergadering.</p>
        <div class="actions"><a class="btn" href="#indienen">Naar indienen</a></div>
      </div>
    </section>

''' + lane('r', 'baksteen', 'lichtblauw', '''        <h2 id="h-route">Van plan tot verantwoording</h2>
        <ol class="flow">
          <li><span class="flow__label">Stap 1</span><h3>Plan maken</h3><p>Beschrijf wat je wilt doen en wat het kost. Twijfel je? Wij denken mee en helpen zoeken naar samenwerking met anderen in het gebied.</p></li>
          <li><span class="flow__label">Stap 2</span><h3>Indienen</h3><p>Mail je aanvraag met begroting voor de indiendatum.</p></li>
          <li><span class="flow__label">Stap 3</span><h3>Vergadering</h3><p>Het bestuur bespreekt je aanvraag. Je bent welkom om je plan toe te lichten.</p></li>
          <li><span class="flow__label">Stap 4</span><h3>Besluit</h3><p>Na de vergadering hoor je of je aanvraag is toegekend en onder welke voorwaarden.</p></li>
          <li><span class="flow__label">Stap 5</span><h3>Verantwoorden</h3><p>Na afloop laat je zien hoe het geld is besteed.</p></li>
        </ol>''', label='h-route') + lane('l', 'lichtblauw', 'groen', '''        <h2 id="h-check">Wat we van je vragen</h2>
        <div class="cols">
          <div>
            <h3>In je aanvraag</h3>
            <!-- [CHECKLIST] laten vaststellen door het bestuur -->
            <ul class="check">
              <li>Naam en adres van je onderneming of organisatie in het Reeland</li>
              <li>Contactpersoon met telefoonnummer en mailadres</li>
              <li>Wat je wilt doen, waar en wanneer</li>
              <li>Waarom het goed is voor de ondernemers en het gebied</li>
              <li>Een begroting met het bedrag dat je aanvraagt</li>
              <li>Andere bijdragen of sponsors, als die er zijn</li>
            </ul>
          </div>
          <div>
            <h3>Achteraf</h3>
            <p>Wij leggen zelf verantwoording af aan het Ondernemersfonds Dordrecht. Daarom vragen we na afloop:</p>
            <ul class="check">
              <li>Een kort verslag van wat er is gebeurd</li>
              <li>Facturen of bonnen van de uitgaven</li>
              <li>Foto's die we mogen gebruiken</li>
            </ul>
          </div>
        </div>''', label='h-check') + lane('r', 'groen', 'oranje', f'''        <h2 id="h-data">Vergaderdata en indientermijn</h2>
        <p class="intro">Het bestuur vergadert ongeveer vier keer per jaar. Stuur je aanvraag uiterlijk op de indiendatum, dan bespreken we hem in de vergadering die erbij hoort. Wil je je plan zelf toelichten of een vergadering bijwonen? Neem dan vooraf contact op.</p>
        <table class="dates">
          <thead><tr><th scope="col">Uiterlijk indienen</th><th scope="col">Vergadering</th></tr></thead>
          <tbody data-dates></tbody>
        </table>''', id_='vergaderdata', label='h-data') + lane('l', 'oranje', 'blauw', f'''        <div class="panel">
          <div>
            <h2 id="h-indienen">Klaar? Mail je aanvraag</h2>
            <p>Eerstvolgende indiendatum: <strong data-next="indienen">&nbsp;</strong>.</p>
          </div>
          <div>
            <a class="btn" href="mailto:{MAIL}?subject=Aanvraag%20Reeland%20voor%20Elkaar">Mail je aanvraag</a>
            <p class="small">Of mail naar <a href="mailto:{MAIL}">{MAIL}</a>. Vragen vooraf mogen ook.</p>
          </div>
        </div>''', id_='indienen', label='h-indienen')

# ---------- Over ons ----------
over = f'''    <section class="pagehead" aria-labelledby="kop">
      <div class="kopband" aria-hidden="true"></div>
      <div class="wrap">
        <h1 id="kop">Stichting Reeland voor Elkaar</h1>
        <p class="lead">Reeland voor Elkaar is een van de 24 trekkingsgebieden van het Ondernemersfonds Dordrecht. Wij beheren het deel dat voor het Reeland bestemd is. Ons doel: de economische structuur en het vestigingsklimaat in het gebied versterken, en initiatieven van ondernemers steunen die ook maatschappelijk van belang zijn.</p>
      </div>
    </section>

''' + lane('r', 'groen', 'baksteen', '''        <h2 id="h-bestuur">Bestuur</h2>
        <p class="intro">Drie ondernemers uit het Reeland. Ze zitten in het bestuur op persoonlijke titel, niet namens hun eigen bedrijf. We zoeken nog versterking: ben jij ondernemer in het Reeland en wil je meedenken? Laat het ons weten.</p>
        <!-- [BESTUUR] per persoon foto, twee zinnen en eigen contactgegevens (voorstel Jolita) -->
        <ul class="board">
          <li><strong>Jolita Meuldijk</strong><span>voorzitter, Schapenhok 94</span></li>
          <li><strong>Akhshid Zia</strong><span>penningmeester, PLUS Vogelplein</span></li>
          <li><strong>Wouter Sieuwerts</strong><span>bestuurslid, Tolly Wolly Studio en Lexlab</span></li>
        </ul>''', label='h-bestuur') + lane('l', 'baksteen', 'oker', f'''        <h2 id="h-contact">Contact en gegevens</h2>
        <p class="intro">Vragen, twijfel of je erbij hoort, of wil je je plan eerst bespreken? Mail ons. Je bent ook welkom om vooraf een vergadering bij te wonen.</p>
        <dl class="facts">
          <dt>Mail</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd>
          <dt>KvK</dt><dd>98417975</dd>
          <dt>RSIN</dt><dd>868484957</dd>
          <dt>Opgericht</dt><dd>25 september 2025, statutair gevestigd in Dordrecht</dd>
          <dt>Onderdeel van</dt><dd><a href="https://www.ondernemersfondsdordrecht.nl/">ONS Dordrecht</a>, het Ondernemersfonds Dordrecht, trekkingsgebied 15</dd>
        </dl>''', label='h-contact')

# ---------- Privacy ----------
privacy = f'''    <section class="pagehead" aria-labelledby="kop">
      <div class="kopband" aria-hidden="true"></div>
      <div class="wrap">
        <h1 id="kop">Privacy</h1>
        <p class="lead">Deze website verzamelt zo weinig mogelijk. Er zijn geen formulieren, geen trackingcookies en geen statistieken.</p>
      </div>
    </section>

''' + lane('r', 'groen', 'baksteen', f'''        <h2 id="h-mail">Als je ons mailt</h2>
        <p>Stuur je een aanvraag of vraag per mail, dan gebruiken we je gegevens alleen om je aanvraag te behandelen en contact met je te houden. Voor de verantwoording aan het Ondernemersfonds Dordrecht delen we van toegekende aanvragen de naam van de aanvrager, het bedrag en de datum. Andere gegevens delen we niet.</p>
        <p>We bewaren aanvragen zo lang als nodig is voor onze administratie en de verantwoording, en niet langer dan wettelijk verplicht.</p>
        <h2 id="h-site" class="mt">Deze website</h2>
        <p>De site wordt gehost via GitHub Pages. GitHub kan voor beveiliging technische gegevens zoals IP-adressen tijdelijk vastleggen. Wij hebben daar geen toegang toe en gebruiken ze niet.</p>
        <h2 id="h-vragen" class="mt">Vragen</h2>
        <p>Wil je weten welke gegevens we van je hebben, of wil je die laten verwijderen? Mail naar <a href="mailto:{MAIL}">{MAIL}</a>.</p>''', label='h-mail')

notfound = '''    <section class="pagehead" aria-labelledby="kop">
      <div class="kopband" aria-hidden="true"></div>
      <div class="wrap">
        <h1 id="kop">Deze pagina bestaat niet</h1>
        <p class="lead">Misschien is de link verouderd. Ga naar de <a href="index.html">homepage</a> of kijk hoe je <a href="aanvragen.html">een aanvraag doet</a>.</p>
      </div>
    </section>
'''

pages = [
  ('index.html', 'Stichting Reeland voor Elkaar | Geld uit het Reeland, voor het Reeland', 'Ondernemers, scholen en verenigingen in het Reeland in Dordrecht betalen mee aan het Ondernemersfonds. Bij Stichting Reeland voor Elkaar vraag je dat geld aan voor de wijk.', 'home', 5, home),
  ('gebied.html', 'Het gebied | Stichting Reeland voor Elkaar', 'De vijf buurten van trekkingsgebied 15 Reeland: Wantijbuurt, Transvaalbuurt, Vogelbuurt, Indische Buurt en Land van Valk.', 'gebied', 2, gebied),
  ('aanvragen.html', 'Aanvraag indienen | Stichting Reeland voor Elkaar', 'Zo dien je een aanvraag in bij Stichting Reeland voor Elkaar: wat erin moet, vergaderdata en indientermijn.', 'aanvragen', 1, aanvragen),
  ('privacy.html', 'Privacy | Stichting Reeland voor Elkaar', 'Hoe Stichting Reeland voor Elkaar omgaat met gegevens.', 'over', 4, privacy),
  ('404.html', 'Pagina niet gevonden | Stichting Reeland voor Elkaar', 'Deze pagina bestaat niet.', 'home', 5, notfound),
  ('over-ons.html', 'Over ons | Stichting Reeland voor Elkaar', 'Bestuur, doel en contactgegevens van Stichting Reeland voor Elkaar, trekkingsgebied 15 van ONS Dordrecht.', 'over', 4, over),
]
for fn, t, d, pair, logo, body in pages:
    open(os.path.join(root, fn), 'w').write(page(fn, t, d, pair, logo, body))
    print('geschreven', fn)
