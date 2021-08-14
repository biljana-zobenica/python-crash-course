
def send_messages (messages, sent_messages):
    print(f"Printed messages:")
    while messages:
        current_message = messages.pop()
        print(f"\t{current_message}")
        sent_messages.append(current_message)
    
    print(f"Sent messages:")
    for message in sent_messages:
        print(f"\t{message}")

messages = ['Be brave!', 'Make each day count.', 'Keep calm and just smile!']
sent_messages = []

send_messages(messages, sent_messages)

print(messages)
print(sent_messages)