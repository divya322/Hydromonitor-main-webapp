from flask import Flask, request, jsonify
from datacl import get_azure_data,len_of_excel,write_to_excel,getdata

#motor="off" #for cntrolling motor, to be added later....
app = Flask("__name__")

@app.route('/fdata',methods=['GET'])
def fdata_func():                           # full data refresh
    """if(request.args["sensor"]=="yes"):
        row = get_azure_data()              # get data from azure in a row
        len_excel = len_of_excel()          # get number of last row in excel
        if (row!=[]):                       # check if data was avaialabe from azure
            write_to_excel(len_excel,row)   # updating excel
    """
    d={}  
    d["val"] = str(getdata("time"))         # getting last upadte time from excel and saving it in dict
    d["temp"] = str(getdata("temp")) 
    d["humidity"] = str(getdata("humidity")) 
    d["light"] = str(getdata("light")) 
    d["soil"] = str(getdata("soil")) 
    d["absoil"] = str(getdata("absoil"))
    d["water"] = str(getdata("water"))
    d["flap"] = str(getdata("flap"))
    d["npk"] = str(getdata("npk")) 
    return jsonify(d)                       # returning the value

@app.route('/putdata',methods=['GET'])
def put_func():
    getdata("time")
    a = request.args["sensor"]
    row = get_azure_data(a)              # get data from azure in a row
    len_excel = len_of_excel()          # get number of last row in excel
    if (row!=[]): 
        write_to_excel(len_excel,row)
    else:
        getdata("time")
    f="Data recieved!"
    return f
    
    
    
if __name__=="__main__":
    app.run(port=71)
