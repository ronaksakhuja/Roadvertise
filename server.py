from flask import Flask
import numpy as np
import pandas as pd
from sklearn import linear_model
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    import datetime
    import os
    import socket
    import json
    import sys
    import urllib3
    http = urllib3.PoolManager()

    if os.name != "nt":
        import fcntl
        import struct

        def get_interface_ip(ifname):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                    ifname[:15]))[20:24])

    def get_lan_ip():
        ip = socket.gethostbyname(socket.gethostname())
        if ip.startswith("127.") and os.name != "nt":
            interfaces = [
                "eth0",
                "eth1",
                "eth2",
                "wlan0",
                "wlan1",
                "wifi0",
                "ath0",
                "ath1",
                "ppp0",
                ]
            for ifname in interfaces:
                try:
                    ip = get_interface_ip(ifname)
                    break
                except IOError:
                    pass
        return ip
    
    

    a=np.random.randint(low=1000, high=1500, size=100)
    #slot 5
    b=np.random.randint(low=1000, high=1200, size=100)
    #slot 6
    c=np.random.randint(low=800,high=1000,size=100)
    #slot 3
    d=np.random.randint(low=600,high=900,size=100)
    #slot 1
    e=np.random.randint(low=400,high=700,size=100)
    #slot 2
    f=np.random.randint(low=200,high=500,size=100)

    arr=np.array([e,f,d,a,b,c])
    data=pd.DataFrame(columns=["DAY_NUM","DAY","SLOT1","SLOT2","SLOT3","SLOT4","SLOT5","SLOT6"])
    data["DAY_NUM"]=np.arange(100)
    days=np.arange(7)
    for i in range(14):
        days=np.append(arr=days,values=np.arange(7))
    days=days[:100]    
    data["DAY"]=days
    data["SLOT1"]=e
    data["SLOT2"]=f
    data["SLOT3"]=d
    data["SLOT4"]=a
    data["SLOT5"]=b
    data["SLOT6"]=c
    x=np.array([]);
    for i in range(6):
        x=np.append(arr=a,values=data.iloc[0, 2:][i])
    slot=0
    from_time=0
    now = datetime.datetime.now()
    hour=now.hour
    if (hour>=23 and hour<24) or (hour>0 and hour<3):
        slot=1
        from_time=3
    if hour>=3 and hour<7:
        slot=2
        from_time=7
    if hour>=7 and hour<11:
        slot=3
        from_time=11
    if hour>=11 and hour<15:
        slot=4
        from_time=15
    if hour>=15 and hour<19:
        slot=5
        from_time=19
    if hour>=19 and hour<23:
        slot=0
        from_time=23
        
    data=pd.read_csv("file.csv")
    data.dropna(inplace=True)
    x_axis=round(70/100*data.shape[0])
    y_axis=data.shape[0]-x_axis

    baseurl=get_lan_ip()+"/img"
    graphing=[0,0,0,0,0,0]
    a=[0,0,0,0,0,0]
    x=0
    nextday=0
    r=http.request('GET','http://localhost/max_bidding.php')
    js=json.loads(r.data)
    for i in range(6):
        train_x=np.array(data.iloc[:x_axis,1])
        print(train_x)

        train_y=np.array(data.iloc[:x_axis,2+slot])
        test=data.iloc[x_axis:,1]
        import datetime
        model=linear_model.LinearRegression()
        train_x=train_x.reshape(-1,1)
        test=test.reshape(-1,1)
        model.fit(train_x,train_y)
        day=now.strftime("%w")
        y=model.predict(np.array(int(day)+nextday).reshape(-1,1))
        graphing[x]=y[0]
        for j in js:
            if j['time']==str(from_time):
                a[x]={"fromTime":from_time,"toTime":(from_time+4)%24,"urlImage":baseurl+str(x)+".png","estTraffic":y[0],"maxBid":j['max_bid'],"minBid":j['min_bid']}
        from_time=from_time+4
        if(from_time>24):
            from_time=from_time%24
        if slot == 5:
            slot=-1
            nextday=1
        slot=slot+1
        x=x+1


    for i in range(6):
        colors=['g']*(i)+['b']+['g']*(6-i-1)
        dfs=pd.DataFrame(graphing)
        ax=dfs.plot(kind='bar',color=colors)
        img=ax.get_figure()
        img.savefig("img"+str(i)+".png")
    return jsonify(a)

if __name__=='__main__':
    app.run(host="0.0.0.0",port="33")