class Gun:
    def __init__(self):
        self.shoot_counter = 0

    def shoot(self):
        self.shoot_counter += 1
        if self.shoot_counter % 2 != 0:
            print("pif")
        else:
            print('paf')


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()

