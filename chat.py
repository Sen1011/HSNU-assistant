import streamlit as st
from google import genai
from semantic_retrieval import semantic_retrieval
import os
import io
from dotenv import load_dotenv
load_dotenv()

st.title("進擊的巨人QA")  # Updated title


# Retrieve API key from environment variable
google_api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=google_api_key)

# Get User Question
user_question = st.text_input("請提問：")

if st.button("尋求解答"):
    if user_question:
        # Get Relevant Documents
        input_txt_dir = os.path.join(".", "week3&4", "doc_vec", "txts") #"./week3&4/doc_vec/txts/"
        input_vec_dir = os.path.join(".", "week3&4", "doc_vec", "vecs") #"./week3&4/doc_vec/vecs/"
        docs = semantic_retrieval(user_question,input_txt_dir,input_vec_dir)

        # Define Prompt Template
        prompt_template = """
        Answer the question as detailed as possible from the provided context, and please use 繁體中文，臺灣用語,
        make sure to provide all the details!
        if the answer is not in, provided context just say, "找不到答案",  don't provide the wrong answer\n\n
        Context:\n{ %s }\n
        Question: \n{ %s }\n
        Answer:
        """%(str(docs),user_question)

        # Get Response
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt_template)

        # Display Answer
        st.subheader("解答：")
        st.write(response.text)

    else:
        st.warning("請輸入提問")