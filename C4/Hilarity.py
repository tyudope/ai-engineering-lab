import asyncio


async def q():
    print("Why can't programmers tell jokes ?")
    await asyncio.sleep(3) # pause me for 3 seconds but don't stop the whole program.
    # go run something else

async def a():
    print("Timing!")
    # this runs immediately
    #

async def main():
    await asyncio.gather(q(), a())

asyncio.run(main()) # starts th event loop


'''
Python thinks when running this example,

1. Execute q(). Well, just the first line right now.
2. OK, you lazy async q(), I've set my stopwatch and I'll comeback to you see in three seconds.
3. In the meantime I'll run a(), printing the answer right away.
4. No other await, so back to q()
5. Boring, event loop! I'll sit here aaand stare for the rest of three second
6. OK, now I'm done.


'''
