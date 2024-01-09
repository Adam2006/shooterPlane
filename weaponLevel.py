
class WeaponLevelText():
    def __init__(self, font, text, position):
        self.font = font
        self.text = text
        self.image = font.render(text, True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=position)
        

    def update(self, new_text):
        self.text = new_text
        self.image = self.font.render(self.text, True, (255, 255, 255))
