import requests
formdata={
    "email": "gongxy@zjbdos.com",
    "password": "keephappysmile12"
}
session=requests.session()
src=session.post("http://183.131.202.93:9071/api/user/login",formdata)
#登陆
print("**********************")
catid=108
formdata_3={
    "catid":catid,
    "limit":1000,
    "page":1
}
src_3=session.get("http://183.131.202.93:9071/api/interface/list_cat",params=formdata_3)
json=src_3.json()
list=json["data"]["list"]
n=0
for list_n in list:
    id=list_n["_id"]
    formdata_2 = {
        "id": id
    }
    src_2 = session.get("http://183.131.202.93:9071/api/interface/get", params=formdata_2)
    json_1=src_2.json
    print(src_2.text)
    n=n+1
print(n)#统计所有接口数量


