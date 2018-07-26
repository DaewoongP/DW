import argparse


parser = argparse.ArgumentParser(description="PtzCamera")
parser.add_argument('-b', '--broker-url', default="localhost:1883", type=str,
                    metavar='PATH', help='mqtt broker address (default: localhost:1883')
parser.add_argument('-o', '--ffserver-url', default='http://localhost:8090/feed1.ffm', type=str,
                    metavar='PATH', help='url used to set up rtsp streaming')


def main():
    global args
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
   main()