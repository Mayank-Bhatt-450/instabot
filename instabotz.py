import shutil,time,datetime
from instabot import Bot
import requests
import secrets,json,os,secrets
username=os.environ['user']
password=os.environ['pass']
to_name=os.environ['celeb']
host='http://mayankbhatt.pythonanywhere.com/'
name=''
for i in range(10):
    name+=secrets.choice([chr(ii) for ii in range(97,122)])
days=0
tem_days=0
#'''
for i in range(0,24):
        #print(24-i,'hours left to next msg , day=',days,' time= ',str(datetime.datetime.now()))
        requests.post(host,{'msg':str([24-i,'hours left to next msg , day=',days,' time_now= ',str(datetime.datetime.now()),' expected_time=',str(datetime.datetime.now()+datetime.timedelta( hours=24-i))])                    })
        requests.post(host+'error',{'msg':name+'     time_now= '+str(datetime.datetime.now())})
        time.sleep(3600)


x = requests.get(host+'insta_day')
try:
    replace_letters=json.loads(str(requests.get(host+'get_replace_data').text))
    text_list=json.loads(requests.get(host+'insta_msg').text)
except Exception as ef:
    requests.post(host+'error',{'msg':name+'   '+str(ef)+'\n time='+str(datetime.datetime.now())})
    hjkhkjhk
days=int(x.text)
try:
    shutil.rmtree('config')
except:
    pass
bot = Bot()
bot.login(username=username, password=password)
user_id = bot.get_user_id_from_username(to_name)
text=str(secrets.choice(text_list)+
         '\n if {u} {r} reading this then {plz} read {convo} from the start{emoji_sweet}')
for i in replace_letters:
    #print('i=',i)
    text=text.replace('{'+str(i)+'}',str(secrets.choice(replace_letters[i])))


bot.send_message(secrets.choice(replace_letters['day'])+' '+str(days)+'  '+secrets.choice(replace_letters['emoji_for_greeting'])+'\n'+text, user_id)

try:
    x1 = requests.post(host+'insta_day')
except Exception as ef:
    requests.post(host+'error',{'msg':name+'   '+str(ef)+'\n time='+str(datetime.datetime.now())})
    time.sleep(360)
    dfgdg
print('should sleep days='+str(days)+' time= '+str(datetime.datetime.now()))



#'''

