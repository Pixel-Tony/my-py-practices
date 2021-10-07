phrase_1 = input('Введите первую фразу: ')
phrase_2 = input('Введите вторую фразу: ')
phrase_1 = phrase_1.lower()
phrase_2 = phrase_2.lower()
i = j = 0
set_1 = set() 
set_2 = set()
for i in phrase_1:
    if i.isalpha() == 1:
        set_1.add(i)

for j in phrase_2:
    if j.isalpha() == 1:
        set_2.add(j)

print(set_1, set_2)
if set_2.issubset(set_1):
    print('Вы можете составить вторую фразу из первой')
else:
    print('Вы не можете составить вторую фразу из первой')
    
# vtoraya

d = {
'a': 1,'e': 1,'i': 1,'l': 1,'n': 1,'o': 1,'r': 1,'s': 1,'t': 1,'u': 1,
'd': 2,'g': 2,
'b': 3,'c': 3,'m': 3,'p': 3,
'f': 4,'h': 4,'v': 4,'w': 4,'y': 4,
'k': 5,
'j': 8,'x': 8,
'q': 10,'z': 10,
' ': -2
}

player_phrase = input('Ваша фраза: ')
char = 0
score = str()
phrase_tuple = tuple(player_phrase)
value = 0
for char in phrase_tuple:
        if char.isspace() == 1:
            if value == 0:
                continue
            score += str(value)+str(' ')
            value = 0
        elif char.isalpha() == 1:     
            value += d[char.lower()]
print(score+str(value))       