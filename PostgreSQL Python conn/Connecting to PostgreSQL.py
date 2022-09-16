#!/usr/bin/env python
# coding: utf-8

# ### import psycopg2

# In[2]:


#Connecting to a database


# In[3]:


hostname = ''
database = ''
username = ''
pwd = ''
port_id = 5432
conn = None
cur = None


# In[4]:


try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id

    )
    cur = conn.cursor()
    
    create_script = '''CREATE TABLE manager (
                            id   int PRIMARY KEY,
                            name varchar(40) NOT NULL
                             
    )
    '''
    
    cur.execute(create_script)
    
    
    conn.commit()
    
   
except Exception as error:
    print(error)
finally:
        if cur is not None:
             cur.close()
        if conn is not None:
             conn.close()
    


# In[ ]:





# In[ ]:




