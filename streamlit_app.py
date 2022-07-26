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
    st.info(f"{p}: {[str(pp) for pp in Path(p).glob('*')]}")
  else:
    st.info(f"{p}")
    
for p in "/usr/local /usr/local/bin /usr/local/share /usr/local/share/cctbx /home/appuser/venv /home/appuser/venv/bin /home/appuser/venv/share /home/appuser/venv/share/cctbx /home/appuser/.conda /home/appuser/.conda/bin /home/appuser/.conda/share /home/appuser/.conda/share/cctbx".split():
  p = Path(p)
  if not p.exists():
    st.info(f"{p}: does not exist")
    continue
  if p.is_dir():
    st.info(f"{p}: {[str(pp) for pp in Path(p).glob('*')]}")
  else:
    st.info(f"{p}")
  

#sys.path = [p for p in sys.path if p.find("3.7")==-1 and not p.startswith("/usr/local")]
#sys.path.append("/home/appuser/venv/lib/python3.9")
#st.info(sys.path)

target = Path("/home/appuser/venv/share/cctbx")
if not target.exists():
  target.symlink_to("/home/appuser/.conda/share/cctbx")

import cctbx
import iotbx
