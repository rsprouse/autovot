#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name = 'autovot',
  packages = ['autovot'],
  scripts = [
    'scripts/auto_vot_append_files.py',
    'scripts/auto_vot_extract_features.py',
    'scripts/auto_vot_train.py',
    'scripts/auto_vot_decode_after_fe.py',
    'scripts/auto_vot_performance.py',
    'scripts/auto_vot_decode.py',
    'scripts/auto_vot_train_after_fe.py',
  ],
  classifiers = [
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'Topic :: Multimedia :: Sound/Audio :: Speech'
  ]
)
