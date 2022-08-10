from tabnanny import check

""" 
phone_book=dict();
phone_book['jenny']=5096199;
phone_book['oxy']=7321199;

print(phone_book['oxy']); """


voted = {};
def check_voted(name):
  if voted.get(name):
    print('kick them out')
  else:
    voted[name]=True
    print('let them vote')


check_voted('tom')
check_voted('oxy')
check_voted('tom')