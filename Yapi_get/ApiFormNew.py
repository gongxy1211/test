import requests
import json
from jinja2 import Template
import os
import xpinyin

def getIdlist(projectId,id):
    i=0
    IdList=[]
    data_1 = session.get("http://183.131.202.93:9071/api/interface/list_menu?project_id=" + projectId).json()["data"]
    if id!= None:
        IdList.extend(id)
    else:
        for data in data_1:
            if data["list"] != []:
                for list in data["list"]:
                    IdList.append(list["_id"])
                    i=i+1
            else:
                continue
    #print(i)
    return IdList
def getTid(groupid):
    TidList=[]
    if groupid!=None:
        data_1 = session.get("http://183.131.202.93:9071/api/interface/list_cat?page=1&limit=200&catid=" + str(groupid)).json()["data"]
        #print("getTid")
        #print(data_1)
        if data_1["list"]!=[]:
            for list in data_1["list"]:
                TidList.append(list["_id"])
        else:
            pass
        return TidList



#获取所有接口id

def getApiInfo(apiId):
    apiInfo={}
    data = []
    apiDetail = session.get("http://183.131.202.93:9071/api/interface/get?id=" + str(apiId)).json()["data"]
    #print(apiDetail.keys())
    if "req_body_type" in apiDetail.keys():
        if apiDetail["req_body_type"]=="form":
            req_body_form=apiDetail["req_body_form"]
            for form_1 in req_body_form:
                    data.append(form_1["name"])
        elif apiDetail["req_body_type"]=="json":
           # print("+++++++++++"+apiDetail["req_body_other"])
            if apiDetail["req_body_other"] !="":
                req_body_other=json.loads(apiDetail["req_body_other"])["properties"]

                #if apiDetail[]
                for form_2 in req_body_other:
                    data.append(form_2)
        else:
            pass
##获取data
    if "api" in apiDetail["path"]:
        url=apiDetail["path"].split("/api")[1]
    else:
        url=apiDetail["path"]
##获取地址
    apiInfo.update({
        "url": url,
        "method": apiDetail["method"],
        "api_name": url.replace("/", "_")[1:],
        "args": data,
        "comment": apiDetail["title"]
    })
    return apiInfo
#获取详情信息

def save_file(dirname,filename, content):
    curPath=os.getcwd()#获取当前路径
    tempPath=dirname
    targetPath=curPath+os.path.sep+tempPath #"os.path.sep"相当于"/"
    #targetPath=curPath+'/'+tempPath
    #print(targetPath)
    if not os.path.exists(targetPath):#判断路径是否已经存在
        os.makedirs(targetPath)
    else:
        pass
#创建文件夹
    filePath=targetPath+os.path.sep+filename
    with open(filePath, "w", encoding="utf-8") as f:
        f.write(content)
 #相当于 open(filename, "w+", encoding="utf-8")打开文件，如果文件不存在则创建文件，字符编码格式为"utf-8",创建并打开文件-写如文件-关闭文件

def getModuleName(projectID):
    res = session.get("http://183.131.202.93:9071/api/project/get?id=" + projectID)
    modules = []
    for i in res.json()["data"]["cat"]:
        modules.append(
            {
                "_id": i["_id"],
                "name": i["name"]
            }
        )
    return modules

#***********************************************************************************************************************************************#
projectId="35"#传递需要的参数
id=None
session=requests.session()#可获取请求头参数
formdata={
    "email": "gongxy@zjbdos.com",
    "password": "keephappysmile12"
}
src=session.post("http://183.131.202.93:9071/api/user/login",formdata)
#登陆
#*******************************************************************************************************#
items=[]
getList=[]
getList.extend(getIdlist(projectId,id))
#print(getList)
for ApiId in getList:
    items.append(getApiInfo(ApiId))
#print(items[1])
#print(items)
#print(len(items))
    #print(getApiInfo(ApiId))
template1='''
{%for item in items%}
@request(url='{{item["url"]}}',method='{{item["method"]}}')
def {{item['api_name']}}(self{% for a in item['args']%}, {{a}}{% endfor %}):
    """{{item['comment']}}"""
    json = {
        {% for args in item['args'] -%}
        "{{args}}": {{ args }},
        {% endfor -%}
        }
    return {'json': json, 'headers': self.headers}
{% endfor -%}
'''#创建pytest接口
#{%for %}{%endfor-%}for循环语句
#{{}}传递参数
content1=Template(template1).render(items=items)#初始化template，并传递参数items
#print(content1)#输出结果
#print("总共生成{}个接口".format(len(items)))
filename="ApiTest"+".py"
dirname1="name"
save_file(dirname1,filename,content1)
#****************************************************************#
modules=getModuleName(projectId)#获取所有大模块id
for  module in modules:
    pinyin=xpinyin.Pinyin()
    dirname="test_"+pinyin.get_pinyin(module["name"],"")#??
    actions=[]
    #print("nihao")
    #print(module["_id"])
    if getTid(module["_id"])!=[]:#获取每个模块下的接口id

        for api in getTid(module["_id"]):
            actions.append(getApiInfo(api))#获取每个接口的接口详情
        #print("action")
        #print(actions)
    else:
        pass

    for item in actions:
        name=[]
        for i in item["api_name"].split("_"):
            name.append(i.capitalize())
        args=item["args"]
        script_template = '''import pytest
from api.wuhe_back import WuheBack


class Test_{{ name }}:
    data=[
        ()
    ]

    @pytest.mark.parametrize("{{ args }}", data)
    def test_{{ item["api_name"] }}(self{% for a in item['args']%}, {{ a }}{% endfor %}):
        user = Front()
        res = user.{{ item["api_name"] }}({{args}})
        res_json = res.json
        assert res.status_code == 200, "接口级别校验_【{{ item['comment'] }}】 " + "请求链接为：" + res.request.url
        assert res.elapsed.seconds <= 3, "接口响应超时"
        assert res_json['code'] == 0, "code校验_【{{ item['comment'] }}】 " + "请求链接为：" + res.request.url

'''
        #print(item)
        content2=Template(script_template).render(item=item,name="".join(name),arg=",".join(args))
        filename="test_" + item["api_name"] + ".py"
        save_file(dirname,filename,content2)
        #print(content2)
   # print(len(actions))








