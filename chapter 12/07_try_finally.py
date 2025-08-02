def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return # used to stop the code in the function

    except Exception as e:
        print(e)
        return

    finally:
        print("hey I am inside of finally")

main()