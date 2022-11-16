import boto3
import logging
from botocore.exceptions import ClientError
import os
import time
import getopt
import sys
import argparse
import json

parser = argparse.ArgumentParser(description="Parse inputfile and polly-synthesize each sentence.",epilog="Specifying both -l and -R will result in error")
parser.add_argument("yourbucket",help="existing s3 bucket to store output of polly tasks")
parser.add_argument("inputfile",help="local path to dialogue input text file")
parser.add_argument("-l","--line_nbr",help="Start MP3 file name prefix at LINE_NBR",type=int,default=1)
parser.add_argument("-R","--ROW",help="Only synthesize line R of inputfile",type=int)

args = parser.parse_args()

inputfile = args.inputfile
yourbucket = args.yourbucket
line_nbr = args.line_nbr
row_nbr = args.ROW

if (line_nbr > 1):
    if(row_nbr):
        print("**ERROR** Invalid parameter combination")
        parser.print_help()
        sys.exit(1)


with open(inputfile,mode='r') as f:
    lines = f.readlines()
    if (row_nbr):
        if len(lines) < row_nbr:
            print("**ERROR** Number of lines in inputfile is less than specified with -R")
            parser.print_help()
            sys.exit(10)

