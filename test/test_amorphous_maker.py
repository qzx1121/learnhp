"""
python v3.7.9
@Project: hotpot
@File   : test_amorphous_maker.py
@Author : Zhiyuan Zhang
@Date   : 2023/4/26
@Time   : 5:09
"""
from src.cheminfo import Molecule as Mol

mol = Mol.create_aCryst_by_mq(
    elements={'C': 1.0}, force_field='aMaterials/SiC.tersoff',
    ff_args=('C',), path_dump_to='/home/qyq/proj/lammps/mq_test_random/try4/melt-quench-0.4.xyz',
    fmt='xyz', density=1.0, melt_temp=5000, highest_temp=10000
)
mol.crystal().space_group = 'P1'
mol.writefile('cif', '/home/qyq/proj/lammps/mq_test_random/try4/mq-0.4.cif')
