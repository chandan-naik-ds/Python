
# try:
#     a = int(input("Enter numerator: "))
#     print(a)

# except Exception as e:
#     print("Some other error occured pleaase check is out!")
#     print(e)

# finally:
#     print("Hey you enterd of finally")

''' as you run it normally no maatter whether the the input is wrong or right 
finally always run but some people say you if you write the same statement 
which isinside finally with normal print(...) the the same thing it also runs
whether the input is right or wrong 

therefore the finally is used in functions , once you return the value in function
then it will not run the further code but if you add i=finally it will run as it is.
'''

def main():
    try:
        a = int(input("Enter numerator: "))
        print(a)

    except Exception as e:
       print("Some other error occured pleaase check is out!")
       print(e)

    finally:
       print("Hey you enterd of finally")

main()
