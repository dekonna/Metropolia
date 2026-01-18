import random

#kolmen numeron koodin arvonta 0-9
kolmen_koodi1 = random.randint(0, 9)
kolmen_koodi2 = random.randint(0, 9)
kolmen_koodi3 = random.randint(0, 9)

#neljän numeron koodin arvonta 1-6
neljan_koodi1 = random.randint(1, 6)
neljan_koodi2 = random.randint(1, 6)
neljan_koodi3 = random.randint(1, 6)
neljan_koodi4 = random.randint(1, 6)

#tulosteet
print(f"Kolmen numeron koodi on: {kolmen_koodi1}-{kolmen_koodi2}-{kolmen_koodi3}")
print(f"Neljän numeron koodi on: {neljan_koodi1}-{neljan_koodi2}-{neljan_koodi3}-{neljan_koodi4}")