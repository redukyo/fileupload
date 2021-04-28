import requests

file_ob = {'uploaded_file': open('/root/test.txt', 'rb')}
print(file_ob)
payload = {
    'remark1': 'hello world',
}
r = requests.post("http://127.0.0.1:8000/upload/", files=file_ob, data=payload)

print(r.status_code)
