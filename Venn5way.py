########################### LIBRARY IMPORT ###########################
import pandas as pd
import matplotlib.pyplot as plt
from __future__ import division
from matplotlib.backends.backend_pdf import PdfPages

########################### FUNCTIONS ################################
# partial sum function
def partial_sums(iterable):
    total = 0
    for i in iterable:
        total += i
        yield total

# Logic test
def logic(includes, excludes=[set()]):
    logic_set = set.intersection(*includes) - set.union(*excludes)
    return len(logic_set),  logic_set


########################### INPUT ####################################  
df = pd.read_csv('/home/mon13m/Data/Linear_venn_diagramm/Venn_tool/list_tabular_5way.csv' , sep='\t')
########################### CORE #####################################
# remove the nans with dropna() and convert each column into a set
setA = set(df.ix[:,0].dropna())
setB = set(df.ix[:,1].dropna())
setC = set(df.ix[:,2].dropna())
setD = set(df.ix[:,3].dropna())
setE = set(df.ix[:,4].dropna())

# initialization
col = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# column1 : in A not in B not in C not in D not in E
col[0], setAonly = logic( [setA], [setB, setC, setD, setE] )
# column2 : in A not in B not in C in D not in E
col[1], setAD = logic( [setA, setD], [setB, setC, setE] )
# column3 : in A not in B not in C in D in E
col[2], setADE = logic( [setA, setD, setE], [setB, setC] )
# column4 : in A not in B not in C not in D in E
col[3], setAE = logic( [setA, setE], [setB, setC, setD] )
# column5 : in A not in B in C not in D not in E
col[4], setAC = logic( [setA, setC], [setB, setE, setD] ) 
# column6 : in A not in B in C not in D in E
col[5], setACE = logic( [setA, setC, setE], [setB, setD ] )  
# column7 : in A not in B in C in D in E
col[6], setACDE = logic( [setA, setC, setD, setE], [setB] ) 
# column8 : in A not in B in C in D not in E
col[7], setACD = logic( [setA, setC, setD], [setB , setE] )       
# column9 : in A in B in C in D in E
col[8], setABCDE = logic( [setA, setB, setC, setD, setE])      
# column10 : in A in B in C in D not in E
col[9], setABCD = logic( [setA, setB, setC, setD], [setE])
# column11 : in A in B in C not in D not in E
col[10], setABC = logic( [setA, setB, setC], [setD, setE])
# column12 : in A in B in C not in D in E
col[11], setABCE = logic( [setA, setB, setC, setE], [setD]) 
# column13 : in A in B not in C not in D in E
col[12], setABE = logic( [setA, setB, setE], [setC, setD])         
# column14 : in A in B not in C in D in E
col[13], setABDE = logic( [setA, setB, setD, setE], [setC])         
# column15 : in A in B not in C in D not in E
col[14], setABD = logic( [setA, setB, setD], [setC, setE])   
# column16 : in A in B not in C notin D not in E
col[15], setAB = logic( [setA, setB], [setC, setD, setE]) 
# column17 : not in A in B not in C not in D not in E
col[16], setBonly = logic( [setB], [setA, setC, setD, setE]) 
# column18 : not in A in B in C not in D not in E
col[17], setBC = logic( [setB, setC], [setA, setD, setE]) 
# column19 : not in A in B in C in D not in E
col[18], setCBD = logic( [setC, setB, setD], [setA, setE]) 
# column20 : not in A in B in C in D in E
col[19], setBCDE = logic( [setB, setC, setD, setE], [setA]) 
# column21 : not in A in B in C not in D in E
col[20], setCBE = logic( [setC, setB, setE], [setA, setD]) 
# column22 : not in A in B not in C not in D in E
col[21], setBE = logic( [setB, setE], [setA, setC, setD]) 
# column23 : not in A in B not in C in D in E
col[22], setEBD = logic( [setE, setB, setD], [setC, setA]) 
# column24 : not in A in B not in C in D not in E
col[23], setBD = logic( [setB, setD], [setA, setC, setE]) 
# column25 : not in A not in B in C not in D not in E
col[24], setConly = logic( [setC], [setA, setB, setD, setE]) 
# column26 : not in A not in B in C in D not in E
col[25], setCD = logic( [setC, setD], [setA, setB, setE]) 
# column27 : not in A not in B in C not in D in E
col[26], setCE = logic( [setC, setE], [setA, setB, setD]) 
# column28 : not in A not in B in C in D in E
col[27], setCDE = logic( [setC, setD, setE], [setA, setB])
# column29 : not in A not in B not in C in D in E
col[28], setDE = logic( [setD, setE], [setA, setB, setC])
# column30 : not in A not in B not in C not in D in E
col[29], setEonly = logic( [setE], [setA, setB, setC, setD]) 
# column31 : not in A not in B not in C in D not in E
col[30], setDonly = logic( [setD], [setA, setB, setC, setE]) 

#  number of observation, non redundant (if shared counted only once)
total = col[0] + col[1] + col[2] + col[3] + col[4] + col[5] + col[6] + col[7] + col[8] + col[9] + col[10] + col[11] + col[12] + col[13] + col[14] + col[15] + col[16] + col[17] + col[18] + col[19] + col[20] + col[21] + col[22] + col[23] + col[24] + col[25] + col[26] + col[27]  + col[28] + col[29] + col[30] 
#print total

# dataframe creation for list output printing
data = [list(setAonly), list(setAD), list(setADE), list(setAE), list(setAC), list(setACE), list(setACDE), list(setACD), list(setABCDE), list(setABCD), list(setABC), list(setABCE), list(setABE), list(setABDE), list(setABD), list(setAB), list(setBonly), list(setBC), list(setCBD), list(setBCDE), list(setCBE), list(setBE), list(setEBD), list(setBD), list(setConly), list(setCD), list(setCE), list(setCDE), list(setDE), list(setEonly), list(setDonly)]
header = ['setAonly', 'setAD', 'setADE', 'setAE', 'setAC', 'setACE', 'setACDE', 'setACD', 'setABCDE', 'setABCD', 'setABC', 'setABCE', 'setABE', 'setABDE', 'setABD', 'setAB', 'setBonly', 'setBC', 'setCBD', 'setBCDE', 'setCBE', 'setBE', 'setEBD', 'setBD', 'setConly', 'setCD', 'setCE', 'setCDE', 'setDE', 'setEonly', 'setDonly']
df_out = pd.DataFrame(data, index = header)
# Transposition needed
df2 = df_out.T

########################## OUTPUT ################################

# printing out csv files
df2.to_csv('/home/mon13m/Data/Linear_venn_diagramm/Venn_tool/list_tabular_5way_lists.csv', sep='\t')########################## OUTPUT ################################


### OUTPUT
# Printing test
#print column_header[0] + "\t|" + str(col[0]) + "\t|" + str(col[1]) + "\t|" + str(col[2]) + "\t|" + str(col[3]) + "\t|" + str(col[4]) + "\t|" + str(col[5]) + "\t|" + str(col[6]) + "\t|" +  str(col[7]) + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +  str(col[10]) + "\t|" +  str(col[11]) + "\t|" +  str(col[12]) + "\t|" +  str(col[13]) + "\t|" +  str(col[14]) + "\t|" + str(col[15]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          +"\n" 
#print column_header[1] + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" +  "-"         + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +  str(col[10]) + "\t|" +  str(col[11]) + "\t|" +  str(col[12]) + "\t|" +  str(col[13]) + "\t|" +  str(col[14]) + "\t|" + str(col[15]) + "\t|" + str(col[16]) + "\t|" + str(col[17]) + "\t|" + str(col[18]) + "\t|" + str(col[19]) + "\t|" + str(col[20]) + "\t|" + str(col[21]) + "\t|" + str(col[22]) + "\t|" + str(col[23]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          +"\n"         
#print column_header[2] + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + str(col[4]) + "\t|" + str(col[5]) + "\t|" + str(col[6]) + "\t|" +  str(col[7]) + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +  str(col[10]) + "\t|" +  str(col[11]) + "\t|" +   "-"         + "\t|" +  "-"          + "\t|" +  "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[17]) + "\t|" + str(col[18]) + "\t|" + str(col[19]) + "\t|" + str(col[20]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[24]) + "\t|" + str(col[25]) + "\t|" + str(col[26]) + "\t|" + str(col[27]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          +"\n"  
#print column_header[3] + "\t|" + "-"         + "\t|" + str(col[1]) + "\t|" + str(col[2]) + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + str(col[6]) + "\t|" +  str(col[7]) + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +   "-"         + "\t|" +   "-"         + "\t|" +   "-"         + "\t|" +  str(col[13]) + "\t|" +  str(col[14]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[18]) + "\t|" + str(col[19]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[22]) + "\t|" + str(col[23]) + "\t|" + "-"          + "\t|" + str(col[25]) + "\t|" + "-"          + "\t|" + str(col[27]) + "\t|" + str(col[28]) + "\t|" + "-"          + "\t|" + str(col[30]) +"\n" 
#print column_header[4] + "\t|" + "-"         + "\t|" + "-"         + "\t|" + str(col[2]) + "\t|" + str(col[3]) + "\t|" + "-"         + "\t|" + str(col[5]) + "\t|" + str(col[6]) + "\t|" +  "-"         + "\t|" +  str(col[8]) + "\t|" +   "-"        + "\t|" +   "-"         + "\t|" +  str(col[11]) + "\t|" +  str(col[12]) + "\t|" +  str(col[13]) + "\t|" +  "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[19]) + "\t|" + str(col[20]) + "\t|" + str(col[21]) + "\t|" + str(col[22]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[26]) + "\t|" + str(col[27]) + "\t|" + str(col[28]) + "\t|" + str(col[29]) + "\t|" + "-"          +"\n"

fig, ax = plt.subplots()

#Title
plt.title('Linear Venn Diagram : 5 ways')
# width of each column
col_length = []
col_length = [(x/total)*100 for x in col]
# starting coords of each column
col_coord = []
col_coord = list(partial_sums(col_length))
# starting coords for length labels
col_coord_label = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
col_coord_label[0]= col_length[0]/2
for i in range(1, 31):
   col_coord_label[i] = col_coord[i-1] + col_length[i]/2
# horizontal bar design
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]) ] , (4, 2), facecolors=('blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue','blue', 'blue', 'blue', 'blue','blue', 'blue', 'blue', 'blue', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white' ), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]) ] , (9, 2), facecolors=('white', 'white', 'white', 'white', 'white', 'white', 'white', 'white','red', 'red', 'red', 'red','red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'white', 'white', 'white', 'white', 'white', 'white', 'white' ), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]) ] , (14, 2), facecolors=('white', 'white', 'white', 'white', 'green', 'green', 'green', 'green','green', 'green', 'green', 'green','white', 'white', 'white', 'white', 'white', 'green', 'green', 'green', 'green', 'white', 'white', 'white', 'green', 'green', 'green', 'green', 'white', 'white', 'white' ), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]) ] , (19, 2), facecolors=('white', 'yellow', 'yellow', 'white', 'white', 'white', 'yellow', 'yellow','yellow', 'yellow', 'white', 'white','white', 'yellow', 'yellow', 'white', 'white', 'white', 'yellow', 'yellow', 'white', 'white', 'yellow', 'yellow', 'white', 'yellow', 'white', 'yellow', 'yellow', 'white', 'yellow' ), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]) ] , (24, 2), facecolors=('white', 'white', 'pink', 'pink', 'white', 'pink', 'pink', 'white','pink', 'white', 'white', 'pink','pink', 'pink', 'white', 'white', 'white', 'white', 'white', 'pink', 'pink', 'pink', 'pink', 'white', 'white', 'white', 'pink', 'pink', 'pink', 'pink', 'white' ), edgecolor = 'none')
# y axis limits
ax.set_ylim(0,30)
# x axis lmits
ax.set_xlim(0,100)
# y axis ticks coordinates
ax.set_yticks([5,10,15,20,25])
# y axis ticks name
ax.set_yticklabels(['setA-' + df.ix[:,0].name, 'setB-' + df.ix[:,1].name, 'setC-' + df.ix[:,2].name, 'setD-' + df.ix[:,3].name, 'setE-' + df.ix[:,4].name])
# add y grid a designed location
ax.set_xticks([col_coord[0], col_coord[1], col_coord[2], col_coord[3], col_coord[4], col_coord[5], col_coord[6], col_coord[7], col_coord[8], col_coord[9], col_coord[10], col_coord[11], col_coord[12], col_coord[13], col_coord[14],col_coord[15], col_coord[16], col_coord[17], col_coord[18], col_coord[19], col_coord[20], col_coord[21], col_coord[22], col_coord[23], col_coord[24], col_coord[25], col_coord[26], col_coord[27], col_coord[28], col_coord[29], col_coord[30]], minor=True)
ax.xaxis.grid(True, which='minor')
#ax.xaxis.grid(True)
ax.set_xticklabels([])
# remove x axis ticks
ax.xaxis.set_tick_params(size=0)
ax.yaxis.set_tick_params(size=0)
# print label of each column length
for i in range(31):
    if col[i] != 0:
        ax.annotate(col[i], xy=(col_coord_label[i],0.2), fontsize = 5)
plt.tight_layout()

plt.show()
# printing the graphic into a pdf file
#pp = PdfPages('/home/mon13m/Data/Linear_venn_diagramm/Venn_tool/list_tabular_5way.pdf')
#pp.savefig(fig)
#pp.close()
