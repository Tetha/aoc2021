
import sys

def main():
    print(sys.argv)
    if sys.argv[1] == "day5":
        import day5.day as day5
        day5.main(sys.argv[1:])

if __name__ == "__main__":
    main()
