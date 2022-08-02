import sys
import shutil
from pathlib import Path
import streamlit as st

# essential to avoid cctbx import errors
target = Path("/home/appuser/venv/share/cctbx")
if not target.exists():
  target.symlink_to("/home/appuser/.conda/share/cctbx")

sys.path += ["/home/appuser/venv/lib/python3.9/lib-dynload"]  
  
import cctbx
import iotbx

# xyz_utils.py
# cctbx imports

from cctbx import xray
from cctbx import maptbx
from cctbx import miller

from cctbx.array_family import flex
# All reported: ImportError: __import__("boost_python_meta_ext"): No module named 'boost_python_meta_ext'
# ====> tested until here
from cctbx import crystal
from cctbx import sgtbx, uctbx

import iotbx
import iotbx.map_tools
from iotbx import crystal_symmetry_from_any
from iotbx import reflection_file_reader
from iotbx import reflection_file_utils
from iotbx.pdb import amino_acid_codes as aac
import iotbx.pdb
import iotbx.ccp4_map

from mmtbx.maps import utils

# mmtbx
from mmtbx.monomer_library import idealized_aa
from mmtbx.monomer_library import server
from mmtbx.geometry_restraints import reference
from cctbx import geometry_restraints
import cctbx.geometry_restraints.manager
from cctbx.maptbx import real_space_refinement_simple

from libtbx.math_utils import ifloor, iceil

# scitbx
import scitbx
from scitbx import matrix
from scitbx import fftpack
from scitbx.math import superpose

# sequence_utils.py
# cctbx imports
from iotbx.pdb import amino_acid_codes as aac

from scipy.special import erf,erfc
from scipy import stats

import numpy as np

from iotbx.bioinformatics import any_sequence_format

# descriptors.py
from cctbx import array_family

# scitbx
import scitbx
from scitbx import matrix
from scitbx.math import superpose


st.info(dir(iotbx))
st.info(dir(cctbx))
st.info(f"cctbx version: {cctbx.get_version()}")
