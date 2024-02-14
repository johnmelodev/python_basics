import webbrowser
import threading
import time
import random


def comment(site, comment):
    print(f'Entering the site: {site}')
    print(f'Leaving a comment: {comment}!')
    time.sleep(5)
    print(f'Data processed on the site: {site}')


comments = ['hi', 'hello', 'liked it', 'enjoyed', 'very good']
threads = []

for site in range(6):
    new_thread = threading.Thread(
        target=comment, args=(site, random.choice(comments)))
    threads.append(new_thread)

for thread in threads:
    thread.start()
    print(f'Starting {thread.name}')

for thread in threads:
    thread.join()
    print(f'Finishing {thread.name}')