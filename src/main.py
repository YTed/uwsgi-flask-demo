from web import run
import sys

if __name__ == '__main__':
    port = 80
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    run(host='0.0.0.0', port=port, debug=False)
