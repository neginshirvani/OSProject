

class SecondChance:

    def give_a_chance(self, pages, frames):

        chance = False
        for j in range(len(pages)):

            for i in range(frames):

                if(pages[j] == frames[i]):
                    chance = True
                else:
                    chance = False
        return chance



    def replace_pages(self, pages, frames):

        for i in range(frames):
            res = self.give_a_chance(pages, frames)



