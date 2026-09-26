# Rev15 enclosure fit

Retain **1.2 mm PCB thickness**. The author's [pool-controller-case](https://github.com/marklynch/pool-controller-case) `BoxV7.FCStd`, commit `222a908dec85139a257c31b71b18a0f9f9488ca6`, defines a **1.3 mm** PCB slot (Sketch005). A 1.6 mm board would not fit that nominal slot. The PCB author changed thickness from 1.6 to 1.2 mm in [commit 07033f0](https://github.com/marklynch/pool-controller-pcb/commit/07033f06fe821ae59426765578216f9a735abf40). The commit does not explain the reason; the case geometry independently supports retaining 1.2 mm. Allow for board-thickness tolerance and printed-slot fit.

The **unmodified case is not compatible with the current RJ12 body envelopes**. Its front sketch has two 13.25 × 11.5 mm openings; the Ckmtw connector bodies are nominally 13.21 × 12.7 mm across the front. Their centres also differ slightly from the old openings. Do not order a printed original case expecting a verified fit.

`scripts/prepare-enclosure.py` generates a variant of the same case with 15 × 13.5 mm RJ12 openings centred on the current connector envelopes. It preserves the case exterior, PCB slot, lid geometry and USB opening. The script requires the author's external CAD as input and checks its SHA-256 before applying cuts. The output includes STL, editable STEP, the unchanged lid STL if supplied alongside the source, and a geometric collision report. It does not change the original FreeCAD file.

Example, with Python and CadQuery 2.8 installed:

```sh
python scripts/prepare-enclosure.py /path/to/pool-controller-case/BoxV7.FCStd /path/to/enclosure-rev15
```

The collision check covers only the nominal board and approximate RJ12 body envelopes. The connector drawing omits an explicit body-to-tail offset; the whole module/USB/header stack is not modelled. The generated solid was valid; nominal board-to-case, board-to-lid and RJ12-envelope collision volumes were zero after enlargement. A passing check is **not complete assembly validation**. Print one case and check the actual two sockets, cable latch operation, header engagement, module/USB access and lid clearance before printing the batch. Samtec socket body height is 8.51 mm; keep this exact socket MPN. The user already owns the Waveshare modules and will fit them after carrier delivery.

The RJ12 drawing recommends a 1.6 mm PCB. Retaining the case-compatible 1.2 mm carrier therefore still needs flush seating during soldering and a retention check; a thinner board would not remove this exception. The updated purchasing instructions state this requirement explicitly.
