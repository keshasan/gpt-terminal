import openai
# ��������� ���� �� ������� �������� openai
openai.api_key = "sk-95Ez2Z1rtgegrRTFFDSTVTdsdfsgdv3422kjhLghnh53QiT8F"
messages = []
while True:
    message = input("User: ")   # ������ ���������
    if message == "quit": break
     
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages)
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role":"assistant", "content": reply})