import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Generate Emails",
                    page_icon='📧 📭',
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header("Generate Emails 📧")
#Function to get the response back
# import os
# os.environ["OPENAI_API_KEY"]
def getLLMResponse(form_input,email_sender,email_recipient,email_style):
    llm = OpenAI(temperature=.3)

    #Template for building the PROMPT
    template = """
    Write a email with {style} style and includes topic :{email_topic}.\n\nSender: {sender}\nRecipient: {recipient}
    \n\nEmail Text:
    
    """
    #Creating the final PROMPT
    prompt = PromptTemplate(
    input_variables=["style","email_topic","sender","recipient"],
    template=template,)

  
    #Generating the response using LLM
    response=llm(prompt.format(email_topic=form_input,sender=email_sender,recipient=email_recipient,style=email_style))

    return response



form_input = st.text_area('Enter the email topic', height=275)

#Creating columns for the UI - To receive inputs from user
col1, col2, col3 = st.columns([10, 10, 5])
with col1:
    email_sender = st.text_input('Sender Name')
with col2:
    email_recipient = st.text_input('Recipient Name')
with col3:
    email_style = st.selectbox('Writing Style',
                                    ('Formal', 'Appreciating', 'Not Satisfied', 'Neutral'),
                                       index=0)


submit = st.button("Generate")

#When 'Generate' button is clicked, execute the below code
if submit:
    st.write(getLLMResponse(form_input,email_sender,email_recipient,email_style))
