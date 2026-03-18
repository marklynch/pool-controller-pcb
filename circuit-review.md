# Circuit Review — Pool Controller PCB (Connect 10)

Schematic revision: Rev 11
Reviewed: 2026-03-18

---

## Summary

Four issues were found, ranging from a critical functional defect (circuit won't power on) to component stress
concerns under full load. Potential damage to the power source is also analysed below.

---

## Issue 1 — D2 Reverse Polarity (CRITICAL)

**Component:** D2 — PMEG6010CEH,115 Schottky diode
**Location:** Schematic position (77.47, 82.55), rotation 270°

D2 is intended to be a **series reverse-polarity protection diode** between the +24 V pool-bus supply and
the VIN input of the buck converter (U1). In the schematic, however, it is placed with the wrong rotation:

| Pin | Expected (correct) | Actual (schematic) |
|-----|-------------------|--------------------|
| Anode | +24 V connector side | VIN bus (circuit side) |
| Cathode | VIN bus (circuit side) | +24 V connector side |

With this orientation the diode is **reverse-biased** during normal operation. No current flows from the
+24 V pool bus into U1 VIN, so the buck converter never starts and the board produces no +5 V rail.

This is consistent with the open TODO in CHANGELOG: _"Test Power circuit works"_ — the power circuit
has never been validated, and this is the likely reason it will fail on first test.

**Fix:** Rotate D2 by 180° (change placement angle from 270° to 90°) so that the anode faces the +24 V
supply and the cathode faces the VIN bus.

---

## Issue 2 — D2 Current Rating Too Low

**Component:** D2 — PMEG6010CEH,115
**Rating:** 1 A continuous forward current

When the buck converter runs at full rated load (LM2678S-5.0 → 5 A output at 5 V):

```
I_in ≈ (P_out / η) / V_in
     = (5 A × 5 V / 0.80) / 24 V
     ≈ 1.3 A
```

This exceeds the 1 A continuous rating of PMEG6010CEH. Under sustained full load D2 will overheat and
can fail open (breaking the supply) or short (removing the reverse-polarity protection).

**Fix:** Replace D2 with a Schottky rated ≥ 2 A at 60 V, for example PMEG6020EJ (2 A, SOD-123F
footprint-compatible) or similar, giving a comfortable 50 % derating margin.

---

## Issue 3 — C5 Output Capacitor Effective Value (Moderate)

**Component:** C5 — GRM32ER61C476KE15L, 47 µF / 16 V X5R MLCC
**Location:** Output of buck converter

X5R ceramic capacitors suffer significant DC-bias derating. The Murata GRM32ER61C476KE15L at 5 V
DC bias on a 16 V-rated part retains approximately 50–60 % of its rated capacitance, giving an effective
output capacitance of roughly **23–28 µF** rather than 47 µF.

The LM2678 datasheet recommends a minimum output capacitance of 47 µF (or an equivalent low-ESR
electrolytic). With the actual capacitance closer to 25 µF the converter may exhibit higher output ripple
and the phase margin of the control loop may be reduced from what the WEBENCH simulation showed.

**Fix:** Either use a 16 V → 25 V or higher rated MLCC (reduces bias derating) or add a second 47 µF
MLCC in parallel. A 25 V-rated X5R 47 µF MLCC in the same 1210 footprint would retain > 80 % at 5 V.

---

## Issue 4 — C2 / C3 Input Capacitor Polarity Symbols (Low / Cosmetic)

**Components:** C2, C3 — GRM32ER71J106KA12L, 10 µF / 63 V MLCC
**Symbol used:** Device:C_Polarized_US

The actual components (Murata GRM32ER71J106KA12L) are **ceramic (MLCC) capacitors** — they are
non-polarized. Using a polarized symbol is misleading during manufacturing review and could cause a
pick-and-place operator or inspector to doubt the orientation. It will not cause an electrical problem
because MLCCs have no polarity requirement.

**Fix:** Change C2 and C3 symbols to Device:C (unpolarized) to accurately reflect the component type.

---

## Potential Damage to the Power Source

### If D1 (catch diode) were reversed

D1 is the freewheeling / catch diode in the buck converter. **D1 is currently correct** (anode → GND,
cathode → VSW/L1). If it were assembled reversed:

- When the LM2678 internal switch turns **ON**, VSW rises toward +24 V. A reversed D1 (anode at VSW,
  cathode at GND) would immediately **forward-bias**, creating a direct short-circuit path from VIN
  through the internal switch transistor and D1 to GND.
- Instantaneous short-circuit current would be limited only by trace and switch resistance — likely
  several tens of amps.
- **Result:** U1 (LM2678S) is destroyed within microseconds. The 24 V pool-bus supply would see a
  large current spike; many pool controllers have overcurrent protection that would trip, but the surge
  could damage the supply's internal fuse or output stage.

### If D2 (protection diode) were reversed — *as it currently is in the schematic*

- **Normal polarity connection:** D2 is reverse-biased → no current to circuit → board is dead but
  the power source is unharmed.
- **Reverse polarity connection (accidentally connecting +/−  backwards):** A reversed D2 would
  now **forward-bias**, conducting reverse current through U1 VIN. The LM2678 does not have internal
  reverse voltage protection. The power source would source current in the reverse direction through
  U1, potentially destroying U1 and stressing the source's output stage.

In summary: a reversed D1 is the scenario most likely to damage the external 24 V supply, as it creates
a high-current short circuit on every switching cycle. D2 reversed (the current defect) means the board
simply does not operate in normal use, with damage risk only during an accidental polarity reversal.

---

## What Looks Correct

- **D1 polarity** ✓ — Anode at GND, Cathode at VSW. Standard buck catch-diode orientation.
- **L1 value** — 120 µH is large for 260 kHz operation (TI WEBENCH simulated) and will result in
  longer transient response, but it is not incorrect.
- **Bootstrap cap C1** (10 nF between VSW and CB pins of U1) ✓ — correct placement and value.
- **RX and TX circuits** — no polarity-sensitive components found incorrectly oriented.
- **Q1 (MMBT3904 NPN)** — base/collector/emitter connections appear consistent with an open-drain
  TX drive topology.
