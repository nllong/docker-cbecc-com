__author__ = 'Nicholas Long'

from ctypes import cdll
import os

# Change your directory to where all the DLLs live
os.chdir('C:\\Program Files (x86)\\CBECC-Com 2013\\')
lib = cdll.LoadLibrary('C:\\Program Files (x86)\\CBECC-Com 2013\\BEMCmpMgr_os.dll')
#
# class CbeccComWrapper(object):
#     def __init__(self):
#         #self.obj = lib.InitBEMProcAndCmpMgrDLLs(self.obj)
#
#     def initBEMProcAndCmpMgrDLLs(self):
#         lib.InitBEMProcAndCmpMgrDLLs(self.obj)
#
#     def bar(self):
#         lib.Foo_bar(self.obj)


rules = "C:\\Users\\nlong\\Documents\\CBECC-Com 2013 Data\\Rulesets\\CEC 2013 Nonres\\CEC 2013 NonRes BEMBase.bin"
bemType = 0
log = None

try:
  lib.InitBEMProcAndCmpMgrDLLs(rules, bemType, log)
except:
  # This error doesn't actually get
  print "ERROR"

#
# http://bees.archenergy.com/Documents/Software/CEC_Compliance_Manager_(com)_software_documentation_v9b.pdf
# const char* pszBEMBasePathFile,
# const char* pszRulesetPathFile,
# const char* pszSimWeatherPath,
# const char* pszCompMgrDLLPath,
# const char* pszDHWWeatherPath,
# const char* pszProcessingPath,
# const char* pszModelPathFile,
# const char* pszLogPathFile,
# const char* pszUIVersionString,
# bool bLoadModelFile,
# const char* pszAnalysisOptionsCSV,
    # StoreBEMDetails: 0
    # Verbose: 0
    # Silent: 0
    # ParallelSimulations: 1
    # LogWritingMode: 2
    # AnalysisThruStep: 100
    # DontAbortOnErrorsThruStep: 0
    # BypassInputChecks: 0
    # BypassUMLHChecks: 0
    # BypassCheckSimRules: 0
    # BypassCheckCodeRules: 0
    # BypassOpenStudio_p: 0
    # BypassOpenStudio_bz: 0
    # BypassOpenStudio_b: 0
    # BypassSimulation_p: 0
    # BypassSimulation_bz: 0
    # BypassSimulation_b: 0
    # OverrideAutosize_p: -1
    # OverrideAutosize_bz: -1
    # OverrideAutosize_b: -1
    # IgnoreFileReadErrors: 0
    # PurgeUnreferencedObjects: 1
    # ComplianceReportPDF: 0
    # ComplianceReportXML: 0
    # SimulationStorage: 1
    # AnalysisStorage: 2
    # ExportHourlyResults: "111" # series of integers
    # ProxyServerAddress: None
    # ProxyServerCredentials: None
    # ModelRpt_ALL: 0
# char* pszErrorMessage,
# int iErrorMsgLength,
# bool bDisplayProgress,
# HWND hWnd,
# char* pszResultsSummary,
# int iResultsSummaryLenv

pszBEMBasePathFile = None
pszRulesetPathFile = "C:\\Users\\nlong\\Documents\\CBECC-Com 2013 Data\\Rulesets\\CEC 2013 NonRes.bin"
pszSimWeatherPath = "C:\\Users\\nlong\\Documents\\CBECC-Com 2013 Data\\EPW\\"
pszCompMgrDLLPath = "C:\\Program Files (x86)\\CBECC-Com 2013\\"  #blank is current directory -- but should be the path where EPlus and T24DHW directories live
pszDHWWeatherPath = None
pszProcessingPath = "test\\s0200006-OffSml-SG-BaseRun\\" # has to exist before running
pszModelPathFile = "test\\0200006-OffSml-SG-BaseRun.cibd" # can be relative
pszLogPathFile = None
pszUIVersionString = "pyCBECC"
bLoadModelFile = True
pszAnalysisOptionsCSV = "Verbose,1,Silent,1,ComplianceReportPDF,1,ComplianceReportXML,1"
pszErrorMessage = None #"" # list of errors that are returned
iErrorMsgLength = None # have to specify the length of the above pszError Message
bDisplayProgress = False
hWnd = None
pszResultsSummary = None
iResultsSummaryLen = None

# Make sure the analysis directory exists
if not os.path.exists(pszProcessingPath):
  os.makedirs(pszProcessingPath)

result = lib.CMX_PerformAnalysis_CECNonRes(pszBEMBasePathFile, pszRulesetPathFile, pszSimWeatherPath, pszCompMgrDLLPath,
  pszDHWWeatherPath, pszProcessingPath, pszModelPathFile, pszLogPathFile, pszUIVersionString, bLoadModelFile,
  pszAnalysisOptionsCSV, pszErrorMessage, iErrorMsgLength, bDisplayProgress, hWnd, pszResultsSummary, iResultsSummaryLen)

print "The result of the CBECC Run was %(result)s" % locals()
print pszErrorMessage

# Look up the Error message
# Error return value mapping:
# 1 : pszBEMBasePathFile doesn't exist
# 2 : pszRulesetPathFile doesn't exist
# 3 : pszSimWeatherPath doesn't exist
# 4 : pszCompMgrDLLPath specified, but doesn't exist
# 5 : Invalid project log file name (too long)
# 6 : Error writing to project log file
# 7 : Building model input/project file not found
# 8 : Error reading/initializing model input/project file
# 9 : Errors encountered evaluating input model defaulting rules
# 10 : Errors encountered evaluating input model defaulting rules (multiple times)
# 11 : Error(s) encountered performing required data & numeric range checks
# 12 : Error(s) encountered checking input model for simulation compatibility
# 13 : Error(s) encountered checking input model for code requirements
# 14 : Error encountered initializing weather file locations and/or names
# 15 : Error creating or accessing the analysis processing directory
# 16 : Error generating Proposed Sizing model
# 17 : Error generating Proposed (final) model
# 18 : Error generating Standard Sizing model
# 19 : Error generating Standard (final) model
# 20 : Error initializing Standard Sizing model
# 21 : Error initializing Standard (final) model
# 22 : Analysis aborted - user chose not to overwrite SDD XML file
# 23 : Error: Unable to write SDD XML file
# 24 : Error(s) encountered simulating Proposed model
# 25 : Error(s) encountered simulating Standard Sizing model
# 26 : Error(s) encountered simulating Standard (final) model
# 27 : Error(s) encountered retrieving Proposed model simulation results
# 28 : Error(s) encountered retrieving Standard Sizing model simulation results
# 29 : Error(s) encountered retrieving Standard (final) model simulation results
# 30 : Proposed model zone(s) exceed unmet load hours limits
# 31 : Error initializing building model database
# 32 : Error loading analysis ruleset
# 33 : User aborted analysis via progress dialog 'Cancel' button
# 34 : Invalid results object types
# 35 : Error copying results objects from a previous model
# 36 : Error copying equipment sizes/flows from source model
# 37 : Error(s) encountered reading building model (input/project) file
# 38 : Error: EnergyPlus simulation engine not found.
# 39 : Error: Version of EnergyPlus installed not compatible with analysis.
# 40 : Error setting up check of weather & design day file hashes
# 41 : DHW simulation not successful
# 42 : Error encountered in creating building geometry
# 43 : Error encountered initializing building geometry DBIDs
# 44 : Error initializing Proposed model
# 45 : Error(s) encountered simulating Proposed Sizing model
# 46 : Error(s) encountered retrieving Proposed Sizing model simulation results
# (return values in the range 101-200 describe issues encountered during/by simulation)
# 101 : SDD XML simulation input file not found
# 102 : Simulation weather file not found
# 103 : Simulation processing path not valid
# 104 : Simulation executable path not valid
# 105 : Simulation error output path/file not valid
# 106 : User aborted analysis
# 131 : Error encountered in OpenStudio loading SDD XML file
# 132 : Error encountered in OpenStudio saving model to OSM file
# 133 : Unable to locate EnergyPlus simulation SQL output file
# 134 : OpenStudio Model not valid following simulation
# 135 : OpenStudio Facility not valid following simulation
# 136 : Error creating OpenStudio Model object
# 161 : Fatal error(s) ocurred in EnergyPlus simulation
# 162 : EnergyPlus simulation did not complete successfully
# 163 : Fatal error(s) ocurred in EnergyPlus simulation (second of run pair)
# 164 : EnergyPlus simulation did not complete successfully (second of run pair)
# 181 : User aborted analysis during building model simulation
