import numpy as np
import os
import pandas as pd
import sys

# @TODO: refactor with argparse --category
categories = ['architecture', 'art', 'celebrations', 'fashion', 'food', 'people']
idx = int(sys.argv[1])
cat = categories[idx]
cure_dataset = pd.read_csv(f'cure_dataset_csv/{cat}.csv')
continents = np.unique(cure_dataset.Continent)
subcats = np.unique(cure_dataset.Category) 

def get_odir_escaped(odir, query):
    odir_new = odir.replace("\\", "")
    return odir_new

for item in subcats:
    data_category = cure_dataset[cure_dataset.Category == item]
    for c in continents:
        data_c = data_category[data_category.Continent == c]
        root_dir = f"../gt_images/{cat}/{item}/"
        for q in data_c.Wikimedia_Category:
            for entry in q.split(";"): # iterate over multiple wikimedia pages, since a single has low GT count
                q_no_spaces = entry.replace(" ", "_")
                odir = f"{root_dir}{q_no_spaces}"
                odir_escaped = get_odir_escaped(odir, q_no_spaces)
                
                if not os.path.exists(odir_escaped):
                    os.makedirs(odir_escaped)
                _, _, files = next(os.walk(odir_escaped))
        
                # if there are no gt images in the folder download them, otherwise skip
                if not len(files) > 1:
                    print(f'\nTrying: {q_no_spaces}')
                    print(odir)
                    print(odir_escaped)
                    os.system(f'bash commons-downloader -c -o {odir} {q_no_spaces} ')
                else:
                    pass
                    _, _, files = next(os.walk(odir_escaped))
    print()