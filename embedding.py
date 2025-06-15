from google import genai
from google.genai import types
import os, time
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

def get_embed(text):
    text = text.replace("\n", " ")
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"請把以下句子精準翻譯成英文: {text}"
        )
    except:
        time.sleep(60)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"請把以下句子精準翻譯成英文: {text}"
        )

    result = client.models.embed_content(
        model="text-embedding-004",
        contents=response.text,
        config=types.EmbedContentConfig(output_dimensionality=10,
                                        task_type="SEMANTIC_SIMILARITY")
    )

    return result.embeddings[0].values

if __name__ == "__main__":
    text = """進擊的巨人

《進擊的巨人》（日語：進撃の巨人）是日本漫畫家諫山創創作的漫畫作品。漫畫於2009年9月至2021年4月間在講談社《別冊少年Magazine》上連載，單行本全34卷。故事建立在人類與巨人之間的衝突，人類居住在由高牆包圍的城市，對抗牆外會吃人的巨人，並尋找著關於巨人的答案。
漫畫系列截至2021年6月發行至第34卷，在日本國內累計發行量突破8,600萬冊，在海外則突破1,200萬冊的銷"""
    embedding = get_embed(text)
    print(embedding)