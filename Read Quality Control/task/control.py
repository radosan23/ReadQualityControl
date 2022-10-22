path = input()
file = open(path)
lines = file.read().splitlines()
lines = [lines[i] for i in range(len(lines)) if i % 4 == 1]
file.close()
lengths = {}
for line in lines:
    lengths[len(line)] = 1 if len(line) not in lengths else lengths[len(line)] + 1
av_len = round(sum(x * lengths[x] for x in lengths) / sum(lengths.values()))
print(f'Reads in the file = {len(lines)}:')
for length in list(sorted(lengths.keys())):
    print(f'\twith length {length} = {lengths[length]}')
print('\nReads sequence average length = ', av_len)
