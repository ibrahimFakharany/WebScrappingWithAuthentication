import requests
from config import username, password
from bs4 import BeautifulSoup as Soup
import hashlib 
def get_md5(s): 
	return hashlib.md5(bytes(s, encoding = 'utf8')).hexdigest()
def main():

	url = 'https://sevashoes.com/en/login'
	with requests.session() as session: 
		response = session.get(url)
		
		soup = Soup(response.text, 'lxml')
		challenge = soup.find('input' , id = 'challenge').get('value')
		headerStr = username + ':'+ get_md5(password)+':'+challenge
		result = get_md5(headerStr)
		data ={ 'username':username, 
				'password':'',
				'challenge':'',
				'response':result }

		response = session.post(url, data=data)
		print(response.text)

		with open('result_page.html', 'w', encoding='utf-8' , errors='ignore') as f: 
			f.write(response.text)

		








if __name__ == '__main__':
	main()