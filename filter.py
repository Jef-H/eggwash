# -*- coding: utf-8 -*-

from __future__ import print_function, division
import pandas as pd
import getopt
import sys


def main(argc, argv):

    # CONSTRAINT target_val MUST BE INT
    inputfile = ''
    outputfile = ''
    column_to_filter = ''
    equality_val = ''
    target_val = 0
    multiple_criteria = False;
    
    column_to_filter_2 = ''
    equality_val_2 = ''
    target_val_2 = 0

    # TODO: figure out how to variably adjust criteria size.

    try:
        opts, args = getopt.getopt(argv,"i:o:c:e:v:x:y:z:", ["ifile=", "ofile=", "column=", "equality=", "value=", "column2=", "equality2=", "value2="])
        print (opts)

    except getopt.GetoptError:
        print('filter.py has a lot of args. they are.. -i <inputfile> -o <outputfile> -c <column>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('missingValues.py -i <inputfile> -o <outputfile> -c <column> -e <equality> -v <valueasInt>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-c","--column"):
            column_to_filter = arg
        elif opt in ("-e","--equality"):
            equality_val = arg
        elif opt in ("-v","--value"):
            target_val = arg
        elif opt in ("-x","--column2"):
            multiple_criteria = True
            column_to_filter_2 = arg
        elif opt in ("-y","--equality2"):
            equality_val_2 = arg
        elif opt in ("-z","--value2"):
            target_val_2 = arg

    # read input
    incoming_df = pd.read_csv(inputfile)
    outgoing_df = pd.DataFrame()

# time to handle equality_val
# TODO: see if I can chain logic with filtering the incoming dataframe
    if equality_val == 'equal':
        outgoing_df = incoming_df.loc[incoming_df[column_to_filter] == int(target_val)].drop_duplicates().reset_index(drop=True)
    elif equality_val == 'greater':
        outgoing_df = incoming_df.loc[incoming_df[column_to_filter] > int(target_val)].drop_duplicates().reset_index(drop=True)
    elif equality_val == 'less':
        outgoing_df = incoming_df.loc[incoming_df[column_to_filter] < int(target_val)].drop_duplicates().reset_index(drop=True)
    else:
        print("equality_val error")
    final_outgoing_df = outgoing_df

    #This isn't a great solution, but it does work for this exercise.

    #this works for OR, NOT AND.
    if multiple_criteria == True:
        print("multiple_criteria =True")
        #if there are multiple criteria we need to make two dataframes, concat them, & remove duplicates.
        outgoing_df2 = pd.DataFrame()

        if equality_val_2 == 'equal':
            outgoing_df2 = outgoing_df.loc[outgoing_df[column_to_filter_2] == int(target_val_2)].drop_duplicates().reset_index(drop=True)
        elif equality_val_2 == 'greater':
            outgoing_df2 = outgoing_df.loc[outgoing_df[column_to_filter_2] >= int(target_val_2)].drop_duplicates().reset_index(drop=True)
        elif equality_val_2 == 'less':
            outgoing_df2 = outgoing_df.loc[outgoing_df[column_to_filter_2] <= int(target_val_2)].drop_duplicates().reset_index(drop=True)
        else:
            print("equality_val error")
        final_outgoing_df = outgoing_df2
        #this line is doing alot. concatenate dfs and remove duplicates.
    #TODO if you wanted to ad OR functionality use outgoing_df and outgoing_df2
    #outgoing_df = pd.concat([outgoing_df, outgoing_df2]).drop_duplicates().reset_index(drop=True)


    #output our file
    final_outgoing_df.to_csv(outputfile, index=False)
    print("successfully wrote new data for " + str(len(final_outgoing_df.index)) + " speakers to " + str(outputfile))


if __name__ == "__main__":
    main(len(sys.argv), sys.argv[1:])
