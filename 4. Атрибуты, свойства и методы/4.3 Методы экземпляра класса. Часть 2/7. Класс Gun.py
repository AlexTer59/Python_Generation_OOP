class Gun:
    def __init__(self):
        self.shots_counter = 0

    def shoot(self):
        self.shots_counter += 1
        if self.shots_counter % 2 != 0:
            print("pif")
        else:
            print('paf')

    def shots_count(self):
        return self.shots_counter

    def shots_reset(self):
        self.shots_counter = 0

gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())