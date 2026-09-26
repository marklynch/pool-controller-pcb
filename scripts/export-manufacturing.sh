#!/usr/bin/env bash
# Refill zones and save the PCB in KiCad before running this script.
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ -z "${KICAD_CLI:-}" ]]; then
  if command -v kicad-cli >/dev/null 2>&1; then
    KICAD_CLI="$(command -v kicad-cli)"
  else
    KICAD_CLI=/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli
  fi
fi
version="$("$KICAD_CLI" version)"
[[ "$version" == 9.* ]] || { echo 'KiCad 9 is required.' >&2; exit 1; }
out=manufacturing/rev15
mkdir -p "$out"
stage="$(mktemp -d)"
trap 'rm -rf "$stage"' EXIT
"$KICAD_CLI" sch erc --format json --exit-code-violations -o "$stage/erc.json" PoolController.kicad_sch
"$KICAD_CLI" pcb drc --schematic-parity --format json --exit-code-violations -o "$stage/drc.json" PoolController.kicad_pcb
mkdir "$stage/gerbers"
"$KICAD_CLI" pcb export gerbers -l F.Cu,B.Cu,F.Paste,B.Paste,F.SilkS,B.SilkS,F.Mask,B.Mask,Edge.Cuts --subtract-soldermask -o "$stage/gerbers/" PoolController.kicad_pcb
"$KICAD_CLI" pcb export drill --format excellon --drill-origin absolute --excellon-units mm --excellon-separate-th -o "$stage/gerbers/" PoolController.kicad_pcb
"$KICAD_CLI" sch export bom --fields 'Reference,Value,Footprint,Manufacturer,MPN,${QUANTITY}' --labels 'Designator,Comment,Footprint,Manufacturer,MPN,Quantity' --group-by Value,Footprint,MPN --ref-range-delimiter '' --exclude-dnp -o "$stage/BOM.csv" PoolController.kicad_sch
"$KICAD_CLI" pcb export pos --format csv --units mm --side both --exclude-dnp -o "$stage/CPL.csv" PoolController.kicad_pcb
"$KICAD_CLI" sch export pdf -o "$stage/schematic.pdf" PoolController.kicad_sch
"$KICAD_CLI" pcb export pdf --mode-single --black-and-white --exclude-value -l F.Fab,F.SilkS,Edge.Cuts --sketch-pads-on-fab-layers --include-border-title -o "$stage/assembly.pdf" PoolController.kicad_pcb
"$KICAD_CLI" pcb export pdf --mode-multipage -l F.Cu,B.Cu --common-layers Edge.Cuts --include-border-title -o "$stage/copper/" PoolController.kicad_pcb
mv "$stage/copper/PoolController.pdf" "$stage/copper.pdf"
python3 scripts/package-manufacturing.py "$stage" "$out" "$version"
echo "Prototype package written to $out. Read its README before requesting assembly."
