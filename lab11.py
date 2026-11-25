# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    async def double(n):
        await asyncio.sleep(0)
        return n * 2

    return await asyncio.gather(*(double(n) for n in numbers))


async def fastest(jobs):
    async def run_job(label, delay):
        await asyncio.sleep(delay)
        return label

    coros = [run_job(label, delay) for label, delay in jobs]
    for finished in asyncio.as_completed(coros):
        return await finished


def echo_once(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.sendall(message.encode())
        data = sock.recv(1024)
        return data.decode()


def main():
    # Optional scratch space - try the async parts here, e.g.:
    print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass


if __name__ == "__main__":
    main()