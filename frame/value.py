class Users:
    def __init__(self, user_id, pwd, name,email,phone,regdate):
        self.user_id = user_id;
        self.pwd = pwd;
        self.name = name;
        self.email = email;
        self.phone = phone;
        self.regdate = regdate;
    def __str__(self):
        return self.user_id+' '+self.pwd+' '+self.name+' '+self.email+' '\
               +self.phone+' '+str(self.regdate);

class Udata:
    def __init__(self, num, id, schooltype, majorcate, age, intern, toeic, tosp, train, jobseek, cert, jobsearch, yrwish, wishhr, wishsalary, jobgradu, liveexp,datadate):
        self.num = num;
        self.id = id;
        self.schooltype = schooltype;
        self.majorcate=majorcate;
        self.age = age;
        self.intern = intern;
        self.toeic = toeic;
        self.tosp = tosp;
        self.train = train;
        self.jobseek = jobseek;
        self.cert = cert;
        self.jobsearch=jobsearch;
        self.yrwish=yrwish;
        self.wishhr=wishhr;
        self.wishsalary=wishsalary;
        self.jobgradu=jobgradu;
        self.liveexp=liveexp;
        self.datadate=datadate;
    def __str__(self):
        return str(self.num) + ' ' + self.id +' '+ str(self.schooltype)+\
               ' '+ str(self.majorcate) + ' '+str(self.age)+' '+str(self.intern)+\
               ' '+str(self.toeic)+' '+str(self.tosp)+' '+str(self.train)+\
               ' '+str(self.jobseek)+' '+str(self.cert)+' '+str(self.jobsearch)+\
               ' '+str(self.yrwish)+' '+str(self.wishhr)+' '+str(self.wishsalary)+\
               ' '+str(self.jobgradu)+' '+str(self.liveexp)+' '+str(self.datadate);

class Res:
    def __init__(self, num,id,result,resdate):
        self.num = num;
        self.id = id;
        self.result = result;
        self.resdate = resdate;

    def __str__(self):
        return str(self.num)+' '+self.id+' '+self.result+' '+str(self.resdate);







