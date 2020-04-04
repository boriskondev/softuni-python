from project.player.player import Player


class BattleField:
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        current_fighters = [attacker, enemy]

        for fighter in current_fighters:
            if fighter.__class__.__name__ == "Beginner":
                fighter.health += 40
                for fighter_card in fighter.card_repository.cards:
                    fighter_card.damage_points += 30
            bonus_health_points = 0
            for fighter_card in fighter.card_repository.cards:
                bonus_health_points += fighter_card.health_points
            fighter.health += bonus_health_points

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)


