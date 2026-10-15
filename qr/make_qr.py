"""Genera els codis QR de l'exposició (un per secció) amb segno, sense cap servei extern.
Ús:  python make_qr.py https://la-teua-url-final/
Crea PNG (per imprimir) i SVG (vectorial) dins d'aquesta carpeta."""
import sys, os, segno
base = sys.argv[1] if len(sys.argv) > 1 else 'https://ausaescoop.github.io/diversitat-montitxelvo/'
if not base.endswith('/'): base += '/'
secs = {'inici': '', 'diversitat': '#diversitat', 'historia': '#historia',
        'referents': '#referents', 'recursos': '#recursos', 'exposicio': '#exposicio'}
out = os.path.dirname(os.path.abspath(__file__))
for name, anchor in secs.items():
    url = base + anchor
    q = segno.make(url, error='h')
    q.save(os.path.join(out, f'qr-{name}.png'), scale=12, border=2, dark='#1d1a21', light='#ffffff')
    q.save(os.path.join(out, f'qr-{name}.svg'), scale=12, border=2, dark='#1d1a21', light='#ffffff')
    print(f'{name:12} -> {url}')
