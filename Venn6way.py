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
df = pd.read_csv('/home/mon13m/Data/Linear_venn_diagramm/Venn_tool/list_tabular_6way.csv', sep='\t')
########################### CORE #####################################
# remove the nans with dropna() and convert each column into a set
setA = set(df.ix[:,0].dropna())
setB = set(df.ix[:,1].dropna())
setC = set(df.ix[:,2].dropna())
setD = set(df.ix[:,3].dropna())
setE = set(df.ix[:,4].dropna())
setF = set(df.ix[:,5].dropna())


# initialization
col = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]



col[0], setFonly = logic( [setF], [setA, setB, setC, setD, setE] )
col[1], setCF = logic( [setC, setF], [setA, setB, setD, setE] )
col[2], setCEF = logic( [setC, setE, setF], [setA, setB, setD] )
col[3], setCDF = logic( [setC, setD, setF], [setA, setB, setE] )
col[4], setCDEF = logic( [setC, setD, setE, setF], [setA, setB] )
col[5], setDF = logic( [setD, setF], [setA, setB, setC, setE] ) 
col[6], setDEF = logic( [setD, setE, setF], [setA, setB, setC] )
col[7], setEF = logic( [setE, setF], [setA, setB, setC, setD] )        
col[8], setEonly = logic( [setE], [setA, setB, setC, setD, setF] )    
col[9], setDE = logic( [setD, setE], [setA, setB, setC, setF] )
col[10], setDonly = logic( [setD], [setA, setB, setC, setE, setF] ) 
col[11], setCD = logic( [setC, setD], [setA, setB, setF, setE] )
col[12], setCDE = logic( [setC, setD, setE], [setA, setB, setF] )       
col[13], setCE = logic( [setC, setE], [setA, setB, setF, setD] )        
col[14], setConly = logic( [setC], [setA, setB, setE, setD, setF] )   
col[15], setAC = logic( [setA, setC], [setB, setD, setE, setF] )
col[16], setACE = logic( [setA, setC, setE], [setB, setD, setF] ) 
col[17], setACDE = logic( [setA, setC, setD, setE], [setF, setB] )
col[18], setACD = logic( [setA, setC, setD], [setB, setE, setF] ) 
col[19], setAD = logic( [setA, setD], [setB, setC, setE, setF] )
col[20], setADE = logic( [setA, setD, setE], [setB, setC, setF] ) 
col[21], setACDEF = logic( [setA, setC, setD, setE, setF], [setB] )
col[22], setADEF = logic( [setA, setD, setE, setF], [setC, setB] ) 
col[23], setAE = logic( [setA, setE], [setB, setC, setD, setF] )
col[24], setAEF = logic( [setA, setF, setE], [setB, setC, setD] )
col[25], setADF = logic( [setA, setF, setD], [setB, setC, setE] ) 
col[26], setACDF = logic( [setA, setD, setC, setF], [setE, setB] ) 
col[27], setACEF = logic( [setA, setE, setC, setF], [setD, setB] ) 
col[28], setACF = logic( [setA, setF, setC], [setB, setD, setE] ) 
col[29], setAF = logic( [setA, setF], [setB, setC, setD, setE] ) 
col[30], setAonly = logic( [setA], [setE, setB, setC, setD, setF] ) 
col[31], setABF = logic( [setA, setF, setB], [setE, setC, setD] )
col[32], setABCEF = logic( [setA, setC, setB, setE, setF], [setD] )
col[33], setABCF = logic( [setA, setB, setC, setF], [setD, setE] )
col[34], setABCDF = logic( [setA, setC, setB, setD, setF], [setE] )
col[35], setABDF = logic( [setA, setB, setD, setF], [setC, setE] )
col[36], setABEF = logic( [setA, setB, setE, setF], [setC, setD] )
col[37], setABDEF = logic( [setA, setE, setB, setD, setF], [setC] )
col[38], setABCDEF = logic( [setA, setC, setB, setD, setE, setF])
col[39], setABCDE = logic( [setA, setE, setB, setD, setC], [setF] )
col[40], setABDE = logic( [setA, setB, setE, setD], [setC, setF] )
col[41], setABE = logic( [setA, setE, setB], [setF, setC, setD] )
col[42], setABD = logic( [setA, setD, setB], [setF, setC, setE] )
col[43], setABCD = logic( [setA, setB, setC, setD], [setE, setF] )
col[44], setABC = logic( [setA, setC, setB], [setF, setD, setE] )
col[45], setABCE = logic( [setA, setB, setE, setC], [setD, setF] )
col[46], setAB = logic( [setA, setB], [setF, setC, setD, setE] ) 
col[47], setBC = logic( [setC, setB], [setF, setA, setD, setE] ) 
col[48], setBCE = logic( [setE, setC, setB], [setF, setD, setA] )
col[49], setBCDE = logic( [setD, setB, setE, setC], [setA, setF] )
col[50], setBCD = logic( [setD, setC, setB], [setF, setE, setA] )
col[51], setBD = logic( [setD, setB], [setF, setA, setC, setE] ) 
col[52], setBDE = logic( [setE, setD, setB], [setF, setC, setA] )
col[53], setBE = logic( [setE, setB], [setF, setA, setC, setD] )
col[54], setBonly = logic( [setB], [setE, setA, setC, setD, setF] ) 
col[55], setBDEF = logic( [setD, setB, setE, setF], [setA, setC] )
col[56], setBEF = logic( [setE, setF, setB], [setD, setC, setA] )
col[57], setBF = logic( [setF, setB], [setE, setA, setC, setD] )
col[58], setBCF = logic( [setF, setC, setB], [setE, setD, setA] )
col[59], setBCDF = logic( [setD, setB, setC, setF], [setA, setE] )
col[60], setBCDEF = logic( [setF, setE, setB, setD, setC], [setA] )
col[61], setBCEF = logic( [setC, setB, setE, setF], [setA, setD] )


#  number of observation, non redundant (if shared counted only once)
total = col[0] + col[1] + col[2] + col[3] + col[4] + col[5] + col[6] + col[7] + col[8] + col[9] + col[10] + col[11] + col[12] + col[13] + col[14] + col[15] + col[16] + col[17] + col[18] + col[19] + col[20] + col[21] + col[22] + col[23] + col[24] + col[25] + col[26] + col[27]  + col[28] + col[29] + col[30] + col[31] + col[32] + col[33] + col[34] + col[35] + col[36] + col[37] + col[38] + col[39] + col[40] + col[41] + col[42] + col[43] + col[44] + col[45] + col[46] + col[47] + col[48] + col[49] + col[50] + col[51] + col[52] + col[53] + col[54] + col[55] + col[56] + col[57] + col[58] + col[59]  + col[60] + col[61]
#print total
# dataframe creation for list output printing
data = [list(setFonly), list(setCF), list(setCEF), list(setCDF), list(setCDEF), list(setDF), list(setDEF), list(setEF), list(setEonly), list(setDE), list(setDonly), list(setCD), list(setCDE), list(setCE), list(setConly), list(setAC), list(setACE), list(setACDE), list(setACD), list(setAD), list(setADE), list(setACDEF), list(setADEF), list(setAE), list(setAEF), list(setADF), list(setACDF), list(setACEF), list(setACF), list(setAF), list(setAonly), list(setABF), list(setABCEF), list(setABCF), list(setABCDF), list(setABDF), list(setABEF), list(setABDEF), list(setABCDEF), list(setABCDE), list(setABDE), list(setABE), list(setABD), list(setABCD), list(setABC), list(setABCE), list(setAB), list(setBC), list(setBCE), list(setBCDE), list(setBCD), list(setBD), list(setBDE), list(setBE), list(setBonly), list(setBDEF), list(setBEF), list(setBF), list(setBCF), list(setBCDF), list(setBCDEF), list(setBCEF)]
header = ['setFonly', 'setCF', 'setCEF', 'setCDF', 'setCDEF', 'setDF', 'setDEF', 'setEF', 'setEonly', 'setDE', 'setDonly', 'setCD', 'setCDE', 'setCE', 'setConly', 'setAC', 'setACE', 'setACDE', 'setACD', 'setAD', 'setADE', 'setACDEF', 'setADEF', 'setAE', 'setAEF', 'setADF', 'setACDF', 'setACEF', 'setACF', 'setAF', 'setAonly', 'setABF', 'setABCEF', 'setABCF', 'setABCDF', 'setABDF', 'setABEF', 'setABDEF', 'setABCDEF', 'setABCDE', 'setABDE', 'setABE', 'setABD', 'setABCD', 'setABC', 'setABCE', 'setAB', 'setBC', 'setBCE', 'setBCDE', 'setBCD', 'setBD', 'setBDE', 'setBE', 'setBonly', 'setBDEF', 'setBEF', 'setBF', 'setBCF', 'setBCDF', 'setBCDEF', 'setBCEF']
df_out = pd.DataFrame(data, index = header)
# Transposition needed
df2 = df_out.T

########################## OUTPUT ################################
# printing out csv files
#df2.to_csv('/home/mon13m/Data/Linear_venn_diagramm/Venn_tool/list_tabular_6way_lists.csv', sep='\t')
df2.to_csv('/home/mon13m/Data/Linear_venn_diagramm/Venn_tool/list_tabular_6way_lists.csv', sep='\t')

### OUTPUT
# Printing test
#print column_header[0] + "\t|" + str(col[0]) + "\t|" + str(col[1]) + "\t|" + str(col[2]) + "\t|" + str(col[3]) + "\t|" + str(col[4]) + "\t|" + str(col[5]) + "\t|" + str(col[6]) + "\t|" +  str(col[7]) + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +  str(col[10]) + "\t|" +  str(col[11]) + "\t|" +  str(col[12]) + "\t|" +  str(col[13]) + "\t|" +  str(col[14]) + "\t|" + str(col[15]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          +"\n" 
#print column_header[1] + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" +  "-"         + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +  str(col[10]) + "\t|" +  str(col[11]) + "\t|" +  str(col[12]) + "\t|" +  str(col[13]) + "\t|" +  str(col[14]) + "\t|" + str(col[15]) + "\t|" + str(col[16]) + "\t|" + str(col[17]) + "\t|" + str(col[18]) + "\t|" + str(col[19]) + "\t|" + str(col[20]) + "\t|" + str(col[21]) + "\t|" + str(col[22]) + "\t|" + str(col[23]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          +"\n"         
#print column_header[2] + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + str(col[4]) + "\t|" + str(col[5]) + "\t|" + str(col[6]) + "\t|" +  str(col[7]) + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +  str(col[10]) + "\t|" +  str(col[11]) + "\t|" +   "-"         + "\t|" +  "-"          + "\t|" +  "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[17]) + "\t|" + str(col[18]) + "\t|" + str(col[19]) + "\t|" + str(col[20]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[24]) + "\t|" + str(col[25]) + "\t|" + str(col[26]) + "\t|" + str(col[27]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          +"\n"  
#print column_header[3] + "\t|" + "-"         + "\t|" + str(col[1]) + "\t|" + str(col[2]) + "\t|" + "-"         + "\t|" + "-"         + "\t|" + "-"         + "\t|" + str(col[6]) + "\t|" +  str(col[7]) + "\t|" +  str(col[8]) + "\t|" +  str(col[9]) + "\t|" +   "-"         + "\t|" +   "-"         + "\t|" +   "-"         + "\t|" +  str(col[13]) + "\t|" +  str(col[14]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[18]) + "\t|" + str(col[19]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[22]) + "\t|" + str(col[23]) + "\t|" + "-"          + "\t|" + str(col[25]) + "\t|" + "-"          + "\t|" + str(col[27]) + "\t|" + str(col[28]) + "\t|" + "-"          + "\t|" + str(col[30]) +"\n" 
#print column_header[4] + "\t|" + "-"         + "\t|" + "-"         + "\t|" + str(col[2]) + "\t|" + str(col[3]) + "\t|" + "-"         + "\t|" + str(col[5]) + "\t|" + str(col[6]) + "\t|" +  "-"         + "\t|" +  str(col[8]) + "\t|" +   "-"        + "\t|" +   "-"         + "\t|" +  str(col[11]) + "\t|" +  str(col[12]) + "\t|" +  str(col[13]) + "\t|" +  "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[19]) + "\t|" + str(col[20]) + "\t|" + str(col[21]) + "\t|" + str(col[22]) + "\t|" + "-"          + "\t|" + "-"          + "\t|" + "-"          + "\t|" + str(col[26]) + "\t|" + str(col[27]) + "\t|" + str(col[28]) + "\t|" + str(col[29]) + "\t|" + "-"          +"\n"

fig, ax = plt.subplots()

#Title
plt.title('Linear Venn Diagram : 6 ways')
# width of each column
col_length = []
col_length = [(x/total)*100 for x in col]
# starting coords of each column
col_coord = []
col_coord = list(partial_sums(col_length))
# starting coords for length labels
col_coord_label = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
col_coord_label[0]= col_length[0]/2
for i in range(1, 62):
   col_coord_label[i] = col_coord[i-1] + col_length[i]/2
# horizontal bar design



ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]), (col_coord[30], col_length[31]), (col_coord[31], col_length[32]), (col_coord[32], col_length[33]), (col_coord[33], col_length[34]), (col_coord[34], col_length[35]), (col_coord[35], col_length[36]), (col_coord[36], col_length[37]), (col_coord[37], col_length[38]), (col_coord[38], col_length[39]), (col_coord[39], col_length[40]), (col_coord[40], col_length[41]), (col_coord[41], col_length[42]), (col_coord[42], col_length[43]), (col_coord[43], col_length[44]), (col_coord[44], col_length[45]), (col_coord[45], col_length[46]), (col_coord[46], col_length[47]), (col_coord[47], col_length[48]), (col_coord[48], col_length[49]), (col_coord[49], col_length[50]), (col_coord[50], col_length[51]), (col_coord[51], col_length[52]), (col_coord[52], col_length[53]), (col_coord[53], col_length[54]), (col_coord[54], col_length[55]), (col_coord[55], col_length[56]), (col_coord[56], col_length[57]), (col_coord[57], col_length[58]), (col_coord[58], col_length[59]), (col_coord[59], col_length[60]), (col_coord[60], col_length[61]) ] , (4, 2), facecolors=('white', 'white', 'white', 'white', 'white', 'white', 'white', 'white','white', 'white', 'white', 'white','white', 'white', 'white', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white','white', 'white', 'white', 'white','white', 'white', 'white' ), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]), (col_coord[30], col_length[31]), (col_coord[31], col_length[32]), (col_coord[32], col_length[33]), (col_coord[33], col_length[34]), (col_coord[34], col_length[35]), (col_coord[35], col_length[36]), (col_coord[36], col_length[37]), (col_coord[37], col_length[38]), (col_coord[38], col_length[39]), (col_coord[39], col_length[40]), (col_coord[40], col_length[41]), (col_coord[41], col_length[42]), (col_coord[42], col_length[43]), (col_coord[43], col_length[44]), (col_coord[44], col_length[45]), (col_coord[45], col_length[46]), (col_coord[46], col_length[47]), (col_coord[47], col_length[48]), (col_coord[48], col_length[49]), (col_coord[49], col_length[50]), (col_coord[50], col_length[51]), (col_coord[51], col_length[52]), (col_coord[52], col_length[53]), (col_coord[53], col_length[54]), (col_coord[54], col_length[55]), (col_coord[55], col_length[56]), (col_coord[56], col_length[57]), (col_coord[57], col_length[58]), (col_coord[58], col_length[59]), (col_coord[59], col_length[60]), (col_coord[60], col_length[61]) ] , (9, 2), facecolors=('white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red','red', 'red', 'red', 'red','red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red','red', 'red', 'red', 'red','red', 'red', 'red', 'red' ), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]), (col_coord[30], col_length[31]), (col_coord[31], col_length[32]), (col_coord[32], col_length[33]), (col_coord[33], col_length[34]), (col_coord[34], col_length[35]), (col_coord[35], col_length[36]), (col_coord[36], col_length[37]), (col_coord[37], col_length[38]), (col_coord[38], col_length[39]), (col_coord[39], col_length[40]), (col_coord[40], col_length[41]), (col_coord[41], col_length[42]), (col_coord[42], col_length[43]), (col_coord[43], col_length[44]), (col_coord[44], col_length[45]), (col_coord[45], col_length[46]), (col_coord[46], col_length[47]), (col_coord[47], col_length[48]), (col_coord[48], col_length[49]), (col_coord[49], col_length[50]), (col_coord[50], col_length[51]), (col_coord[51], col_length[52]), (col_coord[52], col_length[53]), (col_coord[53], col_length[54]), (col_coord[54], col_length[55]), (col_coord[55], col_length[56]), (col_coord[56], col_length[57]), (col_coord[57], col_length[58]), (col_coord[58], col_length[59]), (col_coord[59], col_length[60]), (col_coord[60], col_length[61]) ] , (14, 2), facecolors=('white', 'green', 'green' ,'green', 'green', 'white', 'white', 'white', 'white', 'white', 'white','green', 'green','green', 'green', 'green', 'green','green', 'green',  'white', 'white', 'green', 'white', 'white', 'white', 'white', 'white', 'green', 'green', 'green', 'white', 'white', 'white', 'green', 'green', 'green', 'white', 'white', 'white', 'green', 'green', 'white', 'white', 'white', 'green', 'green','green', 'white', 'green', 'green', 'green', 'green', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'green', 'green', 'green', 'green'), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]), (col_coord[30], col_length[31]), (col_coord[31], col_length[32]), (col_coord[32], col_length[33]), (col_coord[33], col_length[34]), (col_coord[34], col_length[35]), (col_coord[35], col_length[36]), (col_coord[36], col_length[37]), (col_coord[37], col_length[38]), (col_coord[38], col_length[39]), (col_coord[39], col_length[40]), (col_coord[40], col_length[41]), (col_coord[41], col_length[42]), (col_coord[42], col_length[43]), (col_coord[43], col_length[44]), (col_coord[44], col_length[45]), (col_coord[45], col_length[46]), (col_coord[46], col_length[47]), (col_coord[47], col_length[48]), (col_coord[48], col_length[49]), (col_coord[49], col_length[50]), (col_coord[50], col_length[51]), (col_coord[51], col_length[52]), (col_coord[52], col_length[53]), (col_coord[53], col_length[54]), (col_coord[54], col_length[55]), (col_coord[55], col_length[56]), (col_coord[56], col_length[57]), (col_coord[57], col_length[58]), (col_coord[58], col_length[59]), (col_coord[59], col_length[60]), (col_coord[60], col_length[61]) ] , (19, 2), facecolors=('white', 'white', 'white','yellow', 'yellow' ,'yellow', 'yellow', 'white', 'white', 'yellow', 'yellow','yellow', 'yellow', 'white', 'white', 'white', 'white' , 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'white', 'white', 'yellow', 'yellow', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'yellow','yellow', 'white', 'yellow', 'yellow', 'yellow', 'yellow', 'white', 'yellow', 'yellow', 'white', 'white', 'white', 'white', 'white', 'yellow', 'yellow', 'yellow', 'yellow', 'white', 'white', 'yellow', 'white', 'white', 'white', 'yellow', 'yellow', 'white'), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]), (col_coord[30], col_length[31]), (col_coord[31], col_length[32]), (col_coord[32], col_length[33]), (col_coord[33], col_length[34]), (col_coord[34], col_length[35]), (col_coord[35], col_length[36]), (col_coord[36], col_length[37]), (col_coord[37], col_length[38]), (col_coord[38], col_length[39]), (col_coord[39], col_length[40]), (col_coord[40], col_length[41]), (col_coord[41], col_length[42]), (col_coord[42], col_length[43]), (col_coord[43], col_length[44]), (col_coord[44], col_length[45]), (col_coord[45], col_length[46]), (col_coord[46], col_length[47]), (col_coord[47], col_length[48]), (col_coord[48], col_length[49]), (col_coord[49], col_length[50]), (col_coord[50], col_length[51]), (col_coord[51], col_length[52]), (col_coord[52], col_length[53]), (col_coord[53], col_length[54]), (col_coord[54], col_length[55]), (col_coord[55], col_length[56]), (col_coord[56], col_length[57]), (col_coord[57], col_length[58]), (col_coord[58], col_length[59]), (col_coord[59], col_length[60]), (col_coord[60], col_length[61]) ] , (24, 2), facecolors=('white', 'white', 'pink', 'white', 'pink', 'white','pink', 'pink', 'pink', 'pink', 'white', 'white', 'pink', 'pink', 'white', 'white', 'pink', 'pink', 'white', 'white', 'pink', 'pink', 'pink', 'pink', 'pink', 'white', 'white', 'white', 'white', 'pink', 'white', 'white', 'white', 'white', 'pink', 'pink', 'pink', 'pink', 'pink', 'pink', 'white', 'white', 'white', 'pink', 'white', 'white', 'pink', 'pink', 'white', 'white', 'pink', 'pink', 'white', 'pink', 'pink', 'white', 'white', 'white', 'pink', 'pink'  ), edgecolor = 'none')
ax.broken_barh([ (0, col_length[0]), (col_coord[0], col_length[1]), (col_coord[1], col_length[2]), (col_coord[2], col_length[3]), (col_coord[3], col_length[4]), (col_coord[4], col_length[5]), (col_coord[5], col_length[6]), (col_coord[6], col_length[7]), (col_coord[7], col_length[8]), (col_coord[8], col_length[9]), (col_coord[9], col_length[10]), (col_coord[10], col_length[11]), (col_coord[11], col_length[12]), (col_coord[12], col_length[13]), (col_coord[13], col_length[14]), (col_coord[14], col_length[15]), (col_coord[15], col_length[16]), (col_coord[16], col_length[17]), (col_coord[17], col_length[18]), (col_coord[18], col_length[19]), (col_coord[19], col_length[20]), (col_coord[20], col_length[21]), (col_coord[21], col_length[22]), (col_coord[22], col_length[23]), (col_coord[23], col_length[24]), (col_coord[24], col_length[25]), (col_coord[25], col_length[26]), (col_coord[26], col_length[27]), (col_coord[27], col_length[28]), (col_coord[28], col_length[29]), (col_coord[29], col_length[30]), (col_coord[30], col_length[31]), (col_coord[31], col_length[32]), (col_coord[32], col_length[33]), (col_coord[33], col_length[34]), (col_coord[34], col_length[35]), (col_coord[35], col_length[36]), (col_coord[36], col_length[37]), (col_coord[37], col_length[38]), (col_coord[38], col_length[39]), (col_coord[39], col_length[40]), (col_coord[40], col_length[41]), (col_coord[41], col_length[42]), (col_coord[42], col_length[43]), (col_coord[43], col_length[44]), (col_coord[44], col_length[45]), (col_coord[45], col_length[46]), (col_coord[46], col_length[47]), (col_coord[47], col_length[48]), (col_coord[48], col_length[49]), (col_coord[49], col_length[50]), (col_coord[50], col_length[51]), (col_coord[51], col_length[52]), (col_coord[52], col_length[53]), (col_coord[53], col_length[54]), (col_coord[54], col_length[55]), (col_coord[55], col_length[56]), (col_coord[56], col_length[57]), (col_coord[57], col_length[58]), (col_coord[58], col_length[59]), (col_coord[59], col_length[60]), (col_coord[60], col_length[61]) ] , (29, 2), facecolors=('black', 'black', 'black', 'black', 'black', 'black','black', 'black', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'black', 'black', 'white', 'black', 'black', 'black', 'black', 'black', 'black', 'white', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'black', 'black', 'black', 'black', 'black', 'black','black'), edgecolor = 'none')


# y axis limits
ax.set_ylim(0,35)
# x axis lmits
ax.set_xlim(0,100)
# y axis ticks coordinates
ax.set_yticks([5,10,15,20,25,30])
# y axis ticks name
ax.set_yticklabels(['setA-' + df.ix[:,0].name, 'setB-' + df.ix[:,1].name, 'setC-' + df.ix[:,2].name, 'setD-' + df.ix[:,3].name, 'setE-' + df.ix[:,4].name, 'setF-' + df.ix[:,5].name])
# add y grid a designed location
ax.set_xticks([col_coord[0], col_coord[1], col_coord[2], col_coord[3], col_coord[4], col_coord[5], col_coord[6], col_coord[7], col_coord[8], col_coord[9], col_coord[10], col_coord[11], col_coord[12], col_coord[13], col_coord[14], col_coord[15], col_coord[16], col_coord[17], col_coord[18], col_coord[19], col_coord[20], col_coord[21], col_coord[22], col_coord[23], col_coord[24], col_coord[25], col_coord[26], col_coord[27], col_coord[28], col_coord[29], col_coord[30], col_coord[31], col_coord[32], col_coord[33], col_coord[34], col_coord[35], col_coord[36], col_coord[37], col_coord[38], col_coord[39], col_coord[40], col_coord[41], col_coord[42], col_coord[43], col_coord[44], col_coord[45], col_coord[46], col_coord[47], col_coord[48], col_coord[49], col_coord[50], col_coord[51], col_coord[52], col_coord[53], col_coord[54], col_coord[55], col_coord[56], col_coord[57], col_coord[58], col_coord[59], col_coord[60], col_coord[61]], minor=True)
ax.xaxis.grid(True, which='minor')
#ax.xaxis.grid(True)
ax.set_xticklabels([])
# remove x axis ticks
ax.xaxis.set_tick_params(size=0)
ax.yaxis.set_tick_params(size=0)
# print label of each column length
for i in range(62):
    if col[i] != 0:
        ax.annotate(col[i], xy=(col_coord_label[i],0.2), fontsize = 5)
plt.tight_layout()

plt.show()
# printing the graphic into a pdf file
#pp = PdfPages('/home/mon13m/Data/Linear_venn_diagramm/Venn_tool/list_tabular_6way.pdf')
#pp.savefig(fig)
#pp.close()
