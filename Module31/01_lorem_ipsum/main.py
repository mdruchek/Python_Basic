import re


if __name__ == '__main__':
    text: str = r""" Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
    nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
    Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate
    """

    pattern = r'\b\w{4}\b'
    result = re.findall(pattern, text)
    print(result)
