# Rev15 prototype manufacturing package

**Use for a PCBWay prototype quotation; confirm exact-part sourcing and mechanical/process requirements before build.** Use [PCBWay upload and quote instructions](PCBWay-instructions.md). Read [assembly and acceptance requirements](../../docs/rev15-assembly.md) with the supplier. No physical prototypes have yet been validated for this revision.

- `PCBWay-package.zip`: convenient download containing the PCBWay upload files and assembly instructions. Unzip it before uploading the separate fabrication/BOM/centroid files.
- `fabrication.zip`: two copper layers, mask, silkscreen, paste, outline, Gerber job file and separate plated/non-plated Excellon drills. Order **80 × 75 mm, 1.2 mm FR-4, nominal 1 oz copper per side**. Approve finish, panel tooling and thermal-pad via treatment with the assembler.
- `BOM.csv`: 20 carrier components (15 SMT and 5 through-hole). J1/J2 specify Ckmtw R-RJ11R06P-A000 / LCSC C2902699. All carrier parts have nominated supplier links. Current capacitor/inductor MPNs replace the prior legacy lines; J4/J5 use two active Samtec nine-position strips.
- `PCBWay-BOM.csv`: use for the carrier quote; includes all 20 carrier components. Waveshare boards are already customer-owned and must not be purchased again.
- `PCBWay-SMT-CPL.csv`: use as PCBWay’s SMT centroid file (15 SMT parts). The five through-hole components and module fitting are covered by the BOM/drawing/instructions.
- `CPL.csv`: native KiCad CSV placement data, **millimetres, absolute board origin**, front side for all 20 references. Negative Y coordinates follow KiCad's exported Cartesian convention; no origin translation or rotation correction has been applied. Includes through-hole parts. Map `Ref/PosX/PosY/Rot/Side` to the supplier's placement fields and approve every orientation in their preview, especially D3, Q1, U1, RJ12 and J4. Footprint origins are the source placement references; the assembler may adjust feeder/centroid conventions.
- `assembly.pdf`, `schematic.pdf`, `copper.pdf`: reference drawings (front assembly, circuit, and front/back copper respectively).
- `erc.json`, `drc.json`: native KiCad checks including schematic parity, required to pass before export.
- `manifest.json`: KiCad version and SHA-256 fingerprints of source and order artifacts. Regenerate whenever the design changes; do not mix revisions.

The **Waveshare development boards have already been purchased separately** and are excluded from PCBWay procurement. Fit them after delivery, or arrange customer consignment and separately quote header fitting if needed, correct-end insertion, programming and functional tests. Do not assume they are included in automated SMT assembly.

## Regeneration

Use KiCad 9 with its standard symbol/footprint libraries installed, plus Python 3. Refill zones and save the PCB in KiCad, then run from the checkout:

```sh
scripts/export-manufacturing.sh
# Or select a specific KiCad 9 CLI:
KICAD_CLI=/path/to/kicad-cli scripts/export-manufacturing.sh
```

The script requires clean ERC, DRC and schematic parity, checks the 20-reference BOM/placement set and selected revision-specific MPNs, then replaces the generated artifacts. It does not order boards or certify electrical behavior. Timestamps and PDF metadata can differ between export runs; use the manifest to identify this exact package.
