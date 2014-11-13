__author__ = 'Nicholas Long'

#

"""
Reference manual is here:
    http://bees.archenergy.com/Documents/Software/CEC_Compliance_Manager_(com)_software_documentation_v9b.pdf

const char* pszAnalysisOptionsCSV: Default Value
    StoreBEMDetails: 0
    Verbose: 0
    Silent: 0
    ParallelSimulations: 1
    LogWritingMode: 2
    AnalysisThruStep: 100
    DontAbortOnErrorsThruStep: 0
    BypassInputChecks: 0
    BypassUMLHChecks: 0
    BypassCheckSimRules: 0
    BypassCheckCodeRules: 0
    BypassOpenStudio_p: 0
    BypassOpenStudio_bz: 0
    BypassOpenStudio_b: 0
    BypassSimulation_p: 0
    BypassSimulation_bz: 0
    BypassSimulation_b: 0
    OverrideAutosize_p: -1
    OverrideAutosize_bz: -1
    OverrideAutosize_b: -1
    IgnoreFileReadErrors: 0
    PurgeUnreferencedObjects: 1
    ComplianceReportPDF: 0
    ComplianceReportXML: 0
    SimulationStorage: 1
    AnalysisStorage: 2
    ExportHourlyResults: "111" # series of integers
    ProxyServerAddress: None
    ProxyServerCredentials: None
    ModelRpt_ALL: 0
 """

from ctypes import cdll
from os.path import expanduser
import os


class CbeccComWrapper():
    """
    CbeccComWrapper wraps the BEMCmpMgr_os.dll for CEC/AEC CBECC-Com tool
    """

    ERROR_CODES = {
        0: "Completed Successfully",
        1: "pszBEMBasePathFile doesn't exist",
        2: "pszRulesetPathFile doesn't exist",
        3: "pszSimWeatherPath doesn't exist",
        4: "pszCompMgrDLLPath specified, but doesn't exist",
        5: "Invalid project log file name (too long)",
        6: "Error writing to project log file",
        7: "Building model input/project file not found",
        8: "Error reading/initializing model input/project file",
        9: "Errors encountered evaluating input model defaulting rules",
        10: "Errors encountered evaluating input model defaulting rules (multiple times)",
        11: "Error(s) encountered performing required data & numeric range checks",
        12: "Error(s) encountered checking input model for simulation compatibility",
        13: "Error(s) encountered checking input model for code requirements",
        14: "Error encountered initializing weather file locations and/or names",
        15: "Error creating or accessing the analysis processing directory",
        16: "Error generating Proposed Sizing model",
        17: "Error generating Proposed (final) model",
        18: "Error generating Standard Sizing model",
        19: "Error generating Standard (final) model",
        20: "Error initializing Standard Sizing model",
        21: "Error initializing Standard (final) model",
        22: "Analysis aborted - user chose not to overwrite SDD XML file",
        23: "Error: Unable to write SDD XML file",
        24: "Error(s) encountered simulating Proposed model",
        25: "Error(s) encountered simulating Standard Sizing model",
        26: "Error(s) encountered simulating Standard (final) model",
        27: "Error(s) encountered retrieving Proposed model simulation results",
        28: "Error(s) encountered retrieving Standard Sizing model simulation results",
        29: "Error(s) encountered retrieving Standard (final) model simulation results",
        30: "Proposed model zone(s) exceed unmet load hours limits",
        31: "Error initializing building model database",
        32: "Error loading analysis ruleset",
        33: "User aborted analysis via progress dialog 'Cancel' button",
        34: "Invalid results object types",
        35: "Error copying results objects from a previous model",
        36: "Error copying equipment sizes/flows from source model",
        37: "Error(s) encountered reading building model (input/project) file",
        38: "Error: EnergyPlus simulation engine not found.",
        39: "Error: Version of EnergyPlus installed not compatible with analysis.",
        40: "Error setting up check of weather & design day file hashes",
        41: "DHW simulation not successful",
        42: "Error encountered in creating building geometry",
        43: "Error encountered initializing building geometry DBIDs",
        44: "Error initializing Proposed model",
        45: "Error(s) encountered simulating Proposed Sizing model",
        46: "Error(s) encountered retrieving Proposed Sizing model simulation results",
        101: "SDD XML simulation input file not found",
        102: "Simulation weather file not found",
        103: "Simulation processing path not valid",
        104: "Simulation executable path not valid",
        105: "Simulation error output path/file not valid",
        106: "User aborted analysis",
        131: "Error encountered in OpenStudio loading SDD XML file",
        132: "Error encountered in OpenStudio saving model to OSM file",
        133: "Unable to locate EnergyPlus simulation SQL output file",
        134: "OpenStudio Model not valid following simulation",
        135: "OpenStudio Facility not valid following simulation",
        136: "Error creating OpenStudio Model object",
        161: "Fatal error(s) ocurred in EnergyPlus simulation",
        162: "EnergyPlus simulation did not complete successfully",
        163: "Fatal error(s) ocurred in EnergyPlus simulation (second of run pair)",
        164: "EnergyPlus simulation did not complete successfully (second of run pair)",
        181: "User aborted analysis during building model simulation"
    }

    def __init__(self, docker, cbeccFilename, options):
        """ Configure the defaults based on the type the system configurations"""
        self.docker = docker

        # take the options and merge them with the defaults
        self.options = dict(self.getDefaults(docker).items() + options.items())

        # The CBECC Filename has to be backslashes!
        self.cbeccFilename = os.path.realpath(cbeccFilename).replace("/", "\\")

        self.validateConfig()

        # if the config appears to be valid, then chdir to the location of CBECC-Com Installer
        os.chdir(self.options["cbeccInstallRoot"])
        self.lib = cdll.LoadLibrary('BEMCmpMgr_os.dll')


        # Call the DLL method to initialize
        try:
            print("Initializing CBECC-Com Run")
            # bemType is 0 and log is NULL/None (per instructions)
            self.lib.InitBEMProcAndCmpMgrDLLs(self.options["rulesPath"], 0, None)
        except:
            # This error doesn't actually get called
            print "Error calling InitBEMProcAndCmpMgrDLLs"
            raise StandardError

    def CMX_PerformAnalysis_CECNonRes(self):
        """ Run the CBECC Com analysis  """

        # These values are defaulted at the moment.
        pszBEMBasePathFile = None
        pszRulesetPathFile = self.options["cbeccUserRoot"] + "/Rulesets/CEC 2013 NonRes.bin"
        pszSimWeatherPath = self.options["cbeccUserRoot"] + "/EPW/"
        pszCompMgrDLLPath = self.options["cbeccInstallRoot"]
        pszDHWWeatherPath = None
        pszProcessingPath = os.path.dirname(
            self.cbeccFilename) + "\\"  # Make sure to use backslash, will fail if this is a forward slash
        pszModelPathFile = self.cbeccFilename
        pszLogPathFile = None
        pszUIVersionString = "pyCBECC"
        bLoadModelFile = True
        pszAnalysisOptionsCSV = self.options["pszAnalysisOptionsCSV"]
        pszErrorMessage = None  #"" # list of errors that are returned
        iErrorMsgLength = None  # have to specify the length of the above pszError Message
        bDisplayProgress = False
        hWnd = None
        pszResultsSummary = None
        iResultsSummaryLen = None

        print("Ruleset File Path is: " + pszRulesetPathFile)
        print("Processing path is: " + pszProcessingPath)
        print("Model path is: " + pszModelPathFile)
        print("Analysis Options are: " + pszAnalysisOptionsCSV)

        # Make sure the analysis directory exists
        if not os.path.exists(pszProcessingPath):
            os.makedirs(pszProcessingPath)

        print("Running CBECC-Com")
        result = self.lib.CMX_PerformAnalysis_CECNonRes(pszBEMBasePathFile, pszRulesetPathFile, pszSimWeatherPath,
                                                        pszCompMgrDLLPath,
                                                        pszDHWWeatherPath, pszProcessingPath, pszModelPathFile,
                                                        pszLogPathFile, pszUIVersionString, bLoadModelFile,
                                                        pszAnalysisOptionsCSV, pszErrorMessage, iErrorMsgLength,
                                                        bDisplayProgress, hWnd, pszResultsSummary, iResultsSummaryLen)

        # format the result as a string
        # TODO: Catch any exceptions and/or timeouts
        result = "{" + str(result) + ": " + CbeccComWrapper.ERROR_CODES[result] + "}"
        return result

    # alias the method
    run = CMX_PerformAnalysis_CECNonRes

    def exitBEMProcAndCmpMgrDLLs(self):
        """ Call the cleanup script which is part of the DLL """
        print("Finalizing CBECC-Com Run")
        self.lib.ExitBEMProcAndCmpMgrDLLs()

    # alias the method
    finalize = exitBEMProcAndCmpMgrDLLs

    def validateConfig(self):
        """ Some quick validation. The CBECC-Com can hang for awhile to test these simple things, so may as
        well do it up front
        """
        if not os.path.exists(self.options["rulesPath"]):
            print "Could not find rules path: " + self.options["rulesPath"]
            raise StandardError

        if not os.path.exists(self.cbeccFilename):
            print "Could not file cbecc file: " + self.cbeccFilename
            raise StandardError

    def getDefaults(self, docker):
        """
        Return the default configurations based on where this is running
        """
        options = {}
        if docker == True:
            # These paths have to be backslashed
            options["cbeccInstallRoot"] = "C:\\Program Files\\CBECC-Com 2013\\"
            options["cbeccUserRoot"] = "C:\\users\\root\\My Documents\\CBECC-Com 2013 Data"
            options["rulesPath"] = options["cbeccUserRoot"] + "\\Rulesets\\CEC 2013 Nonres\\CEC 2013 NonRes BEMBase.bin"
        else:  # windows version
            options["cbeccInstallRoot"] = "C:\\Program Files (x86)\\CBECC-Com 2013\\"
            options["cbeccUserRoot"] = expanduser("~") + "\\My Documents\\CBECC-Com 2013 Data"
            options["rulesPath"] = options["cbeccUserRoot"] + "\\Rulesets\\CEC 2013 Nonres\\CEC 2013 NonRes BEMBase.bin"

        options["pszAnalysisOptionsCSV"] = "Verbose,1,Silent,1,ComplianceReportPDF,1,ComplianceReportXML,1,BypassInputChecks,1"
        return options
