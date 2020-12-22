# -*- coding: utf-8 -*-

from __future__ import print_function, division
import os
import pandas as pd
import getopt
import sys

from shutil import copyfile


def main(argv):
    inputfile = 'new_metadata.csv'
    outputdir = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('comeWithMe.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('comeWithMe.py -i <inputfile> -o <outputdir>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputdir = arg
    # read input
    data = pd.read_csv(inputfile)

    # TODO update output dir.

    targetDirText = outputdir + 'text/'
    targetDirAudio = outputdir + 'audio/'

    os.makedirs(targetDirAudio, mode=0o777)
    os.makedirs(targetDirText, mode=0o777)

    print("attempting to copy appropriate files")
    i = 0
    for i in range(len(data.index)):
        raw_speaker_id = data.at[i, 'speakerid']

        # ASSUMPTION WARNING: data files will always have this naming convention so I can take the last 4 letters.
        # DEBUGGING print statement
        # print(rawSpeakerId[-4:])
        # last 4 chars of the cell
        speaker_id = raw_speaker_id[-4:]

        #TODO: these could be added as positional arguments, but you get the main idea.
        inputDirAudio = 'Dataset/audio/'
        fileEndingAudio = '.wav'

        inputDirText = 'Dataset/text/'
        fileEndingText = '.xml'

        # cp audio file
        copyfile(inputDirAudio + speaker_id + fileEndingAudio, targetDirAudio + speaker_id + fileEndingAudio)

        # cp text file
        copyfile(inputDirText + speaker_id + fileEndingText, targetDirText + speaker_id + fileEndingText)

    print("copied audio & text data files for " + str(len(data.index)) + " speakers to " + targetDirAudio +" and " + targetDirText)


if __name__ == "__main__":
    main(sys.argv[1:])
