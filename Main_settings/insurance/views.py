from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage
# Create your views here.
import array as arr

def index(request):
    return render(request,'dashboard.html')

def maindashboardV(request):
    return render(request,'pages/maindashboard.html')

def admindashboardV(request):
    return render(request,'pages/admin/admindashboard.html')

def companyandbranchV(request):
    Coinfo=BranchInformationM.objects.all()[:1]
    return render(request,'pages/admin/forms/companyandbranch.html',{'Coinfo':Coinfo})

def CompanySaveV(request):

    if request.method == 'POST' and request.FILES:
        cname = request.POST.get('cname')
        names = request.POST.get('bname')
        addresss = request.POST.get('baddress')
        snames = request.POST.get('sname')
        phones = request.POST.get('pnumber')
        faxs = request.POST.get('fnumber')
        emails = request.POST.get('enumber')
        bcodes = request.POST.get('bcode')
        image = request.FILES['clogo']
        store = FileSystemStorage()
        filename = store.save(image.name, image)
        profile_pic_url = store.url(filename)
        data = BranchInformationM(Branch_Name=names, Address=addresss, Short_Name=snames, Phone=phones, Fax=faxs,
                                  Email=emails, Branch_Code=bcodes, BranchLogo=filename, Company_Name=cname)
        data.save()
        messages.info(request, 'Data Saved')
    else:
        cname = request.POST.get('cname')
        names = request.POST.get('bname')
        addresss = request.POST.get('baddress')
        snames = request.POST.get('sname')
        phones = request.POST.get('pnumber')
        faxs = request.POST.get('fnumber')
        emails = request.POST.get('enumber')
        bcodes = request.POST.get('bcode')
        data = BranchInformationM(Branch_Name=names, Address=addresss, Short_Name=snames, Phone=phones, Fax=faxs,
                                  Email=emails, Branch_Code=bcodes, Company_Name=cname)
        data.save()
        messages.info(request, 'Data Saved')

    Coinfo = BranchInformationM.objects.all()[:1]
    return render(request,'pages/admin/report/company.html',{'Coinfo':Coinfo})

    # return HttpResponse('abc')

import requests,json
import cx_Oracle
def UMP_APIV(request):
    cnx = cx_Oracle.connect('jashim/jashim@//localhost:1521/orcl')
    mycursor = cnx.cursor()
    mycursor.execute("BEGIN LOAD_MONEY_RECEIPT(); END;")
    mycursor.execute("""SELECT
        mrSerialNumber,                      
        officeBranchCode,                   
        officeBranchName,                   
        mrNumber,                          
        mrDate,                              
        classInsurance,                      
        insuredName,                         
        insuredAddress,                     
        insuredMobile,                       
        insuredEmail,                        
        modeOfPayment,                      
        paymentDetail ,                     
        coverNoteNumber,                  
        policyNumber,                
        addendumNumber,            
        endorsementNumber,                
        netPremium,                          
        vat,                                 
        stamp,                          
        others,                            
        totalPremium,                      
        chequeDrawnOn,                   
        chequeDate,                          
        depositDate,                      
        depositedToBank,                    
        depositedToBranch,                  
        depositedToAccountNumber,          
        mfs,                               
        mfsAccountNumber,                   
        isCoInsurance,                     
        isLeader,                            
        financingBankName,                  
        financingBankAddress,               
        financingBankEmail,                  
        financingBankMobile,                
        isMultiDocument,                    
        multiDocuments,                     
        currency,             
        leaderDocument,                     
        paymentReceivedFrom,                
        serviceCharge,                  
        coInsurerPremiumAmount,             
        bankGuaranteeNumber,                 
        requeston ,                         
        responseon,                          
        response,                            
        mrURL,                               
        umpStatus,                          
        depositStatus from ump_mr where umpStatus ='N'                
        """)
    myresults = mycursor.fetchall()
    # for (mrSerialNumber,
    #      officeBranchCode,
    #      officeBranchName,
    #      mrNumber,
    #      mrDate,
    #      classInsurance,
    #      insuredName,
    #      insuredAddress,
    #      insuredMobile,
    #      insuredEmail,
    #      modeOfPayment,
    #      paymentDetail,
    #      coverNoteNumber,
    #      policyNumber,
    #      addendumNumber,
    #      endorsementNumber,
    #      netPremium,
    #      vat,
    #      stamp,
    #      others,
    #      totalPremium,
    #      chequeDrawnOn,
    #      chequeDate,
    #      depositDate,
    #      depositedToBank,
    #      depositedToBranch,
    #      depositedToAccountNumber,
    #      mfs,
    #      mfsAccountNumber,
    #      isCoInsurance,
    #      isLeader,
    #      financingBankName,
    #      financingBankAddress,
    #      financingBankEmail,
    #      financingBankMobile,
    #      isMultiDocument,
    #      multiDocuments,
    #      currency,
    #      leaderDocument,
    #      paymentReceivedFrom,
    #      serviceCharge,
    #      coInsurerPremiumAmount,
    #      bankGuaranteeNumber,
    #      requeston,
    #      responseon,
    #      response,
    #      mrURL,
    #      umpStatus,
    #      depositStatus) in myresults:
    #     payload = {'client_id': 'paramount', 'client_secret': 'admin'}
    #     r = requests.post('https://idra-ump.com/test/app/extern/v1/authenticate', json=payload)
    #     access_para = json.loads(r.text)
    #     access_tokenpara = access_para['access_token']
    #     refresh_para = json.loads(r.text)
    #     refresh_tokenpara = refresh_para['refresh_token']
    #     token_para = json.loads(r.text)
    #     token_typepara = token_para['token_type']
    #     payloads = {"mrSerialNumber": mrSerialNumber,
    #                 "officeBranchCode": str(officeBranchCode),
    #                 "officeBranchName": officeBranchName,
    #                 "mrNumber": mrNumber,
    #                 "mrDate": mrDate,
    #                 "classInsurance": classInsurance,
    #                 "insuredName": insuredName,
    #                 "insuredAddress": insuredAddress,
    #                 "insuredMobile": insuredMobile,
    #                 "insuredEmail": insuredEmail,
    #                 "modeOfPayment": modeOfPayment,
    #                 "paymentDetail": paymentDetail,
    #                 "coverNoteNumber": coverNoteNumber,
    #                 "policyNumber": policyNumber,
    #                 "addendumNumber": addendumNumber,
    #                 "endorsementNumber": endorsementNumber,
    #                 "netPremium": netPremium,
    #                 "vat": vat,
    #                 "stamp": stamp,
    #                 "others": others,
    #                 "totalPremium": totalPremium,
    #                 "chequeDrawnOn": chequeDrawnOn,
    #                 "chequeDate": chequeDate,
    #                 "depositDate": depositDate,
    #                 "depositedToBank": depositedToBank,
    #                 "depositedToBranch": depositedToBranch,
    #                 "depositedToAccountNumber": depositedToAccountNumber,
    #                 "mfs": mfs,
    #                 "mfsAccountNumber": mfsAccountNumber,
    #                 "isCoInsurance": isCoInsurance,
    #                 "isLeader": isLeader,
    #                 "financingBankName": financingBankName,
    #                 "financingBankAddress": financingBankAddress,
    #                 "financingBankEmail": financingBankEmail,
    #                 "financingBankMobile": financingBankMobile,
    #                 "bankGuaranteeNumber": bankGuaranteeNumber,
    #                 "isMultiDocument": isMultiDocument,
    #                 "currency": currency,
    #                 "serviceCharge": serviceCharge,
    #                 "leaderDocument": leaderDocument,
    #                 "paymentReceivedFrom": paymentReceivedFrom,
    #                 "coInsurerPremiumAmount": coInsurerPremiumAmount,
    #                 "multiDocuments": multiDocuments}
    #
    #     print(payloads)
    return render(request,'pages/admin/api.html',{'myresults':myresults})



def UMP_APIsV(request):
    mr=request.POST.getlist('vehicle1')
    cnx = cx_Oracle.connect('jashim/jashim@//localhost:1521/orcl')
    mycursor = cnx.cursor()
    mycursor.execute("BEGIN LOAD_MONEY_RECEIPT(); END;")
    c = min([len(mr)])
    for i in range(c):
        mycursor.execute("""SELECT
                mrSerialNumber,
                officeBranchCode,
                officeBranchName,
                mrNumber,
                mrDate,
                classInsurance,
                insuredName,
                insuredAddress,
                insuredMobile,
                insuredEmail,
                modeOfPayment,
                paymentDetail ,
                coverNoteNumber,
                policyNumber,
                addendumNumber,
                endorsementNumber,
                netPremium,
                vat,
                stamp,
                others,
                totalPremium,
                chequeDrawnOn,
                chequeDate,
                depositDate,
                depositedToBank,
                depositedToBranch,
                depositedToAccountNumber,
                mfs,
                mfsAccountNumber,
                isCoInsurance,
                isLeader,
                financingBankName,
                financingBankAddress,
                financingBankEmail,
                financingBankMobile,
                isMultiDocument,
                multiDocuments,
                currency,
                leaderDocument,
                paymentReceivedFrom,
                serviceCharge,
                coInsurerPremiumAmount,
                bankGuaranteeNumber,
                requeston ,
                responseon,
                response,
                mrURL,
                umpStatus,
                depositStatus from ump_mr where umpStatus ='N' and mrnumber in (:mr)
                """,[mr[i]])
        myresultss = mycursor.fetchall()
        for (mrSerialNumber,
             officeBranchCode,
             officeBranchName,
             mrNumber,
             mrDate,
             classInsurance,
             insuredName,
             insuredAddress,
             insuredMobile,
             insuredEmail,
             modeOfPayment,
             paymentDetail,
             coverNoteNumber,
             policyNumber,
             addendumNumber,
             endorsementNumber,
             netPremium,
             vat,
             stamp,
             others,
             totalPremium,
             chequeDrawnOn,
             chequeDate,
             depositDate,
             depositedToBank,
             depositedToBranch,
             depositedToAccountNumber,
             mfs,
             mfsAccountNumber,
             isCoInsurance,
             isLeader,
             financingBankName,
             financingBankAddress,
             financingBankEmail,
             financingBankMobile,
             isMultiDocument,
             multiDocuments,
             currency,
             leaderDocument,
             paymentReceivedFrom,
             serviceCharge,
             coInsurerPremiumAmount,
             bankGuaranteeNumber,
             requeston,
             responseon,
             response,
             mrURL,
             umpStatus,
             depositStatus) in myresultss:
            payload = {'client_id': 'paramount', 'client_secret': 'admin'}
            r = requests.post('https://idra-ump.com/test/app/extern/v1/authenticate', json=payload)
            access_para = json.loads(r.text)
            access_tokenpara = access_para['access_token']
            refresh_para = json.loads(r.text)
            refresh_tokenpara = refresh_para['refresh_token']
            token_para = json.loads(r.text)
            token_typepara = token_para['token_type']
            payloads = {"mrSerialNumber": mrSerialNumber,
                        "officeBranchCode": str(officeBranchCode),
                        "officeBranchName": officeBranchName,
                        "mrNumber": mrNumber,
                        "mrDate": mrDate,
                        "classInsurance": classInsurance,
                        "insuredName": insuredName,
                        "insuredAddress": insuredAddress,
                        "insuredMobile": insuredMobile,
                        "insuredEmail": insuredEmail,
                        "modeOfPayment": modeOfPayment,
                        "paymentDetail": paymentDetail,
                        "coverNoteNumber": coverNoteNumber,
                        "policyNumber": policyNumber,
                        "addendumNumber": addendumNumber,
                        "endorsementNumber": endorsementNumber,
                        "netPremium": netPremium,
                        "vat": vat,
                        "stamp": stamp,
                        "others": others,
                        "totalPremium": totalPremium,
                        "chequeDrawnOn": chequeDrawnOn,
                        "chequeDate": chequeDate,
                        "depositDate": depositDate,
                        "depositedToBank": depositedToBank,
                        "depositedToBranch": depositedToBranch,
                        "depositedToAccountNumber": depositedToAccountNumber,
                        "mfs": mfs,
                        "mfsAccountNumber": mfsAccountNumber,
                        "isCoInsurance": isCoInsurance,
                        "isLeader": isLeader,
                        "financingBankName": financingBankName,
                        "financingBankAddress": financingBankAddress,
                        "financingBankEmail": financingBankEmail,
                        "financingBankMobile": financingBankMobile,
                        "bankGuaranteeNumber": bankGuaranteeNumber,
                        "isMultiDocument": isMultiDocument,
                        "currency": currency,
                        "serviceCharge": serviceCharge,
                        "leaderDocument": leaderDocument,
                        "paymentReceivedFrom": paymentReceivedFrom,
                        "coInsurerPremiumAmount": coInsurerPremiumAmount,
                        "multiDocuments": multiDocuments}

            print(payloads)
            # try:
            #     ab = requests.post('https://idra-ump.com/test/app/extern/v1/money-receipt', json=payloads,headers={'Authorization': f"Bearer {access_tokenpara}"})
            #     print(ab.json())
            # except:
            #     print("data not error")
            mycursor.execute("update ump_mr set umpStatus='Y' where mrNumber =:mrNumber", [mr[i]])
            # cnx.commit()
            mycur = cnx.cursor()
            for x in range(c):
                mycur.execute("""SELECT
                        mrSerialNumber,
                        officeBranchCode,
                        officeBranchName,
                        mrNumber,
                        mrDate,
                        classInsurance,
                        insuredName,
                        insuredAddress,
                        insuredMobile,
                        insuredEmail,
                        modeOfPayment,
                        paymentDetail ,
                        coverNoteNumber,
                        policyNumber,
                        addendumNumber,
                        endorsementNumber,
                        netPremium,
                        vat,
                        stamp,
                        others,
                        totalPremium,
                        chequeDrawnOn,
                        chequeDate,
                        depositDate,
                        depositedToBank,
                        depositedToBranch,
                        depositedToAccountNumber,
                        mfs,
                        mfsAccountNumber,
                        isCoInsurance,
                        isLeader,
                        financingBankName,
                        financingBankAddress,
                        financingBankEmail,
                        financingBankMobile,
                        isMultiDocument,
                        multiDocuments,
                        currency,
                        leaderDocument,
                        paymentReceivedFrom,
                        serviceCharge,
                        coInsurerPremiumAmount,
                        bankGuaranteeNumber,
                        requeston ,
                        responseon,
                        response,
                        mrURL,
                        umpStatus,
                        depositStatus from ump_mr where umpStatus ='N' and mrnumber not in  (:mr)
                        """, [mr[x]])
                myresults = mycur.fetchall()
            return render(request,'pages/admin/apis.html',{'myresults':myresults})




