class Math:

    @staticmethod  # They do something but don't access to instances, so they don't change anything
    def add5(x):  # So there is no need for self or cls
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")


print(Math.add5(5))
print(Math.add10(5))
Math.pr()

