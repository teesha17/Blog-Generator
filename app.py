import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def getLLamaresponse(input_text,no_words,blog_style):
    ###llama 2 model
    llm =CTransformers(model="https://www.dropbox.com/scl/fi/nx9wnk0vt226b4ywayb5c/llama-2-7b-chat.ggmlv3.q8_0.bin?rlkey=wmvfn7dlbo8o9xq4gr01ei4on&st=nzlc18cx&dl=0",
                       model_type='llama',
                       config={'max_new_tokens':256,
                               'temperature':0.01})
    template="""write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words"""
    prompt = PromptTemplate(input_variables=["blog_style","input_text","n0_words"],template=template)
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs",
                   page_icon="",
                   layout="centered",
                   initial_sidebar_state="collapsed")
st.header("Generate Blogs ")
input_text = st.text_input("Enter the blog topic")

##creating two more columns for additional 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No. of words')
with col2:
    blog_style=st.selectbox('Writing the blog for: ',('Researchers','Data Scientists','Common people'),index=0)

submit = st.button("Generate")

##Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))