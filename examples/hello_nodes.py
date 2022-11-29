
from snakey.nodes import *
from snakey.nodes.scene import Scene
from snakey.nodes.transformable import translate

if __name__ == '__main__':
    scene = Scene()


    @scene.action
    def load(group: Group, ref):
        ref.player = RectangleShape(15, 15) | translate((3, -3))

        group ^ (RectangleShape(3, 3) | translate((3, 3)), RectangleShape(1, 1))
        group ^ ref.player

        move = translate((1.0 / 3, 0.1 + 0.2))
        group | move


    @scene.action
    def update(group: Group, ref):
        player = ref.player

        print(f"Group: {group.position}")
        print(f"Player: {player.position}")

        [print(child.position) for child in group]


    @scene.action
    def draw(group: Group):
        pass


    @scene.action
    def close(group: Group):
        pass


    print(scene.events)

    scene.events["load"](scene.root, scene.references)
    scene.events["update"](scene.root, scene.references)
    scene.events["draw"](scene.root, scene.references)