import os
import glob
import pandas as pd
import sys
import getopt

def main(argv):
   inputDir = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('combine.py -i <inputdir>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('combine.py -i <inputdir>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputDir = arg
   os.chdir(inputDir)     
   # read input 
   extension = 'csv'
   all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

   #combine all files in the list
   combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
   #export to csv
   combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

    
if __name__ == "__main__":
   main(sys.argv[1:])
