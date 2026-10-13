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
  // SHA-256 in gewoon JavaScript: crypto.subtle werkt alleen via HTTPS, deze versie altijd.
  function sha(ascii) {
    function rr(v, n) { return (v >>> n) | (v << (32 - n)); }
    var i, j, res = '', words = [], k = [], h = [];
    var bits = unescape(encodeURIComponent(ascii));
    var len = bits.length * 8, p = 2, c, x;
    for (c = 0; k.length < 64; p++) {
      var prime = true; for (x = 2; x * x <= p; x++) if (p % x === 0) { prime = false; break; }
      if (prime) { if (h.length < 8) h.push((Math.pow(p, 1 / 2) * 4294967296) | 0); k.push((Math.pow(p, 1 / 3) * 4294967296) | 0); }
    }
    bits += '\x80';
    while (bits.length % 64 - 56) bits += '\x00';
    for (i = 0; i < bits.length; i++) words[i >> 2] |= bits.charCodeAt(i) << ((3 - i) % 4) * 8;
    words[words.length] = (len / 4294967296) | 0;
    words[words.length] = len;
    for (j = 0; j < words.length;) {
      var w = words.slice(j, j += 16), old = h.slice(0);
      for (i = 0; i < 64; i++) {
        var w15 = w[i - 15], w2 = w[i - 2], a = h[0], e = h[4];
        var t1 = h[7] + (rr(e, 6) ^ rr(e, 11) ^ rr(e, 25)) + ((e & h[5]) ^ (~e & h[6])) + k[i] +
          (w[i] = i < 16 ? w[i] : (w[i - 16] + (rr(w15, 7) ^ rr(w15, 18) ^ (w15 >>> 3)) + w[i - 7] + (rr(w2, 17) ^ rr(w2, 19) ^ (w2 >>> 10))) | 0);
        var t2 = (rr(a, 2) ^ rr(a, 13) ^ rr(a, 22)) + ((a & h[1]) ^ (a & h[2]) ^ (h[1] & h[2]));
        h = [(t1 + t2) | 0].concat(h); h[4] = (h[4] + t1) | 0; h.length = 8;
      }
      for (i = 0; i < 8; i++) h[i] = (h[i] + old[i]) | 0;
    }
    for (i = 0; i < 8; i++) for (j = 3; j + 1; j--) { var b = (h[i] >> (j * 8)) & 255; res += (b < 16 ? '0' : '') + b.toString(16); }
    return res;
  }
  document.addEventListener('DOMContentLoaded', function () {
    var g = document.createElement('div');
    g.className = 'gate';
    g.innerHTML = '<form><img src="assets/logo/logo-5.svg" alt="Stichting Reeland voor Elkaar">' +
      '<label for="gate-code">Toegangscode</label><input id="gate-code" type="password" autocomplete="current-password" autofocus>' +
      '<button type="submit">Bekijken</button><p role="status">Deze website is in opbouw.</p></form>';
    document.body.prepend(g);
    g.querySelector('form').addEventListener('submit', function (e) {
      e.preventDefault();
      if (sha(g.querySelector('input').value.trim().toLowerCase()) === HASH) {
        try { localStorage.setItem(KEY, HASH); } catch (err) {}
        g.remove();
        document.documentElement.classList.remove('gesloten');
      } else {
        var p = g.querySelector('p'); p.textContent = 'Deze code klopt niet.'; p.className = 'fout';
      }
    });
  });
})();
