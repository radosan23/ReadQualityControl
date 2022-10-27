import gzip


class FASTQdata:

    def __init__(self, path):
        self.reads = FASTQdata.get_data(path)
        self.av_len = self.av_length()
        self.av_GC = self.av_gc_cont()
        self.repeats = len(self.reads) - len(set(self.reads))
        self.ln_with_n, self.ns_per_seq = self.ns_seq()
        self.quality = self.eval_quality()

    @staticmethod
    def get_data(path):
        file = gzip.open(path, 'rt')
        lines = str(file.read()).splitlines()
        file.close()
        lines = [lines[i] for i in range(len(lines)) if i % 4 == 1]
        return lines

    def print_results(self):
        print(f'Reads in the file = {len(self.reads)}')
        print(f'Reads sequence average length = {self.av_len}')
        print(f'\nRepeats = {self.repeats}')
        print(f'Reads with Ns = {self.ln_with_n}')
        print(f'\nGC content average = {self.av_GC}%')
        print(f'Ns per read sequence = {self.ns_per_seq}%')

    def av_length(self):
        lengths = {}
        for line in self.reads:
            lengths[len(line)] = 1 if len(line) not in lengths else lengths[len(line)] + 1
        return round(sum(x * lengths[x] for x in lengths) / sum(lengths.values()))

    def av_gc_cont(self):
        gc_cont = list()
        for line in self.reads:
            gc_cont.append(round((line.count('G') + line.count('C')) / len(line) * 100, 2))
        return round(sum(gc_cont) / len(gc_cont), 2)

    def ns_seq(self):
        ns = [round(line.count('N') / len(line) * 100, 2) for line in self.reads if 'N' in line]
        return len(ns), round(sum(ns) / len(self.reads), 2)

    def eval_quality(self):
        return 1 / (self.repeats + self.ln_with_n + self.ns_per_seq)
