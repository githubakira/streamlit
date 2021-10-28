import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

data=0
if st.checkbox('Show raw data'):
  st.write(data)

a=0

def wow(a):
  if a == 1:
    return a=0
  else:
    return a=1

st.button(label: hiiiii,on_click: def wow(a))
