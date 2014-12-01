# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 19:49:49 2014

@author: Israel
"""
# import package
from assgn8.invest import *

# set inputs
input_positions=[1,10,100,1000]
input_trials=10000

# gamble :)
results = invest(input_positions,input_trials)

# calculate summary stats
means=DataFrame(results.mean(),columns=["Mean by Position"])
stddev=DataFrame(results.std(),columns=["Std Dev by Position"])

# write summary stats to results.txt
f = open('results.txt','w')
f.write(str(means))
f.write('\n')
f.write('\n')
f.write(str(stddev))
f.flush()
f.close()

# plots
for p in input_positions:
 label = "%04d" % (p,)
 plt.figure(p)
 plt.hist(np.array(results[p]),100,range=[-1,1])
 plt.title(str(p)+" Positions")
 plt.xlabel('Daily Return')
 plt.plot()
 plt.savefig('histogram_'+label+'_pos.pdf')
