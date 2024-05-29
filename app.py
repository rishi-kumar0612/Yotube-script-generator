import os 
from apikey import API_KEY
import streamlit as st
from langchain_openai.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
from langchain.memory.buffer import ConversationBufferMemory
from langchain.utilities.wikipedia import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = API_KEY

#title
st.title('🦜🔗Youtube GPT Creator')
prompt = st.text_input('Enter your prompt here')

title_template = PromptTemplate(
     input_variables= ['title'],
     template = 'write me a youtube video title about {topic}' 

    
)

script_template = PromptTemplate(
     input_variables= ['title','wikipedia_research'],
     template = 'write me a youtube video script based on this title: {title} but also while leveragin this wikipedia reasearch : {wikipedia_research}' 
)

#memory

title_memory = ConversationBufferMemory( input_key='topic',memory_key= 'chat_history')
script_memory = ConversationBufferMemory( input_key='title',memory_key= 'chat_history')
# Llms 

llm = OpenAI(temperature = 0.9)
title_Chain = LLMChain(llm = llm, prompt = title_template, verbose = True, output_key= 'title', memory= title_memory)
script_Chain = LLMChain(llm = llm, prompt = script_template, verbose = True, output_key= 'script', memory= script_memory)
#sequential_chain = SequentialChain(chains=[title_Chain,script_Chain],input_variables=['topic'],output_variables = ['title', 'script'],verbose = True)

wiki = WikipediaAPIWrapper()
# show stuff to the screen 
if prompt :
     title = title_Chain.run(prompt)
     wiki_research = wiki.run(prompt)
     script = script_Chain.run(title=title, wikipedia_research=wiki_research)#,  title = title

     st.write(title)
     st.write(script)

     with st.expander('title History'):
          st.info(title_memory.buffer)

     with st.expander('script History'):
          st.info(script_memory.buffer)

     with st.expander('Wikipedia History'):
          st.info(wiki_research)