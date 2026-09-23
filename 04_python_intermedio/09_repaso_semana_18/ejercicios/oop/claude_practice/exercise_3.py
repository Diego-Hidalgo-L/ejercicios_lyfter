
class Hand:
    def __init__(self):
        self.fingers = 5
    
    def can_grip(self, object_name):
        print(f"Gripping {object_name}")


class Arm:
    hand: Hand

    def __init__(self, hand):
        self.hand = hand
        self.max_distance = 1.5

    def can_reach(self, distance):
        if distance <= self.max_distance:
            print(f"Extending arm {distance} meters")
        else:
            print("Too far to reach")


class Foot:
    def __init__(self):
        self.toes = 5
        self.shoe_size = 10


class Leg:
    foot: Foot

    def __init__(self, foot):
        self.foot = foot

    def can_kick(self, object_name):
        print(f"Kicking {object_name}")
    
    def step_forward(self, side):
        print(f"{side} leg forward")
    
    def step_backward(self, side):
        print(f"{side} leg backward")


class Eye:
    def __init__(self, color):
        self.color = color

class Brain:
    def __init__(self, iq):
        self.iq = iq

    def think(self, thought):
        print(f"Brain thought about: {thought}")


class Head:
    brain: Brain
    right_eye: Eye
    left_eye: Eye

    def __init__(self, brain, right_eye, left_eye):
        self.brain = brain
        self.right_eye = right_eye
        self.left_eye = left_eye
    
    def look(self, object_to_look):
        print(f"Looking at {object_to_look}")


class Torso:
    head: Head
    right_arm: Arm
    left_arm: Arm
    right_leg: Leg
    left_leg: Leg

    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


class Human:
    torso: Torso

    def __init__(self, name, age, torso):
        self.name = name
        self.age = age
        self.torso = torso
    
    def __str__(self):
        return f"{self.name}, age {self.age}, IQ: {self.torso.head.brain.iq}"
    
    def walk(self, steps):
        for step in range(steps):
            self.torso.right_leg.step_forward("Right")
            self.torso.left_leg.step_forward("Left")

    def wave(self):
        print("Right hand waving")
    
    def think(self, thought):
        self.torso.head.brain.think(thought)
    
    def look(self, object_to_look):
        self.torso.head.look(object_to_look)


right_hand = Hand()
left_hand = Hand()

right_arm = Arm(right_hand)
left_arm = Arm(left_hand)

right_foot = Foot()
left_foot = Foot()

right_leg = Leg(right_foot)
left_leg = Leg(left_foot)

right_eye = Eye("green")
left_eye = Eye("green")
brain = Brain(150)

head = Head(brain, right_eye, left_eye)

torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

human = Human("Diego", 29, torso)

human.think("Gym")
human.walk(3)

human.look("Boobs")