# find out file size
# move file pointer to end - chunk
# read backwards from end of chunk and count newlines
# once you've read x newlines, stop, print everything after the last newline

import sys
import os

INITIAL_CHUNKSIZE = 4096
NUM_LINES = 10
MAX_CHUNKSIZE = 1024 * 1024

with open(sys.argv[1]) as f:
    newlines_seen = 0
    chunk_size = INITIAL_CHUNKSIZE
    remaining_bytes = os.stat(sys.argv[1]).st_size
    chunk = ''
    last_char = True

    while remaining_bytes:
        if chunk_size < remaining_bytes:
            remaining_bytes -= chunk_size
        else:
            chunk_size = remaining_bytes
            remaining_bytes = 0
        f.seek(remaining_bytes)
        chunk = f.read(chunk_size)
        i = chunk_size

        while newlines_seen <= NUM_LINES:
            i -= 1
            if i < 0:
                break
            if chunk[i] == '\n' or last_char:
                newlines_seen += 1
                last_char = False

        if newlines_seen > NUM_LINES:
            break

        chunk_size = min(MAX_CHUNKSIZE, chunk_size * 2)

    if chunk:
        sys.stdout.write(chunk[i+1:])
        while chunk:
            chunk = f.read(MAX_CHUNKSIZE)
            sys.stdout.write(chunk)
