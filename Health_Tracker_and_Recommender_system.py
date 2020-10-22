#!/usr/bin/env python
# coding: utf-8

# In[5]:


from covid import Covid #Ctrl + r then pip install Covid
import operator
import matplotlib.pyplot as plt #Ctrl +r then pip install matplotlib
covid = Covid()
x=str(input("Enter country name"))
y=covid.get_status_by_country_name(x)
data1=[]
data2=[]
for x in y:
  data1.append(y[x])
for x in y.keys():
    data2.append(x)
a=data1[2:6]
b=data2[2:6]
new = dict(zip(b, a))
print(new)
new_d = sorted(new.items(), key=operator.itemgetter(1))
di={}
for a, b in new_d:
     di.setdefault(a, []).append(b)
keys_values = di.items()
new_d2 = {str(key): str(value) for key, value in keys_values }
keys =new_d2.keys()
values = new_d2.values()
plt.bar(keys,values)
plt.show()

from tkinter import *
def plot():
    from covid import Covid
    import operator
    import matplotlib.pyplot as plt
    covid = Covid()
    y=covid.get_status_by_country_name(countryent.get())
    data1=[]
    data2=[]
    for x in y:
      data1.append(y[x])
    for x in y.keys():
        data2.append(x)
    a=data1[2:6]
    b=data2[2:6]
    new = dict(zip(b, a))
    new_d = sorted(new.items(), key=operator.itemgetter(1))
    di={}
    for a, b in new_d:
         di.setdefault(a, []).append(b)
    keys_values = di.items()
    new_d2 = {str(key): str(value) for key, value in keys_values}
    keys =new_d2.keys()
    values = new_d2.values()
    plt.bar(keys,values)
    plt.show()

root=Tk()
frame2=Frame(root,borderwidth=2,relief=SUNKEN,bg="lightblue")
frame2.grid(padx=23,pady=55)
Label(frame2,text="Health tracker",font="helvatica 25",bg="grey",fg="blue").grid(row=0)
Label(frame2,text="Enter country name whose data you want to find.",font="helvatica 25 ",fg="blue",bg="grey").grid(pady=45)
countryval=StringVar(value='Enter country name here! and click on the button given below')
countryent=Entry(frame2,textvariable=countryval,width=50,font="45",borderwidth=6,fg="blue",bg="grey",insertbackground="green")
countryent.grid()
Button(frame2,text="click",command=plot,fg="blue",bg="grey").grid(pady=10)
root.mainloop()


