from engine.game_engine import GameEngine
from engine.game.game_system import GameSystem
from engine.game.event_system import EventSystem
from engine.game.player_system import PlayerSystem
from engine.render.render_system import RenderSystem

game = GameEngine()
game.add_system(GameSystem(game))
game.add_system(EventSystem(game))
game.add_system(PlayerSystem(game))
game.add_system(RenderSystem(game))

game.run()