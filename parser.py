import pandas as pd 
  
data = pd.read_json('messages.json')

sender= input('Sender Username: ')
receiver= input('Receiver Username: ')

messages = []

template = '<html><head><title>IGDM Parser</title></head><style>@import url(https://fonts.googleapis.com/css?family=Poppins:200,400);:root{--green:#00bc84;--light-grey:#dce8e8;--dark-grey:#4a575b}*{box-sizing:border-box;margin:0;padding:0}body{font-family:Poppins,sans-serif;font-size:14px;color:var(--dark-grey)}img{height:250px;margin:0 1em;box-shadow:0 2px 5px rgba(0,0,0,.1);align-self:flex-end}input[type=text]:focus{outline:0}h3{font-size:22px;font-weight:300;padding:2rem 0 4rem 0;text-transform:uppercase}h3 span{display:block;text-align:center;color:var(--green);font-size:16px;font-weight:400;border-bottom:1px solid var(--light-grey)}.wrapper{max-width:400px;margin:0 auto;padding:0 1em;display:flex;flex-direction:column;justify-content:center;align-items:center}.chat-item{display:flex;align-items:center;margin-bottom:1em;overflow:hidden}.chat-item_body{padding:1em 2em;border:1px solid var(--light-grey);border-radius:40px;border-bottom-left-radius:0;box-shadow:0 1px 5px rgba(0,0,0,.1);align-self:flex-end}.chat-item_body.alt{background-color:var(--light-grey);border-bottom-left-radius:0}.new-message{margin-top:4em;margin-bottom:2rem;display:flex;border:1px solid var(--green);border-radius:20px;overflow:hidden}.message-body{border:0;padding:1em 2rem}.message-button{background-color:var(--green);border:none;padding:0 1em;color:var(--light-grey);cursor:pointer}</style><body><div class="wrapper"><h3>IGDM Parser</h3><section class="chat-interface">'

for i in range(len(data)):
    if receiver in data['participants'][i]:
        for _ in range(len(data['conversation'][i])):
            if 'text' in data['conversation'][i][_]:
                if data['conversation'][i][_]['sender'] == receiver:
                    html = '<figure class="chat-item"><figcaption class="chat-item_body">'+data["conversation"][i][_]["text"]+'</figcaption></figure>'
                else:
                    html = '<figure class="chat-item"><figcaption class="chat-item_body alt">'+data["conversation"][i][_]["text"]+'</figcaption></figure>'
            elif 'media' in data['conversation'][i][_]:
                if data['conversation'][i][_]['sender'] == receiver:
                    html = '<figure class="chat-item"><figcaption class="chat-item_body"><img src="'+data["conversation"][i][_]["media"]+'"></figcaption></figure>'
                else:
                    html = '<figure class="chat-item"><figcaption class="chat-item_body alt"><img src="'+data["conversation"][i][_]["media"]+'"></figcaption></figure>'
            elif 'media_share_url' in data['conversation'][i][_]:
                if data['conversation'][i][_]['sender'] == receiver:
                    html = '<figure class="chat-item"><figcaption class="chat-item_body"><img src="'+data["conversation"][i][_]["media_share_url"]+'"></figcaption></figure>'
                else:
                    html = '<figure class="chat-item"><figcaption class="chat-item_body alt"><img src="'+data["conversation"][i][_]["media_share_url"]+'"></figcaption></figure>'
            elif 'profile_share_username' in  data['conversation'][i][_]:
                if data["conversation"][i][_]["profile_share_username"] is not None:
                    if data['conversation'][i][_]['sender'] == receiver:
                        html = '<figure class="chat-item"><figcaption class="chat-item_body">'+data["conversation"][i][_]["profile_share_username"]+'</figcaption></figure>'
                    else:
                        html = '<figure class="chat-item"><figcaption class="chat-item_body alt">'+data["conversation"][i][_]["profile_share_username"]+'</figcaption></figure>'
            messages.append(html)
    else:
        print('One or more of the given usernames not found.')
        break

messages = messages[::-1]

if len(messages) > 1:
    with open("chat.html", "w") as file:
        file.write(template)
    with open('chat.html', 'a') as f:
        for item in messages:
            f.write("%s\n" % item)
    print('Parsed '+str(len(messages))+' messages to chat.html')
