import joblib

from config.settings import DATA_DIRS
from frame.udatadb import UdataDb
import pandas as pd;
load_model = joblib.load(DATA_DIRS[0]+'\\lgb_clf_mid.pkl')
#
# ResDb().resultinsert(id, result);
# result=load_model.predict(pd.DataFrame({'jobsearch':,'yrwish':yrwish,'wishhr':wishhr,'wishsalary':wishsalary,
#                                        'jobgradu':jobgradu,'liveexp':liveexp,'schooltype':schooltype,'majorcate':majorcate,
#                                        'age':age,'intern':intern,'toeic':toeic,'tosp':tosp,
#                                        'train':train,'jobseek':jobseek,'cert':cert}));
#

mid_code = pd.read_csv(DATA_DIRS[0]+'\\midjobCate_code.csv');



if __name__ == '__main__':
    result=UdataDb().selectone('hakdj');

    mld=load_model.predict(pd.DataFrame({'jobsearch':[int(result.jobsearch)],'yrwish':[int(result.yrwish)],'wishhr':[int(result.wishhr)],'wishsalary':[int(result.wishsalary)],
                                           'jobgradu':[int(result.jobgradu)],'liveexp':[int(result.liveexp)],'schooltype':[int(result.schooltype)],'majorcate':[int(result.majorcate)],
                                           'age':[int(result.age)],'intern':[int(result.intern)],'toeic':[int(result.toeic)],'tosp':[int(result.tosp)],
                                           'train':[int(result.train)],'jobseek':[int(result.jobseek)],'cert':[int(result.cert)]}));
    chs=mld[0]

    for i in range(0,len(mid_code)):
        if chs==mid_code.iloc[:,0][i]:
            key=mid_code.iloc[:,1][i];
            ctext={
                'c':key
            };
            print(ctext);

