import hotpot as hp
mol = hp.Molecule.read_from('c1ccccc1', 'smi')
print(mol.has_3d)
mol.build_3d(force_field='UFF')
print(mol.has_3d)
mol.normalize_labels()
for atom in mol.atoms:
  print(atom.label, atom.symbol, atom.coordinates)