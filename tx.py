import requests
host = "kmustjwcxk1.kmust.edu.cn"
sturl = "http://kmustjwcxk1.kmust.edu.cn/jwweb"
#退选用cookies
txhead = {
"Host": host,
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"Origin": "http://" + host,
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"DNT": "1",
"Referer": sturl + "/wsxk/stu_zxjg_rpt.aspx",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.8"
}
print("目前学期为20171学期，其他学期请勿使用")
cookin = input("输入教务网登录点1的ASP.NET_SessionId：")
cook = {"ASP.NET_SessionId":cookin}
kckh = input("输入退选课程的课程号-上课班级（可查看退选复选框value值）：")
chkcon = input("输入退选前已选课程总数：")
postdata = "chkDel12="+ kckh +"%23&chkCount=" + str(chkcon) + "&deleteValue=TTT," + kckh + "%23&sel_xnxq=20171"
print("请求数据:"+postdata+"\n")
print("请求头:"+str(txhead)+"\n")
print("Cookies:"+str(cook)+"\n")
if(input("输入Y或yes来确认，否则请直接关闭软件") in("Y","yes")):
    tdurl = sturl + "/wsxk/stu_zxjg_rpt.aspx?func=1"
    res = requests.post(tdurl,data = postdata,headers = txhead,cookies = cook)
    res.encoding = 'gb2312'
    print("退选请求已发送")
    try:
        if re.search("退选成功",res.text):
            print("退选成功")
        else:
            print("没有匹配到成功提示，请手动验证退选结果，若失败，请检查输入内容并与开发者联系")
    except:
        print("请手动检查退选结果")
    print("软件退出，Cookies等同于密码，复制、截图请注意安全")
else:
    print("没有进行退选，软件退出，Cookies等同于密码，复制、截图请注意安全")
input()
