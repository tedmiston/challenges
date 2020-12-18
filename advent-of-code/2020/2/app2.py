from dataclasses import dataclass

@dataclass
class Password:
    first_idx: int
    second_idx: int
    char: str
    password: str

    @classmethod
    def parse(cls, row):
        nums, password  = row.split(': ')
        nums, char = nums.split(' ')
        first_idx, second_idx = map(int, nums.split('-'))
        return cls(first_idx, second_idx, char, password)

    def is_valid(self):
        a = self.password[self.first_idx-1] == self.char
        b = self.password[self.second_idx-1] == self.char
        return a ^ b


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
