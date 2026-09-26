"""Generate a Rev15 front-opening variant from the author's external BoxV7.FCStd.

Requires CadQuery 2.8; usage: python prepare-enclosure.py BoxV7.FCStd output-dir
The original CAD is an input, not redistributed by this PCB repository.
"""
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import zipfile

import cadquery as cq

source, out = map(Path, sys.argv[1:3])
expected = 'b3a799a3120478a39fe5507cd7fe07e3def7676603423f4285bb2d3dfbaacddd'
if hashlib.sha256(source.read_bytes()).hexdigest() != expected:
    raise SystemExit('Expected BoxV7.FCStd from pool-controller-case commit 222a908; review changed CAD first.')
out.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / 'case.brep'
    with zipfile.ZipFile(source) as archive:
        path.write_bytes(archive.read('Body.Shape.brp'))
    original = cq.Shape.importBrep(str(path))
    with zipfile.ZipFile(source) as archive:
        path.write_bytes(archive.read('Body001.Shape.brp'))
    lid_shape = cq.Shape.importBrep(str(path)).translate((0, -40, 79))


def box(x, y, z, dx, dy, dz):
    return cq.Solid.makeBox(dx, dy, dz, cq.Vector(x, y, z))


# Original FreeCAD coordinates: X across front, Y height, Z front-to-back.
# PCB x=65..145 maps to case Z=1..81; PCB y=40..115 maps to X=37.5..-37.5.
# The front panel has a 2 mm pocket from Z=3 back to Z=1.
# PCB bottom Y=-7, top=-5.8; retain the original 1.3 mm slot and lid.
# Nominal Ckmtw body centres derive from current PCB pad origins, not old windows.
centres = [-0.675, -19.225]
case = original
for centre in centres:
    case = case.cut(box(centre - 7.5, -6.0, -0.1, 15.0, 13.5, 3.2))
case = case.clean()
if not case.isValid() or len(case.Solids()) != 1:
    raise SystemExit('Invalid enclosure result')

board = box(-37.5, -7, 1, 75, 1.2, 80)
# Approximate RJ12 envelopes: supplier does not dimension the body/tail offset.
bodies = [box(c - 6.605, -5.8, -0.54, 13.21, 12.7, 20.54) for c in centres]
report = {
    'source_commit': '222a908dec85139a257c31b71b18a0f9f9488ca6',
    'source_sha256': expected,
    'cadquery_version': cq.__version__,
    'valid_solid': True,
    'pcb_thickness_mm': 1.2,
    'original_slot_mm': 1.3,
    'new_rj12_openings_mm': {'width': 15, 'height': 13.5, 'x_centres': centres, 'y_min': -6},
    'pcb_collision_mm3': case.intersect(board).Volume(),
    'lid_pcb_collision_mm3': lid_shape.intersect(board).Volume(),
    'original_rj12_envelope_collision_mm3': [original.intersect(b).Volume() for b in bodies],
    'revised_rj12_envelope_collision_mm3': [case.intersect(b).Volume() for b in bodies],
    'limitations': 'Nominal board/RJ12 envelopes only. Actual body offset, latch/cable access, module header engagement, USB access and printed tolerances require a physical fit check. USB opening is unchanged.',
}
if report['pcb_collision_mm3'] > 1e-5 or report['lid_pcb_collision_mm3'] > 1e-5 or any(v > 1e-5 for v in report['revised_rj12_envelope_collision_mm3']):
    raise SystemExit('Nominal board/connector collision: ' + json.dumps(report))
cq.exporters.export(case, str(out / 'BoxV7-Rev15-Case.stl'), tolerance=0.05, angularTolerance=0.1)
cq.exporters.export(case, str(out / 'BoxV7-Rev15-Case.step'))
lid = source.with_name('BoxV7-Lid.stl')
if lid.exists():
    shutil.copyfile(lid, out / lid.name)
(out / 'fit-report.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
