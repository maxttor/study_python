#Task description: https://stepik.org/lesson/24464/step/4
class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for item in self.iterable:
            pos, neg = 0, 0
            for func in self.funcs:
                if func(item):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield item