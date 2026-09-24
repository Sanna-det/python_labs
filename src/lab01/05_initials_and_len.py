d = input("ФИО: ").split()

print(f"Инициалы: {''.join([i[0].upper() for i in d])}.")
print(f"Длина (символов): {len(' '.join(d))}")