import shutil,time,datetime
from instabot import Bot
import requests
import random,json,os
username=os.environ['user']
password=os.environ['pass']
to_name=os.environ['celeb']
host='http://mayankbhatt.pythonanywhere.com/'

days=0
tem_days=0
#'''
while True:
    try:
        x = requests.get(host+'insta_day')
        replace_letters=json.loads(str(requests.get(host+'get_replace_data').text))
        text_list=json.loads(requests.get(host+'insta_msg').text)
        days=int(x.text)
        
        try:
            shutil.rmtree('config')
        except:
            pass
        #'''
        bot = Bot()
        bot.login(username=username, password=password)
        user_id = bot.get_user_id_from_username(to_name)
        #'''
        #print(type(replace_letters))
        text=str(random.choice(text_list)+
                 '\n if {u} {r} reading this then {plz} read {convo} from the start{emoji_sweet}')
        for i in replace_letters:
            #print('i=',i)
            text=text.replace('{'+str(i)+'}',str(random.choice(replace_letters[i])))
                                                               
        #'''
        bot.send_message(random.choice(replace_letters['day'])+' '+str(days)+'  '+random.choice(replace_letters['emoji_for_greeting'])+'\n'+text, user_id)
        user_info = bot.get_user_info(user_id)
        # print(user_info['biography'])
        #'''
        
        x1 = requests.post(host+'insta_day')
        print('should sleep days='+str(days)+' time= '+str(datetime.datetime.now()))
        for i in range(0,24):
            #print(24-i,'hours left to next msg , day=',days,' time= ',str(datetime.datetime.now()))
            requests.post(host,{'msg':str([24-i,'hours left to next msg , day=',days,' time_now= ',str(datetime.datetime.now()),' expected_time=',str(datetime.datetime.now()+datetime.timedelta( hours=24-i))])
                                })
            time.sleep(3600)
            
    except Exception as e:
        print(e)
        try:
            requests.post(host+'error',{'msg':str(e)+'\n time='+str(datetime.datetime.now())})
        except Exception as ee:
            print(ee)      
#'''
