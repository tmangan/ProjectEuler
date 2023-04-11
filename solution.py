# Solution class to ProjectEuler Math/Coding Problems:

class solution_1:
    divisible_numbers = [3, 5]
    highest_value = 1000
    running_total = 0

    def solve(self):
        for i in range(self.highest_value):
            truth_table = []
            for j in self.divisible_numbers:
                if i % j == 0:
                    truth_table.append(True)
                else:
                    truth_table.append(False)
            if any(truth_table):
                self.running_total += i

        print(self.running_total)


def main():
    s = solution_1()
    print(s.solve())


if __name__ == "__main__":
    main()
