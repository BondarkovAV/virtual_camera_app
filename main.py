import flet as ft
from templates.ui import MainLayout


def main(page: ft.Page):
    def pick_files_result(e: ft.FilePickerResultEvent):
        main_layout.selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        main_layout.selected_files.update()
        print(e.files[0].path)

    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.theme = ft.Theme(color_scheme_seed=ft.colors.LIGHT_BLUE_ACCENT_700, font_family="Ubuntu")
    page.window_resizable = False
    page.window_maximizable = False
    page.window_height = page.window.height / 2
    page.window_width = page.window.width / 2
    page.spacing = 20
    page.title = "Virtual Camera App"

    main_layout = MainLayout(page)

    page.add(
        main_layout.build_page(pick_files_result)
    )
    page.update()


ft.app(target=main, view=ft.AppView.FLET_APP)
