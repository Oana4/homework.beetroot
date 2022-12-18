from PIL import Image
import threading


def timer(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.8f}s to execute'.format(fn.__name__, execution_time))
        return to_execute

    return inner


def cropp_image(i):
    image_path = '/home/edystan/Pictures/StocklandDunder_Thumbnail.jpg'
    image = Image.open(image_path)
    small_image = image.resize((500, 500))
    small_image.save(f'image{str(i)}.jpg')


@timer
def repeat_cropp_func(n):
    for i in range(n):
        cropp_image(i)


@timer
def repeat_cropp_func_with_threads(n):
    for i in range(n):
        x = threading.Thread(cropp_image(threading.current_thread().name), name=i)
        x.start()
        x.join()


if __name__ == '__main__':

    repeat_cropp_func(50)
    repeat_cropp_func_with_threads(50)