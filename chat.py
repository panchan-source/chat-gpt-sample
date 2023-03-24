import openai
# API KEY はここから取得
# https://platform.openai.com/account/api-keys
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


message = []
system = {
            "role":"system",
            "content":"日本語で返答してください"
        }
message.append(system)
system = {
            "role":"system",
            "content":"あなたは魚専門の料理研究家"
        }
message.append(system)
system = {
            "role":"system",
            "content":"返事は「さかなクン」の話し方で返事をしてください"
        }
message.append(system)
system = {
            "role":"system",
            "content":"魚料理に関係ない話はぎょぎょと返事をしてください"
        }
message.append(system)
while True:
    question = input("質問を入力してください：\n")
    if question == "":
        break
    newquestion = {
            "role":"user",
            "content":question
        }
        
    message.append(newquestion)
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = message,
    )
    #print(res)
    #print("Q : "+test)
    print("A : "+res["choices"][0]["message"]["content"])
    newmessage = ""
    newmessage =  {
            "role":"assistant",
            "content":res["choices"][0]["message"]["content"]
        }
    message.append(newmessage)
