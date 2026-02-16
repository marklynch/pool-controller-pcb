Version 1.1.0
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [TODO]
- Test Power circuit works

## [Unreleased]
- Updated readme.md file and include power calculation reference and docs.

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