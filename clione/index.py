import argparse

def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        raise ValueError('Can not divide by 0')
    return a/b

def main():
    parser =argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument('operation',choices=['add','substract','multiply','division'],help='Operation to perform')
    parser.add_argument('a',type=float,help='first number')
    parser.add_argument('b',type=float,help='second number')
    args=parser.parse_args()
    
    if args.operation=='add':
        result =add(args.a,args.b)
    elif args.operation=='substract':
        result =substract(args.a,args.b)
    elif args.operation=='multiply':
        result =multiply(args.a,args.b)
    elif args.operation=='division':
        try:
            result =division(args.a,args.b)
        except ValueError as e:
            print(e)
            return
    print(f"Result of {args.operation} {args.a} and {args.b} is {result}")

if __name__=="__main__":
    main()
    
