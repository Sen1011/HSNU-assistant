from google import genai
from semantic_retrieval import semantic_retrieval
import os
from time import asctime
from dotenv import load_dotenv
load_dotenv()

# Retrieve API key from environment variable
google_api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=google_api_key)

def get_response(user_question):
    # Get Relevant Documents
    input_txt_dir = os.path.join(".", "documents", "txts") #"./documents/txts/"
    input_vec_dir = os.path.join(".", "documents", "vecs") #"./documents/vecs/"
    docs = semantic_retrieval(user_question,input_txt_dir,input_vec_dir)

    # Define Prompt Template
    prompt_template = f"""
    It's {asctime()} now. You are a helpful assistant that answers questions based on the provided context.
    Answer the question as detailed as possible from the provided context, and please use 繁體中文，臺灣用語,
    make sure to provide all the details!
    if the answer is not in, provided context just say, "找不到答案",  don't provide the wrong answer\n\n
    Context:\n{str(docs)}\n
    Question: \n{user_question}\n
    Answer:
    """

    # Get Response
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt_template)
    
    return response.text

if __name__ == "__main__":
    user_question = input("請提問：")
    print("Bot:", get_response(user_question))