class Quest:
    def __init__(self, title, description, target_item=None, required_amount=0):
        self.title = title
        self.description = description
        self.completed = False
        self.target_item = target_item
        self.required_amount = required_amount
        self.collected = 0

    def update_progress(self, inventory):
        count = sum(1 for item in inventory.items if item.name == self.target_item)
        self.collected = count
        if self.collected >= self.required_amount:
            self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else f"{self.collected}/{self.required_amount}"
        return f"{self.title}: {self.description} (Прогресс: {status})"

class QuestManager:
    def __init__(self, player):
        self.player = player
        self.quests = self.init_quests()

    def init_quests(self):
        quests = []
        quests.append(Quest("Сбор трав", "Соберите 3 травы", target_item="Трава", required_amount=3))
        quests.append(Quest("Крысы в подвале", "Победите 2 крыс", target_item="Крыса", required_amount=2))
        quests.append(Quest("Сбор шкур", "Соберите 2 шкуры", target_item="Шкура", required_amount=2))
        quests.append(Quest("Таинственный амулет", "Найдите таинственный амулет", target_item="Амулет", required_amount=1))
        return quests

    def update_quests(self):
        for quest in self.quests:
            quest.update_progress(self.player.inventory)

    def show_active_quests(self):
        self.update_quests()
        print("\nКвесты:")
        for quest in self.quests:
            print(quest)
