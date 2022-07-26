import sys
import shutil
from pathlib import Path
import streamlit as st

# essential to avoid cctbx import errors
target = Path("/home/appuser/venv/share/cctbx")
if not target.exists():
  target.symlink_to("/home/appuser/.conda/share/cctbx")

import cctbx
import iotbx
from cctbx.xray.ext import *

st.info(dir(iotbx))
st.info(dir(cctbx))
st.info(f"cctbx version: {cctbx.get_version()}")
