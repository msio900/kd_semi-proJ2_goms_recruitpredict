from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.http import urlencode

from config.settings import DATA_DIRS
from frame.error import ErrorCode
from frame.resdb import ResDb
from frame.sql import Sql
from frame.udatadb import UdataDb
from frame.userdb import UsersDB
from frame.value import Udata
from myanalysis.ml import load_model
import pandas as pd;

mid_code = pd.read_csv(DATA_DIRS[0]+'\\midjobCate_code.csv');

def home(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def index(request):
    return render(request, 'index.html')
def elements(request):
    return render(request, 'elements.html')
def generic(request):
    return render(request, 'generic.html')
def register(request):
    return render(request, 'register.html')
def machine(request):
    return render(request, 'machine.html')

# register
def useraddimpl(request):
    # id, pwd, name 을 입력 받아 데이터베이스에 입력 하고
    user_id = request.POST['user_id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    email = request.POST['email'];
    phone = request.POST['phone'];
    try:
        UsersDB().insert(user_id,pwd,name,email,phone);
    except:
        context = { 'msg': ErrorCode.e0001};
        return render(request, 'error.html',context);
    # 조회 화면으로 이동 한다.
    return redirect('index.html');

# login
def loginimpl(request):
    user_id = request.POST['user_id'];
    pwd = request.POST['pwd'];
    next = 'loginimpl.html';
    try:
        user = UsersDB().selectone(user_id);
        if pwd == user.pwd:
            # 로그 아웃하기 전까지
            request.session['loginuser'] =  {'user_id':user.user_id,'name':user.name};
            context = None;
        else:
          raise Exception;
    except:
        context = { 'msg':ErrorCode.e0003 };
        next = 'error.html';
    return render(request, next, context);
# logout
def logout(request):
    if request.session['loginuser'] != None:
        del request.session['loginuser'];
    return render(request,'index.html');

# userinfo
def userinfo(request):
    user_id = request.GET['user_id'];
    user = UsersDB().selectone(user_id);
    context = {'u': user};
    return render(request, 'userinfo.html', context);

def userdelete(request):
    user_id = request.GET['user_id'];
    UsersDB().delete(user_id);
    return redirect('index.html');

def userupdate(request):
    user_id = request.GET['user_id'];
    user = UsersDB().selectone(user_id);
    context = {'u': user};
    return render(request, 'userupdate.html', context);

def userupdateimpl(request):
    user_id = request.POST['user_id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    email = request.POST['email'];
    phone = request.POST['phone'];
    UsersDB().update(user_id,pwd,name,email,phone);
    qstr = urlencode({'user_id': user_id});
    return HttpResponseRedirect('%s?%s' % ('userinfo', qstr));

def formimpl(request):
    id = request.POST['id'];
    schooltype = request.POST['schooltype'];
    majorcate = request.POST['majorcate'];
    age = request.POST['age'];
    intern = request.POST['intern'];
    toeic = request.POST['toeic'];
    tosp = request.POST['tosp'];
    train = request.POST['train'];
    jobseek = request.POST['jobseek'];
    cert = request.POST['cert'];
    jobsearch = request.POST['jobsearch'];
    yrwish = request.POST['yrwish'];
    wishhr = request.POST['wishhr'];
    wishsalary = request.POST['wishsalary'];
    jobgradu = request.POST['jobgradu'];
    liveexp = request.POST['liveexp'];

    try:
        UdataDb().insert(id, schooltype, majorcate, age, intern, toeic, tosp, train, jobseek, cert, jobsearch, yrwish,
                         wishhr, wishsalary, jobgradu, liveexp)
    except:
        context = { 'msg': ErrorCode.e0001};
        return render(request, 'error.html',context);

    result=UdataDb().selectone(id);
    mld=load_model.predict(pd.DataFrame({'jobsearch':[int(result.jobsearch)],'yrwish':[int(result.yrwish)],'wishhr':[int(result.wishhr)],'wishsalary':[int(result.wishsalary)],
                                           'jobgradu':[int(result.jobgradu)],'liveexp':[int(result.liveexp)],'schooltype':[int(result.schooltype)],'majorcate':[int(result.majorcate)],
                                           'age':[int(result.age)],'intern':[int(result.intern)],'toeic':[int(result.toeic)],'tosp':[int(result.tosp)],
                                           'train':[int(result.train)],'jobseek':[int(result.jobseek)],'cert':[int(result.cert)]}));
    chs=mld[0]
    ResDb().insert(id,chs);

    rlist = ResDb().select(id);

    for i in range(0,len(mid_code)):
        if chs==mid_code.iloc[:,0][i]:
            key=mid_code.iloc[:,1][i];
    rtext={
        'r':rlist,'c':key
    };


    return render(request, 'result.html',rtext);

def result(request):
    return render(request, 'result.html');


def datalist(request):
    user_id = request.GET['user_id'];
    datalist = UdataDb().selectall(user_id)
    context = {'datalist':datalist}
    return render(request,'datalist.html',context);

def datadelete(request):
    id = request.GET['user_id'];
    UdataDb().delete(id);

    return redirect('index.html');
