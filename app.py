from flask import Flask, render_template, request
import numpy as np
import pickle
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def send():
    if request.method == 'POST':
        typ = int(request.form['type'])
        # locality = request.form['locality']
        # latitude = float(request.form['latitude'])
        # longitude = float(request.form['longitude'])
        lease_type = int(request.form['lease_type'])
        gym = int(request.form['gym'])
        lift = int(request.form['lift'])
        swimming_pool = int(request.form['swimming_pool'])
        furnishing = int(request.form['furnishing'])
        Parking = int(request.form['Parking'])
        size = int(request.form['size'])
        age = int(request.form['age'])
        floor = int(request.form['floor'])
        bathroom = int(request.form['bathrooms'])
        INTERNET = int(request.form['INTERNET'])
        AC = int(request.form['AC'])
        CLUB = int(request.form['CLUB'])
        INTERCOM = int(request.form['INTERCOM'])
        CPA = int(request.form['CPA'])
        FS = int(request.form['FS'])
        SERVANT = int(request.form['SERVANT'])
        SECURITY = int(request.form['SECURITY'])
        SC = int(request.form['SC'])
        GP = int(request.form['GP'])
        PARK = int(request.form['PARK'])
        RWH = int(request.form['RWH'])
        STP = int(request.form['STP'])
        HK = int(request.form['HK'])
        PB = int(request.form['PB'])
        VP = int(request.form['VP'])
        Water_supply = int(request.form['Water_supply'])
        building_type = int(request.form['building_type'])
        balconies = int(request.form['balconies'])
        

        
        w = np.array([typ,4,lease_type,gym,lift,swimming_pool,furnishing,Parking,size,age,floor,bathroom, INTERNET,
                     AC,CLUB,INTERCOM,CPA,FS,SERVANT,SECURITY,SC,GP,PARK,RWH,STP,HK,PB,
                     VP,Water_supply,building_type,size,floor,bathroom,balconies,1,0,1])

        # w = [1.00000000e+00, 9.65000000e+02, 1.29065457e+01, 7.75912731e+01,
        # 3.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
        # 1.00000000e+00, 2.00000000e+00, 0.00000000e+00, 1.20000000e+03,
        # 1.00000000e+01, 2.00000000e+00, 7.00000000e+00, 2.00000000e+00,
        # 1.00000000e+00, 1.00000000e+00, 2.00000000e+00, 2.00000000e+00,
        # 0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
        # 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
        # 1.00000000e+00, 1.00000000e+00, 0.00000000e+00, 1.00000000e+00,
        # 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00,
        # 1.00000000e+00]
        # w = [1, lease_type, latitude, longitude,
        # 3.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
        # 1.00000000e+00, 2.00000000e+00, 0.00000000e+00, 1.20000000e+03,
        # 1.00000000e+01, 2.00000000e+00, 7.00000000e+00, 2.00000000e+00,
        # 1.00000000e+00, 1.00000000e+00, 2.00000000e+00, 2.00000000e+00,
        # 0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 0.00000000e+00,
        # 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00,
        # 1.00000000e+00, 1.00000000e+00, 0.00000000e+00, 1.00000000e+00,
        # 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00,
        # 1.00000000e+00]
                

        model = pickle.load(open('model.pkl','rb'))
        # w = [1,	1061,	12.936601,	77.576914,	3,	0,	0,	0,	0,	2,	...	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0]
        rent = model.predict(np.array(w).reshape(1,37))
        import math
        res=math.floor(rent)
        
        return render_template("out.html", outcome=res)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run()