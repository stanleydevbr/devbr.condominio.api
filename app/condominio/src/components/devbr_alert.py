import flet as ft


def alert(title: str, descricao: str) -> ft.AlertDialog:
    comp = ft.AlertDialog(
        title=ft.Text(value=title),
        content=ft.Text(value=descricao),
        content_padding=ft.padding.all(30),
        inset_padding=ft.padding.all(30),
        modal=False,
        shape=ft.RoundedRectangleBorder(radius=5),

        actions=[
            ft.TextButton(text='Cancelar',style=ft.ButtonStyle(color=ft.colors.RED)),
            ft.ElevatedButton(text='Confirmar', style=ft.ButtonStyle(bgcolor=ft.colors.GREEN))
        ],
        actions_alignment=ft.MainAxisAlignment.END,

    )
    return comp
