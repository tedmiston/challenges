def load_data():
    with open('input.txt') as fp:
        data = fp.read().strip().split()
    data = [int(x) for x in data]
    return data


def search(data, n, sum_):
    """Search for answer."""
    match = False
    numbers = []
    if n == 2:
        for idx_i, i in enumerate(data):
            for idx_j, j in enumerate(data):
                if not match:
                    if i + j == sum_:
                        print('match:', i, j)
                        match = True
                        numbers = [i, j]
                        break
    elif n == 3:
        for idx_i, i in enumerate(data):
            for idx_j, j in enumerate(data):
                for idx_k, k in enumerate(data):
                    if not match:
                        if sum([i, j, k]) == sum_:
                            print('match:', i, j, k)
                            match = True
                            numbers = [i, j, k]
                            break
    return numbers


def multiply(numbers):
    answer = 1
    for i in numbers:
        answer *= i
    return answer


def main():
    data = load_data()

    # part 1
    numbers = search(data, n=2, sum_=2020)
    answer = multiply(numbers)
    print(f'answer a: {answer}')

    # part 2
    numbers = search(data, n=3, sum_=2020)
    answer = multiply(numbers)
    print(f'answer b: {answer}')

if __name__ == '__main__':
    main()
