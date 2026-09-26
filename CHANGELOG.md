Version 1.1.0
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [TODO]
- Complete revision 15 prototype acceptance (see docs/rev15-assembly.md).


## [Unreleased] — Revision 15 prototype — 2026-09-12
### Added
- D3 BAT54,215 RX clamp to the Waveshare module 3.3 V rail through J4 pin 3 (issue #3).
- Project-local clamp symbol and retained custom RJ12 footprint.
- Enclosure CAD assessment and reproducible same-case RJ12 opening adjustment; retain 1.2 mm for the original 1.3 mm slot.
- Sample fabrication/assembly outputs and a functional acceptance checklist.
- Pin-adjacent VIN/RX/TX/GND labels for J3.
- PCBWay carrier BOM excluding already-purchased Waveshare modules, SMT-only centroid, and nominated supplier links for all carrier parts.

### Changed
- R3 TX base resistor from 1 kΩ to 560 Ω (issue #4; called R4 in older revisions). R4 stays 100 kΩ.
- J1/J2 to Ckmtw R-RJ11R06P-A000 (LCSC C2902699), with new drilled footprint and connector-region routing. Larger tab-down body requires enclosure/retention review.
- C1/C2/C3/C5 and L1 to current production/active-listed parts; record capacitor DC-bias qualification limits.
- Obsolete DIP-24 socket to J4/J5 Samtec SSW-109-01-T-S nine-position socket strips with manufacturer-derived 1.04 mm drill pattern.

### Validation status
- Prototype revision; physical validation remains required. The rail clamp does not provide power-off isolation.
- PCBWay quote acceptance, exact-part allocation, connector fit on the 1.2 mm board and module installation remain required before assembly.

## [1.1.0] - 2026-08-01
### Changed
- Set the board thickness to 1.2mm instead of default 1.6mm
### Fixed
- Rev 14 - Fixed TX circuit to handle 12v as well as 7v

## [1.0.0] - 2026-04-01
### Fixed
- Rev 13 - Fixed pinout for transistor
- Rev 13 - Tightend up layout for TX and RX components

## [0.10.2] - 2026-03-15
### Changed
- Rev 12 - fixed error in connecting vias shorting gnd to Net D2-K 
- Rev 12 - tidy up routing of D2

## [0.10.1] - 2026-02-26
### Changed
- Rev 11 - changed RJ12 connectors to 5324 6P6C pieces and updated pcb
- Rev 11 - additional gnd connecting vias under buck (U1)

## [0.10.0] - 2026-02-23
### Added
- Added Licence: CERN Open Hardware Licence Version 2 - Permissive

### Changed
- Rev 10 - moved C5 closer to U1
- Rev 10 - added via under U1
- Rev 10 - minor layout improvements.
- Rev 10 - Updated all part numbers and use MPN instead of PartNum
- Cleaned up some documentation


## [0.0.9] - 2026-02-17
### Added
- Updated readme.md file and include power calculation reference and docs.
- Added 3d model files - thanks @alangarf

### Changed
- Rev 9 - Moved the power buck to surface mount component LM2678S-5.0/NOPB
- Rev 9 - Moved the transistor to a SMD
- Rev 9 - Added copper pour for GND on both sides
- Rev 9 - Tided up annotations
- Rev 9 - Reorient header and move labelling closer

## [0.0.8] - 2026-02-16

### Added
- Initial commit of to GitHub
- RX, TX and Power circuits created
- Tested RX circuit works
- Reworked and tested TX circuit

### Changed
- Rev 6 - Reorient board to allow all plugs on one side
- Rev 7 - Reorient power circuit again to make cleaner
- Rev 8 - Updated all footprints to correct specs
- Rev 8 - Updated components to include part numbers
- Rev 8 - Respecced the power circuit based on TI toolins

### Fixed
- Fixed all the DRC rule violations and all but one of the ERC issues
- Make the component imports be relative paths
- Fixed last ERC consistency issue - modified symbol needed an update