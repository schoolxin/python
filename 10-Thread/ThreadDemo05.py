import threading, queue

q = queue.Queue()


def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')
        q.task_done()


# turn-on the worker thread
threading.Thread(target=worker).start()

# send thirty task requests to the worker
for item in range(30):
    q.put(item)
print('All task requests sent\n', end='')

# block until all tasks are done
q.join()
print('All work completed')

url_tpl = "{}/admin/orders.json?limit={}&status=any&updated_at_min={}&updated_at_max={}&since_id={{}}".format(
                1, 2,
                3,
                3)

print(url_tpl)