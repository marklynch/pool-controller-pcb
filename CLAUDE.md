# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is a **KiCad 6+ hardware project**, not a software project. There is no build/lint/test toolchain — design work happens inside the KiCad GUI, and "source files" are the schematic and PCB:

- `PoolController.kicad_pro` — project file (open this in KiCad)
- `PoolController.kicad_sch` — schematic
- `PoolController.kicad_pcb` — PCB layout
- `PoolController.kicad_prl` — local project settings (gitignored)

The board is a Connect 10 pool-controller interface (TX/RX single-wire serial + LM2678S-5.0 buck regulator) that pairs with the ESP32-C6 firmware in https://github.com/marklynch/pool-controller-code.

## Legacy `AstralPool` naming

Some files (`AstralPool.kicad_prl`, `AstralPool-backups/`, older gerbers in `output/`) use the prior project name. The active project is `PoolController.*` — treat the `AstralPool*` files as historical and don't propagate the old name into new outputs.

## Custom component libraries

Custom symbols/footprints live under `components/` and are wired up via `sym-lib-table` and `fp-lib-table` using `${KIPRJMOD}` so the paths stay relative and portable. If you add a new custom part, register it in both tables the same way — don't use absolute paths.

`components/3dmodels/` holds STEP/STP models referenced by footprints.

## Revisions, versions, and the CHANGELOG

Two parallel version numbers exist and they are not the same thing:

- **Rev N** (e.g. "Rev 13") = a physical PCB revision. Most CHANGELOG entries are tagged with the Rev they correspond to. Whenever the board layout changes meaningfully, bump the Rev.
- **SemVer tag** (e.g. `1.0.0`) = the release tag on the repo, grouping one or more Revs.

`CHANGELOG.md` follows Keep a Changelog. New work goes under `[Unreleased]` in the appropriate Added/Changed/Fixed/etc. section. There is also a `[TODO]` section at the top tracking outstanding work (e.g. power-circuit bring-up).

## Outputs are not in git

`output/` and `*-backups/` directories, plus `*.csv` / `*.net` / `*.dsn` / `*.ses` exports, are gitignored (see `.gitignore`). Don't commit generated gerbers, BOMs, or position files. When regenerating, name them with the current Rev (e.g. `gerbers_v13.zip`, `BOM_v13.csv`) to match the existing convention.

## License

Hardware is CERN-OHL-P v2 (see `LICENCE`). Keep that in mind for any derived files added to the repo.
