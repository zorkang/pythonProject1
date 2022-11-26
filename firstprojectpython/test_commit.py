class Pistol:
    mag_size = int
    bang_str = 'BANG!!!'

    def __init__(self, mag_size):
        self.mag_size = mag_size

    def recharge(self):
        for i in range(1, self.mag_size + 1):
            print(i, self.bang_str)
            if i == self.mag_size:
                print('Replay? Press Y or continue')
                x = input()
                if x == 'Y':
                    return self.recharge()



weap = Pistol(8)
print(weap.recharge())

# s = 'bang'
# a = 8
#
# for i in range(1, a + 1):
#     print(i, s)
#     if i == a:
#         print('Vse, replay?')
#         x = input()
#         if x == 'Y':
#             print('return self.method')
