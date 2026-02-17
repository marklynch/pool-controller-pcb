Version 1.1.0
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [TODO]
- Test Power circuit works

## [Unreleased]
### Added
### Removed
### Changed
### Fixed

## [0.0.9] - 2026-02-17
### Added
- Updated readme.md file and include power calculation reference and docs.
- Added 3d model files - thanks @alangarf

### Changed
- Rev 9 - Moved the power buck to surface mount component LM2678S-5.0/NOPB
- Rev 9 - Moved the transistor to a SMD
- Rev 9 - Added copper pour for GND on both sides
- Rev 9 - Tided up annotations

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