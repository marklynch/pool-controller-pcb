"""Validate the carrier reference set and package KiCad exports (stdlib only)."""
import csv
import hashlib
import json
from pathlib import Path
import shutil
import sys
import zipfile

stage, out = map(Path, sys.argv[1:3])
version = sys.argv[3]
with (stage / 'BOM.csv').open(newline='') as f:
    bom = list(csv.DictReader(f))
with (stage / 'CPL.csv').open(newline='') as f:
    positions = list(csv.DictReader(f))
refs = [ref for row in bom for ref in row['Designator'].split(',')]
expected = {f'{prefix}{i}' for prefix, count in [('C', 5), ('D', 3), ('J', 5), ('L', 1), ('Q', 1), ('R', 4), ('U', 1)] for i in range(1, count + 1)}
assert len(refs) == len(set(refs)) == 20 and set(refs) == expected
assert len(positions) == 20 and {r['Ref'] for r in positions} == expected
assert all(r['Side'] == 'top' for r in positions)
parts = {ref: row for row in bom for ref in row['Designator'].split(',')}
assert parts['R3']['MPN'] == 'RC0603FR-07560RL'
assert parts['R4']['MPN'] == 'RC0603FR-07100KL'
assert parts['D3']['MPN'] == 'BAT54,215'
assert parts['L1']['MPN'] == 'SRR1050HA-121Y'
assert parts['J4']['MPN'] == parts['J5']['MPN'] == 'SSW-109-01-T-S'
procurement = json.loads(Path('manufacturing/procurement.json').read_text())
assert parts['J1']['MPN'] == parts['J2']['MPN'] == 'R-RJ11R06P-A000'
for row in bom:
    source = procurement[row['MPN']]
    for field in ['Supplier', 'Supplier Part', 'Supplier URL', 'Procurement note']:
        row[field] = source.get(field, '')
with (stage / 'BOM.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(bom[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(bom)
# PCBWay requests SMT-only centroid data. Keep full CPL for engineering review.
with (stage / 'PCBWay-SMT-CPL.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(positions[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(r for r in positions if not r['Ref'].startswith('J'))
# The user already owns the Waveshare boards. Do not include them in procurement.
with (stage / 'PCBWay-BOM.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(bom[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(bom)
with zipfile.ZipFile(stage / 'fabrication.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for path in sorted((stage / 'gerbers').iterdir()):
        z.write(path, path.name)
for name in ['BOM.csv', 'CPL.csv', 'PCBWay-BOM.csv', 'PCBWay-SMT-CPL.csv', 'schematic.pdf', 'assembly.pdf', 'copper.pdf', 'erc.json', 'drc.json', 'fabrication.zip']:
    shutil.copyfile(stage / name, out / name)
with zipfile.ZipFile(out / 'PCBWay-package.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    for name in ['fabrication.zip', 'CPL.csv', 'PCBWay-BOM.csv', 'PCBWay-SMT-CPL.csv', 'assembly.pdf', 'schematic.pdf', 'PCBWay-instructions.md']:
        z.write(out / name, name)
    z.write('docs/rev15-assembly.md', 'docs/rev15-assembly.md')
    z.write('docs/rev15-enclosure.md', 'docs/rev15-enclosure.md')
source_paths = [Path(n) for n in ['PoolController.kicad_pcb', 'PoolController.kicad_sch', 'PoolController.kicad_pro', 'fp-lib-table', 'sym-lib-table']]
source_paths += sorted(Path('components').rglob('*.kicad_sym'))
source_paths += sorted(Path('components').rglob('*.kicad_mod'))
source_paths += sorted(Path('scripts').glob('*'))
source_paths += [Path('manufacturing/procurement.json'), Path('docs/rev15-assembly.md'), Path('docs/rev15-enclosure.md'), Path('manufacturing/rev15/PCBWay-instructions.md')]
manifest = {'kicad_version': version, 'carrier_parts': 20, 'source_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}, 'artifact_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.iterdir()) if p.suffix in {'.csv', '.pdf', '.zip'}}, 'status': 'Prototype; procurement and physical acceptance remain required. See README.md and docs/rev15-assembly.md.'}
(out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
