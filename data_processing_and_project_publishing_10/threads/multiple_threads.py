import webbrowser
import threading
import time


def comment(site):
    print(f'Entering the site: {site}')
    time.sleep(5)
    print(f'Data processed on the site: {site}')


threads = []

for site in range(100):
    new_thread = threading.Thread(target=comment, args=(site,))
    threads.append(new_thread)

for thread in threads:
    thread.start()
    # print(f'Starting (thread.name)')

for thread in threads:
    thread.join()
    # print(f'Finishing (thread.name)')