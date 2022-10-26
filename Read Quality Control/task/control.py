from fastqdata import FASTQdata


def main():
    data1 = FASTQdata(input())
    data2 = FASTQdata(input())
    data3 = FASTQdata(input())
    best = max(data1, data2, data3, key=FASTQdata.eval_quality)
    best.print_results()


if __name__ == '__main__':
    main()
