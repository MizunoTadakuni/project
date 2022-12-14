import unicodedata


class WhatIsGit:
    def about(self, lang = 'en'):
        # 式展開のためにシングルクオートを使う
        print(f'https://{lang}.wikipedia.org/wiki/Git/')

    def show(self):
        answer = input('Do you understand the basis of Git? [yes/no]')
        if(answer == "yes" or answer == "y"):
            print('Git is easy')
        else:
            print('Git is difficult...')

    def myInput(message):
        planeAnswer = input(message)
        return unicodedata.normalize("NFKC", planeAnswer)