def get_data(path):
    file = open(path)
    lines = file.read().splitlines()
    file.close()
    lines = [lines[i] for i in range(len(lines)) if i % 4 == 1]
    return lines


def print_results(r, ln, rep, gc):
    print(f'Reads in the file = {len(r)}')
    print(f'Reads sequence average length = {ln}')
    print(f'\nRepeats = {rep}')
    print(f'\nGC content average = {gc}%')


def av_length(data):
    lengths = dict()
    for line in data:
        lengths[len(line)] = 1 if len(line) not in lengths else lengths[len(line)] + 1
    return round(sum(x * lengths[x] for x in lengths) / sum(lengths.values()))


def av_gc_cont(data):
    gc_cont = list()
    for line in data:
        gc_cont.append(round((line.count('G') + line.count('C')) / len(line) * 100, 2))
    return round(sum(gc_cont) / len(gc_cont), 2)


reads = get_data(input())
av_len = av_length(reads)
av_GC = av_gc_cont(reads)
repeats = len(reads) - len(set(reads))
print_results(reads, av_len, repeats, av_GC)
