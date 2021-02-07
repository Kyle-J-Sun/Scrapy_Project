'''----------------------------------------------------Title------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------'''

import pymysql

class MySQLKCLPipline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost', port = 3306, user = 'root', passwd = 'Kyle9975', db = 'Admission_Report', charset = 'utf8')
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into KCL_adm_report (Coursename, Acc_Rate, Adm_Rate, En_Year, Apply_Num, Offer_Num, Adm_Num, href) values (%s, %s, %s, %s, %s, %s, %s, %s);'
        courseinfo = [item['Course_name'], item['Accep_Rate'], item['Admission_Rate'], item['Enroll_Year'], item['Apply_Num'], item['Offer_Num'], item['Admission_Num'], item['href']]
        self.cursor.execute(sql, courseinfo)
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()