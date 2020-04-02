"""
this script is responsible for downloading the data from 
https://www.kaggle.com/imdevskp/corona-virus-report
and unzip and clean it

requirements :
1 - kaggle account
2 - kaggle package (you can install it using pip install (https://github.com/Kaggle/kaggle-api))
3 - go to  www.kaggle.com -> Your Account -> Create New API token
4 - move kaggle.json file to ~/.kaggle
"""
import os
import sys
from pythonScripts.cleanEgyptData import GetEgyptData
from pythonScripts.cleanEgyptWebData import cleanEgyptDataForWebSite
from pythonScripts.cleanWorldDataforWeb import cleanWorldDataForWebSite

print ("do you want to download the latest data set from kaggle ? [Y/N]")
print("if Yes please make sure you have kaggle api installed")
ans = input()
if ans == "Y" or ans == "y" or ans.lower() == "yes" :
    os.system('kaggle datasets download -d imdevskp/corona-virus-report')
    os.system('unzip corona-virus-report.zip')
    os.system('rm corona-virus-report.zip')
    GetEgyptData()
    cleanEgyptDataForWebSite()
    cleanWorldDataForWebSite()
else :
    GetEgyptData()
    cleanEgyptDataForWebSite()
    cleanWorldDataForWebSite()