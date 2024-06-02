import flet as ft

from components.devbr_navbar import DevBrNavRail, DevBrNavBar, DevBrNavDrawer, DevBrAppBar


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.main()
    def main(self):
        itens = [
            {'icon': 'home', 'label': 'Home'},
            {'icon': 'settings', 'label': 'Settings'},
            {'icon': 'info', 'label': 'About'},
        ]
        sidebar = DevBrNavRail()
        navbar = DevBrNavBar()
        navDrawer = DevBrNavDrawer()
        # appBar = DevBrAppBar()
        # row = ft.Row(controls=[sidebar.build(itens)], expand=True)
        # row = navbar.build(itens)
        # self.page.drawer =  navDrawer.build(itens)
        # self.page.drawer.open = True
        # self.page.update()
        # self.page.add(row)

        appBar = ft.AppBar(
            title=ft.Text(value='DevBR'),
            leading=ft.IconButton(
                icon='menu',
                on_click=lambda e: show_drawer(e),
            ),
            actions=[
                ft.IconButton(
                    icon='search',
                    on_click=lambda e: print('search'),
                ),
                ft.IconButton(
                    icon='settings',
                    on_click=lambda e: print('settings'),
                ),
            ],
            bgcolor=ft.colors.GREY_900,
            elevation=0,
            shadow_color=ft.colors.BLACK12,
            title_text_style=ft.TextStyle(color=ft.colors.WHITE),
            color=ft.colors.AMBER_500,

        )

        def show_drawer(e):
            self.page.drawer = navDrawer.build(itens)
            self.page.drawer.open = True
            self.page.update()

        self.page.appbar = appBar
        self.page.update()


if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets', view=ft.AppView.WEB_BROWSER)
