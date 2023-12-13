import flet as ft




def radiogroup_changed(e):
    if e.control.value == "Modo Oscuro":
        page.theme_mode = ft.ThemeMode.DARK
    elif e.control.value == "Modo claro":
      page.theme_mode = ft.ThemeMode.LIGHT
