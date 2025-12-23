from flask import Flask,jsonify,request
from flask_cors import CORS
import json
import os

userid_list=json.loads(os.getenv("apiuserid"))

app=Flask(__name__)
CORS(app)


this_dir=os.path.dirname(os.path.abspath(__file__))

idiom_file_path=os.path.join(this_dir,"idiom.json")

with open(idiom_file_path,"r",encoding="utf-8") as idiom_file:
    idiom_data=json.load(idiom_file)


word=[a_idiom_data["word"] for a_idiom_data in idiom_data]


def check_userid(userid):
    return userid in userid_list

@app.route('/api',methods=['GET'])
def home():
    return jsonify({"msg":"","status":"","value":"所有api固定参数：userid（请联系 bilibili：一只爱编程的小狮子 申请）\n"
    "目前已有api："+
    "相对网址：/idiom || 用法：查询成语含义、拼音、解释、出处、例句、缩写 || 参数：idiom（要查询的成语）"})

@app.route('/api/idiomsearch',methods=['GET'])
def idiom_search():
    userid=request.args.get("userid","")
    idiom=request.args.get("idiom","")

    if not(userid in userid_list):
        return jsonify({"msg":"userid不可用","status":"error"})
    
    if not(idiom in word):
        return jsonify({"msg":"成语库中没有此成语","status":"error"})
    
    return jsonify({"msg":"","error":"","value":idiom_data[word.index(idiom)]})

if __name__=="__main__":
    port=int(os.getenv("PORT",8000))
    app.run(host="0.0.0.0",port=port,debug=True)