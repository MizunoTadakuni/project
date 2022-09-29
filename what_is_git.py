class WhatIsGit:
    def about(self, lang = 'en'):
        print(f'https://{lang}.wikipedia.org/wiki/Git')

    def show(self):
        answer = input('Do you understand the basis? [yes/no]')
        if(answer == "yes"):
            print('Git is easy')
        else:
            print('Git is difficult...')
