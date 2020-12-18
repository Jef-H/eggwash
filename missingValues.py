import pandas as pd
import sys
import getopt

def main(argv):
   inputfile = ''
   # TODO: add outputfile functionality :) 
   outputfile =''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('missingValues.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('missingValues.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   # read input 
   data = pd.read_csv(inputfile)
    
   #print total nulls
   print (data.isnull().sum(axis=0))
   #print total NOT null
   print (data.notnull().sum(axis=0))
   #print the percentage of null (this is where we could add something to delete crap fields.)
   print ("percentage of null data: ")
   print (data.isnull().sum(axis=0)/data.notnull().sum(axis=0))
    
if __name__ == "__main__":
   main(sys.argv[1:])
