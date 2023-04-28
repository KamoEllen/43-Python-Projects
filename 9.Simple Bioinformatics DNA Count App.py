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
sequence = sequence[1:] #skip first line , start at 1 
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


st.write(X)

st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80) # controls width of bar.
)
st.write(p)
           
           
           


