
#Creates SCAD and STL files of SOFT ROBOT MOULDS
#Original Version O_Bridgewater-Smith, 25/09/19, V1.1
# Do not delete the following import lines
#Refer to README for defining P1-P6

from __future__ import division
import os
import sys
from os import listdir
from subprocess import run
from solid import *
from solid.utils import *
import numpy as np
import tkinter
from tkinter import messagebox
from tkinter import filedialog


class SoftRobotBuild:
	cham_array1=[]
	arraysp = []
	def __init__(self):
		
		self.root = tkinter.Tk()
		self.root.call('wm', 'attributes', '.', '-topmost', True)
		self.root.title("Soft Robot Builder")
		bgColor = "#EDEDED"
		self.root.configure(bg=bgColor)
		self.Values = {}
		tkinter.Label(self.root, text = "Select the values to input in mm:", font=("Helvetica Neue Bold", 14), bg = bgColor).grid(row = 0, column = 2, columnspan = 3, padx = (0, 10), pady = (10, 5), sticky = 'w')
		#tkinter.Label(self.root, text = "Input Values (mm)", font=("Helvetica Neue Bold", 14), bg = bgColor).grid(row = 1, column = 2, columnspan = 4, padx = 10, sticky = 'w')
		tkinter.Label(self.root, text = "Please fill in the boxes with your values or keep the default values", font=("Helvetica Neue", 11), bg = bgColor).grid(row = 7, column = 2,columnspan=4, padx = 10, sticky = 'w')
		
		#BrowseButton
		tkinter.Label(self.root, text = "Choose folder to store output:", font=("Helvetica Neue", 14), bg = bgColor).grid(row = 1, column = 2, padx = 10, sticky = 'w')
		self.Browse = tkinter.StringVar()
		
		self.dirbut = tkinter.Button(self.root, text = 'Browse', fg = 'black', command= self.openDirectory).grid(row =1, column = 3, pady = (5, 5), sticky = 'e')
		tkinter.Entry(self.root, textvariable = self.Browse, justify = 'right', width = 20, font=("Helvetica Neue", 14), highlightbackground = bgColor).grid(row = 1, column = 4, columnspan = 7, sticky = 'w')
		
		
		###Width##
		tkinter.Label(self.root, text = "Chamber Width:", font=("Helvetica Neue", 14), bg = bgColor).grid(row = 3, column = 2, padx = 10, sticky = 'w')
		self.Width = tkinter.StringVar()
		self.Width.set('16')
		tkinter.Entry(self.root, textvariable = self.Width, justify = 'right', width = 10, font=("Helvetica Neue", 14), highlightbackground = bgColor).grid(row = 3, column = 3, columnspan = 2, sticky = 'w')
		
		##Length##
		tkinter.Label(self.root, text = "Chamber Length:", font=("Helvetica Neue", 14), bg = bgColor).grid(row = 4, column = 2, padx = 10, sticky = 'w')
		self.Length = tkinter.StringVar()
		self.Length.set('6')
		tkinter.Entry(self.root, textvariable = self.Length, justify = 'right', width = 10, font=("Helvetica Neue", 14), highlightbackground = bgColor).grid(row = 4, column = 3, columnspan = 2, sticky = 'w')
		
		##Depth/Height##
		tkinter.Label(self.root, text = "Chamber Depth:", font=("Helvetica Neue", 14), bg = bgColor).grid(row = 5, column = 2, padx = 10, sticky = 'w')
		self.Depth = tkinter.StringVar()
		self.Depth.set('14')
		tkinter.Entry(self.root, textvariable = self.Depth, justify = 'right', width = 10, font=("Helvetica Neue", 14), highlightbackground = bgColor).grid(row = 5, column = 3, columnspan = 2, sticky = 'w')
		
		##Chamber Spacing##
		tkinter.Label(self.root, text = "Chamber Spacing:", font=("Helvetica Neue", 14), bg = bgColor).grid(row = 3, column = 10, padx = 10, sticky = 'w')
		self.Spacing = tkinter.StringVar()
		self.Spacing.set('4')
		tkinter.Entry(self.root, textvariable = self.Spacing, justify = 'right', width = 10, font=("Helvetica Neue", 14), highlightbackground = bgColor).grid(row = 3, column = 13, columnspan = 2, sticky = 'w')
		
		##Chamber Number##
		tkinter.Label(self.root, text = "Number of Chambers:", font=("Helvetica Neue", 14), bg = bgColor).grid(row =4, column = 10, padx = 10, sticky = 'w')
		self.ChamNo = tkinter.StringVar()
		self.ChamNo.set('5')
		tkinter.Entry(self.root, textvariable = self.ChamNo, justify = 'right', width = 10, font=("Helvetica Neue", 14), highlightbackground = bgColor).grid(row = 4, column = 13, columnspan = 2, sticky = 'w')
		
		##Chamber Tray Height##
		tkinter.Label(self.root, text = "Tray Height:", font=("Helvetica Neue", 14), bg = bgColor).grid(row = 5, column = 10, padx = 10, sticky = 'w')
		self.Tray = tkinter.StringVar()
		self.Tray.set('5')
		tkinter.Entry(self.root, textvariable = self.Tray, justify = 'right', width = 10, font=("Helvetica Neue", 14), highlightbackground = bgColor).grid(row = 5, column = 13, columnspan = 2, sticky = 'w')
		
		tkinter.Button(self.root, text = "Exit", highlightbackground = bgColor, command = self.Exit).grid(row = 8, column = 3, pady = (5, 5), sticky = 'e')
		tkinter.Button(self.root, text = "Submit", highlightbackground = bgColor, command = self.Submit).grid(row = 8, column = 4, pady = (5, 5), sticky = 'e')

		self.root.withdraw()
		self.root.update_idletasks()

		x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
		y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 3
		self.root.geometry('+0+1'.format(x, y))
		self.root.resizable(False,False)

		self.root.deiconify()
		self.root.mainloop()
	
	def openDirectory(self):
		dirtext = 'wow'
		self.root.directory = filedialog.askdirectory()
		self.Browse.set(self.root.directory)
		print(self.root.directory)

	def Exit(self):
        # Calling the destroy() method on our GUI will close it.
		self.root.destroy()
		exit()
		
	def Warning(self):
		self.root.withdraw()
		messagebox.showerror("Error", "Values cannot be blank or 0")
		#messagebox.showwarning("Warning","Warning message")
		#messagebox.showinfo("Information","Informative message")
		exit()
	
	def Submit(self):
		print("The user clicked the 'Submit' button.")
		self.value = self.Width.get()
		if self.value == '' or self.value =='0':
			self.Warning()
		else:
			self.value = int(self.Width.get())
			SoftRobotBuild.cham_array1.append(self.value)
			print(self.Width.get())
		
		self.value1 = self.Length.get()
		if self.value1 == '' or self.value1 =='0':
			self.Warning()
		else:
			self.value1 = int(self.Length.get())
			SoftRobotBuild.cham_array1.append(self.value1)
		
		self.value2 = self.Depth.get()
		if 	self.value2 == '' or self.value2 =='0':
			self.Warning()
		else:
			self.value2 = int(self.Depth.get())
			SoftRobotBuild.cham_array1.append(self.value2)
		self.value3 = self.Spacing.get()
		if self.value3 == '' or self.value3 =='0':
			self.Warning()
		else:
			self.value3 = int(self.Spacing.get())
			SoftRobotBuild.arraysp.append(self.value3)
		self.value4 = self.ChamNo.get()
		if self.value1 == '' or self.value1 =='0':
			self.Warning()
		else:
			self.value4 = int(self.ChamNo.get())
			SoftRobotBuild.arraysp.append(self.value4)
		self.value5 = self.Tray.get()
		if self.value1 == '' or self.value1 =='0':
			self.Warning()
		else:
			self.value5 = int(self.Tray.get())
			SoftRobotBuild.arraysp.append(self.value5)
		SoftRobotBuild.arraysp.append(self.root.directory)
		self.root.destroy()

def ChamberPlacement(Dist_cham,n):
	#function to calculate and store values for chamber locations
	#Function changes depending on if the number of chambers(n) is odd or even
	mod = n % 2
	if mod > 0:
		print("This is an odd number.")
		sequence = (n-1)/2
		min_val = -(sequence*Dist_cham)
		max_val = sequence*Dist_cham
		Cham_array1 = np.arange(start=min_val, stop=(max_val+0.1),step=Dist_cham)   #+0.1 no good
	else:
		print("This is an even number.")
		sequence = ((n-1)/2)
		min_val = -(sequence*Dist_cham)
		max_val = sequence*Dist_cham
		Cham_array1 = np.arange(start=min_val, stop=(max_val+0.1),step=Dist_cham)   #+0.1 no good
	return Cham_array1


def Geometry_Values(cham_vals,spacing_val,n,Tray_depth):
	#function calculates geometry based on users input
	#Pass in values cham_vals=[W,L,D], n = number of chambers, spacing_val = Distance between chambers, Tray_depth = depth/height of the outside tray
	#coef are constants
	
	Tot_ChamL= (n*cham_vals[1])+((n-1)*spacing_val)
	Dist_Chambers = cham_vals[1]+spacing_val
	#P5 air chamber values
	P5_Depth_coef = 7.5 #air chamber width (larger means bigger)
	P5_D = round(cham_vals[0]/P5_Depth_coef)+2
	#Location+Values for chamber structures
	P6_X_loc = cham_vals[0]/4
	P6_Y_loc = Dist_Chambers/2
	P6_L = 1.0
	
	P3 = [cham_vals[0],Tot_ChamL,2]
	P4 = [P3[0]+2,P3[1]+2,Tray_depth]
	P5 = [P5_D, P3[1], Tray_depth]
	P2 = [cham_vals[0]+10,P3[1]+10,Tray_depth]										#10 4mm each side plus top mould
	P1 = [P2[0]+4.5,P2[1]+4.5, Tray_depth]												#2mm wall each side
	P6 = [P6_L, P6_L, Tray_depth]
	
	
	return(P3,P4,P5,P2,P1,P6, P6_X_loc,P6_Y_loc,P5_D,Dist_Chambers)
	
def basic_geometry(cham_vals,n,spacing_val,Tray_depth):
	#This function builds the model
	#First it recieves the values from def Geometry_values
	#_trans means the translation of a part
	P3,P4,P5,P2,P1,P6, P6_X_loc,P6_Y_loc,P5_D,Dist_Chambers = Geometry_Values(cham_vals,spacing_val,n,Tray_depth)
	P1_trans = Tray_depth/2
	Cham_trans = cham_vals[2]/2 +1
	
	#This creates P1,P2,P4 - Creates P1 then removes material using P2 and P4
	#Removal#
	tray = up(P1_trans)(cube(P1, center=True)) - up(P1_trans+3)(cube(P2, center=True))
	remove_mat = up(P1_trans+2)(cube(P4, center=True))
	tray = tray - remove_mat
	
	#Initialise the chamber array, storing location coord for each chamber
	#Creates each chamber and translates it into position and adds the airchamber(P5)
	#union#
	Cham_array=[]
	X_loc = [0,-(2*P6_X_loc)]
	Cham_array = ChamberPlacement(Dist_Chambers,n)
	chamber_trans = cham_vals[2]/2+1
	air_chamber=0
	for x in Cham_array:
		cham= forward(x)(cube(cham_vals, center=True))
		chamber= up(chamber_trans)(cham)
		air_chamber += chamber
	air_chamber += up(P1_trans)(cube(P5, center=True))
	
	#Creates chamber structures(P6) and P3
	#P6 will be translated in the X and Y locations for a continous pattern either side of the air chamber(P5)
	#Removal#
	air_ap=0
	holes= up(2)(cube(P3, center=True))
	for b in X_loc:
		for x in Cham_array:
			air = right(P6_X_loc+b)(cube(P6, center=True))
			air = up(2)(air)
			air = forward((P6_Y_loc+x))(air)
			air_ap+=air
			print(P6_X_loc)
		
	holes = holes - air_ap
	print(Cham_array)
	return union()(air_chamber, tray,holes)
	
def top_Part(cham_vals,n,spacing_val,Tray_depth):
	P3,P4,P5,P2,P1,P6, P6_X_loc,P6_Y_loc,P5_D,Dist_Chambers = Geometry_Values(cham_vals,spacing_val,n,Tray_depth)
	P1_trans = Tray_depth/2
	box = up(P1_trans)(cube([cham_vals[0]+9,P3[1]+9,cham_vals[2]],center=True))
	
	Cham_array =[]
	X_loc = [0,-(2*P6_X_loc)]
	Cham_array = ChamberPlacement(Dist_Chambers,n)
	chamber_trans = cham_vals[2]/2+1
	air_chamber=0
	cham_new = [cham_vals[0]+4, cham_vals[1]+3.5,cham_vals[2]+80]   #plus 4 [cham_vals[0]+4, cham_vals[1]+3,cham_vals[2]+15]   
	Part3 = up(-Tray_depth)(cube([cham_new[0],P3[1]+5,Tray_depth],center=True))
	for x in Cham_array:
		cham= forward(x)(cube(cham_new, center=True))
		chamber= up(chamber_trans)(cham)
		air_chamber += chamber
	box -= air_chamber
	box -= Part3
	return box
	
def tray(cham_vals,Tray_depth):
	P3,P4,P5,P2,P1,P6, P6_X_loc,P6_Y_loc,P5_D,Dist_Chambers = Geometry_Values(cham_vals,spacing_val,n,Tray_depth)
	P1 = [P1[0]+4,P1[1]+4, P1[2]]
	P2 = [P2[0]+4,P2[1]+4, P2[2]]
	P1_trans = Tray_depth/2
	tray = up(P1_trans)(cube(P1, center=True)) - up(P1_trans+3)(cube(P2, center=True))
	
	return tray

if __name__ == '__main__':
	SEGMENTS = 48
	cham_vals = [16,6,10]          													#input chamber values
	spacing_val = 6.5																#spacing input value
	n = 4
	Tray_depth = 5

	SoftRobotBuild()
	cham_vals = SoftRobotBuild.cham_array1
	spacing_val = SoftRobotBuild.arraysp[0]
	n = SoftRobotBuild.arraysp[1]
	Tray_depth = SoftRobotBuild.arraysp[2]
	outdirectory = SoftRobotBuild.arraysp[3]
	print('dir',outdirectory)
	a = basic_geometry(cham_vals,n,spacing_val,Tray_depth)
	B = top_Part(cham_vals,n,spacing_val,Tray_depth)
	c = tray(cham_vals,Tray_depth)
	#out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
	out_dir = outdirectory
	file_out = os.path.join(out_dir, 'basic_geometry_BOTTOM.scad')
	file_out1 = os.path.join(out_dir, 'basic_geometry_TOP.scad')
	file_out2 = os.path.join(out_dir, 'basic_geometry_TRAY.scad')

	print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())
	scad_render_to_file(a, file_out, file_header='$fn = %s;' % SEGMENTS)
	scad_render_to_file(B, file_out1, file_header='$fn = %s;' % SEGMENTS)
	scad_render_to_file(c, file_out2, file_header='$fn = %s;' % SEGMENTS)
	#f = "O:\OLIVIA\SCRIPTS\basic_geometry1.scad"
	#print('wow',f)
	#of = str(f.replace('.scad', '.stl')) # name of the outfile .stl
	#print(of)
	#cmd = run (["O:\OLIVIA\OpenSCAD-2019.05-x86-32\openscad-2019.05\openscad.com",  "-o", "O:\OLIVIA\SCRIPTS\basic_geometry1.stl",  "O:\OLIVIA\SCRIPTS\basic_geometry1.scad"])#create openscad command
	#exec(cmd)