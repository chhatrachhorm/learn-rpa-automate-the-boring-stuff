import threading
import time

print('Start of program')


def take_a_nap():
    time.sleep(5)
    print('Wake Up')


t1 = threading.Thread(target=take_a_nap)
t1.start()
print('End of program')


# passing args
t2 = threading.Thread(target=print, args=['Cats', 'Dogs'], kwargs={'sep': ' & '})
# print('Cats', 'Dogs', sep=' & '
t2.start()
