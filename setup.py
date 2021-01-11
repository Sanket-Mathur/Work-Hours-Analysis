from db import Management

def main():
    setup = Management()
    setup.createTable()
    setup.printTable()

    print('Created')

if __name__ == '__main__':
    main()