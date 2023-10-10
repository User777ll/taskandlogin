
import flet as ft

# views
from regular.signup_view import SignupView
from regular.home_view import HomeView
from regular.settings_view import SettingsView
from regular.signin_view import SigninView



class Router:

    def __init__(self, page):
        self.page = page
        self.ft = ft
        self.routes = {
            "/": HomeView(page),
            "/signup": SignupView(page),
            "/settings": SettingsView(page),
            "/signin": SigninView(page)
        }
        self.body = ft.Container(content=self.routes['/'])

    def route_change(self, route):
        self.body.content = self.routes[route.route]
        self.body.update()