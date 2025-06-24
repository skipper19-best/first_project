import string
import random

while True:
 while True:
  try:
    length=int(input("Введи длину пароля:"))
    if length>0:
       break
    else:
      print("Ошибка:число должно быть больше 0")
  except ValueError:
   print("Ошибка:нужно ввести целое число")
 symbols=string.ascii_letters
 password_list=random.choices(symbols,k=length)
 password=''.join (password_list)
 print("Сгенерированный пароль:",password)
 ответ=input("еще раз?,(да/нет:) ").lower()
 if ответ != 'да':
   break

