"""Reproduce published reference assembly-index examples.
Run locally: pip install rdkit assembly-theory assemblytheorytools
Then: python scripts/validate_assembly.py
"""
import csv
from pathlib import Path
from rdkit import Chem
import assembly_theory as daymude
import assemblytheorytools as att

records = list(csv.DictReader((Path(__file__).resolve().parents[1] / "data" / "reference_molecules.csv").open()))
failures = 0
for row in records:
    smi = row["smiles"]
    if row["molecule"] == "Anthracene":
        mol = Chem.MolFromSmiles(smi)
        assert mol is not None
        observed = daymude.index(Chem.MolToMolBlock(mol))
        engine = "DaymudeLab assembly-theory"
    elif row["molecule"] == "Caffeine":
        observed, _, _ = att.calculate_assembly_index(att.smi_to_nx(smi), strip_hydrogen=True)
        engine = "ELIFE-ASU assemblytheorytools"
    else:
        continue
    expected = int(row["reference_index"])
    ok = int(observed) == expected
    failures += not ok
    print(f'{row["molecule"]}: expected={expected}, calculated={observed}, engine={engine}, {"PASS" if ok else "FAIL"}')
if failures:
    raise SystemExit(f"{failures} reference mismatches")
