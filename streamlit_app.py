import os, sys
import shutil
from pathlib import Path
import streamlit as st

sys.path += ["/home/appuser/venv/lib/python3.9/lib-dynload"]

st.info(list(Path("/").rglob("*hmmer*")))
st.info(list(Path("/").rglob("*findmysequence*")))
st.info(os.environ["DL_LIBRARY_PATH"])

st.info(list(Path("/home/appuser/venv/")))

st.info(os.environ["PATH"])
st.info(shutil.which("phmmer"))
st.info(shutil.which("findmysequence"))

os.environ["PATH"] += os.pathsep + "/home/appuser/.conda/bin"
st.info(os.environ["PATH"])
st.info(shutil.which("phmmer"))
st.info(shutil.which("findmysequence"))
