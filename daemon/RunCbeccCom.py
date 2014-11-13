__author__ = 'Nicholas Long'

"""
This script will configure and run the CBECC-Com tool.

Arguments:
    -i : input file (either the XML or the CBID)
    --optionValues : options. A string of options that will override the defaults in the CbeccComWrapper.py file.
        For example to change the pszAnalysisOptionsCSV then run "--pszAnalysisOptionsCSV "a,2,b,3""

Example usage:
$ python RunCbeccCom.py -i run/0200016-OffSml-SG-BaseRun.xml -o "{

The simulation will run in the same directory as the model.
"""

import sys, getopt, json
from lib.CbeccComWrapper import CbeccComWrapper


def main(argv):
    inputfile = ''
    system = 'docker'
    options = {}

    try:
        opts, args = getopt.getopt(argv, "i:s:", ["input=", "system=" "pszAnalysisOptionsCSV="])

    except getopt.GetoptError:
        print 'RunCbeccCom.py -i <cbecc-file-name-and-path> -o <run-options-as-hash-string>'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print 'RunCbeccCom.py -i <cbecc-file-name-and-path> -o <run-options-as-hash-string>'
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-s", "--system"):
            system = arg
        else:
            print arg
            options[opt.replace("--","")] = arg

    if inputfile == '':
        print "No input file passed"
        print 'RunCbeccCom.py -i <cbecc-file-name-and-path> -o <run-options-as-hash-string>'
        sys.exit(2)

    ccw = CbeccComWrapper(system == 'docker', inputfile, options)
    result = ccw.run()
    ccw.finalize()

    print result


if __name__ == "__main__":
    main(sys.argv[1:])

