import Render
import flet as ft

# presetPath1080 = r"C:\Users\John\Documents\Adobe\Adobe Media Encoder\23.0\Presets\1080.epr"
# presetPath2257 = r"C:\Users\John\Documents\Adobe\Adobe Media Encoder\23.0\Presets\2257.epr"
# clipSequence = "Clips"
# finalVersionSequence = "Full"


def main(page: ft.Page):
    def submit_button_pressed(e):
        Render.render2257(finalVersionSequence.value, presetPath2257.value, name_of_project.value)
        Render.render1080(finalVersionSequence.value, presetPath1080.value, name_of_project.value)
        Render.renderclips(clipSequence.value, presetPath1080.value, name_of_project.value)

    page.title = "Title"
    page.window_center()
    name_of_project = ft.TextField(label="Project Name",hint_text="What is the name of this project?")
    presetPath1080 = ft.TextField(value=r"C:\Users\John\Documents\Adobe\Adobe Media Encoder\23.0\Presets\1080.epr", hint_text="What is the Path to your 1080 preset?")
    presetPath2257 = ft.TextField(value=r"C:\Users\John\Documents\Adobe\Adobe Media Encoder\23.0\Presets\2257.epr", hint_text="What is the Path to your 2257 preset?")
    clipSequence = ft.TextField(value="Clips",hint_text="What is the name of the track containing your teaser clips?")
    finalVersionSequence = ft.TextField(value="Full",hint_text="What is the name of the track containing your final, full cut?")
    page.add(name_of_project, presetPath1080, presetPath2257, clipSequence, finalVersionSequence)
    page.add(ft.TextButton(text="Submit", on_click=submit_button_pressed))


ft.app(target=main)
