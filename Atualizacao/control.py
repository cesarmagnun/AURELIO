from persistence import QuestaoDao

class ViewController:

    def indiceQuestao(self):
        aux = QuestaoDao().indiceQuestao()
        for show in aux:
            r = show
        return r
