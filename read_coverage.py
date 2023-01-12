from coverage import CoverageData

def read():
    data = CoverageData()
    data.read()
    pairs = data.arcs('/Users/mpatrick/workspace/test/coverage-test/sut.py')
    
    if pairs:
        for pair in pairs:
            print(pair)
    else:
        print('No Data')

if __name__ == '__main__':
    read()