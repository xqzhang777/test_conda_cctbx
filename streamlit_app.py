import sys
import shutil 
import streamlit as st

st.info(sys.path)
st.info(sys.executable)
st.info(shutil.which("python"))
st.info(shutil.which("conda"))
st.info(shutil.which("streamlit"))

sys.path = [p for p in sys.path if p.find("3.7")==-1 and not p.startswith("/usr/local")]
sys.path.append("/home/appuser/venv/lib/python3.9")
st.info(sys.path)

from pathlib import Path
target = Path("/home/appuser/venv/share/cctbx")
if not target.exists():
  Path("/home/appuser/venv/lib/python3.9/site-packages/cctbx").symlink_to(target)
import cctbx
import iotbx
