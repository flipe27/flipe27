from assets import BIRD_IMAGES, pygame


# Bird object
class Bird:
    IMGS = BIRD_IMAGES
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.velocity = 0
        self.height = self.y
        self.time = 0
        self.image_count = 0
        self.image = self.IMGS[0]

    def jump(self):
        self.velocity = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
        # Calculating the displacement
        self.time += 1
        displacement = 1.5 * (self.time ** 2) + (self.velocity * self.time)

        # Restricting the displacement
        if displacement > 16:
            displacement = 16
        elif displacement < 0:
            displacement -= 2

        self.y += displacement

        # The bird's angle
        if displacement < 0 or self.y < (self.height + 50):
            if self.angle < self.MAX_ROTATION:
                self.angle = self.MAX_ROTATION
        else:
            if self.angle > -90:
                self.angle -= self.MAX_ROTATION

    def draw(self, screen):
        # Defining which bird image to use
        self.image_count += 1

        if self.image_count < self.ANIMATION_TIME:
            self.image = self.IMGS[0]
        elif self.image_count < (self.ANIMATION_TIME * 2):
            self.image = self.IMGS[1]
        elif self.image_count < (self.ANIMATION_TIME * 3):
            self.image = self.IMGS[2]
        elif self.image_count < (self.ANIMATION_TIME * 4):
            self.image = self.IMGS[1]
        elif self.image_count < (self.ANIMATION_TIME * 5):
            self.image = self.IMGS[0]
            self.image_count = 0

        # Don't flap the wing when the bird is falling
        if self.angle <= -80:
            self.image = self.IMGS[1]
            self.image_count = self.ANIMATION_TIME * 2

        # Draw the image
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        image_center_pos = self.image.get_rect(topleft=(self.x, self.y)).center
        rectangle = rotated_image.get_rect(center=image_center_pos)
        screen.blit(rotated_image, rectangle.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
