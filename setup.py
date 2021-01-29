from db import Management

def main():
    setup = Management()
    setup.createTable()
    setup.insertData(['2021-01-05',20,2])
    setup.printTable()

    print('Created')

if __name__ == '__main__':
    main()