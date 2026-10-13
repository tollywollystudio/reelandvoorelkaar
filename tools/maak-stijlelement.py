# Gebruik: python3 tools/maak-stijlelement.py assets/slinger.svg
# Stijlelement naar het blad van Leen Oud: twee gespiegelde kolommen slingers,
# banen op gelijke hoogte, kleurwissel midden in elke bocht.
import sys
SW, R = 40, 27                 # banddikte, straal hart; tussenruimte = 2R - SW = 14
P = 2 * R                      # afstand tussen banen
C = ['#b2dde5', '#af5248', '#7c986c', '#e05031', '#c1d2c5', '#d2b649', '#0d3183', '#f6bdc1']

def kolom(xl, xr, rows, first_bend):
    """rows: lijst (rij, kleur). first_bend: 'r' of 'l' = kant van de eerste bocht."""
    paden = []
    n = len(rows)
    for i, (k, kl) in enumerate(rows):
        y = 20 + k * P
        bend_out = first_bend if i % 2 == 0 else ('l' if first_bend == 'r' else 'r')   # bocht na deze baan
        bend_in = None if i == 0 else ('l' if bend_out == 'r' else 'r')                # bocht voor deze baan
        # richting: naar de kant van bend_out
        sx, ex = (xl, xr) if bend_out == 'r' else (xr, xl)
        d = ''
        if bend_in is None:
            d += f'M{sx:.0f} {y} '
        else:
            cx = xl if bend_in == 'l' else xr
            px = cx - R if bend_in == 'l' else cx + R
            sweep = 0 if bend_in == 'l' else 1
            d += f'M{px:.0f} {y - R} A{R} {R} 0 0 {sweep} {cx:.0f} {y} '
        if i < n - 1:
            d += f'H{ex:.0f} '
            mx = ex + R if bend_out == 'r' else ex - R
            sweep = 1 if bend_out == 'r' else 0
            d += f'A{R} {R} 0 0 {sweep} {mx:.0f} {y + R}'
        else:
            d += f'H{ex:.0f}'
        paden.append(f'<path d="{d}" stroke="{kl}"/>')
    return paden

B = R + SW / 2                         # hoe ver een bocht uitsteekt
M = 12                                 # ruimte tussen de bochten in het midden
KOL = 150                              # lengte van de rechte stukken
lx0 = B; lx1 = lx0 + KOL
rx0 = lx1 + 2 * B + M; rx1 = rx0 + KOL
W = rx1 + B
# rechterkolom: rij 0..7, eerste bocht rechts; linkerkolom: rij 1..6, eerste bocht links (spiegel)
rechts = kolom(rx0, rx1, [(k, C[k]) for k in range(8)], 'r')
links = kolom(lx0 - 0, lx1, [(k, C[k]) for k in range(1, 7)], 'l')
# open uiteinden: rechterkolom begint links bij het midden, eindigt aan de rechterkant;
# linkerkolom begint en eindigt bij het midden.
H = 20 + 7 * P + SW / 2
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.0f}" fill="none" stroke-width="{SW}" aria-hidden="true">']
svg += ['  ' + p for p in links + rechts]
svg.append('</svg>')
open(sys.argv[1], 'w').write('\n'.join(svg) + '\n')
