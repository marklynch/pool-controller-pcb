# AstralPool Controller PCB

PCB design files for an AstralPool-compatible pool controller interface board.

## Overview

This project contains a custom PCB designed to interface with AstralPool systems. The board features RS-232 like communication on a single wire (TX/RX) and a regulated power supply to enable reliable communication and control.

**Current Version:** 0.9.0 (Rev 9)

## Features

- **Communication Interface**
  - Dedicated RX (receive) circuit - tested and verified
  - Dedicated TX (transmit) circuit - tested and verified

- **Regulated Power Supply**
  - Based on TI LM2678S-5.0 buck converter
  - 5V output voltage
  - Designed using TI WEBENCH tools for optimal performance

- **Optimized Layout**
  - All connectors positioned on one side for easy installation
  - Clean signal routing with minimal crosstalk
  - DRC/ERC compliant design

## Project Status

- [x] RX circuit designed and tested
- [x] TX circuit designed and tested
- [x] Power circuit designed and specified
- [x] PCB layout optimized (Rev 8)
- [x] DRC/ERC violations resolved
- [x] Manufacturing files generated (Gerbers, BOM)
- [ ] Power circuit testing pending

## Project Structure

```
pool-controller-pcb/
├── AstralPool.kicad_pro     # KiCad project file
├── AstralPool.kicad_sch     # Schematic design
├── AstralPool.kicad_pcb     # PCB layout
├── components/              # Custom component libraries
│   └── ul_LM2678T-5-0-NOPB/ # LM2678 voltage regulator footprint/symbol
├── docs/                    # Datasheets and design documentation
│   ├── ZV1636_datasheetMain_96004.pdf
│   └── WBDesign1_Bode Plot-1.pdf
├── output/                  # Manufacturing files
│   ├── gerbers_v8.zip      # Latest Gerber files for PCB fabrication
│   ├── BOM_v8.csv          # Bill of Materials
│   └── ...
├── CHANGELOG.md            # Version history
└── README.md              # This file
```

## Manufacturing Files

Ready-to-manufacture files are available in the `output/` directory:

- **Gerber Files:** `gerbers_v8.zip` - Contains all layers for PCB fabrication
- **Bill of Materials:** `BOM_v8.csv` - Complete component list with part numbers
- **Drill Files:** Included in gerber package (PTH and NPTH)

## Requirements

- **KiCad 6.0 or later** - Required to open and edit the design files
- All custom components and footprints are included in the `components/` directory

## Getting Started

1. Clone this repository
2. Open `AstralPool.kicad_pro` in KiCad
3. Custom component libraries should load automatically via relative paths

## Documentation

- See [CHANGELOG.md](CHANGELOG.md) for detailed version history and changes
- Component datasheets are available in the `docs/` directory
- Power supply design based on TI WEBENCH simulations (see Bode plot in docs)

## Version History

See [CHANGELOG.md](CHANGELOG.md) for a complete list of changes.

**Latest Release (0.0.8 - 2026-02-16):**
- Updated all footprints to correct specifications
- Added manufacturer part numbers to all components
- Redesigned power circuit using TI WEBENCH tools
- Resolved all DRC/ERC violations

## Notes

- Component library paths are configured as relative paths for portability
- Automatic backup files are saved to `AstralPool-backups/`
- Output files are excluded from git tracking (see `.gitignore`)

## License

[Add your license information here]
