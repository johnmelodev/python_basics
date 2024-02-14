import webbrowser
import threading
import time

def extract_data_from_site(site):
    print(f'We are navigating to the site {site}')
    webbrowser.open_new(site)
    for i in range(1, 20):
        print(f'Processing data - {i}/19')
        time.sleep(1)
    print('Data extraction from the site completed')

def download_files():
    for i in range(1, 10):
        print(f'Downloading files - {i}/10')
        time.sleep(1)
    print('Files downloaded')

new_thread = threading.Thread(target=extract_data_from_site, args=('https://www.devaprender.com',), daemon=True)
new_thread.start()
download_files()
new_thread.join()
