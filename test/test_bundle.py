"""
python v3.7.9
@Project: hotpot
@File   : test_bundle.py
@Author : Zhiyuan Zhang
@Date   : 2023/3/19
@Time   : 21:25
"""
from src.bundle import MolBundle


if __name__ == '__main__':
    dir_log = '/home/zz1/proj/gauss/new/log/Cs-VOHSAM-5'
    mb = MolBundle.read_from_dir('g16log', dir_log, generate=True)
    sum_mol = mb.sum_conformers()
