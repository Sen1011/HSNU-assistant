from embedding import *
from glob import glob
import os

input_dir = os.path.join("documents", "txts") # documents/txts/
output_dir = os.path.join("documents", "vecs") # documents/vecs/
file_list = glob(os.path.join(input_dir, "*.txt"))
file_list.sort()

for ll in file_list:
  head, tail = os.path.split(ll)
  output_path = os.path.join(output_dir, tail)

  if os.path.isfile(output_path):
    print(f'file {ll} exist, skip to next one')
    continue

  print('get embed for',ll)
  input_txt = open(ll, encoding="utf8").read()
  result = get_embed(input_txt)
  output_name = ll.split('/')[-1]
  output = open(output_path,'w')
  output.write(str(result)+'\n')
  output.close()
