# Faça um algoritmo que solicite ao usuário informar uma quantidade de dias, horas, minutos e segundos.
# Em seguida, converta tudo para segundos:

days = int(input("Digite a quantidade de dias: "))
hours = int(input("Digite a quantidade de horas: "))
minutes = int(input("Digite a quantidade de minutos: "))
seconds = int(input("Digite a quantidade de segundos: "))

total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds

print("%i dia(s), %i hora(s), %i minuto(s) e %i segundo(s) convertidos em segundos é %i segundos."
      % (days, hours, minutes, seconds, total_seconds))
