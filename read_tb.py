import json
from pprint import pprint
import pandas as pd 

############################### Transfer models ##############################
### Rewards
with open('run1_reward.json') as f:
    run1 = json.load(f)
run1 = pd.DataFrame(run1)

with open('run2_reward.json') as g:
    run2 = json.load(g)
run2 = pd.DataFrame(run2)

with open('run3_reward.json') as h:
    run3 = json.load(h)
run3 = pd.DataFrame(run3)

#combine rewards
run_summary = pd.concat([run1.iloc[:,2],run2.iloc[:,2],run3.iloc[:,2]],axis=1,join_axes=[run1.iloc[:,1]])
run_summary.to_csv('reward_transfer_model.csv')
###combine q
with open('run1_avg_max_q.json') as f:
    run1q = json.load(f)
run1q = pd.DataFrame(run1q)

with open('run2_max_avg_q.json') as g:
    run2q = json.load(g)
run2q = pd.DataFrame(run2q)

with open('run3_max_avg_q.json') as h:
    run3q = json.load(h)
run3q = pd.DataFrame(run3q)

#combine q
run_q = pd.concat([run1q.iloc[:,2],run2q.iloc[:,2],run3q.iloc[:,2]],axis=1,join_axes=[run1q.iloc[:,1]])
run_q.to_csv('run_q.csv')

###combine loss
with open('run1_loss.json') as f:
    run1loss = json.load(f)
run1loss= pd.DataFrame(run1loss)

with open('run2_avg_loss.json') as g:
    run2loss = json.load(g)
run2loss = pd.DataFrame(run2loss)

with open('run3_loss.json') as h:
    run3loss = json.load(h)
run3loss = pd.DataFrame(run3loss)

#combine q
run_loss = pd.concat([run1loss.iloc[:,2],run2loss.iloc[:,2],run3loss.iloc[:,2]],axis=1,join_axes=[run1loss.iloc[:,1]])
run_loss.to_csv('run_loss.csv')

############################### New Model models ##############################
### Rewards

with open('run1_new_reward.json') as f:
    run1 = json.load(f)
run1 = pd.DataFrame(run1)

with open('run2_new_reward.json') as g:
    run2 = json.load(g)
run2 = pd.DataFrame(run2)

with open('run3_new_reward.json') as h:
    run3 = json.load(h)
run3 = pd.DataFrame(run3)

#combine rewards
run_summary = pd.concat([run1.iloc[:,2],run2.iloc[:,2],run3.iloc[:,2]],axis=1,join_axes=[run1.iloc[:,1]])
run_summary.to_csv('reward_new_model.csv')

###combine q
with open('run1_new_maxq.json') as f:
    run1q = json.load(f)
run1q = pd.DataFrame(run1q)

with open('run2_new_maxq.json') as g:
    run2q = json.load(g)
run2q = pd.DataFrame(run2q)

with open('run3_new_maxq.json') as h:
    run3q = json.load(h)
run3q = pd.DataFrame(run3q)

#combine q
run_q = pd.concat([run1q.iloc[:,2],run2q.iloc[:,2],run3q.iloc[:,2]],axis=1,join_axes=[run1q.iloc[:,1]])
run_q.to_csv('run_new_q.csv')


###combine loss
with open('run1_new_loss.json') as f:
    run1q = json.load(f)
run1q = pd.DataFrame(run1q)

with open('run2_new_loss.json') as g:
    run2q = json.load(g)
run2q = pd.DataFrame(run2q)

with open('run2_new_loss.json') as h:
    run3q = json.load(h)
run3q = pd.DataFrame(run3q)

#combine q
run_q = pd.concat([run1q.iloc[:,2],run2q.iloc[:,2],run3q.iloc[:,2]],axis=1,join_axes=[run1q.iloc[:,1]])
run_q.to_csv('run_new_loss.csv')