n=int(input("Введите кол-во английских слов в словаре: "))
lat_to_eng= {}
for i in range(n):
    eng_word, lat_word = input().split(' - ')
    lat_list = lat_word.split(', ')
    for latin_word in lat_list:
            lat_to_eng[latin_word] = set()
            lat_to_eng[latin_word].add(eng_word)

print(len(lat_to_eng))
for latin_word, eng_translations in sorted(lat_to_eng.items()):
    print(latin_word + ' - ' + ', '.join(eng_translations))
