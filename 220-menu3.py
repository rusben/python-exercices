from math import pi

radi=int(raw_input('\nIntrodueix el radi: '))

print '\na. Calcular area circunferencia'
print 'b. Calcular longitud circunferencia'
print 's. Sortir'
opcio=raw_input('escull opcio: ')

while opcio<>'s':

 if opcio=='a':
      area = pi*radi*radi
      print area
 else: 
     if opcio=='b':
        longitud = 2 * pi * radi
        print longitud
     else: 
	 if opcio<>'s': 
            print '\nOpcio incorrecta !!\n'

 print '\na. Calcular area circunferencia'
 print 'b. Calcular longitud circunferencia'
 print 's. Sortir'
 opcio=raw_input('escull opcio: ')

print 'Deu !!'
