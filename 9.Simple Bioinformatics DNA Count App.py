import pandas as pd 
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open("dna-logo.jpg")

st.image(image, use_column_width=True)

st.write("""
#DNA NUCLEOTIDE COUNT WEB APP

This app counts the nucleotide composition of query DNA!

***
""")

st.header('Enter DNA sequence')

sequence_input = ">GAACACGTGGAGGCAGGTAAGAAGAACTTATTCCTACGGAGA\nACACGTGGAGGCAGGTAAGAAGAACTTATTCCTACG\nGGTAAGAAGAACTTATTCCTACGGAGAGA"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequnce[1:] #skip first line , start at 1 
sequence = ''.join(sequence) #concatenates list to string

st.write("""
***
""")

st.header('INPUT (DNA Query)') #prints the input DNA sequence
sequence

st.header('OUTPUT (DNA Nucleotide Count)') #DNA nucleotide count

st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
   d = dict([
           ('A',seq.count('A')),
           ('T',seq.count('T')),
           ('G',seq.count('G')),
           ('C',seq.count('C')),
           ])
   return d
   
X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

 
           
           
           
           


