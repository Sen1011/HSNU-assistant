# 師大附中小助手
[展示網頁](https://hsnu-assistant.streamlit.app/)<br/>
基於 Gemini 2.0 flash 與 RAG 技術，提供附中學生易用的校園小幫手

## 專案架構
```mermaid
graph TD
    subgraph Frontend
        UI[Streamlit UI]
        UI --> |User Input| Handler[Chat Handler]
    end

    subgraph Core_Processing
        Handler --> |Question| SR[Semantic Retrieval]
        SR --> |Relevant Docs| Generator[Response Generator]
        
        subgraph Document_Processing
            Chunking[Text Chunker]
            Embedding[Embeddings Generator] 
            Storage[Document Storage]
            Chunking --> Embedding
            Embedding --> Storage
        end
        
        SR --> Storage
    end

    subgraph External_Services
        GeminiAPI[Google Gemini API]
        Generator --> GeminiAPI
        Embedding --> GeminiAPI
    end
```

## 本機部署
必要環境：Python 3.9+
1. clone repo
  ```bash
  git clone https://github.com/Sen1011/HSNU-assistant.git
  ```
2. 安裝套件
  ```bash
  pip install requirements.txt
  ```
3. 進入專案目錄執行
  ```bash
  streamlit run app.py
  ```
