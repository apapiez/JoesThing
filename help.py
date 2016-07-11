# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:02:44 2016

@author: s1582670
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

Simple reading/writing program for managing Gwwidion input/output files
"""

import os, glob
import time
import sys
#import matplotlib.pyplot as plt
import pylab
import numpy as np
import math
import matplotlib.pyplot as plt
#fig = plt.figure()
#ax = fig.add_subplot(2,1,1)
#import pickle

print("boy\nI'mma lay you out")
class Interface(object):
    def __init__(self, _dir, _file, _mean, _square, FName, x, y, z):
        self._dir()
        self.file()
        self.mean()
        self.square()
        self.FName = FName
        self.x = x
        self.y = y
        self.z = z
        self.Dir = Dir
    
    def _dir(self):
        """
        Points to the right directory
        """
        print("Current directory:", os.getcwd())
        while True:     
            while True:#try:
                global x, y, z, FName, Dir
                Dir = "C:\Py\Test"#input("Please input target directory: \n")   
                os.chdir(Dir)
                FName = input("Input file name or press enter for Maxima comparison\n")
                if len(FName) == 0:
                    print("Batch Initiated")
                    file = Interface._HighRanger(1)
                else:
                    data = np.genfromtxt(FName)
                    x = data[:,0]
                    y = data[:,1]
                    z = data[:,2]
                    print(FName, "Opened")
                break
            #except:
                print("[WinError 2] The system cannot find the file specified:", Dir, FName, "\n or input file is not in .xyz format.\n Please try again")
        file = Interface._file(1)
    
    def _file(self):
        TransF = int(input("Input tranformation:\n1. Mean of a range\n2. Squaring the data\n3. Square rooting\n4. Roughness Ranger\n5. Smooth Jazz\n6. Logs\n7. Distribution function\n8. Maxima comparison\n"))
        if TransF == 1:
            file = Interface._mean(1)
        elif TransF == 2:
            file = Interface._square(1)
        elif TransF == 3:
            file = Interface._squareRT(1)
        elif TransF == 4:
            file = Interface._RRanger(1)
        elif TransF == 5:
            file = Interface._SJazz(1)
        elif TransF == 6:
            file = Interface._Lumber(1)
        elif TransF == 7:
            file = Interface._Distro(1)
        elif TransF == 8:
            file = Interface._HighRanger(1)
        else:
            print("Incorrect input")
            file = Interface._file(1)
        
    def _mean(self):
        Range = int(input("Input range: "))
        InitL = 0
        EndL = Range
        xa, ya, za = [], [], []
        while EndL < len(x):
            TempX = [np.mean(x[InitL:EndL])]
            #TempX = TempX*3
            xa.append(TempX)
            TempX = []
            InitL = InitL + Range
            EndL = EndL + Range
            print("Goosebumps has sold ", InitL, " copies, Tunnocks have sold ", EndL, " teacakes.")
        else:
            print("broke")
            InitL, EndL = 0, Range
        while EndL < len(y):
            TempY = [np.mean(y[InitL:EndL])]
            #TempY = TempY*3
            ya.append(TempY)
            TempY = []
            InitL = InitL + Range
            EndL = EndL + Range
            print("No one sings about ", EndL, " fish like Gaston.")
        else:
            print("broke")
            InitL, EndL = 0, Range
        while EndL < len(y):
            TempZ = [np.mean(z[InitL:EndL])]
            #TempY = TempY*3
            za.append(TempZ)
            TempZ = []
            InitL = InitL + Range
            EndL = EndL + Range
            print(EndL, "Bottles of chocolate milk on the wall, take", InitL, "down and there will be 3.")
        else:
            print("broke")
            InitL, EndL = 0, Range
        File = open("R"+str(Range)+"Avg"+FName, 'w')
        while InitL < len(za):
            #Write = xa[InitL]+
            #pickle.dump(Write, " ", File)
            #Write = ya[InitL]
            #pickle.dump(Write, " ", File)
            #Write = (za[InitL]
            #pickle.dump(Write, "\n", File)
            Write = str(xa[InitL])
            Write = Write.strip("[]")
            File.write(Write)
            File.write(" ")
            Write = str(ya[InitL])
            Write = Write.strip("[]")
            File.write(Write)
            File.write(" ")
            Write = str(za[InitL])
            Write = Write.strip("[]")
            File.write(Write)
            File.write("\n")
            InitL = InitL + 1
            print("Don't I deserve", InitL, " donuts?")
        File.close
        print("Yes I do")
    
    def _square(self):
        InitL = 0
        sx, sy, sz = [], [], []
        Command = input("Please specify what to square: x, y or z (Lowercase): ")
        while InitL < len(z):
            if "x" in Command:
                TempX = x[InitL]*x[InitL]
                sx.append(TempX)
            if "y" in Command:
                TempY = y[InitL]*y[InitL]
                sy.append(TempY)
            if "z" in Command:
                TempZ = z[InitL]*z[InitL]
                sz.append(TempZ)
            InitL = InitL + 1
            print("Da sind", InitL, "Katzen in meine kopf.")
        else:
            InitL = 0
        File = open("Squared"+FName, 'w')
        while InitL < len(z):
            if "x" in Command:
                Write = str(sx[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            else:
                Write = str(x[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            if "y" in Command:
                Write = str(sy[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            else:
                Write = str(y[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            if "z" in Command:
                Write = str(sz[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write("\n")
            else:
                Write = str(z[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write("\n")
            InitL = InitL + 1
            print("Don't I deserve", InitL, "donuts?")
        File.close
        print("Yes I do")

    def _squareRT(self):
        InitL = 0
        sx, sy, sz = [], [], []
        Command = input("Please specify what to square: x, y or z (Lowercase): ")
        while InitL < len(z):
            if "x" in Command:
                TempX = math.sqrt(x[InitL])
                sx.append(TempX)
            if "y" in Command:
                TempY = math.sqrt(y[InitL])
                sy.append(TempY)
            if "z" in Command:
                TempZ = math.sqrt(z[InitL])
                sz.append(TempZ)
            InitL = InitL + 1
            print("Da sind", InitL, "Katzen in meine kopf.")
        else:
            InitL = 0
        File = open("Sqrt"+FName, 'w')
        while InitL < len(z):
            if "x" in Command:
                Write = str(sx[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            else:
                Write = str(x[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            if "y" in Command:
                Write = str(sy[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            else:
                Write = str(y[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            if "z" in Command:
                Write = str(sz[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write("\n")
            else:
                Write = str(z[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write("\n")
            InitL = InitL + 1
            print("Don't I deserve", InitL, "donuts?")
        File.close
        print("Yes I do")
    
    def _RRanger(self):
        InitL, EndL, RCount = 0, 512, 0
        SumX, SumY, SumZ = [], [], []
        x6 = x * 1E6
        y6 = y * 1E6
        z9 = z * 1E9
        while RCount < 512:
            SumX.append(x6[InitL:EndL])
            SumY.append(y6[InitL:EndL])
            SumZ.append(z9[InitL:EndL])
            RCount = RCount + 1
            InitL = InitL + 512
            EndL = EndL + 512
            print("Step", RCount, "of 512")
        InitL, EndL, RCount = 0, 512, 0
        NewDir = FName + 'Output'
        os.mkdir(NewDir)
        print("Output: ", NewDir)
        os.chdir(NewDir)
        ZofX = []
        RCount, AvgCount, AvgZ, AZofX, ZMinZ, ZMaxZ, SZofX = 0, 0, [], 0, [], [], []
        while AvgCount < 512:
            while RCount < 512:
                ZofX.append(SumZ[RCount][AvgCount])
                RCount = RCount + 1
            AvgZ.append(np.average(ZofX))
            ZMaxZ.append(np.max(ZofX))
            ZMinZ.append(np.min(ZofX))
            AvgCount = AvgCount+1
            print("Step", AvgCount, "Of 512 completed")
            ZofX = []
            RCount = 0
        MaxZ = np.max(SumZ)
        MinZ = np.min(SumZ)
        RCount = 0
        plt.figure(figsize = (10, 6.66))
        while RCount < 512:
            plt.plot(SumX[RCount],SumZ[RCount])
            plt.plot(SumX[RCount],AvgZ, linestyle='--')
            plt.plot(SumX[RCount],ZMaxZ)
            plt.plot(SumX[RCount],ZMinZ)
            pylab.ylim([MinZ,MaxZ])
            plt.ylabel ("Height (nm)")
            plt.xlabel ("Lateral distance (Microns)")
            RCount = RCount + 1
            print ("Plotting no.", RCount, "of 512")
            PngName = FName + str(RCount) + '.png'
            plt.savefig(PngName, dpi=100)
            plt.clf()
        print("Texas styled")
        RCount, AvgCount, AvgZ, AZofX, ZMinZ, ZMaxZ, SZofX, SumX, SumY, SumZ = 0, 0, [], 0, [], [], [], [], [], []
        sys.exit()
            
    def _SJazz(self):
        print("Smooth jazz deployed")
        InitL, EndL, sx, sy, sz = 0, 1, [], [], []
        sx.extend([x[InitL]])
        sy.extend([y[InitL]])
        sz.extend([z[InitL]])
        while InitL < len(z):   
            TempX = np.mean(x[InitL:EndL])
            sx.extend([TempX])
            sx.extend([x[EndL]])
            print("First number:", x[InitL], "Average number:", TempX, "Second number:", x[EndL], "Length:", len(sx))
            TempY = np.mean(y[InitL:EndL])
            sy.extend([TempY])
            sy.extend([y[EndL]])
            TempZ = np.mean(z[InitL:EndL])
            sz.extend([TempZ])
            sz.extend([z[EndL]])
            InitL = InitL +1
            EndL = EndL + 1
        InitL = 0
        File = open("Smooth"+FName, 'w')
        while InitL < len(sz):
            Write = str(sx[InitL])
            Write = Write.strip("[]")
            File.write(Write)
            File.write(" ")
            Write = str(sy[InitL])
            Write = Write.strip("[]")
            File.write(Write)
            File.write(" ")
            Write = str(sz[InitL])
            Write = Write.strip("[]")
            File.write(Write)
            File.write("\n")
            InitL = InitL + 1
            print(InitL, "of", len(sz))
        print("Smooth jazz deployed")
        File.close
        
    def _Lumber(self):
        InitL, sx, sy, sz = 0, [], [], []
        Command = input("Please specify what to Log: x, y or z (Lowercase): ")
        Base = input("Please input base: ")
        FBase = float(Base)
        while InitL < len(z):
            if "x" in Command:
                sx.extend([math.log(x[InitL], FBase)])
            if "y" in Command:
                sy.extend([math.log(y[InitL], FBase)])
            if "z" in Command:
                sz.extend([math.log(z[InitL], FBase)])
            InitL = InitL + 1
        InitL = 0
        File = open("Log"+Base+FName, 'w')
        while InitL < len(sz):
            if "x" in Command:
                Write = str(sx[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            else:
                Write = str(x[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            if "y" in Command:
                Write = str(sy[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            else:
                Write = str(y[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write(" ")
            if "z" in Command:
                Write = str(sz[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write("\n")
            else:
                Write = str(z[InitL])
                Write = Write.strip("[]")
                File.write(Write)
                File.write("\n")
            InitL = InitL + 1
            print(InitL, "Trees felled.")
        File.close
    
    def _Distro(self):
        InitL, BinZ = 0, []
        while InitL < len(z):
            BinZ.append(z[InitL])
            InitL = InitL + 1
        np.histogram(z, bins=512, range=None, normed=False, weights=None)
        MaxZ = np.max(z)
        MinZ = 0
        pylab.ylim([MinZ,MaxZ])
        plt.figure(figsize = (10, 6.66))        
        plt.xlabel ("Count")
        plt.ylabel ("Height (nm)")
        plt.title(FName)
        plt.hist(BinZ, bins=512, orientation='horizontal')  # plt.hist passes it's arguments to np.histogram
        plt.show()
        
    def _HighRanger(self):
        Dir = "C:\Py\Test\Batch"                                     #  Changes dir and points user to place files in directory
        print(Dir)        
        os.chdir(Dir)                                            #
        input("Please place all .xyz files in one folder then enter path:") #
        InitL, EndL, RCount, FCount, x, y, z = 0, 512, 0, 0, [], [], []         # 
        SumX, SumY, SumZ, FileList = [], [], [], []     # Varible Initilisation
        FileList = glob.glob('*.xyz')     # List of files in dir
        print(FileList)
        print(FileList[FCount])
        while len(FileList) > FCount:    #Loops for each file
            data = np.genfromtxt(FileList[FCount])       #Slices x, y, z data into different varibles
            x = data[:,0]
            y = data[:,1]
            z = data[:,2]
            x6 = x * 1E6        #
            y6 = y * 1E6        # Converts data to correct scale (Microns for xy and nanometers for z)       
            z9 = z * 1E9        #
            print(len(x), len(y), len(z)) # testing
            while RCount < 512: #loops for 512 times (the length of the list)
                SumX.append(x6[InitL:EndL])  # Splits the 512^2 data into a list of 512 entrees that are 512 long, for the x value
                SumY.append(y6[InitL:EndL])  # same for y
                SumZ.append(z9[InitL:EndL])  # same for z
                RCount = RCount + 1     # counts the number of loops
                InitL = InitL + 512     #starting slicing value
                EndL = EndL + 512       #ending slicing value
            print("Stage:", FCount, "of", len(FileList), "Part 1/3: Step", RCount, "completed") # test
            RCount, AvgCount, AvgZ, AZofX, ZMinZ, ZMaxZ, SZofX, ZofX, InitL, EndL = 0, 0, [], 0, [], [], [], [], 0, 512 # resets varibles and defines them
            while AvgCount < 512: # counts which number the averager is looking at
                while RCount < 512: # counts what loop it's on
                    ZofX.append(SumZ[RCount][AvgCount]) #takes a single value from the dataset, ie if it's averaging the first value it takes the first bit of data for every entree and creates a list of them
                    RCount = RCount + 1 #counts the loop so it takes all 512 bits of data
                AvgZ.append(np.average(ZofX))   #Averages the data taken into one point and adds it to a list
                ZMaxZ.append(np.max(ZofX))  #Finds the lowest value and adds it to a list
                ZMinZ.append(np.min(ZofX))  ## finds the highest value and adds it to a list
                AvgCount = AvgCount+1   # increases the average count so that 512 bits of data are averaged/minimized/maximized
                ZofX = []   # resets ZofX for next loop
                RCount = 0 # resets RCount for next loop
            print("Stage:", FCount, "of", len(FileList), "Part 2/3: Step", AvgCount, "completed")
            RCount = 0 # resets RCount for later loops
            PLabel = FileList[FCount].replace(".xyz", "") # Cuts off the .xyz of the input file for the legend
            print ("Stage:", FCount, "of", len(FileList), "Part 3/3: Plotting dataset.")

            plt.figure(2) #create a seperate figure
            if FCount == 0: #Initial parameters for the graph
                plt.figure(figsize = (15, 8)) #size of graph
                plt.ylabel ("Height (nm)") #axis labeling
                plt.xlabel ("Lateral distance (Microns)")   #axis labeling
            MinZ = np.min(AvgZ) #Normalises the lowest point for all data so they all scale around 0
            AvgZ = AvgZ - MinZ  # See above
            plt.plot(SumX[0],AvgZ, label=PLabel) #plots x vs the average of each Z point as y, since x is just a linear increase 0 is used (the first 512 points of the data, I've tried using RCount instead)
            print(FCount, "avg", PLabel) #Flavour text
            if int(FCount) == len(FileList) - 1: #On the last loop add a legend and save the figure to the folder
                pylab.legend(loc='upper right')
                plt.savefig("Average.png", dpi=100)
                print("Average.png plotted")
                
            plt.figure(3)               #The same as above but for minimum
            if FCount == 0:
                plt.figure(figsize = (15, 8))
                plt.ylabel ("Height (nm)")
                plt.xlabel ("Lateral distance (Microns)")
            MinZ = np.min(ZMaxZ)
            ZMaxZ = ZMaxZ - MinZ
            plt.plot(SumX[RCount],ZMaxZ, label=PLabel)
            print(FCount, "max", PLabel)
            if int(FCount) == len(FileList) - 1:
                pylab.legend(loc='upper right')
                plt.savefig("Max.png", dpi=100)
                print("Max.png plotted")
                
            plt.figure(4)              #The same as above but for Maximum
            if FCount == 0:
                plt.figure(figsize = (15, 8))
                plt.ylabel ("Height (nm)")
                plt.xlabel ("Lateral distance (Microns)")
            MinZ = np.min(ZMinZ)
            ZMinZ = ZMinZ - MinZ
            plt.plot(SumX[RCount],ZMinZ, label=PLabel)
            print(FCount, "min", PLabel)
            if int(FCount) == len(FileList) - 1:
                pylab.legend(loc='upper right')
                plt.savefig("Min.png", dpi=100)
                print("Min.png plotted")     
                
            plt.figure(5)               #The same as above but for all
            if FCount == 0:
                plt.figure(figsize = (15, 8))
                plt.ylabel ("Height (nm)")
                plt.xlabel ("Lateral distance (Microns)")
            MinZ = np.min(AvgZ)
            AvgZ = AvgZ - MinZ
            tPLabel = PLabel + "Avg"
            plt.plot(SumX[RCount],AvgZ, label=tPLabel)
            print(FCount, "Aavg", PLabel)
            MinZ = np.min(ZMaxZ)
            ZMaxZ = ZMaxZ - MinZ
            tPLabel = PLabel + "Max"
            plt.plot(SumX[RCount],ZMaxZ, label=tPLabel)
            print(FCount, "Amax", PLabel)
            MinZ = np.min(ZMinZ)
            ZMinZ = ZMinZ - MinZ
            tPLabel = PLabel + "Min"
            plt.plot(SumX[RCount],ZMinZ, label=tPLabel)
            print(FCount, "Amin", PLabel)
            if int(FCount) == len(FileList) - 1:
                pylab.legend(loc='upper right')
                plt.savefig("All.png", dpi=100)
                print("All.png plotted")
            RCount, AvgCount, AvgZ, AZofX, ZMinZ, ZMaxZ, SZofX, SumX, SumY, SumZ, x, y, z = 0, 0, [], 0, [], [], [], [], [], [], [], [], [] # reset varibles (ie garbage collection)
            FCount = FCount + 1 
        print("done!")
            
                
                    
                    
if __name__ == "__main__":
    dir = Interface._dir(1)  #initial starting script, points to Interface and Dir
#if __name__ == "__main__":
#    my_interface = Interface(1, 1, 1, 1, 1, [], [], [])
#    my_interface._dir()  #initial starting script, points to Interface and Dir