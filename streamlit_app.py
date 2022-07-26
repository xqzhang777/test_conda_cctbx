import sys
import streamlit as st

st.info(sys.executable)
st.info(sys.path)

sys.path = [p for p in sys.path if p.find("3.7")==-1 and not p.startswith("/usr/local")]
st.info(sys.path)

import cctbx
import iotbx
