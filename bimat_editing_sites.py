import pandas as pd
import glob
import numpy as np
from itertools import chain
import sys
import os

output_matrix = sys.argv[1]
directory = os.getcwd()
binary_mat = pd.DataFrame([])
for filename in sorted(os.listdir(directory)):
  print('Processing ' + filename + ' gene')
  es_pos_files = glob.glob(filename + "/*.csv")

#read csv file, select editing sites positions, store
  pos_dict = {}
  for file in sorted(es_pos_files):
      pos_temp = pd.read_csv(file, usecols=[1, 2, 3], header=None)
      pos_dict[file] = pos_temp[2].tolist()

#concatenate all editing sites positions from dict, take unique values and sort
  uniq_pos = sorted(set(chain.from_iterable(pos_dict.values())))

#compare editing positions of each species with unique editing positions and set binary values
  pos_comp = []
  for key, value in pos_dict.items():
      pos_comp_temp = [1 if x in value else 0 for x in uniq_pos]
      pos_comp.append(pos_comp_temp)

  pos_comp.append(uniq_pos)

#convert list to dataframe
  pos_comp_df = pd.DataFrame(pos_comp)
  pos_comp_df = pos_comp_df.astype(int)

#move bottom line (editing site positions) to the top
  pos_comp_df_roll = pos_comp_df.apply(np.roll, shift=1)

#drop first column containing '0' positions
  pos_comp_df_roll_drop = pos_comp_df_roll.drop(pos_comp_df_roll.columns[0], axis=1)
  binary_mat = pd.concat([binary_mat, pos_comp_df_roll_drop], axis = 1)

#save results to csv file
binary_mat.to_csv(output_matrix, sep='\t', index=False, header=False)
