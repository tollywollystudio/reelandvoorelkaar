(function () {
  var data = window.REELAND || { vergaderingen: [], straten: [] };
  var today = new Date().toISOString().slice(0, 10);
  var fmt = function (iso) {
    return new Date(iso + 'T12:00:00').toLocaleDateString('nl-NL', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' });
  };
  var next = data.vergaderingen.filter(function (v) { return v.indienen >= today; })[0];

  // Eerstvolgende indiendatum
  document.querySelectorAll('[data-next="indienen"]').forEach(function (el) { el.textContent = next ? fmt(next.indienen) : 'volgt binnenkort'; });
  document.querySelectorAll('[data-next="vergadering"]').forEach(function (el) { el.textContent = next ? fmt(next.vergadering) : 'volgt binnenkort'; });

  // Tabel met alle vergaderingen
  document.querySelectorAll('[data-dates]').forEach(function (tbody) {
    if (!data.vergaderingen.length) {
      tbody.innerHTML = '<tr><td colspan="2">De vergaderdata voor de komende periode volgen binnenkort.</td></tr>';
    }
    data.vergaderingen.forEach(function (v) {
      var tr = document.createElement('tr');
      if (v.indienen < today) tr.className = 'is-past';
      else if (v === next) tr.className = 'is-next';
      [v.indienen, v.vergadering].forEach(function (d) {
        var td = document.createElement('td'); td.textContent = fmt(d); tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
  });

  // Straatzoeker
  var norm = function (s) { return s.toLowerCase().replace(/[0-9].*$/, '').replace(/[^a-zà-ÿ]/g, ''); };
  document.querySelectorAll('[data-straatcheck]').forEach(function (form) {
    var input = form.querySelector('input');
    var out = form.parentNode.querySelector('.result');
    var list = document.getElementById('straten-lijst');
    if (list && !list.children.length) {
      data.straten.forEach(function (s) { var o = document.createElement('option'); o.value = s.straat; list.appendChild(o); });
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var q = norm(input.value);
      if (!q) return;
      var hit = data.straten.filter(function (s) { return norm(s.straat) === q; })[0];
      out.className = 'result ' + (hit ? 'result--ja' : 'result--nee');
      out.textContent = hit
        ? 'Ja, ' + hit.straat + ' hoort bij het trekkingsgebied (' + hit.buurt + ').'
        : data.stratenCompleet
          ? 'Deze straat staat niet in onze lijst. Twijfel je? Mail ons, dan zoeken we het uit.'
          : 'Onze stratenlijst wordt nog aangevuld. Mail ons, dan laten we weten of je pand erbij hoort.';
    });
  });

  // Volledige stratenlijst
  document.querySelectorAll('[data-stratenlijst]').forEach(function (ul) {
    data.straten.slice().sort(function (a, b) { return a.straat.localeCompare(b.straat, 'nl'); }).forEach(function (s) {
      var li = document.createElement('li'); li.textContent = s.straat; ul.appendChild(li);
    });
  });
})();
