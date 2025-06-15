output_dir = "doc_vec/"
doc: str = open(file="./titan_all.txt").read()

def fixed_size_chunking_with_overlap(text: str, chunk_size: int, overlap: int) -> list[str]:
    chunks:list[str] = []
    words: str = text
    start = 0
  
    while start < len(words):
        end: int = start + chunk_size
        chunk: str = words[start:end]
    
        chunks.append(chunk)

        start += chunk_size - overlap
  
    return chunks

chunks: list[str] = fixed_size_chunking_with_overlap(text=doc, chunk_size=200, overlap=20)

for i,ch in enumerate(chunks):
    file_name: str = 'chunk_%d.txt'%i
    with open(file=output_dir+file_name, mode='w') as opt:
       _ = opt.write(ch)
