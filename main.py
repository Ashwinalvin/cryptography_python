def machine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    value = keys[-1]+keys[0:-1] # this line is up to designer i can change it yhe way i want
    encry = dict(zip(keys,value))
    decry = dict(zip(value,keys))
    msg=input("enter the message ")
    mode=input("enter E for encryption and enter D for decryption")
    if mode=='E':
        new_message = [encry[i] for i in msg.lower()]
        new_message = ''.join(new_message)
    if mode=='D':
        new_message = [decry[i] for i in msg.lower()]
        new_message = ''.join(new_message)
    return new_message
print(machine())
# here we use dictonary concept
#for dictanry 1
#message is my keys and value is my encrypted
# for dictnary 2
# encrypted is my keys and value will be output message
# note print(dict1[i]) output will be its value
#dict1={H:g,e:}
