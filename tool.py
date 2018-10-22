import random


def generate_serect_key(count):
    '''
    生成count位的密钥
    :param count:
    :return:
    '''
    result = ''
    for _ in range(count):
        result += chr(random.randint(50,130))
    return result


if __name__ == '__main__':
    print(generate_serect_key(15))