import Unit_2

class Chaser(Unit):
    def __init__(self, game, team):
        Unit.__init__(self, game, team)
        self.type = "chaser"
        self.acceleration = 0.01

        self.shoot_distance = 500
        self.shoot_power = 30

        self.skill_attack = 5
        self.skill_defend = 8

        self.max_speed = self.max_velocity + math.floor(random.random() * 5)

    def getShootDist(self):
        return self.shoot_distance

    def update(self):
        self._update()

        if self.controller == 2:
            if self.speed < self.max_speed:
                self.speed += self.acceleration
            else:
                self.speed = self.max_speed
       

        if self.controller == 1:
            self.checkQuaffle()

    def checkQuaffle(self):
        if self.game.quaffle.getPossession() is None:
            if Event.pixel_collide(self.game.quaffle, self):
                self.game.quaffle.setPossession(self)

    def shoot(self):
        oppGoal = self.game.get_goal(self)
        vec_between = (oppGoal.position - self.position).normalized()
        self.game.quaffle.throw(vec_between, self.shoot_power)

    def pass_to(self, other):
        vec_between = (other.position - self.position).normalized()
        self.game.quaffle.throw(vec_between, self.shoot_power)

    def pass_quaffle(self):
        if self.pointing == 1:
            self.game.quaffle.position.x = self.position.x + self.start_image.get_width()
        self.game.quaffle.throw(self.velocity, self.shoot_power)

    def tackle(self, oppChaser):
        tackle_chance = math.floor((self.skill_attack + random.random() * 4))
        if tackle_chance > oppChaser.skill_defend:
            return True
        else:
            return False




