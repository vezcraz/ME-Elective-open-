from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import re
from io import BytesIO as IO
import xlsxwriter 
def getPref(request):
    final=pd.DataFrame()
    #The script doesn't work if the models are not refreshed. 
    #That's why objectCode and this header should be always be put here instead of top
    from users.models import Student_Info as students
    #encodeed all the types in a map
    full= students.objects.all()
    for x in full:
        temp={}
        temp['ID']=x.Identity
        temp['Name']=x.name
        pref_list=x.p.split('**')
        for preference in pref_list:
            if preference!='':
                print(preference.split('|'))
                pno=preference.split('|')[0]
                opn=preference.split('|')[-1]
                temp[pno]=opn
        print(temp)
        final=final.append(temp, ignore_index=True)
        print(final)
    filename="ME_Elective_Preferences"
    response=download(final,filename)
    #reset global vars
    final=pd.DataFrame() 
    return response

def download(final,filename):
    #final is the dataframe that contains all the details of the students approved by the hod
    excel_file=IO() #create a io memory stream
    xlwriter=pd.ExcelWriter(excel_file,engine='xlsxwriter') #xlsxwriter is a requirement
    final.to_excel(xlwriter, f'{filename}', index=False) #chosen the sheetname to be the same as filename
    xlwriter.save()
    xlwriter.close()
    excel_file.seek(0) #place the pointer at the start of the file
    response=HttpResponse(excel_file.read(),content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition']=f'attachment; filename={filename}.xlsx' #makes an http file response of the excel
    print(final) #for debugging
    
    return response
