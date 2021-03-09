import shutil,time,datetime
from instabot import Bot
import os
text_list=["{stillornot} waiting for ur replay {emoji_sweet}  ",
"{grettings}{emoji_hi}  Billie hope you {r} doing well {emoji_sweet}, just a reminder i m {stillornot} waiting for {ur} reply  {emoji_funny} ",
"{grettings}{emoji_hi}  Billie still waiting for {ur} reply {emoji_sweet}have a nice day ",
"{grettings}{emoji_hi} , its bhatt how {u} doing just wanna tell i {m} {stillornot} waiting for {ur} replay",
"wanna tell {u} a secre 🤐 that i {m} {stillornot} waiting for {ur} reply  {emoji_funny} l0l",
"i know what {u} {r}forgetting ,................................................................................1...........................................................................................2..................................................................................3.................................................................. replying me {emoji_funny}",
'how determined i m i hope {u} see {emoji_sweet} , don`t you forget replying me lol {emoji_funny}  try to rhyme but {u} got the msg']



import random
#'''
username=os.environ['user']
password=os.environ['pass']
to_name=os.environ['celeb']
while True:
    try:
        file=open('days.txt','r')
        days=int(file.read())
        file.close()
        try:
            shutil.rmtree('config')
        except:
            pass
        
        bot = Bot()
        bot.login(username=username, password=password)
        user_id = bot.get_user_id_from_username(to_name)
        text=str(text_list[random.randint(0,len(text_list))]+'\n if {u} {r} reading this then {plz} read {convo} from the start{emoji_sweet}').format(grettings =random.choice(['hi','hey','yo','hello']),
                                                                stillornot=random.choice(['still','']),
                                                                u=random.choice(['u','you']),
                                                                ur=random.choice(['ur','your']),
                                                                m=random.choice(['m','am']),
								r=random.choice(['r','are']),
								plz=random.choice(['please','plz']),
								convo=random.choice(['','the conversation']),
								emoji_funny=random.choice(['😂','🤣','😁','😜']),
								emoji_sweet=random.choice(['😇','😊','☺️','🤗','🤭','😋']),
								emoji_hi=random.choice(['👋🏻','🤚🏻','🖐🏻','✋🏻','🖖🏻','🤟🏻','🤘🏻']), 
								                                                      
                                                                )
        bot.send_message(random.choice(['DAY', '𝔇𝔄𝔜',  '𝕯𝕬𝖄',  '𝓓𝓐𝓨',  '𝒟𝒜𝒴',  '𝔻𝔸𝕐',  'ＤＡＹ',  '𝐃𝐀𝐘',  '𝗗𝗔𝗬',  '𝘋𝘈𝘠',  '𝘿𝘼𝙔',  '𝑫𝑨𝒀',  '𝙳𝙰𝚈',  '｡｡  🎀  𝒟𝒜𝒴  🎀  ｡｡',  'ᴅᴀʏ',  '⅄∀ᗡ',  'D⃣   A⃣   Y⃣',  '🄳🄰🅈',  'YAᗡ',  'D̴͍̺͚̣͍̗̥̤̱͒̄͛͂̾ͅA̶̢̪͗̏̓̅́̃̄̊̚ͅÝ̵̗͖̦̾̍́́͐̔',  '🅳🅰🆈',  'DₐY',  'ᴰᴬʸ',  'ⒹⒶⓎ',  '๔คץ',  'DAY',  'ɖǟʏ',   'ɖąყ',  '໓คฯ',  'DΛY',  '∂αу',  'ÐÄ¥',  'Đ₳Ɏ',  'ᗪ卂ㄚ',  'りﾑﾘ',  '【D】【A】【Y】',  '『D』『A』『Y』',  '≋D≋A≋Y≋',  '░D░A░Y░',  '(っ◔◡◔)っ ♥ DAY ♥',  '[̲̅D][̲̅A][̲̅Y]',  'D҉A҉Y҉',  'ᎠȺӋ',  'ᗪᗩY',  'ᕲᗩᖻ',  'D̶A̶Y̶',  'D̴A̴Y̴',  'D̷A̷Y̷',  'D̲A̲Y̲',  'D̳A̳Y̳',  'D̾A̾Y̾',  'D♥A♥Y',  'D͎A͎Y͎',  'D͓̽A͓̽Y͓̽', 'Day'])+' '+str(days)+'  '+random.choice(['🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐻‍❄️','🐯','🦁','🐮','🐸','🐵','🙈','🙉','🙊','🐒','🐔','🐧','🐦','🐤','🐣','🐥','🦆','🦅','🦉','🦇','🐺','🐗','🐴','🦄','🐝','🐛','🦋','🐌','🐞','🐜','🦟','🦗','🕷','🕸','🦂','🐢','🐍','🦎','🦖','🦕','🐙','🦑','🦐','🦞','🦀','🐡','🐠','🐟','🐬','🐳','🐋','🦈','🐊','🐅','🐆','🦓','🦍','🦧','🐘','🦛','🦏','🐪','🐫','🦒','🦘','🐃','🐂','🐄','🐎','🐖','🐏','🐑','🦙','🐐','🦌','🐕','🐩','🦮','🐕‍','🦺','🐈','🐈‍⬛','🐓','🦃','🦚','🦜','🦢','🦩','🕊','🐇','🦝','🦨','🦡','🦦','🦥','🐁','🐀','🐿','🦔','🐾','🐉','🐲','🌵','🎄','🌲','🌳','🌴','🌱','🌿','☘️','🍀','🎍','🎋','🍃','🍂','🍁','🍄','🐚','🪨','🌾','💐','🌷','🌹','🥀','🌺','🌸','🌼','🌻','🌞','🌝','🌛','🌜','🌚','🌕','🌖','🌗','🌘','🌑','🌒','🌓','🌔','🌙','🌎','🌍','🌏','🪐','💫','⭐️','🌟','✨','⚡️','☄️','💥','🔥','🌪','🌈','☀️','🌤','⛅️','🌥','☁️','🌦','🌧','⛈','🌩','🌨','❄️','☃️','⛄️','🌬','💨','💧','☔️','☂️','🌊','🌫'])+'\n'+text, user_id)
        user_info = bot.get_user_info(user_id)
        # print(user_info['biography'])
        days+=1

        file=open('days.txt','w')
        file.write(str(days))
        file.close()
        print('should sleep days='+str(days)+' time= '+str(datetime.datetime.now()))
        for i in range(0,24):
            print(24-i,'hours left to next msg , day=',days,' time= ',str(datetime.datetime.now()))
            time.sleep(3600)
            

    except Exception as e:
        print(e)
        pass
        

        
#'''
