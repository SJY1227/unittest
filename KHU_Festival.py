class KHU_Festival:
    def __init__(self, name="", balance=0, lineup=None):
        if lineup is None:
            lineup = []
        self.name = name
        self.balance = balance
        self.lineup = lineup

    def set_name(self, name):
        self.name = name

    def set_balance(self, balance):
        self.balance = balance

    def set_lineup(self, lineup):
        self.lineup = lineup

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def get_lineup(self):
        return self.lineup

    def print_lineup(self):
        output = ""
        for i, day_lineup in enumerate(self.lineup, start=1):
            output += f"{i}일차 라인업\n"
            for artist in day_lineup:
                output += f"{artist}\n"
            output += "\n"
        print(output)

# Example usage:
global_campus_festival = KHU_Festival("Adelante", 130000000, [["Lacuna", "STAYC", "하이라이트"], ["창모", "YB"]])
print(f"축제 이름: {global_campus_festival.get_name()}")
print(f"예산: {global_campus_festival.get_balance()}")
global_campus_festival.print_lineup()