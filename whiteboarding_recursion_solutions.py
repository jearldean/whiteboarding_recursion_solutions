
class myclass():
    count_em = 0
    sum_em = 0

    # Recursion has 3 things: base case, incremental change (works towards the base case), calls itself.

    def recursey_count(self, a_list):

        if not a_list:
            print(self.count_em)
            return 0
        else:
            last_guy = a_list.pop()
            self.count_em += 1
            self.recursey_count(a_list)

    def recursey_sum(self, a_list):

        if not a_list:
            print(self.sum_em)
            return 0
        else:
            last_guy = a_list.pop()
            self.sum_em += last_guy
            self.recursey_sum(a_list)


def recursey_count_outside_class(a_list):

    if not a_list:
        return 0
    else:
        last_guy = a_list.pop()
        return 1 + recursey_count_outside_class(a_list)


def recursey_sum_outside_class(a_list):

    if not a_list:
        return 0
    else:
        last_guy = a_list.pop()
        return last_guy + recursey_sum_outside_class(a_list)


if __name__ == '__main__':
    m = myclass()
    m.recursey_count([1, 2, 3])
    m.recursey_sum([1, 2, 3])
    print(recursey_count_outside_class([1, 2, 3]))
    print(recursey_sum_outside_class([1, 2, 3]))