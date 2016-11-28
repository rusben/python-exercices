from math import pi

radi=int(raw_input('Introdueix el radi: '))

print 'a. Calcular area circunferencia'
print 'b. Calcular longitud circunferencia'

opcio=raw_input('escull opcio: ')

if opcio=='a':
      area = pi*radi*radi
      print 'el resultat es', area

elif opcio=='b':
        longitud = 2 * pi * radi
        print 'el resultat de la longitud es', longitud
else: print 'Opcio incorrecta'
