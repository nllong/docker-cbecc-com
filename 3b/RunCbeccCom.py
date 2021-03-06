__author__ = 'Nicholas Long'

"""
This script will configure and run the CBECC-Com tool.

Arguments:
    -i : input file (either the XML or the CBID)
    -o : A string of options that will override the defaults in the CbeccComWrapper.py file.
         For example to run with program defaults and AnalysisStorage level 3 do '-o AnalysisStorage,3'
         'None' is a reserved word to remove all the default options and use the CBECC program defaults.
    -s : Type of system. This is only 'docker' or blank. Blank assumes Windows at the moment.

Example usage:
$ python RunCbeccCom.py -i run/0200016-OffSml-SG-BaseRun.xml -o AnalysisStorage,3

The simulation will run in the same directory as the model.
"""

import sys
import argparse

from lib.CbeccComWrapper import CbeccComWrapper


def main(argv):
    system = 'docker'

    parser = argparse.ArgumentParser(prog='RunCbeccCom.py')
    parser.add_argument('-i', '--input',  type=str, help='input file name', required=True)
    parser.add_argument('-s', '--system',  type=str, help='set to docker if running on docker')
    parser.add_argument('-o', '--options',  type=str, help='pszAnalysisOptions as a string')

    args = parser.parse_args()
    print "[RunCbeccCom.py] Arguments are {}".format(args)

    if args.options and args.options.lower() == 'none':
        args.options = "none"

    if args.system:
        system = args.system

    ccw = CbeccComWrapper(system == 'docker', args.input, args.options)
    result = ccw.run()
    ccw.finalize()

    print result

if __name__ == "__main__":
    main(sys.argv[1:])
