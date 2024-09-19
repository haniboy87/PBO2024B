nama_tactical_doll = input("Masukkan nama Tactical Doll: ")
firepower = int(input("Masukkan nilai Firepower: "))
rate_of_fire = int(input("Masukkan nilai Rate of Fire: "))
accuracy = int(input("Masukkan nilai Accuracy: "))
evasion = int(input("Masukkan nilai Evasion: "))

def hitung_dps(firepower, rate_of_fire):
    dps = (firepower * rate_of_fire) / 60
    return round(dps, 2) 

def combat_effectiveness(firepower, rate_of_fire, accuracy, evasion):
    combat_effectiveness = (
        30 * firepower + 
        40 * (rate_of_fire**2 / 120) +
        15 * (accuracy + evasion)
    )
    return int(combat_effectiveness)

dps = hitung_dps(firepower, rate_of_fire)
ce = combat_effectiveness(firepower, rate_of_fire, accuracy, evasion)

print("\n===== Tactical Doll Info =====")
print(f"Nama Tactical Doll: {nama_tactical_doll}")
print(f"Firepower: {firepower}")
print(f"Rate of Fire: {rate_of_fire}")
print(f"Accuracy: {accuracy}")
print(f"Evasion: {evasion}")
print(f"Damage per second (DPS): {dps}")
print(f"Combat effectiveness (CE): {ce}")
