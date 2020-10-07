from datetime import datetime, date

checksumInt = 0

def checksum(pesel):
  if len(pesel) != 11:
    print("Not valid pesel")
    return
  elif not pesel.isnumeric():
    print("Provide only numbers")
    return
  else:
    print("Validating...")
    multiplers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    array = list(map(int, pesel))
    global checksumInt
    sum_control = 0
    for i in range(len(array) - 1):
      checksumInt += multiplers[i] * array[i]

    sum_control = checksumInt % 10
    if array[10] != 0:
      sum_control = 10 - sum_control
    print(f"Checksum: {sum_control == array[10]}")
    showPeselInfo(pesel)

def showPeselInfo(pesel):
  yearDecode = [19, 20, 21, 22, 18]
  byear = int(str(yearDecode[int(pesel[2]) // 2]) + pesel[0:2])
  months = ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia", "września", "października", "listopada", "grudnia"]
  month = months[getMonth(pesel)]
  gender = getGender(pesel)
  t1 = date.today()
  t2 = date(year=int(byear), month=int(getMonth(pesel)), day=int(pesel[4]))
  print("------------------------")
  print(f"Rok urodzenia: {pesel[4]}{pesel[5]} {month} {byear}")
  print(f"Numer seryjny: {pesel[7]}{pesel[8]}{pesel[9]}")
  print(f"Płeć: {gender}")
  print(f"Suma kontrolna: {checksumInt} ({pesel[10]})")
  print(f"Wiek: {t1 - t2}")

def getMonth(pesel):
  month = 10 * int(pesel[2])
  month += int(pesel[3])
  if month > 80 and month < 93:
    month -= 80
  elif month > 20 and month < 33:
    month -= 20
  elif month > 40 and month < 53:
    month -= 40
  elif month > 60 and month < 73:
    month -= 60
  return month

def getGender(pesel):
  if int(pesel[9]) % 2 == 1:
    return "Mężczyzna"
  else:
    return "Kobieta"


typedpesel = input("Enter pesel: ")
checksum(typedpesel)