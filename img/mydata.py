from skimage import io

root = "C:/Users/Antonio Carlos/PycharmProjects/scikit-image-examples/img/models/"


def beatles():
    img = io.imread(root + 'beatles.jpg')
    return img


def fire():
    img = io.imread(root + 'fire.jpg')
    return img


def bird():
    img = io.imread(root + 'bird.jpg')
    return img


def neymar():
    img = io.imread(root + 'neymar.jpeg')
    return img


def hollywood():
    img = io.imread(root + 'hollywood.jpg')
    return img


def elvis():
    img = io.imread(root + 'elvis.jpg')
    return img


def lion():
    return io.imread(root + 'lion-3d.png')


def retina():
    return io.imread(root + 'retina.jpg')


def devil():
    return io.imread(root + 'devil.png')


def bacteria():
    return io.imread(root + 'bacteria.png')
