import requests
from django.shortcuts import render
import json
from django.http import JsonResponse
import traceback

from django.http import HttpResponse

from django.views import View

def index(request):
    return render(request,'navigation/test.html')


import requests
from django.shortcuts import render
import json
from django.http import JsonResponse
import traceback

from django.views import View


class RunMethod():
    # url不可能为空，data不一定不能为空，header可能为空  #参数名叫headers  #if header !=None:  #返回res,初始为空  #返回的结果一般为.json()
    def get_main(self, url, key_value_params):
        data = {"status": 0, "res": ""}
        try:
            res = requests.get(url=url, params=key_value_params)
            if res.status_code != 200:
                data["status"] = 1
                data["msg"] = "接口请求失败，响应状态码:" + str(res.status_code)
                data["res"] = res.text
                return data
        except requests.exceptions.MissingSchema as e:
            print('发送请求异常：', e)
            data["msg"] = "请求失败，请检查接口前缀！"
            data["status"] = 1
            return data
        try:
            #将请求的返回值转换为json格式
            response_data = res.json()
        except:
            #输出详细的异常信息
            traceback.print_exc()
            data["status"] = 1
            data["msg"] = "接口运行失败，请检查带入的参数是否正确"
            return data
        data["res"] = res.text
        print(data)
        return data

# 接口测试
def interface_tool(request):
    if request.method == "GET":
        return render(request, "navigation/interface_tool.html")
    elif request.method == "POST":
        method = request.POST['method']
        url = request.POST['url']
        datatype = request.POST['datatype_select']
        key_value_params = {}
        if datatype == "JSON":
            param = request.POST['body_input']
        elif datatype == "FORM" or "带参":
            key_value = request.POST['key_value']
            # 解析json数组，将json转换为字典
            key_value = json.loads(key_value)

            for i in key_value:
                # 如果键为空，此键值对参数不传
                if i['key'].replace(" ", ""):
                    # 处理成字典格式参数
                    key_value_params[i['key']] = i['value'].replace(" ", "")
        # 转为json格式
        # key_value_params = json.dumps(key_value_params)
        if method == "GET":
            run = RunMethod()
            data = run.get_main(url,key_value_params)
            return JsonResponse(data)

        if method == "POST":
            data = {"status": 0, "res": ""}
            body = {}

            if datatype == "JSON":
                if param:
                    try:
                        body = json.loads(param)
                    except:
                        data["status"] = 1
                        data["msg"] = "入参需要输入字典格式，请检查入参格式是否正确"
                        return JsonResponse(data)
                else:
                    body = ""
                try:
                    res = requests.post(url=url, json=body)
                    if res.status_code != 200:
                        data["status"] = 1
                        data["msg"] = "接口请求失败，响应状态码：" + str(res.status_code) + "， 请检查接口或传参为空"
                        data["res"] = res.text
                        return JsonResponse(data)
                except requests.exceptions.MissingSchema as e:
                    print('发送请求异常', e)
                    data["status"] = 1
                    data["msg"] = "请求失败，请检查接口前缀！"
                    return JsonResponse(data)
                try:
                    response_data = res.json()
                    data["res"] = res.text
                except:
                    data["status"] = 1
                    data["msg"] = "接口运行失败，请检查带入的json格式参数是否正确"
                    return JsonResponse(data)

            elif datatype == "FORM":
                if key_value_params:
                    body = key_value_params
                try:
                    res = requests.post(url=url, params=body)
                    if res.status_code != 200:
                        data["status"] = 1
                        data["msg"] = "接口请求失败，响应状态码：" + str(res.status_code)
                        data["res"] = res.text
                        return JsonResponse(data)
                except requests.exceptions.MissingSchema as e:
                    print('发送请求异常', e)
                    data["status"] = 1
                    data["msg"] = "请求失败，请检查接口前缀！"
                    return JsonResponse(data)
                try:
                    response_data = res.json()
                    data["res"] = res.text
                except:
                    data["status"] = 1
                    data["msg"] = "接口运行失败，请检查带入的参数是否正确"
                    return JsonResponse(data)

            elif datatype == "无参":
                try:
                    res = requests.post(url=url)
                    if res.status_code != 200:
                        data["status"] = 1
                        data["msg"] = "接口请求失败，响应状态码：" + str(res.status_code)
                        data["res"] = res.text
                        return JsonResponse(data)
                except requests.exceptions.MissingSchema as e:
                    print('发送请求异常', e)
                    data["status"] = 1
                    data["msg"] = "请求失败，请检查接口前缀！"
                    return JsonResponse(data)

            try:
                response_data = res.json()
                data["res"] = res.text
            except:
                data["status"] = 1
                data["msg"] = "返回数据错误或返回为html，请检查接口及参数是否正确"
                data["res"] = res.text
                return JsonResponse(data)

            data["res"] = res.text
            return JsonResponse(data)



