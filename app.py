import os
import streamlit as st
import google.generativeai as genai

os.environ['GOOGLE_API_KEY']="your api key"

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])    


model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")


# Initialize session state for chat history (if not already initialized)
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input field for user query
input_text = st.text_input("Input: ", key="input")

# Button to trigger response
submit = st.button("Ask the question")

if submit and input_text:
    # Get response from your `get_gemini_response` function (assuming it's defined)
    response = get_gemini_response(input_text)

    # Check if `response` contains valid data before accessing chunks
    if response:
        for chunk in response:
            st.session_state['chat_history'].append(("You", input_text))
            st.subheader("The Response is")
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))
    else:
        # Handle cases where no valid response is generated
        st.error("No response received from the model.")

# Display chat history
#st.subheader("The Chat History is")
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")



