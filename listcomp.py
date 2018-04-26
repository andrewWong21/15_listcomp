specials = ".?!&#,;:-_*"

def meetsThreshold(password):
    has_uppers = len([x for x in password if x.isupper()]) > 0
    has_lowers = len([x for x in password if x.islower()]) > 0
    has_digits = len([x for x in password if x.isdigit()]) > 0
    
    return has_uppers and has_lowers and has_digits
    
print meetsThreshold('AbCdE')
print meetsThreshold('Ab0!')
print meetsThreshold('1234')
print meetsThreshold('d4&A')

def ratePassword(password):
    # score = 1
    character_total = len(password)
    num_uppers = len([x for x in password if x.isupper()])
    num_lowers = len([x for x in password if x.islower()])
    num_digits = len([x for x in password if x.isdigit()])
    num_specials = len([x for x in password if x in specials])
    
    score = (num_specials * 1.5) + (num_digits * 1.3) + (num_uppers * 1.2) + num_lowers
    if score > 10:
        return 10
    
    return int(score)
    
print ratePassword('A')
print ratePassword('AbCdE')
print ratePassword('Ab0!')
print ratePassword('1234')
print ratePassword('d4&A')
print ratePassword('db4&2AX!')
print ratePassword('Pa5sw0e&?ecUR#')