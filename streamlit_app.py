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
    a=0
    st.write('woooooooooo')
    return
  else:
    a=1
    st.write('oooooooooow')
    return

st.button(label='hii',on_click = wow(a))
