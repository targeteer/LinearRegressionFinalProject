import os
import argparse
import json
import glob
import pandas as pd

parser = argparse.ArgumentParser(description='METASOFT post-processing.')
parser.add_argument('categ_dir', help="Directory with category data.")
parser.add_argument('-o', '--output_dir', default='.', help='Output directory')
args = parser.parse_args()

def main():
    
    categ_files = glob.glob(os.path.join(args.categ_dir, '*category_id.json'))

    categ_df = pd.DataFrame(columns=['Label', 'ID', 'Title'])
    for cf in categ_files:
        with open(cf) as fp:
            cj = json.load(fp)

        categ_label = os.path.split(cf)[1].split('_')[0]
        for cc in cj['items']:
            categ_df = categ_df.append(pd.Series([categ_label, cc['id'], cc['snippet']['title']], index=['Label', 'ID', 'Title']), ignore_index=True) 

    outfile = os.path.join(args.output_dir, 'trending_categories_map.txt')
    categ_df.to_csv(outfile, sep='\t')

    print('wrote category  map to: {}'.format(outfile))
            
if __name__ == '__main__':
    main()
