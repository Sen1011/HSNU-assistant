from embedding_en_new import *
from glob import glob
import os

input_dir = os.path.join("week3&4", "doc_vec", "txts")#"week3&4\\doc_vec\\txts\\"  #doc_vec/txts/
output_dir = os.path.join("week3&4", "doc_vec", "vecs") #doc_vec/vecs/
file_list = glob(os.path.join(input_dir, "*.txt"))
file_list.sort()

for ll in file_list:
  output_path = os.path.join(output_dir, ll.split('/')[-1])

  """if os.path.isfile(output_path):
    print(f'file {ll} exist, skip to next one')
    continue"""

  print('get embed for',ll)
  input_txt = open(ll, encoding="utf8").read()
  result = get_embed(input_txt)
  output_name = ll.split('/')[-1]
  output = open(output_path,'w')
  output.write(str(result)+'\n')
  output.close()
