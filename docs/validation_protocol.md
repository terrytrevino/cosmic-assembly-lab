# Assembly index validation protocol (v0.2)

This stage validates molecular graph assembly indexes independently of the speculative magnetodynamics simulator.

## References
- ELIFE-ASU: https://github.com/ELIFE-ASU/assemblytheorytools (caffeine = 9; hydrogen-stripped graph).
- DaymudeLab: https://github.com/DaymudeLab/assembly-theory (anthracene = 6; .mol graph).

## Procedure
1. Install Python, RDKit, `assembly-theory`, and `assemblytheorytools` in an isolated environment.
2. Run `python scripts/validate_assembly.py`.
3. Confirm the reference scores; record library versions, molecule normalization, and execution date.
4. Expand to reference datasets with explicit provenance and licenses.
5. Only then feed validated scores to the browser dashboard.

## Important limitations
- Reference numbers are sourced from repository documentation, not yet independently reproduced here.
- Different graph conventions and algorithms can yield non-comparable indexes.
- No chemical reaction rates, biological interpretations, or magnetic effects are established by these tests.
