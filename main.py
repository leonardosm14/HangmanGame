from random_word import RandomWords

class Game:
    @classmethod
    def PickRandom(cls):
        return cls.Play(RandomWords().get_random_word())

    @staticmethod
    def LivesLeft(counter):
        if counter == 0:
            print('YOU LOSE!')
        else:
            print(counter, 'lives left!')

    @staticmethod
    def ChecksWinner(word, traces):
        final = "".join(traces)
        return word == final

    @classmethod
    def Play(cls, word):
        counter = 10
        end = False
        traces = ['_'] * len(word)

        print(*traces)

        while counter >= 0 or not end:
            user_input = input()

            if user_input not in word:
                counter -= 1
                cls.LivesLeft(counter)

            for w in range(len(word)):
                if word[w] == user_input:
                    traces[w] = user_input
            
            if cls.ChecksWinner(word, traces):
                print('YOU WIN! The word is', word)
            
            print(*traces)

Game.PickRandom()
