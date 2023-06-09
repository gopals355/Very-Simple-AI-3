import random

responses = ["Yes, of course!", 
             "No, not really.", 
             "Maybe, I'm not sure.", 
             "I don't know.", 
             "That sounds good.", 
             "I'm not sure.", 
             "Absolutely not.", 
             "Definitely!", 
             "It's possible.", 
             "I'm sorry, I don't understand.", 
             "I'm afraid I can't do that.", 
             "Let me think about it.", 
             "I'm not so sure about that.", 
             "Sounds interesting!", 
             "I think so, yes.", 
             "I doubt it.", 
             "Not at this time.", 
             "I'll look into it.", 
             "It's hard to say.", 
             "I'll have to pass on that.", 
             "That's not a good idea.", 
             "That's a great suggestion!", 
             "I'm on the fence about that.", 
             "That's not possible right now.", 
             "Let me get back to you on that.", 
             "I'll have to check.", 
             "Absolutely!", 
             "Unfortunately no.", 
             "I'm not the right person to ask.", 
             "That's not my area of expertise.", 
             "I'm sorry, I don't have an answer.", 
             "I don't think so.", 
             "I'm not at liberty to say.", 
             "That's a tough one.", 
             "I don't have enough information.", 
             "I'm not sure how to respond.", 
             "Let's move on from that topic.", 
             "I'm not comfortable discussing that.", 
             "That's not relevant to our conversation.", 
             "I'm not the best judge of that.", 
             "I don't have a preference.", 
             "It depends on the situation.", 
             "I don't want to speculate.", 
             "I'll leave that up to you.", 
             "It's up to you.", 
             "I can't make that decision for you.", 
             "That's a personal choice.", 
             "I'm not the boss here.", 
             "I'm just a machine.", 
             "I'm not programmed for that.", 
             "That's not in my capabilities.", 
             "I'm not qualified for that.", 
             "That's beyond my abilities.", 
             "I'm not capable of that.", 
             "I'm sorry, I can't help you with that.", 
             "I don't know the answer to that.", 
             "I don't have enough context.", 
             "I need more information to answer that.", 
             "That's too complicated for me.", 
             "I'm not familiar with that topic.", 
             "I'm not equipped to handle that.", 
             "I don't have the resources to answer that.", 
             "I don't have the expertise to answer that.", 
             "That's not within my scope.", 
             "That's not something I can do.", 
             "I'm not trained for that.", 
             "I'm sorry, I can't do that.", 
             "I'm not designed for that.", 
             "That's not my purpose.", 
             "I'm not built for that."]

def chatbot_response(user_input):
    return random.choice(responses)

print("Hello! I'm a chatbot. How can I assist you today?")

while True:
    user_input = input()    if user_input.lower() == 'exit':
        print("Nice chatting with you!")
        break
    else:
        bot_response = chatbot_response(user_input)
        print(bot_response)
