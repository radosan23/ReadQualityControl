def get_data(path):
    file = open(path)
    lines = file.read().splitlines()
    file.close()
    lines = [lines[i] for i in range(len(lines)) if i % 4 == 1]
    return lines


def print_results(r, ln, rep, gc, n, nps):
    print(f'Reads in the file = {len(r)}')
    print(f'Reads sequence average length = {ln}')
    print(f'\nRepeats = {rep}')
    print(f'Reads with Ns = {n}')
    print(f'\nGC content average = {gc}%')
    print(f'Ns per read sequence = {nps}%')


def av_length(data):
    lengths = {}
    for line in data:
        lengths[len(line)] = 1 if len(line) not in lengths else lengths[len(line)] + 1
    return round(sum(x * lengths[x] for x in lengths) / sum(lengths.values()))


def av_gc_cont(data):
    gc_cont = list()
    for line in data:
        gc_cont.append(round((line.count('G') + line.count('C')) / len(line) * 100, 2))
    return round(sum(gc_cont) / len(gc_cont), 2)


def ns_seq(data):
    ns = [round(line.count('N') / len(line) * 100, 2) for line in data if 'N' in line]
    return len(ns), round(sum(ns) / len(data), 2)


reads = get_data(input())
av_len = av_length(reads)
av_GC = av_gc_cont(reads)
repeats = len(reads) - len(set(reads))
with_n, ns_per_seq = ns_seq(reads)
print_results(reads, av_len, repeats, av_GC, with_n, ns_per_seq)
