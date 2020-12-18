from dataclasses import dataclass

@dataclass
class Password:
    min_count: int
    max_count: int
    char: str
    password: str

    @classmethod
    def parse(cls, row):
        nums, password  = row.split(': ')
        nums, char = nums.split(' ')
        min_count, max_count = map(int, nums.split('-'))
        return cls(min_count, max_count, char, password)

    def is_valid(self):
        return self.min_count <= self.password.count(self.char) <= self.max_count


def load_data():
    with open('input.txt') as fp:
        data = fp.read().strip().splitlines()
    return data


def parse_data(data):
    return [Password.parse(row) for row in data]


def main():
    data = load_data()
    passwords = parse_data(data)
    valid_count = sum(x.is_valid() for x in passwords)
    print(valid_count)


if __name__ == '__main__':
    main()
