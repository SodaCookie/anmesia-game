from engine.game_system import GameSystem
from engine.game.event_system import EventSystem
from engine.game.player_system import PlayerSystem
from engine.render.render_system import RenderSystem
from engine.render.lighting_system import LightingSystem

game = GameSystem()
game.add_system(EventSystem(game))
game.add_system(PlayerSystem(game))
game.add_system(LightingSystem(game))
game.add_system(RenderSystem(game))

game.run()