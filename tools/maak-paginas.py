# Bouwt alle HTML-pagina's (gedeelde kop, menu en footer + inhoud per pagina).
# Gebruik: python3 tools/maak-paginas.py .   (vanuit de hoofdmap)
# Pas teksten hier aan en draai het script opnieuw, anders gaan handmatige wijzigingen in de HTML verloren.
import sys, os
root = sys.argv[1]
slinger = open(os.path.join(root, 'assets/slinger.svg')).read().replace('<svg ', '<svg class="hero__art" ', 1)

import time
V = time.strftime('%Y%m%d%H%M')  # versienummer tegen oude cache

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
  <link rel="stylesheet" href="assets/style.css?v={V}">
  <script src="assets/gate.js?v={V}"></script>
</head>
<body data-pair="{pair}">
  <a class="skip" href="#inhoud">Naar de inhoud</a>

  <header class="top">
    <div class="wrap top__bar">
      <a class="logo" href="index.html"><img src="assets/logo/logo-{logo}.svg" alt="Stichting Reeland voor Elkaar" width="249" height="94"></a>
      <nav class="nav" aria-label="Hoofdmenu">
        {nav}
        <a class="btn" href="aanvraag.html">Aanvraag indienen</a>
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

  <script src="assets/data.js?v={V}"></script>
  {f'<script src="assets/aanvraag.js?v={V}" defer></script>' if fn == 'aanvraag.html' else ''}
  <script src="assets/script.js?v={V}" defer></script>
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

checker = '''        <div class="panel panel--slinger">
          <span class="flow__label">Check je straat</span>
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
      <div class="wrap">
        <ul class="cijfers" aria-label="Het Reeland in cijfers">
          <li><strong>175</strong><span>ondernemers en organisaties</span></li>
          <li><strong>5</strong><span>buurten</span></li>
          <li><strong>15</strong><span>trekkingsgebied, van de 24 in Dordrecht</span></li>
        </ul>
      </div>
    </section>

''' + lane('r', 'baksteen', 'groen', '''        <h2 id="h-werkt">Een fonds van en voor het Reeland</h2>
        <p class="intro">Het is geen subsidie van buiten. Het is jullie eigen geld, dat wij op aanvraag teruggeven aan plannen die het gebied ten goede komen. Wij bepalen niet wat er moet gebeuren; dat doen de ondernemers, verenigingen en organisaties uit het Reeland samen.</p>
        <ol class="flow">
          <li><span class="flow__label">Stap 1</span><h3>Je betaalt mee</h3><p>Eigenaren en gebruikers van panden die geen woning zijn, betalen een kleine opslag op de onroerendezaakbelasting (OZB). De gemeente Dordrecht draagt dat af aan het Ondernemersfonds Dordrecht, ONS Dordrecht.</p></li>
          <li><span class="flow__label">Stap 2</span><h3>Het blijft in het Reeland</h3><p>Dordrecht is verdeeld in 24 trekkingsgebieden. Het fonds houdt het geld per gebied bij elkaar. Het Reeland is trekkingsgebied 15, en Stichting Reeland voor Elkaar beheert het geld voor dit gebied.</p></li>
          <li><span class="flow__label">Stap 3</span><h3>Het komt terug</h3><p>Ondernemers en organisaties uit het Reeland dienen samen een plan in. Het bestuur beoordeelt de aanvraag en ziet erop toe dat het geld goed wordt besteed.</p></li>
        </ol>''', label='h-werkt') + lane('l', 'groen', 'oranje', checker.format(k='home') + '''
        <p class="small mt-s">Of bekijk <a href="gebied.html">de vijf buurten</a>.</p>''', id_='hoor-ik-erbij', label='h-check') + lane('r', 'oranje', 'oker', '''        <h2 id="h-thema">Waarvoor kun je aanvragen?</h2>
        <p class="intro">Voor plannen van en voor ondernemers die ook goed zijn voor het gebied. Hoe meer ondernemers en organisaties uit het Reeland je plan steunen, hoe sterker je aanvraag. Bijvoorbeeld op deze terreinen:</p>
        <ul class="list list--2 tiles">
          <li><h3>Samen organiseren</h3><p>Ondernemers in het Reeland beter met elkaar verbinden en organiseren.</p></li>
          <li><h3>Gezamenlijke activiteiten</h3><p>Activiteiten die ondernemers samen opzetten, voor het hele gebied.</p></li>
          <li><h3>Schoon, heel en veilig</h3><p>De leefbaarheid van straten, pleinen en bedrijfsomgeving.</p></li>
          <li><h3>Duurzaamheid en innovatie</h3><p>Plannen die het Reeland duurzamer of vernieuwender maken.</p></li>
          <li><h3>Promotie en marketing</h3><p>Het Reeland en zijn ondernemers zichtbaar maken.</p></li>
          <li><h3>Overleg en vertegenwoordiging</h3><p>Een stem voor het gebied in relevante overleggen.</p></li>
          <li><h3>Onderzoek en data</h3><p>Weten wat er speelt, zodat plannen beter aansluiten.</p></li>
        </ul>
        <p class="small mt-s">Het Ondernemersfonds Dordrecht noemt zelf voorbeelden als feestverlichting, camerabeveiliging en onderzoek, of projecten rond verbinding, duurzaamheid en gezondheid. Of je nu een school, stichting, vereniging of bedrijf bent.</p>
        <div class="deadline">
          <div><small>Eerstvolgende indiendatum</small><strong data-next="indienen">&nbsp;</strong></div>
          <div><small>Besproken in de vergadering van</small><strong data-next="vergadering">&nbsp;</strong></div>
          <a class="btn" href="aanvragen.html">Aanvraag indienen</a>
        </div>''', label='h-thema') + lane('l', 'oker', 'blauw', '''        <h2 id="h-gesteund">Nieuws en mijlpalen</h2>
        <ol class="tijdlijn">
          <li><time datetime="2026-10-14">14 oktober 2026</time><h3>In De Reelander</h3><p>Het wijkblad schrijft over de start van Reeland voor Elkaar, en roept ondernemers, verenigingen en organisaties op om met ideeën voor de wijkeconomie te komen.</p></li>
          <li><time datetime="2026-06-24">24 juni 2026</time><h3>Eerste bijeenkomst met ondernemers</h3><p>Ondernemers uit het Reeland komen bij elkaar om ideeën te verzamelen. De stichting schreef alle 175 bedrijven en organisaties in het gebied aan om zich voor te stellen.</p></li>
          <li><time datetime="2026-01">Begin 2026</time><h3>Eerste gesteunde initiatief</h3><p>Muziek rond de Reeweg 2026: muziek in de wijk, georganiseerd vanuit het Reeland zelf.</p></li>
          <li><time datetime="2025-09-25">25 september 2025</time><h3>Stichting opgericht</h3><p>Bij de notaris in Dordrecht wordt Stichting Reeland voor Elkaar opgericht.</p></li>
        </ol>
        <h2 id="h-meer" class="mt">Meer weten</h2>
        <ul class="list list--3">
          <li><a class="linkcard" href="gebied.html"><h3>Het gebied</h3><p>Wantijbuurt, Transvaalbuurt, Vogelbuurt, Indische Buurt en Land van Valk.</p></a></li>
          <li><a class="linkcard" href="aanvragen.html"><h3>Aanvragen</h3><p>Wat erin moet, wanneer we vergaderen, en antwoorden op veelgestelde vragen.</p></a></li>
          <li><a class="linkcard" href="over-ons.html"><h3>Over ons</h3><p>Wie in het bestuur zitten en hoe je ons bereikt.</p></a></li>
        </ul>''', label='h-meer')

# ---------- Gebied ----------
gebied = '''    <section class="pagehead" aria-labelledby="kop">
      <div class="kopband" aria-hidden="true"></div>
      <div class="wrap">
        <h1 id="kop">Het gebied</h1>
        <p class="lead">Het Reeland ligt ten oosten van de binnenstad van Dordrecht, tussen de Oranjelaan en de Krommedijk, de N3 en het Wantij. Trekkingsgebied 15 bestaat uit vijf buurten met samen ongeveer 175 ondernemers, scholen, verenigingen en organisaties.</p>
      </div>
    </section>

''' + lane('r', 'oranje', 'groen', '''        <h2 id="h-buurten">Vijf buurten</h2>
        <p class="intro">Heb je een pand in een van deze buurten dat geen woning is? Dan betaal je mee aan het fonds en kun je een aanvraag doen.</p>
        <ul class="list list--3">
          <li><h3>Wantijbuurt</h3><p>Het groene noorden aan het Wantij, gebouwd in de jaren dertig. Ruim opgezet, met villa's, het Wantijpark en Villa Augustus.</p></li>
          <li><h3>Transvaalbuurt</h3><p>De oudste buurt, gebouwd rond 1900 tegen de negentiende-eeuwse stadsrand aan. Een compacte stadsbuurt met winkels en bedrijven rond de Transvaalstraat.</p></li>
          <li><h3>Vogelbuurt</h3><p>Gebouwd in de jaren vijftig, na de oorlog. Met het Vogelplein als hart: supermarkt, cafetaria en buurtwerk vanuit Het Vogelnest.</p></li>
          <li><h3>Indische Buurt</h3><p>Het hart van het Reeland, gebouwd tussen 1910 en 1940 op voormalige tuinderijen. Langs de Reeweg Oost zitten bakker, slager, groenteboer en andere winkels.</p></li>
          <li><h3>Land van Valk</h3><p>Vooroorlogse woonbuurt met zorgvuldig metselwerk, aangevuld met de nieuwere bouw van Nieuw Land van Valk.</p></li>
        </ul>''', label='h-buurten') + lane('r', 'groen', 'oranje', '''        <h2 id="h-naam">Waar de naam vandaan komt</h2>
        <p class="intro">Een ree is een rechte grenslijn. In 1560 trokken landmeters zo'n lijn tussen de stad Dordrecht en de toenmalige heerlijkheid Dubbeldam. De Reeweg volgt die oude grens nog steeds. Het gebied werd later bij Dordrecht gevoegd en buurt voor buurt bebouwd: van de Transvaalbuurt rond 1900 tot Plan Tij in 2004.</p>''', label='h-naam') + lane('l', 'groen', 'baksteen', '''        <h2 id="h-kaart">Grenzen van het gebied</h2>
        <!-- [KAART] zodra de kaart van ONS er is: <figure class="map"> met assets/kaart.svg terugzetten -->
        <p class="intro">De precieze grenzen van het trekkingsgebied zijn vastgelegd door het Ondernemersfonds Dordrecht. Een kaart met alle straten volgt. Twijfel je of je pand erbij hoort? Gebruik de straatzoeker hieronder of mail ons.</p>''', label='h-kaart') + lane('r', 'baksteen', 'oker', checker.format(k='gebied') + '''
        <h3 class="mt">Alle straten</h3>
        <ul class="streets" data-stratenlijst></ul>''', id_='hoor-ik-erbij', label='h-check')

# ---------- Aanvragen ----------
aanvragen = f'''    <section class="pagehead" aria-labelledby="kop">
      <div class="kopband" aria-hidden="true"></div>
      <div class="wrap">
        <h1 id="kop">Aanvraag indienen</h1>
        <p class="lead">Ondernemers en organisaties uit het Reeland kunnen een aanvraag doen. Je vult het aanvraagformulier in en stuurt je plan met een begroting mee. Het bestuur beoordeelt het in de eerstvolgende vergadering.</p>
        <div class="actions"><a class="btn" href="aanvraag.html">Naar het aanvraagformulier</a></div>
      </div>
    </section>

''' + lane('r', 'baksteen', 'lichtblauw', '''        <h2 id="h-route">Van plan tot verantwoording</h2>
        <ol class="flow">
          <li><span class="flow__label">Stap 1</span><h3>Plan maken</h3><p>Beschrijf wat je wilt doen en wat het kost. Twijfel je? Wij denken mee en helpen zoeken naar samenwerking met anderen in het gebied.</p></li>
          <li><span class="flow__label">Stap 2</span><h3>Indienen</h3><p>Vul het aanvraagformulier in en stuur projectplan en begroting mee, voor de indiendatum.</p></li>
          <li><span class="flow__label">Stap 3</span><h3>Vergadering</h3><p>Het bestuur bespreekt je aanvraag. Je bent welkom om je plan toe te lichten.</p></li>
          <li><span class="flow__label">Stap 4</span><h3>Besluit</h3><p>Na de vergadering hoor je of je aanvraag is toegekend en onder welke voorwaarden.</p></li>
          <li><span class="flow__label">Stap 5</span><h3>Verantwoorden</h3><p>Na afloop laat je zien hoe het geld is besteed.</p></li>
        </ol>''', label='h-route') + lane('l', 'lichtblauw', 'groen', '''        <h2 id="h-check">Wat we van je vragen</h2>
        <div class="cols">
          <div>
            <h3>In je aanvraag</h3>
            <!-- [CHECKLIST] laten vaststellen door het bestuur -->
            <ul class="check">
              <li>Naam en adres van je onderneming of organisatie in het Reeland, en of je eigenaar of huurder bent</li>
              <li>Contactpersoon met telefoonnummer en mailadres</li>
              <li>Een korte beschrijving van je plan: wat, waar, wanneer en hoe lang</li>
              <li>Waarom het goed is voor de ondernemers en het gebied</li>
              <li>Welke andere ondernemers of organisaties uit het Reeland je plan steunen</li>
              <li>Een begroting met het bedrag dat je aanvraagt, en andere bijdragen of sponsors als die er zijn</li>
              <li>Hoe je het plan bekend maakt</li>
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
        </div>''', label='h-check') + lane('l', 'groen', 'oranje', '''        <h2 id="h-faq">Veelgestelde vragen</h2>
        <div class="faq">
          <details><summary>Moet ik lid worden of me aanmelden?</summary><p>Nee. Heb je een pand in het Reeland dat geen woning is, dan betaal je al mee via de OZB en kun je een aanvraag doen. Je hoeft nergens lid van te worden.</p></details>
          <details><summary>Ik huur mijn pand. Kan ik dan ook aanvragen?</summary><p>Ja. De opslag wordt betaald door eigenaren én gebruikers van panden die geen woning zijn. Huurders horen er dus ook bij.</p></details>
          <details><summary>Kan ik in mijn eentje een aanvraag doen?</summary><p>Het geld is bedoeld voor plannen die meerdere ondernemers of organisaties in het gebied ten goede komen. Een plan voor alleen je eigen bedrijf komt niet in aanmerking. Laat in je aanvraag zien wie er nog meer achter je plan staan.</p></details>
          <details><summary>Kan ik ook aanvragen via de site van ONS Dordrecht?</summary><p>Ja. Kies in het formulier van ONS trekkingsgebied 15, Het Reeland. Omdat het Reeland een eigen stichting heeft, stuurt ONS je aanvraag door naar ons bestuur. Rechtstreeks via ons formulier is iets sneller.</p></details>
          <details><summary>Wie beslist over mijn aanvraag?</summary><p>Het bestuur van de stichting, in een vergadering, bij meerderheid van stemmen. Heeft een bestuurslid zelf belang bij een aanvraag, dan praat en stemt die niet mee.</p></details>
          <details><summary>Hoeveel geld kan ik aanvragen?</summary><p>Dat hangt af van je plan en van wat er voor het Reeland beschikbaar is. Er is geen vast bedrag. Neem gerust vooraf contact op, dan denken we mee over een realistische begroting.</p></details>
          <details><summary>Wat gebeurt er met geld dat niet wordt gebruikt?</summary><p>Dat blijft gereserveerd voor het Reeland bij het Ondernemersfonds Dordrecht. Het gaat niet naar een andere wijk.</p></details>
          <details><summary>Moet ik achteraf iets laten zien?</summary><p>Ja. Na afloop stuur je een kort verslag en de bonnen of facturen. Wij leggen op onze beurt verantwoording af aan het Ondernemersfonds Dordrecht.</p></details>
          <details><summary>Ik weet niet zeker of mijn pand in het gebied ligt.</summary><p>Gebruik de straatzoeker op de pagina Het gebied, of mail ons. We zoeken het voor je uit.</p></details>
        </div>''', id_='vragen', label='h-faq') + lane('r', 'groen', 'oranje', f'''        <h2 id="h-data">Vergaderdata en indientermijn</h2>
        <p class="intro">Het bestuur vergadert ongeveer vier keer per jaar. Stuur je aanvraag uiterlijk op de indiendatum, dan bespreken we hem in de vergadering die erbij hoort. Wil je je plan zelf toelichten of een vergadering bijwonen? Neem dan vooraf contact op.</p>
        <table class="dates">
          <thead><tr><th scope="col">Uiterlijk indienen</th><th scope="col">Vergadering</th></tr></thead>
          <tbody data-dates></tbody>
        </table>''', id_='vergaderdata', label='h-data') + lane('l', 'oranje', 'blauw', f'''        <div class="panel">
          <div>
            <h2 id="h-indienen">Klaar? Vul het formulier in</h2>
            <p>Eerstvolgende indiendatum: <strong data-next="indienen">&nbsp;</strong>.</p>
          </div>
          <div>
            <a class="btn" href="aanvraag.html">Naar het aanvraagformulier</a>
            <p class="small">Of mail naar <a href="mailto:{MAIL}">{MAIL}</a>. Vragen vooraf mogen ook. Je kunt ook het aanvraagformulier op de site van <a href="https://ondernemersfondsdordrecht.nl/">ONS Dordrecht</a> gebruiken; kies dan trekkingsgebied 15, Het Reeland.</p>
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

''' + lane('r', 'groen', 'baksteen', '''        <figure class="photo">
          <img src="assets/foto-oprichting.jpg" alt="De oprichters van de stichting aan tafel bij de notaris" width="640" height="480" loading="lazy">
          <figcaption>Oprichting van de stichting bij Notariaat Nonhebel in Dordrecht, 25 september 2025. Foto: Peter ter Hark.</figcaption>
        </figure>
        <h2 id="h-bestuur" class="mt">Bestuur</h2>
        <p class="intro">Drie ondernemers uit het Reeland. Ze zitten in het bestuur op persoonlijke titel, niet namens hun eigen bedrijf. We zoeken nog versterking: ben jij ondernemer in het Reeland en wil je meedenken? Laat het ons weten.</p>
        <!-- [BESTUUR] per persoon foto, twee zinnen en eigen contactgegevens (voorstel Jolita) -->
        <ul class="board">
          <li><strong>Jolita Meuldijk</strong><span>voorzitter. Eigenaar van Het Schapenhok aan de Reeweg Oost.</span></li>
          <li><strong>Akhshid Zia</strong><span>penningmeester. Ondernemer van PLUS Vogelplein, de supermarkt op het Vogelplein.</span></li>
          <li><strong>Wouter Sieuwerts</strong><span>bestuurslid. Eigenaar van Tolly Wolly Studio en Lexlab aan de Bötgensstraat.</span></li>
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
        <p class="lead">Deze website verzamelt zo weinig mogelijk. Er zijn geen trackingcookies en geen statistieken, en het aanvraagformulier stuurt niets naar ons of naar anderen.</p>
      </div>
    </section>

''' + lane('r', 'groen', 'baksteen', f'''        <h2 id="h-mail">Als je ons mailt</h2>
        <p>Het aanvraagformulier op deze site verstuurt zelf niets. Het maakt een mail aan in je eigen mailprogramma, die je zelf verstuurt. Tot je de pagina sluit, bewaart je browser je antwoorden tijdelijk, alleen op je eigen apparaat.</p>
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


# ---------- Aanvraagformulier ----------
# Zelfde vragen als het aanvraagformulier van ONS Dordrecht. Geen server: het formulier
# maakt een mail aan voorzitter@ (of je kopieert de tekst); bijlagen voeg je in je mail toe.
def veld(id_, label, kind='text', req=True, hint='', extra=''):
    r = ' required' if req else ''
    h = f'<small>{hint}</small>' if hint else ''
    if kind == 'textarea':
        inp = f'<textarea id="{id_}" name="{id_}" rows="5"{r}{extra}></textarea>'
    else:
        inp = f'<input id="{id_}" name="{id_}" type="{kind}"{r}{extra}>'
    return f'<div class="field"><label for="{id_}">{label}{"" if req else " <span>(optioneel)</span>"}</label>{h}{inp}</div>'

def keuze(id_, label, opties, req=True):
    r = ' required' if req else ''
    knoppen = ''.join(f'<label class="opt"><input type="radio" name="{id_}" value="{o}"{r}> {o}</label>' for o in opties)
    return f'<fieldset class="field"><legend>{label}</legend><div class="opts">{knoppen}</div></fieldset>'

aanvraag = f'''    <section class="pagehead" aria-labelledby="kop">
      <div class="kopband" aria-hidden="true"></div>
      <div class="wrap">
        <h1 id="kop">Aanvraagformulier</h1>
        <p class="lead">Vul de vragen in. Met de knop onderaan maak je een mail aan het bestuur, met al je antwoorden erin. Voeg in die mail je projectplan, begroting en andere stukken toe als bijlage, en verstuur hem.</p>
      </div>
    </section>

    <section class="block" aria-labelledby="h-form">
      <div class="wrap">
        <h2 id="h-form" class="sr">Formulier</h2>
        <form class="aanvraag" id="aanvraagformulier" novalidate>
          <fieldset class="group"><legend>Over jou</legend>
            {veld('organisatie', 'Naam van je organisatie of bedrijf')}
            {veld('adres', 'Adres van de vestiging in het Reeland')}
            {keuze('eigendom', 'Ben je eigenaar of huurder van dit adres?', ['Eigenaar', 'Huurder'])}
            {veld('naam', 'Voornaam en achternaam', extra=' autocomplete="name"')}
            {veld('telefoon', 'Telefoonnummer', 'tel', extra=' autocomplete="tel"')}
            {veld('email', 'Mailadres', 'email', extra=' autocomplete="email"')}
          </fieldset>
          <fieldset class="group"><legend>Over je plan</legend>
            {veld('titel', 'Naam van je initiatief')}
            {veld('beschrijving', 'Korte beschrijving van het initiatief', 'textarea', hint='Wat ga je doen, waar en voor wie?')}
            {veld('ontstaan', 'Hoe zijn het idee en de besluitvorming tot stand gekomen?', 'textarea')}
            {keuze('draagvlak', 'Wordt het plan breed en aantoonbaar gesteund door meerdere ondernemingen of organisaties in het Reeland?', ['Ja', 'Nee'])}
            {veld('steun', 'Welke ondernemingen of organisaties steunen het plan?', 'textarea', req=False, hint='Naam en contactpersoon. Een lijst kun je ook als bijlage meesturen.')}
            {keuze('eerder', 'Heb je dit plan al eerder aangevraagd bij een ander trekkingsgebied?', ['Nee', 'Ja'])}
            {veld('start', 'Startdatum', 'date')}
            {veld('looptijd', 'Looptijd', hint='Bijvoorbeeld: 1 dag, 3 maanden')}
          </fieldset>
          <fieldset class="group"><legend>Geld</legend>
            {veld('begroot', 'Totaal begroot bedrag (euro)', 'number', extra=' min="0" step="1" inputmode="numeric"')}
            {veld('gevraagd', 'Bedrag dat je aanvraagt (euro)', 'number', extra=' min="0" step="1" inputmode="numeric"')}
            {keuze('cofinanciering', 'Zijn er ook andere bijdragen of sponsors?', ['Nee', 'Ja'])}
            {veld('cofinanciers', 'Zo ja: welke organisaties en welke bedragen?', 'textarea', req=False)}
            {veld('iban', 'Bankrekeningnummer (IBAN) voor de uitbetaling', extra=' autocomplete="off" spellcheck="false"')}
          </fieldset>
          <fieldset class="group"><legend>Bijlagen</legend>
            <p>Deze stuur je mee als bijlage in de mail die het formulier aanmaakt:</p>
            <ul class="check">
              <li>Projectplan of projectomschrijving</li>
              <li>Begroting</li>
              <li>Lijst met ondernemers en organisaties die het plan steunen</li>
              <li>Communicatieplan: hoe maak je het bekend?</li>
            </ul>
          </fieldset>
          <fieldset class="group"><legend>Tot slot</legend>
            {veld('opmerking', 'Eventuele opmerking', 'textarea', req=False)}
            <label class="opt"><input type="checkbox" name="waarheid" required> Alle gegevens zijn naar waarheid ingevuld.</label>
            <label class="opt"><input type="checkbox" name="privacy" required> Ik ga akkoord met de <a href="privacy.html">privacyverklaring</a>.</label>
          </fieldset>
          <p class="fout" role="alert" hidden></p>
          <div class="actions">
            <button class="btn" type="submit">Maak de mail aan</button>
            <button class="btn btn--licht" type="button" data-kopieer>Kopieer de tekst</button>
          </div>
          <p class="small" data-status role="status"></p>
          <p class="small">Opent er geen mailprogramma? Kopieer dan de tekst en plak hem in een mail aan <a href="mailto:{MAIL}">{MAIL}</a>. Je antwoorden blijven alleen in deze browser bewaard tot je de pagina sluit.</p>
        </form>
      </div>
    </section>
'''

pages = [
  ('index.html', 'Stichting Reeland voor Elkaar | Geld uit het Reeland, voor het Reeland', 'Ondernemers, scholen en verenigingen in het Reeland in Dordrecht betalen mee aan het Ondernemersfonds. Bij Stichting Reeland voor Elkaar vraag je dat geld aan voor de wijk.', 'home', 5, home),
  ('gebied.html', 'Het gebied | Stichting Reeland voor Elkaar', 'De vijf buurten van trekkingsgebied 15 Reeland: Wantijbuurt, Transvaalbuurt, Vogelbuurt, Indische Buurt en Land van Valk.', 'gebied', 2, gebied),
  ('aanvragen.html', 'Aanvraag indienen | Stichting Reeland voor Elkaar', 'Zo dien je een aanvraag in bij Stichting Reeland voor Elkaar: wat erin moet, vergaderdata en indientermijn.', 'aanvragen', 1, aanvragen),
  ('aanvraag.html', 'Aanvraagformulier | Stichting Reeland voor Elkaar', 'Doe een aanvraag bij Stichting Reeland voor Elkaar, trekkingsgebied 15 van ONS Dordrecht.', 'aanvragen', 1, aanvraag),
  ('privacy.html', 'Privacy | Stichting Reeland voor Elkaar', 'Hoe Stichting Reeland voor Elkaar omgaat met gegevens.', 'over', 4, privacy),
  ('404.html', 'Pagina niet gevonden | Stichting Reeland voor Elkaar', 'Deze pagina bestaat niet.', 'home', 5, notfound),
  ('over-ons.html', 'Over ons | Stichting Reeland voor Elkaar', 'Bestuur, doel en contactgegevens van Stichting Reeland voor Elkaar, trekkingsgebied 15 van ONS Dordrecht.', 'over', 4, over),
]
for fn, t, d, pair, logo, body in pages:
    open(os.path.join(root, fn), 'w').write(page(fn, t, d, pair, logo, body))
    print('geschreven', fn)
