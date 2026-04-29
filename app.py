from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyAkcm5Z5Vec4WxWCgdiqA8g8klHLddOqAE"

tweet_template = "Give me {number} tweets on{topic}"

tweet_prompt = PromptTemplate(template =tweet_template, input_variables=['number' , 'topic'])

gemini_model =ChatGoogleGenerativeAI(model="gemini-2.5-flash")

tweet_chain = tweet_prompt | gemini_model

# response = tweet_chain.invoke({"number" : 5, "topics" : "wars in middle east"})


st.header("Tweet Generator")

st.header("Generate tweets using generative ai")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value = 1, max_value=10, value=1, step=1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(tweets.content)


# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import PromptTemplate
# import streamlit as st
# import os

# # Set API Key
# os.environ["GOOGLE_API_KEY"] = "AIzaSyAkcm5Z5Vec4WxWCgdiqA8g8klHLddOqAE"

# # Prompt
# tweet_template = "Give me {number} tweets on {topic}"

# tweet_prompt = PromptTemplate(
#     template=tweet_template,
#     input_variables=['number', 'topic']
# )

# # Model
# gemini_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# # Chain (new syntax)
# tweet_chain = tweet_prompt | gemini_model

# # Streamlit UI
# st.header("Tweet Generator 🤖")

# topic = st.text_input("Enter Topic")
# number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1)

# if st.button("Generate"):
#     tweets = tweet_chain.invoke({"number": number, "topic": topic})
#     st.write(tweets.content)