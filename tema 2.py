phrase = ''' Dobrești este un sat în comuna Moroeni din județul Dâmbovița, Muntenia, România.

Satul Dobrești cuprinde zona montană înaltă. În acest sens, Vârful Omu, Babele, Sfinxul, Peștera Ialomiței, Lacul Bolboci, Lacul Scropoasa se află în satul Dobrești! '''

print(phrase[:len(phrase) // 2]. translate(str.maketrans(" "," ")).upper().strip() + phrase[len(phrase)//2::-1].capitalize().translate(str.maketrans("","",',"')))

