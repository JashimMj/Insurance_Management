from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import auth,messages
from django.core.files.storage import FileSystemStorage
# Create your views here.
import array as arr
from django.contrib import messages
import requests,json
import cx_Oracle
import datetime
## PDF CODE ###
from django.template.loader import get_template
from xhtml2pdf import pisa




companyName=BranchInformationM.objects.all()[:1]


def index(request):
    userprofile = UserProfileM.objects.filter(id=request.user.id)
    return render(request,'dashboard.html',{'companyName':companyName,'userprofile':userprofile})

def maindashboardV(request):
    userprofile = UserProfileM.objects.filter(id=request.user.id)
    cnx = cx_Oracle.connect('jashim/jashim@//localhost:1521/orcl')
    abc = cnx.cursor()
    abc.execute("""select count(*) as a from ump_mr where RESPONSE is null """)
    send = abc.fetchall()
    sended = cnx.cursor()
    sended.execute("""select count(*) as a from ump_mr where RESPONSE is not null """)
    previously=sended.fetchall()
    return render(request,'pages/maindashboard.html',{'companyName':companyName,'userprofile':userprofile,'send':send,'previously':previously})

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


def UMP_APIV(request):
    userprofile = UserProfileM.objects.filter(id=request.user.id)
    cnx = cx_Oracle.connect('jashim/jashim@//localhost:1521/orcl')
    mycursor = cnx.cursor()
    mycursor.execute("""BEGIN LOAD_MONEY_RECEIPT(); END;""")
    cnx.commit()
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
        depositStatus from ump_mr where RESPONSE is null
        """)
    myresults = mycursor.fetchall()

    return render(request,'pages/admin/api.html',{'myresults':myresults,'companyName':companyName,'userprofile':userprofile})



def UMP_APIsV(request):
    mr=request.POST.getlist('vehicle1')
    cnx = cx_Oracle.connect('jashim/jashim@//localhost:1521/orcl')
    mycursor = cnx.cursor()
    mycursor.execute("BEGIN LOAD_MONEY_RECEIPT(); END;")
    cnx.commit()
    c = min([len(mr)])
    for i in range(c):
        mycursor.execute("""SELECT
                mrSerialNumber,
                officeBranchCode,
                officeBranchName,
                mrNumber,
                to_char(mrDate, 'YYYY-MM-DD') as mrDate,
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
                to_char(chequeDate, 'YYYY-MM-DD') as chequeDate,
                to_char(depositDate, 'YYYY-MM-DD') as depositDate,
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
                depositStatus from ump_mr where mrnumber in (:mr)
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
            print(access_tokenpara)
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

            # print(payloads)
            try:
                ab = requests.post('https://idra-ump.com/test/app/extern/v1/money-receipt', json=payloads,headers={'Authorization': f"Bearer {access_tokenpara}"})
                print(ab.json())
                ur = json.loads(ab.text)
                mrur = ur["url"]
                mycursor.execute("update ump_mr set mrurl=:mrur where mrNumber =:mrNumber", [mrur,mr[i]])
                cnx.commit()
                mycursor.execute("update ump_mr set umpStatus='Y' where mrNumber =:mrNumber", [mr[i]])
                cnx.commit()
                mycursor.execute("update ump_mr set RESPONSE='Y' where mrNumber =:mrNumber and DEPOSITSTATUS ='N'",
                                 [mr[i]])
                cnx.commit()
                messages.info(request, "Data sended")
            except:
                messages.info(request,"Data Not sended")

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
                        depositStatus from ump_mr where RESPONSE is null
                        """)
                myresults = mycur.fetchall()
            return render(request,'pages/admin/apis.html',{'myresults':myresults})


def UMP_APIsendeV(request):
    userprofile = UserProfileM.objects.filter(id=request.user.id)

    return render(request,'pages/admin/forms/dashboard.html',{'userprofile':userprofile,'companyName':companyName})

def previouslysende(request):
    userprofile = UserProfileM.objects.filter(id=request.user.id)
    fromDate = request.POST.get('fdate')
    fdate = datetime.datetime.strptime(fromDate, '%Y-%m-%d')
    toDate = request.POST.get('tdate')
    tdate = datetime.datetime.strptime(toDate, '%Y-%m-%d')

    cnx = cx_Oracle.connect('jashim/jashim@//localhost:1521/orcl')
    mycursor = cnx.cursor()
    mycursor.execute("""BEGIN LOAD_MONEY_RECEIPT(); END;""")
    cnx.commit()
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
              depositStatus from ump_mr where RESPONSE is not null and mrDate between :fdate and :tdate
              """, [fdate, tdate])
    myresults = mycursor.fetchall()
    return render(request,'pages/admin/report/previousreport.html',{'companyName':companyName,'userprofile':userprofile,'myresults':myresults})

def previouslysendePDFV(request):
    fromDate = request.POST.get('fdate')
    fdate = datetime.datetime.strptime(fromDate, '%Y-%m-%d')
    toDate = request.POST.get('tdate')
    tdate = datetime.datetime.strptime(toDate, '%Y-%m-%d')
    cnx = cx_Oracle.connect('jashim/jashim@//localhost:1521/orcl')
    mycursor = cnx.cursor()
    mycursor.execute("""BEGIN LOAD_MONEY_RECEIPT(); END;""")
    cnx.commit()
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
                 depositStatus from ump_mr where RESPONSE is not null and mrDate between :fdate and :tdate
                 """, [fdate, tdate])
    myresults = mycursor.fetchall()
    template_path = 'pages/admin/report/MRPDF.html'
    context = {'companyName':companyName,'myresults':myresults}
    response = HttpResponse(content_type='application/pdf')
    # for downlode
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response






