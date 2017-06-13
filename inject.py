#!/usr/bin/python27

# IMPORT
import os
import sys
import time
import shutil

# INIT
if os.name == "nt":
    clr = "cls"
else:
    clr = "clear"
os.system(clr)
header = "NES ROM Injector for NDS by bennyman123abc"

# DEF
def main():
    print(header)
    print("")
    maindir = os.path.dirname(os.path.realpath(__file__))
    for file in os.listdir(maindir):
        if file.endswith(".nes"):
            base = os.path.basename(file)
            game = os.path.splitext(base)[0]
            print("Starting to inject " + game)
            print("Copying template...")
            if os.path.isdir(maindir + "/template") == False:
                print("ERROR: Template does not exist!")
                print("SOLUTION: Redownload this tool")
                sys.exit()
            if os.path.isdir(maindir + "/" + game) == True:
                print("ERROR: Injection folder already exists!")
                print("SOLUTION: Delete the folder and try again")
                sys.exit()
            shutil.copytree(maindir + "/template", maindir + "/" + game)
            print("Template copied successfully!")
            print("Copying ROM...")
            shutil.copy(file, maindir + "/" + game + "/arm9/data")
            os.remove(maindir + "/" + game + "/arm9/data/rom.nes")
            os.rename(maindir + "/" + game + "/arm9/data/" + file, maindir + "/" + game + "/arm9/data/rom.nes")
            print("ROM Copied Successfully!")
            print("Editing the Makefile...")
            with open(maindir + "/" + game + "/" + "Makefile", "r") as makefile:
                data = makefile.readlines()
            print("")
            print("ROM Name: " + file)
            print("Enter the game's name: ")
            print("")
            gname = raw_input("Game Name: ")
            data[9] = "export GAME_TITLE		:=	" + gname + "\n"
            data[10] = "export GAME_SUBTITLE1	:=	" + "\n"
            print("Enter the game's author/publisher: ")
            print("Ex. Nintendo")
            print("")
            gpub = raw_input("Game Author/Publisher: ")
            data[11] = "export GAME_SUBTITLE2	:=	" + gpub + "\n"
            data[13] = "export TARGET		:=	" + game + "\n"
            with open(maindir + "/" + game + "/" + "Makefile", "w") as makefile:
                makefile.writelines( data )
            print("Makefile finished!")
            print("Building the inject...")
            os.chdir(maindir + "/" + game)
            os.system("make")
            os.chdir(maindir)
            print("Inject Built!")
            print(game + " Finished!")
    print("All Finished!")

# CODE
main()