import os
# -*- coding: utf-8 -*-  
def deleteip(tfile,sstr):
    try:

        lines=open(tfile,'r').readlines()

        flen=len(lines)-1

        for i in range(flen):

            if sstr in lines[i]:

                lines[i]=''

        open(tfile,'w').writelines(lines)

        

    except Exception,e:

        print e

def getfilelist(filepath, tabnum=1):  
    simplepath = os.path.split(filepath)[1]  
    returnstr = simplepath+"目录<>"+"\n"  
    returndirstr = ""  
    returnfilestr = ""  
    filelist = os.listdir(filepath)  
    for num in range(len(filelist)):  
        filename=filelist[num]  
        if os.path.isdir(filepath+"/"+filename):  
            returndirstr += "\t"*tabnum+getfilelist(filepath+"/"+filename, tabnum+1)  
        else:  
            returnfilestr += "\t"*tabnum+filename+"\n"
            print filepath+"/"+filename
            deleteip(filepath+"/"+filename,'add-resource')
    returnstr += returnfilestr+returndirstr  
    return returnstr+"\t"*tabnum+"</>\n"  

#deleteip('/home/li/android/LetvAccount_Simple/mylibrary/src/main/res/values/le_dimens.xml','add-resource')

getfilelist('/home/li/android/LetvAccount_Simple/mylibrary/src/main/res')