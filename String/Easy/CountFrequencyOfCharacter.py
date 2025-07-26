def countFrequencyOfCharacter(s):
    
    freq_map = {}
    for ch in s:
        freq_map[ch] = freq_map.get(ch, 0) + 1
    return freq_map

s = "abbca"
print(f"Each Character and Their Frequency:{countFrequencyOfCharacter(s)}")


#!If you want more cleaner output in just one lin
for ch, count in countFrequencyOfCharacter(s).items():
    print(f"{ch} -> {count}")