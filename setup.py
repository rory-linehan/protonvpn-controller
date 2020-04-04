# Copyright 2020 Rory Linehan
# this code is distributed under the terms of the GNU General Public License

from distutils.core import setup

setup(
    name='protonvpn-controller',
    packages=['pypvpnctl.py',],
    license='GNU GPL',
    long_description=open('README.md').read(),
)
