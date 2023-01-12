from coverage import CoverageData

def read():
    data = CoverageData()
    # print(data.data_filename())
    data.read()
    # print(data.measured_files)
    pairs = data.arcs('/Users/mpatrick/workspace/test/coverage-test/sut.py')
    
    if pairs:
        print(len(pairs))
        for pair in pairs:
            print(pair)
    else:
        print('No Data')

if __name__ == '__main__':
    read()