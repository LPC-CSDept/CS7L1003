
class Rectangle:
    #########################################
    # Code your program here
    # Define the class Rectangle
    #########################################
    def __init__(self, h, w):
        self.height = h
        self.width = w


def main():

    r = Rectangle(10, 20)
    print(f'Height: {r.height} \t Width: {r.width}')

    r.height = 100
    r.width = 200
    print(f'Height: {r.height} \t Width: {r.width}')
    r.set_height(200)
    r.set_width(300)
    print(f'Height: {r.height} \t Width: {r.width}')

    # test _height and _width
    r._height = 999
    print(f'Height: {r.height} \t Width: {r._width}')


if __name__ == '__main__':
    main()
