from google import genai
from semantic_retrieval import semantic_retrieval
import os
from dotenv import load_dotenv
load_dotenv()

# Retrieve API key from environment variable
google_api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=google_api_key)

# Get User Question
user_question = input("請提問：")

# Get Relevant Documents
input_txt_dir = os.path.join(".", "documents", "doc_vec", "txts") #"./documents/doc_vec/txts/"
input_vec_dir = os.path.join(".", "documents", "doc_vec", "vecs") #"./documents/doc_vec/vecs/"
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

print(f"Bot: {response}")