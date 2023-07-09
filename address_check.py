from requests import session
list_state = {"Alabama":2,"Alaska":3,"Arizona":4,"Arkansas":5,"California":6,"Colorado":7,"Connecticut":8,"Delaware":9,"Florida":10,"Georgia":11,"Hawaii":12,"Idaho":13,"Illinois":14,"Indiana":15,"Iowa":16,"Kansas":17,"Kentucky":18,"Louisiana":19,"Maine":20,"Maryland":21,"Massachusetts":22,"Michigan":23,"Minnesota":24,"Mississippi":25,"Missouri":26,"Montana":27,"Nebraska":28,"Nevada":29,"New Hampshire":30,"New Jersey":31,"New Mexico":32,"New York":33,"North Carolina":34,"North Dakota":35,"Ohio":36,"Oklahoma":37,"Oregon":38,"Pennsylvania":39,"Puerto Rico":40,"Rhode Island":41,"South Carolina":42,"South Dakota":43,"Tennessee":44,"Texas":45,"Utah":46,"Vermont":47,"Virginia":48,"Washington":49,"Washington D.C.":50,"West Virginia":51,"Wisconsin":52,"Wyoming":53}
list_state_code = {"Ohio":"OH","Iowa":"IA","Utah":"UT","Texas":"TX","Maine":"ME","Idaho":"ID","Alaska":"AK","Oregon":"OR","Nevada":"NV","Hawaii":"HI","Kansas":"KS","Alabama":"AL","Arizona":"AZ","Florida":"FL","Georgia":"GA","Indiana":"IN","Montana":"MT","Vermont":"VT","Wyoming":"WY","Delaware":"DE","Kentucky":"KY","Maryland":"MD","Nebraska":"NE","Michigan":"MI","Missouri":"MO","Virginia":"VA","New York":"NY","Oklahoma":"OK","Arkansas":"AR","Colorado":"CO","Illinois":"IL","Minnesota":"MN","Louisiana":"LA","Tennessee":"TN","Wisconsin":"WI","California":"CA","New Jersey":"NJ","New Mexico":"NM","Washington":"WA","Puerto Rico":"PR","Connecticut":"CT","Mississippi":"MS","North Dakota":"ND","Pennsylvania":"PA","Rhode Island":"RI","South Dakota":"SD","New Hampshire":"NH","Massachusetts":"MA","West Virginia":"WV","North Carolina":"NC","South Carolina":"SC","Washington D.C.":"DC"}


def check_address(data):
    api = f'https://publicapi-p.evine.net/QASValidationAPI/api/Web/ScrubAddresses'
    header = {
        'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '181',
    'Content-Type': 'application/json',
    'Host': 'publicapi-p.evine.net',
    'Origin': 'https://www.shophq.com',
    'Referer': 'https://www.shophq.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
        }
    address = data['street']
    city = data['city']
    state = data['state']
    zipcode = data['zip']
    state_code = list_state_code[state]
    playload = [{"Address1":f"{address}","Address2":f"{address}","City":f"{city}","State":f"{state_code}","Zip":f"{zipcode}","AddressType":"1","DPV":"N","QasAddressValidation":"True"}]
    print(playload)
    try:
        response = session().post(url=api , headers= header , json=playload).json()[0]['QASResponseType']
        print(response)
        if response == 0:
            with open('good_address.txt','a',encoding='utf-8') as f:
                f.write(str(data)+'\n')
                print(data)
        else:
             with open('bad_address.txt','a',encoding='utf-8') as f:
                f.write(str(data)+'\n')
                print(data)

    except Exception as exp_msg:
        print(exp_msg)
        with open('error.txt','a',encoding='utf-8') as f:
                f.write(str(data)+'\n')
                print(data)

from json import loads
data_list = open('data.txt','r',encoding='utf-8').readlines()
for x in data_list:
    data = x.strip()
    try:
        check_address(data=loads(data))
    except:
        pass
