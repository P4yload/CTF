# This tool is used to submit a malicious file to hybridanalysis.com for static analysis and shows the url and the virustotal report
# Dependencies: python >= 3.5
# Usage: python3 hybridanalysis.py FILENAMETOANALYZE

#!/usr/bin/python3
import os
import sys
import subprocess
import argparse
import json

parser = argparse.ArgumentParser(description='The malware sample to submit for static analysis.')    
parser.add_argument('file', type=argparse.FileType('r'), help='Enter the file')    
args = parser.parse_args()    

full_path = os.path.realpath(__file__)
path = os.path.dirname(full_path)

print("file path is " + path + "/" + sys.argv[1])
file = sys.argv[1]
print("file to submit for static analysis is: %s" % file)
print("Submitting file now for cyb3r analys1s..")  
command = ['./vxapi.py', 'submit_file', path + '/' + file, '-env', '100', '-pv', 'yes','-q']

#submitted file returns JSON value from Hybrid Analysis. Decide what the URL is
result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
jsonresult = json.loads(result.stdout)
s = str(jsonresult)
hashcode = s[25:89]
url = "https://www.hybrid-analysis.com/sample/" + hashcode
virustotalurl = "https://www.virustotal.com/en/file/" + hashcode + "/analysis"
print("File successfully submitted, URL is \n" + url )
print("VirusTotal URL is: \n" + virustotalurl)

#os.system("python3 vxapi.py" + " submit_file "  + file + " -env 100 -pv yes -q")
# TODO: Try catch, more beautifull code
