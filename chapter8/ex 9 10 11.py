messages=['message1','message2','message3']
sent_messages=[]

def show_messages(messages, sent_messages):
    while messages:
        current_message =  messages.pop()
        print(f"Le message '{current_message}' est envoyé.")
        sent_messages.append(current_message)

show_messages(messages[:], sent_messages)
print(messages)