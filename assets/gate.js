// Tijdelijke toegangscode zolang de site in opbouw is.
// Dit is een gordijn, geen beveiliging: de bestanden zelf zijn openbaar op GitHub.
// Verwijderen bij livegang: dit bestand, de <script src="assets/gate.js"> en de robots-meta in elke pagina.
(function () {
  var HASH = '9a3067ab4e70cf3d2218e61b4f7d9f7b4cf575041db9d3a28ff2d562e38fcbe9';
  var KEY = 'rve-toegang';
  try { if (localStorage.getItem(KEY) === HASH) return; } catch (e) {}
  document.documentElement.classList.add('gesloten');
  var css = document.createElement('style');
  css.textContent = 'html.gesloten body>*:not(.gate){display:none!important}' +
    '.gate{min-height:100vh;display:grid;place-items:center;padding:1.25rem;font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;color:#0d3183}' +
    '.gate form{width:100%;max-width:22rem;text-align:center}.gate img{width:11rem;margin:0 auto 2rem;display:block}' +
    '.gate label{display:block;font-weight:700;margin-bottom:.5rem}.gate input{width:100%;font:inherit;padding:.75rem .9rem;border:1px solid #b9bfd6;border-radius:4px;margin-bottom:.75rem}' +
    '.gate button{width:100%;font:inherit;font-weight:700;padding:.8rem;border:0;border-radius:4px;background:#af5248;color:#fff;cursor:pointer}' +
    '.gate p{font-size:.9rem;color:#46507f;margin:1rem 0 0}.gate .fout{color:#af5248;font-weight:700}';
  document.head.appendChild(css);
  async function sha(t) {
    var b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t));
    return Array.from(new Uint8Array(b)).map(function (x) { return x.toString(16).padStart(2, '0'); }).join('');
  }
  document.addEventListener('DOMContentLoaded', function () {
    var g = document.createElement('div');
    g.className = 'gate';
    g.innerHTML = '<form><img src="assets/logo/logo-5.svg" alt="Stichting Reeland voor Elkaar">' +
      '<label for="gate-code">Toegangscode</label><input id="gate-code" type="password" autocomplete="current-password" autofocus>' +
      '<button type="submit">Bekijken</button><p role="status">Deze website is in opbouw.</p></form>';
    document.body.prepend(g);
    g.querySelector('form').addEventListener('submit', async function (e) {
      e.preventDefault();
      if (await sha(g.querySelector('input').value.trim()) === HASH) {
        try { localStorage.setItem(KEY, HASH); } catch (err) {}
        g.remove();
        document.documentElement.classList.remove('gesloten');
      } else {
        var p = g.querySelector('p'); p.textContent = 'Deze code klopt niet.'; p.className = 'fout';
      }
    });
  });
})();
