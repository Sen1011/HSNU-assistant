from embedding_en_new import *
from glob import glob
from scipy import spatial
import sys


def cos_sim(a,b):
  return 1 - spatial.distance.cosine(a, b)

def semantic_retrieval(question, input_txt_dir, input_vec_dir, candidate=10):
  file_list = glob(os.path.join(input_vec_dir, "*.txt"))
  list_vec = []
  q_embed = get_embed(question)
  for ll in file_list:
    head, tail = os.path.split(ll)
    txt_name = os.path.join(input_txt_dir, tail)#input_txt_dir + '/'+ ll.split('/')[-1]
    txt = open(txt_name, encoding='utf-8').read()
    vec = eval(open(ll).read())
    score = cos_sim(vec,q_embed)
    list_vec.append((txt,score))

  #TODO: 排序
  list_vec.sort(key=lambda x: x[1], reverse=True)

  result = []
  for lstv in list_vec[:candidate]:
    result.append(lstv[0])

  return result


if __name__ == '__main__':
  input_txt_dir = os.path.join(".", "week3&4", "doc_vec", "txts") #doc_vec/txts/
  input_vec_dir = os.path.join(".", "week3&4", "doc_vec", "vecs") #doc_vec/vecs/
  question = input("Please insert your question: ")
  search = semantic_retrieval(question, input_txt_dir, input_vec_dir)
  for answer in search:
    print(answer)
    print('------------------')
