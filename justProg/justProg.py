import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

user_agent = UserAgent()
headers = {'user-agent': user_agent.random}

url = 'https://hidemy.name/ru/proxy-list/'
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res, 'lxml')

block = soup.find('div', class_='services_proxylist services')
part1 = block.find('div', class_='inner')
part2 = part1.find('div', class_='table_block')

pings = []
ips = []
valid_pings = []
valid_ip = []
valid_ping_without_mc = ''
temp = ''

print('Список прокси с первой страницы в формате:' + '\n')
for i in range(65):
    pre_results = part2.find_all('tr')[i]
    ping = pre_results.find_all('td')[3].text
    ip = pre_results.find_all('td')[0].text
    pings.append(ping)
    ips.append(ip)
    for j in range(7):
        results = pre_results.find_all('td')[j].text
        print(results)
    print('\n')

for i in range(1, 65):
    temp = str(pings[i])
    valid_ping_without_mc = ''
    for j in range(len(temp)):
        if temp[j] != ' ':
            valid_ping_without_mc += temp[j]
        else:
            break
    if 1 <= int(valid_ping_without_mc) <= 100:
        valid_pings.append(valid_ping_without_mc)
        valid_ip.append(ips[i])

print('Список валидных прокси:')
print('\n'.join(valid_ip))
