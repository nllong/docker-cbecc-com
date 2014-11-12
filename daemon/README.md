


wine /root/.wine/drive_c/windows/system32/rundll32.exe /root/.wine/drive_c/Program\ Files/CBECC-Com\ 2013/BEMCmpMgr_os.dll


# Example Run
wine /root/.wine/drive_c/windows/system32/rundll32.exe BEMCmpMgr_os.dll,CMX_PerformAnalysis_CECNonRes,NULL


wine /root/.wine/drive_c/windows/system32/rundll32.exe BEMCmpMgr_os.dll,CMX_PerformAnalysis_CECNonRes,NULL,"~/CBECC-Com 2013 Data/Rulesets/CEC 2013 NonRes.bin"


wine /root/.wine/drive_c/windows/system32/rundll32.exe BEMCmpMgr_os.dll,CMX_PerformAnalysis_CECNonRes,NULL,"~/CBECC-Com 2013 Data/Rulesets/CEC 2013 NonRes.bin","~/CBECC-Com 2013 Data/EPW/",NULL,NULL

wine /root/.wine/drive_c/windows/system32/rundll32.exe BEMCmpMgr_os.dll,CMX_PerformAnalysis_CECNonRes,NULL,"~/CBECC-Com 2013 Data/Rulesets/CEC 2013 NonRes.bin","~/CBECC-Com 2013 Data/EPW/",NULL,NULL,"/var/cbecc-com-files/cbecc-test-inputs/junk","/var/cbecc-com-files/cbecc-test-inputs/0200006-OffSml-SG-BaseRun.cibd",NULL,"Docker",true,"0,0,0,1,2,100,0,0,0,0,0,0,0,-1,0,1,0,0,1,2",NULL,0,false,NULL,NULL,2056

# without commas
cd /root/.wine/drive_c/Program\ Files/CBECC-Com\ 2013/ &&
wine /root/.wine/drive_c/windows/system32/rundll32.exe BEMCmpMgr_os.dll,CMX_PerformAnalysis_CECNonRes NULL "~/CBECC-Com 2013 Data/Rulesets/CEC 2013 NonRes.bin" "~/CBECC-Com 2013 Data/EPW/" NULL NULL "/var/cbecc-com-files/cbecc-test-inputs/junk" "/var/cbecc-com-files/cbecc-test-inputs/0200006-OffSml-SG-BaseRun.cibd" NULL "Docker" 1 "0,0,0,1,2,100,0,0,0,0,0,0,0,-1,0,1,0,0,1,2" NULL 0 0 NULL NULL 2056


# testing on windows VM
RUNDLL32.EXE SHELL32.DLL,Control_RunDLL desk.cpl,,0

rundll32.exe BEMCmpMgr_os.dll,InitBEMProcAndCmpMgrDLLs "C:\Users\nlong\Documents\CBECC-Com 2013 Data\Rulesets\CEC 2013 Nonres\CEC 2013 NonRes BEMBase.bin",0,NULL
