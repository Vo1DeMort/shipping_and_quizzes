class Department:
    def __init__(self, name, remark):
        self.name = name
        self.remark = remark

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Missing Department")
        if value not in ["Administration", "HumanResource", "Finance", "IT"]:
            raise ValueError("Invalid Department")
        self._name = value

    def __str__(self):
        return f"{self.name} - {self.remark}"


def main():
    dept = get_department()
    print(dept)

    try:
        dept.name = "Accounting"
    except ValueError as err:
        print(err)

    try:
        dept.name = None
    except ValueError as err:
        print(err)


def get_department():
    return Department("IT", "Hello, I am from IT")


if __name__ == "__main__":
    main()
