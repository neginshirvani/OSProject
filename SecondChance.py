

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



    def replace_pages(self, pages, frames, x):

        i = 0
        # Cause we have 4 rows in our TLB
        while(i < 4):
            # for i in range(frames):
            chance = self.give_a_chance(pages, frames)

            if(chance == False):
                frames[i] = x
                i += 1
            else:
                chance = False
                i += 1

            






