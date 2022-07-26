import sys
import shutil
from pathlib import Path
import streamlit as st

st.info(sys.path)
st.info(sys.executable)
st.info(dir(sys))
st.info(shutil.which("python"))
st.info(shutil.which("conda"))
st.info(shutil.which("streamlit"))

for p in sys.path:
  p = Path(p)
  if p.is_dir():
    st.info(f"{p}: {list(Path(p).glob('*'))}")
  else:
    st.info(f"{p}")

#sys.path = [p for p in sys.path if p.find("3.7")==-1 and not p.startswith("/usr/local")]
#sys.path.append("/home/appuser/venv/lib/python3.9")
#st.info(sys.path)

target = Path("/home/appuser/venv/share/cctbx")
if not target.exists():
  target.symlink_to("/home/appuser/venv/lib/python3.9/site-packages/cctbx")

import cctbx
import iotbx
