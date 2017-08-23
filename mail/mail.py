#coding=utf-8

import re
import time
import js2py
import requests


class Mail139(object):
    def __init__(self,email,password):
        self.email= email
        self.password = password


    def __get_cguid(self):
        getCGUID = '''function() {
            function a(a, b) {
                var e = (b || 2) - (1 + Math.floor(Math.log(a | 1) / Math.LN10 + 1E-15));
                return Array(e + 1).join("0") + a
            }
            var b = new Date;
            return "" + a(b.getHours()) + a(b.getMinutes()) + a(b.getSeconds()) + a(b.getMilliseconds(), 3) + a(Math.ceil(9999 * Math.random()), 4)
        }
        '''
        cguid = js2py.eval_js(getCGUID)
        cguid = cguid()
        return cguid

    def __sha1_account(self):
        sha1 = '''function(a) {
            function b(a, b) {
                var c = (a & 65535) + (b & 65535);
                return (a >> 16) + (b >> 16) + (c >> 16) << 16 | c & 65535
            }
            for (var d = [], c = 0; c < 8 * a.length; c += 8)
                d[c >> 5] |= (a.charCodeAt(c / 8) & 255) << 24 - c % 32;
            a = 8 * a.length;
            d[a >> 5] |= 128 << 24 - a % 32;
            d[(a + 64 >> 9 << 4) + 15] = a;
            a = Array(80);
            for (var c = 1732584193, e = -271733879, f = -1732584194, h = 271733878, j = -1009589776, k = 0; k < d.length; k += 16) {
                for (var l = c, m = e, n = f, p = h, q = j, g = 0; 80 > g; g++) {
                    a[g] = 16 > g ? d[k + g] : (a[g - 3] ^ a[g - 8] ^ a[g - 14] ^ a[g - 16]) << 1 | (a[g - 3] ^ a[g - 8] ^ a[g - 14] ^ a[g - 16]) >>> 31;
                    var r = b(b(c << 5 | c >>> 27, 20 > g ? e & f | ~e & h : 40 > g ? e ^ f ^ h : 60 > g ? e & f | e & h | f & h : e ^ f ^ h), b(b(j, a[g]), 20 > g ? 1518500249 : 40 > g ? 1859775393 : 60 > g ? -1894007588 : -899497514))
                      , j = h
                      , h = f
                      , f = e << 30 | e >>> 2
                      , e = c
                      , c = r
                }
                c = b(c, l);
                e = b(e, m);
                f = b(f, n);
                h = b(h, p);
                j = b(j, q)
            }
            d = [c, e, f, h, j];
            a = "";
            for (c = 0; c < 4 * d.length; c++)
                a += "0123456789abcdef".charAt(d[c >> 2] >> 8 * (3 - c % 4) + 4 & 15) + "0123456789abcdef".charAt(d[c >> 2] >> 8 * (3 - c % 4) & 15);
            return a
        }
            '''
        _params = js2py.eval_js(sha1)
        params = _params(str(self.email))
        return params

    def __digest_password(self):
        Digest_pd = '''
            function(b) {
                        function a(a, d) {
                        var c = (a & 65535) + (d & 65535);
                        return (a >> 16) + (d >> 16) + (c >> 16) << 16 | c & 65535
                                            }
            for (var d = (b.length + 8 >> 6) + 1, c = Array(16 * d), e = 0; e < 16 * d; e++)
                c[e] = 0;
            for (e = 0; e < b.length; e++)
                c[e >> 2] |= b.charCodeAt(e) << 24 - 8 * (e & 3);
            c[e >> 2] |= 128 << 24 - 8 * (e & 3);
            c[16 * d - 1] = 8 * b.length;
            b = Array(80);
            for (var d = 1732584193, e = -271733879, f = -1732584194, h = 271733878, j = -1009589776, k = 0; k < c.length; k += 16) {
                for (var l = d, m = e, n = f, p = h, q = j, g = 0; 80 > g; g++) {
                    b[g] = 16 > g ? c[k + g] : (b[g - 3] ^ b[g - 8] ^ b[g - 14] ^ b[g - 16]) << 1 | (b[g - 3] ^ b[g - 8] ^ b[g - 14] ^ b[g - 16]) >>> 31;
                    var r = a(a(d << 5 | d >>> 27, 20 > g ? e & f | ~e & h : 40 > g ? e ^ f ^ h : 60 > g ? e & f | e & h | f & h : e ^ f ^ h), a(a(j, b[g]), 20 > g ? 1518500249 : 40 > g ? 1859775393 : 60 > g ? -1894007588 : -899497514))
                      , j = h
                      , h = f
                      , f = e << 30 | e >>> 2
                      , e = d
                      , d = r
                }
                d = a(d, l);
                e = a(e, m);
                f = a(f, n);
                h = a(h, p);
                j = a(j, q)
            }
            c = [d, e, f, h, j];
            b = "";
            for (d = 0; d < 4 * c.length; d++)
                b += "0123456789abcdef".charAt(c[d >> 2] >> 8 * (3 - d % 4) + 4 & 15) + "0123456789abcdef".charAt(c[d >> 2] >> 8 * (3 - d % 4) & 15);
            return b
        }'''
        password = js2py.eval_js(Digest_pd)
        password = password('fetion.com.cn:%s' %str(self.password))
        return password

    def login(self):
        cguid=self.__get_cguid()
        print cguid,type(cguid)
        params = self.__sha1_account()
        print params,type(params)
        url = 'https://mail.10086.cn/Login/Login.ashx?_fv=4&cguid=%s&_=%s&resource=indexLogin'\
                        %(cguid,params)
        print url
        password = self.__digest_password()
        data={'UserName':self.email,
                'verifyCode':'',
                'webVersion':'25',
                'auto':'on',
                'Password':password,
                'authType':'2'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            }
        s = requests.session()
        html = s.post(url,data=data,headers=headers)
        print s.cookies
        sid = s.cookies['Os_SSo_Sid']
        rmkey = s.cookies['RMKEY']
        return s,sid,rmkey

    def inbox(self):
        cguid = self.__get_cguid()
        url = 'http://appmail.mail.10086.cn/s?func=mbox:listMessages&sid=%s&&comefrom=54&cguid=%s'%(sid,cguid)
        data = '''<object>
                  <int name="fid">1</int>
                  <string name="order">receiveDate</string>
                  <string name="desc">1</string>
                  <int name="start">1</int>
                  <int name="total">2</int>
                  <string name="topFlag">curr_task</string>
                  <int name="sessionEnable">2</int>
                  </object>'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            }
        html = s.post(url,data)
        print html.content
        url = 'http://smsrebuild1.mail.10086.cn/sms/sms?func=sms:sendSms&sid=%s&rnd=0.4378995041011722&cguid=%s'%(sid,cguid)

        data = '''<object>
        <int name="doubleMsg">0</int>
        <int name="submitType">1</int>
        <string name="smsContent">test123123123132[中国网络]</string>
        <string name="receiverNumber">8615705211213</string>
        <string name="comeFrom">104</string>
        <int name="sendType">2</int>
        <int name="smsType">1</int>
        <int name="serialId"></int>
        <int name="isShareSms">0</int>
        <string name="sendTime"></string>
        <string name="validImg"></string>
        <int name="groupLength">50</int>
        <int name="isSaveRecord">1</int>
        <int name="smsIds"></int>
        <array name="receiverList"></array>
        </object>'''
        html=s.post(url=url,data=data)
        print html.content

mail=Mail139(15705211213,'wk123456')
# mail._Mail139__check_password()
s,sid ,rekey = mail.login()
mail.inbox()


