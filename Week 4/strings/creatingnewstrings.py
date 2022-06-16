#Copy these into the interpreter to see the response

message = "A kong string with a silly typo"

new_message = message[0:2] + "l" + message[3:]
print(new_message)

message2 = "This is  new message"
print(message2)

message3 = "and another one"
print(message3)

pets = "Cats & Dogs"
pets.index("&")

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])

"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])

"This is another example".split()