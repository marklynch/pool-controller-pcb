# Pool Controller PCB

KiCad design for a Connect 10 compatible pool-bus interface, using the finished **Waveshare ESP32-C6 Mini Development Board (ESP32-C6-Zero)** plugged into a carrier socket. The board provides a 5 V buck supply and single-wire receive/transmit interface. Firmware is maintained in [pool-controller-code](https://github.com/marklynch/pool-controller-code).

## Current revision

**Revision 15 is a prototype for validation.** It adds the 3.3 V RX clamp from [issue #3](https://github.com/marklynch/pool-controller-pcb/issues/3) and changes the TX base resistor to 560 Ω as proposed in [issue #4](https://github.com/marklynch/pool-controller-pcb/issues/4). It retains the existing 80 × 75 mm outline and 1.2 mm thickness.

The RX clamp requires the Waveshare 3.3 V rail and does not provide power-off isolation. Confirm operation during boot/reset/shutdown and at both 7 V and 12 V data-high levels before field use. The power-supply design report's detailed operating point is **5 V / 0.5 A**; a 5 A regulator IC does not make this a 5 A board.

See [revision 15 assembly and acceptance](docs/rev15-assembly.md) before ordering. J1/J2 now specify distributor-stocked Ckmtw R-RJ11R06P-A000 (LCSC C2902699), with a matching new footprint and connector routing. The original case has a 1.3 mm PCB slot, so retain the 1.2 mm board. Its RJ12 openings need enlargement: see [enclosure fit and same-case variant](docs/rev15-enclosure.md). Confirm snap-peg retention on the 1.2 mm board with PCBWay. The Waveshare boards have already been purchased separately; PCBWay should supply the soldered carrier and its two Samtec socket strips, with no additional module purchase.

## Files

- `PoolController.kicad_pro`, `.kicad_sch`, `.kicad_pcb`: source project, schematic and routed PCB.
- `components/`: project-specific symbols, footprints and existing 3D models.
- `docs/`: component/design references and prototype assembly instructions.
- `manufacturing/rev15/`: revision-specific sample-order exports and validation record.
- `scripts/export-manufacturing.sh`: reproduce manufacturing exports using KiCad 9.

Use **KiCad 9** to open and validate the project. Custom library paths are relative to the project. A 3D model is not a substitute for checking the dimensions and pin mapping of the actual purchased part.

## Ordering prototypes

For PCBWay, use `PCBWay-BOM.csv` (carrier parts only; Waveshare boards are customer-supplied) and `PCBWay-SMT-CPL.csv`. Read the assembly notes, confirm exact-part allocation and module installation, and review their DFM and placement previews before authorizing fabrication/assembly. Gerbers and drill files cover the bare board; the BOM, placement file and assembly drawing define fitted carrier parts. Fit the customer-owned module after delivery, or arrange consignment and separately quote installation/programming with PCBWay.

Physical checks, supplier approval, firmware programming and functional testing are distinct from KiCad ERC/DRC. Generated files are a prototype build package, not proof of field reliability.

## Licence

Hardware designs are licensed under the CERN Open Hardware Licence Version 2 — Permissive; see [LICENCE](LICENCE). See [CHANGELOG.md](CHANGELOG.md) for revision history.
