
# coding: utf-8

# In[1]:


proj1 = './proj01.ged'
proj2 = './proj02test.ged'


# In[2]:


tag_level0 = {'HEAD','TRLR','NOTE'}
tag_level1 = {'NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV'}
tag_level2 = {'DATE'}
tag_exception = {'INDI', 'FAM'}
wrong_tagid = {'id'}


def isvalid_level(l):
    if l[0] == '0' and l[1] in tag_level0:
        return True
    if l[0] == '1' and l[1] in tag_level1:
        return True
    if l[0] == '2' and l[1] in tag_level2:
        return True
    else:
        return False

    
def isvalid_order(l):
    if l[0] == '0' and l[2] in tag_exception:
        return True

    
def rest_list(a):
    x = ''
    for i in a:
        x += i + ' '
    return x


# In[3]:


with open(proj2) as f:
    lines = f.readlines()
    for line in lines:
        tmp = []
        print("--> " + line.strip())
        for word in line.split():
            tmp.append(word)
#         print(tmp)
        if isvalid_level(tmp):
            print("<-- " + tmp[0] + "|" + tmp[1] + "|" + 'Y' + "|" + rest_list(tmp[2:]))
        elif len(tmp) >= 3 and isvalid_order(tmp):
            print("<-- " + tmp[0] + "|" + tmp[2] + "|" + 'Y' + "|" + tmp[1])
        else:
            print("<-- " + tmp[0] + "|" + tmp[1] + "|" + 'N' + "|" + rest_list(tmp[2:]))
            


# In[ ]:




