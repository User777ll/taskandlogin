from flet import *
from regular.FletRouter import Router


def main(page: Page):

    page.window_width = 1920
    page.window_height = 1080

    myRouter = Router(page)
    page.on_route_change = myRouter.route_change
    page.add(
        myRouter.body
    )

    page.padding = 0

    page.go('/signup')


if __name__ == '__main__':
    app(target=main, assets_dir="assets")