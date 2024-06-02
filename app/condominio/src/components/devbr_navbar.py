import flet as ft


class DevBrAppBar(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self, page: ft.Page, items: list = None):
        return ft.AppBar(
            title=ft.Text(value='DevBR'),
            leading=ft.IconButton(
                icon='menu',
                on_click=lambda e: self.shwo_drawer(page, items),
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

    def show_drawer(self, page: ft.Page, items: list = None):
        page.drawer = DevBrNavDrawer().build(items)
        page.drawer.open = True
        page.update()


class DevBrNavRail(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self, items: list = None):
        return ft.NavigationRail(
            destinations=[
                ft.NavigationRailDestination(
                    icon=item['icon'],
                    label=item['label'],
                ) for item in items
            ],
            # label_type=ft.NavigationRailLabelType.SELECTED,
            bgcolor=ft.colors.GREY_900,
            extended=False,
            # indicator_color=ft.colors.PRIMARY,
            unselected_label_text_style=ft.TextStyle(color=ft.colors.WHITE),
            selected_label_text_style=ft.TextStyle(color=ft.colors.AMBER_500),

            leading=ft.CircleAvatar(content=ft.Text(value='SD')),
            on_change=lambda e: print(e.control.selected_index),
            indicator_shape=ft.RoundedRectangleBorder(radius=5),

        )


class DevBrNavBar(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self, items: list = None):
        return ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(
                    icon=item['icon'],
                    tooltip=item['label'],
                    label=item['label'],
                ) for item in items
            ],
            indicator_shape=ft.RoundedRectangleBorder(radius=5),

        )


class DevBrNavDrawer(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand = True

    def build(self, items: list = None):
        return ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(
                    icon=f'{item["icon"]}_outlined',
                    label=item['label'],
                    selected_icon=item['icon'],
                ) for item in items
            ],
            bgcolor=ft.colors.GREY_900,
            indicator_color=ft.colors.PRIMARY,
            indicator_shape=ft.RoundedRectangleBorder(radius=10),
            tile_padding=ft.padding.all(5),
            on_change=lambda e: print(e.control.selected_index),

        )
