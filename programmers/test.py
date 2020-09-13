import re
def clean(id) :
    new_id = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》{}]', '', id)
    return new_id

'~!@#$%^&*()=+[{]}:?,<>'

new_id = "...!@BaT#*..y.abcdefghijklm~!@#$%^&*()=+[{]}:?,<>"
new_id = new_id.lower()
new_id = clean(new_id)
new_id = re.sub('[.]{1,}','.', new_id)
print(new_id)

if new_id :
    if new_id[0] == '.':
        new_id = new_id[1:]
    elif new_id[-1] == '.':
        new_id = new_id[:-1]

print(4)
print(new_id)

if not new_id:
    new_id = 'a'
print(5)
print(new_id)

if len(new_id) >= 16 :
    new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
print(6)
print(new_id)

if len(new_id) <= 2 :
    while len(new_id) < 3 :
        new_id += new_id[-1]

print(new_id)