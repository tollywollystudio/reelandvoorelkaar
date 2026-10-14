// Aanvraagformulier: maakt een mail aan het bestuur met alle antwoorden.
// Geen server en geen externe dienst; antwoorden blijven alleen in deze browser (sessionStorage).
(function () {
  var form = document.getElementById('aanvraagformulier');
  if (!form) return;
  var MAIL = 'voorzitter@reelandvoorelkaar.nl';
  var KEY = 'rve-aanvraag';
  var fout = form.querySelector('.fout');
  var status = form.querySelector('[data-status]');

  var vragen = [
    ['Over jou', null],
    ['Organisatie of bedrijf', 'organisatie'], ['Adres vestiging', 'adres'], ['Eigenaar of huurder', 'eigendom'],
    ['Naam', 'naam'], ['Telefoon', 'telefoon'], ['Mail', 'email'],
    ['Over het plan', null],
    ['Naam initiatief', 'titel'], ['Beschrijving', 'beschrijving'], ['Ontstaan en besluitvorming', 'ontstaan'],
    ['Breed gesteund door ondernemers/organisaties in het Reeland', 'draagvlak'], ['Steun van', 'steun'],
    ['Eerder aangevraagd bij ander trekkingsgebied', 'eerder'], ['Startdatum', 'start'], ['Looptijd', 'looptijd'],
    ['Geld', null],
    ['Begroot bedrag', 'begroot', '€ '], ['Gevraagd bedrag', 'gevraagd', '€ '], ['Andere bijdragen of sponsors', 'cofinanciering'],
    ['Welke', 'cofinanciers'], ['IBAN', 'iban'],
    ['Overig', null],
    ['Opmerking', 'opmerking']
  ];

  function waarde(naam) {
    var el = form.elements[naam];
    if (!el) return '';
    return (el.value || '').trim();
  }

  function tekst() {
    var regels = ['Aanvraag Stichting Reeland voor Elkaar (trekkingsgebied 15)'];
    var kop = null;
    vragen.forEach(function (v) {
      if (!v[1]) { kop = v[0]; return; }
      var w = waarde(v[1]);
      if (!w) return;
      if (kop) { regels.push('', kop.toUpperCase()); kop = null; }
      regels.push(v[0] + ': ' + (v[2] || '') + w);
    });
    regels.push('', 'Bijlagen: projectplan, begroting, lijst met steun, communicatieplan.',
      'Alle gegevens zijn naar waarheid ingevuld. Akkoord met de privacyverklaring.');
    return regels.join('\n');
  }

  function controleer() {
    var leeg = [];
    Array.prototype.forEach.call(form.querySelectorAll('[required]'), function (el) {
      var ok = el.type === 'checkbox' ? el.checked
        : el.type === 'radio' ? !!form.querySelector('input[name="' + el.name + '"]:checked')
        : el.value.trim() !== '' && el.checkValidity();
      var veld = el.closest('.field, .opt');
      if (veld) veld.classList.toggle('is-fout', !ok);
      if (!ok && leeg.indexOf(el.name) < 0) leeg.push(el.name);
    });
    if (leeg.length) {
      fout.hidden = false;
      fout.textContent = 'Nog niet alles is (goed) ingevuld. De velden met een rode rand missen nog.';
      var eerste = form.querySelector('.is-fout input, .is-fout textarea');
      if (eerste) eerste.focus();
      return false;
    }
    fout.hidden = true;
    return true;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!controleer()) return;
    var onderwerp = 'Aanvraag: ' + (waarde('titel') || 'Reeland voor Elkaar');
    var body = tekst();
    var url = 'mailto:' + MAIL + '?subject=' + encodeURIComponent(onderwerp) + '&body=' + encodeURIComponent(body);
    window.location.href = url;
    status.textContent = 'Je mailprogramma opent nu. Voeg de bijlagen toe en verstuur de mail. Lukt dat niet, gebruik dan "Kopieer de tekst".';
  });

  form.querySelector('[data-kopieer]').addEventListener('click', function () {
    var t = tekst();
    function klaar() { status.textContent = 'De tekst staat op je klembord. Plak hem in een mail aan ' + MAIL + ' en voeg de bijlagen toe.'; }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(t).then(klaar, fallback);
    } else { fallback(); }
    function fallback() {
      var ta = document.createElement('textarea'); ta.value = t; document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); klaar(); } catch (err) { status.textContent = 'Kopiëren lukte niet. Selecteer en kopieer de tekst zelf.'; }
      ta.remove();
    }
  });

  // Tussentijds bewaren binnen deze browsersessie
  try {
    var bewaard = JSON.parse(sessionStorage.getItem(KEY) || '{}');
    Object.keys(bewaard).forEach(function (n) {
      var els = form.querySelectorAll('[name="' + n + '"]');
      Array.prototype.forEach.call(els, function (el) {
        if (el.type === 'radio') el.checked = el.value === bewaard[n];
        else if (el.type === 'checkbox') el.checked = !!bewaard[n];
        else el.value = bewaard[n];
      });
    });
  } catch (e) {}
  form.addEventListener('input', function (e) {
    var el = e.target;
    if (el.closest('.is-fout')) el.closest('.is-fout').classList.remove('is-fout');
    try {
      var b = JSON.parse(sessionStorage.getItem(KEY) || '{}');
      b[el.name] = el.type === 'checkbox' ? el.checked : el.value;
      sessionStorage.setItem(KEY, JSON.stringify(b));
    } catch (err) {}
  });
})();
