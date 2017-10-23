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
df = pd.read_csv('/home/mon13m/Data/Linear_venn_diagramm/Venn_tool/list_tabular_4way_SH.csv', sep='\t')

########################### CORE #####################################
# remove the nans with dropna() and convert each column into a set
setA = set(df.ix[:,0].dropna())
setB = set(df.ix[:,1].dropna())
setC = set(df.ix[:,2].dropna())
setD = set(df.ix[:,3].dropna())

# initialization
col = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# column1 : in A not in B not in C not in D
col[0], setAonly = logic( [setA], [setB, setC, setD] )
# column2 : in A not in B not in C in D
col[1], setAD = logic( [setA, setD], [setB, setC] )
# column3 : in A not in B in C not in D
col[2], setAC = logic( [setA, setC], [setB, setD] )
# column4 : in A not in B in C in D
col[3], setACD = logic( [setA, setC, setD], [setB] )
# column5 : not in A not in B not in C in D
col[4], setDonly = logic( [setD], [setB, setA, setC] ) 
# column6 : not in A not in B in C in D
col[5], setCD = logic( [setC, setD], [setB, setA ] )  
# column7 : not in A not in B in C not in D
col[6], setConly = logic( [setC], [setB, setA , setD] )
# column8 : not in A in B in C not in D
col[7], setBC = logic( [setB, setC], [setA , setD] )       
# column9 : not in A in B in C in D
col[8], setBCD = logic( [setB, setC, setD], [setA] )      
# column10 : in A in B in C in D
col[9], setABCD = logic( [setA, setB, setC, setD])
# column11 : in A in B in C not in D
col[10], setABC = logic( [setA, setB, setC], [setD]) 
# column12 : in A in B not in C not in D
col[11], setAB = logic( [setA, setB], [setD, setC]) 
# column13 : in A in B not in C in D
col[12], setABD = logic( [setA, setB, setD], [setC])         
# column14 : not in A in B not in C in D
col[13], setBD = logic( [setB, setD], [setA, setC])         
# column15 : not in A in B not in C not in D
col[14], setBonly = logic( [setB], [setA, setC, setD])   

#  number of observation, non redundant (if shared counted only once)
total = col[0] + col[1] + col[2] + col[3] + col[4] + col[5] + col[6] + col[7] + col[8] + col[9] + col[10] + col[11] + col[12] + col[13] + col[14] 
#print total

# dataframe creation for list output printing
data = [list(setAonly), list(setAD), list(setAC), list(setACD), list(setDonly), list(setCD), list(setConly), list(setBC), list(setBCD), list(setABCD), list(setABC), list(setAB), list(setABD), list(setBD), list(setBonly)]
header = ['setAonly', 'setAD', 'setAC', 'setACD', 'setDonly', 'setCD', 'setConly','setBC', 'setBCD', 'setABCD', 'setABC', 'setAB', 'setABD','setBD', 'setBonly']
df_out = pd.DataFrame(data, index = header)
# Transposition needed
df2 = df_out.T


########################## OUTPUT ################################

# printing out csv files
df2.to_csv('/home/mon13m/Data/Linear_venn_diagramm/Venn_tool/list_tabular_4way_lists_SH.csv', sep='\t')


# Printing test
#print df.ix[:,0].name + "\t|" + str(col[0]) + "\t|" + str(col[1]) + "\t|" + str(col[2]) + "\t|" + str(col[3]) + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" +  "-"         + "\t|" +  "-"         + "\t|" +  str(col[9]) + "\t|" +  str(col[10]) + "\t|" +  str(col[11]) + "\t|" +  str(col[12]) + "\t|" +  "-"          + "\t|" +  "-"          + "\n"
#print df.ix[:,1].name + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" +  str(col[7]) + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +  str(col[10]) + "\t|" +  str(col[11]) + "\t|" +  str(col[12]) + "\t|" +  str(col[13]) + "\t|" +  str(col[14]) + "\n"
#print df.ix[:,2].name + "\t|" + "-"         + "\t|" + "-"         + "\t|" + str(col[2]) + "\t|" + str(col[3]) + "\t|" + "-"         + "\t|" + str(col[5]) + "\t|" + str(col[6]) + "\t|" +  str(col[7]) + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +  str(col[10]) + "\t|" +   "-"         + "\t|" +   "-"         + "\t|" +  "-"          + "\t|" +  "-"          + "\n"
#print df.ix[:,3].name + "\t|" + "-"         + "\t|" + str(col[1]) + "\t|" + "-"         + "\t|" + str(col[3]) + "\t|" + str(col[4]) + "\t|" + str(col[5]) + "\t|" + "-"         + "\t|" +  "-"         + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +   "-"         + "\t|" +   "-"         + "\t|" +  str(col[12]) + "\t|" +  str(col[13]) + "\t|" +  "-"          + "\n"

fig, ax = plt.subplots()

#Title
plt.title('Linear Venn Diagram : 4 ways')
# width of each column
col_length = []
col_length = [(x/total)*100 for x in col]
# starting coords of each column
col_coord = []
col_coord = list(partial_sums(col_length))
# starting coords for length labels
col_coord_label = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
col_coord_label[0]= col_length[0]/2
for i in range(1, 15):
   col_coord_label[i] = col_coord[i-1] + col_length[i]/2
# horizontal bar design
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]) ] , (4, 2), facecolors=('blue', 'blue', 'blue', 'blue', 'white', 'white', 'white', 'white', 'white', 'blue', 'blue', 'blue', 'blue', 'white', 'white' ), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]) ] , (9, 2), facecolors=('white', 'white', 'white', 'white', 'white', 'white', 'white', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red' ), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]) ] , (14, 2), facecolors=('white', 'white', 'green', 'green', 'white', 'green', 'green', 'green', 'green', 'green', 'green', 'white', 'white', 'white', 'white' ), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]) ] , (19, 2), facecolors=('white', 'yellow', 'white', 'yellow', 'yellow', 'yellow', 'white', 'white', 'yellow', 'yellow', 'white', 'white', 'yellow', 'yellow', 'white' ), edgecolor = 'none')
# y axis limits
ax.set_ylim(0,25)
# x axis lmits
ax.set_xlim(0,100)
# y axis ticks coordinates
ax.set_yticks([5,10,15,20])
# y axis ticks name
ax.set_yticklabels(['setA-' + df.ix[:,0].name,'setB-' +  df.ix[:,1].name,'setC-' +  df.ix[:,2].name,'setD-' +  df.ix[:,3].name])
# add y grid a designed location
ax.set_xticks([col_coord[0], col_coord[1], col_coord[2], col_coord[3], col_coord[4], col_coord[5], col_coord[6], col_coord[7], col_coord[8], col_coord[9], col_coord[10], col_coord[11], col_coord[12], col_coord[13], col_coord[14]], minor=True)
ax.xaxis.grid(True, which='minor')
ax.set_xticklabels([])
# remove x axis ticks
ax.xaxis.set_tick_params(size=0)
ax.yaxis.set_tick_params(size=0)
# print label of each column length
for i in range(15):
    if col[i] != 0:
        ax.annotate(col[i], xy=(col_coord_label[i],0.2), fontsize = 5)
plt.tight_layout()

#plt.show()

# printing the graphic into a pdf file
pp = PdfPages('/home/mon13m/Data/Linear_venn_diagramm/Venn_tool/list_tabular_4way_SH.pdf')
pp.savefig(fig)
pp.close()
