from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class MeineApp(App):
    def build(self):
        # Hauptlayout erstellen
        self.window = GridLayout()
        self.window.cols = 1

        # Logo hinzufügen
        self.window.add_widget(Image(source='logo_weiss.png'))

        # PIN-Code-Abfrage hinzufügen
        self.pin_label = Label(text='Bitte gib deinen PIN-Code ein:')
        self.window.add_widget(self.pin_label)
        self.pin_input = TextInput(multiline=False, password=True)
        self.window.add_widget(self.pin_input)

        # "Eintreten"-Button hinzufügen
        self.entrance_button = Button(text='Eintreten')
        self.entrance_button.bind(on_press=self.pin_check)
        self.window.add_widget(self.entrance_button)

        # Variable für Tagebucheinträge
        self.diary_entries = []

        return self.window

    def pin_check(self, instance):
        # Überprüfe den PIN-Code
        if self.pin_input.text == "1234":
            # Name abfragen
            self.window.clear_widgets()
            self.greeting = Label(text='Wie ist dein Name?')
            self.window.add_widget(self.greeting)
            self.user = TextInput(multiline=False)
            self.window.add_widget(self.user)

            # "Eintreten"-Button hinzufügen
            self.entrance_button.text = 'Eintreten'
            self.entrance_button.unbind(on_press=self.pin_check)
            self.entrance_button.bind(on_press=self.entrance_button_behaviour)
            self.window.add_widget(self.entrance_button)
        else:
            popup = Popup(title='Fehler',
                          content=Label(text='Falscher PIN!'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()

    def entrance_button_behaviour(self, instance):
        # Name eingeben und Text aktualisieren
        self.greeting.text = f'Herzlich Willkommen {self.user.text}'

        # Altersabfrage hinzufügen
        self.age_label = Label(text='Wie alt bist du?')
        self.window.add_widget(self.age_label)
        self.age_input = TextInput(multiline=False)
        self.window.add_widget(self.age_input)

        # Wohnortabfrage hinzufügen
        self.city_label = Label(text='Wo wohnst du?')
        self.window.add_widget(self.city_label)
        self.city_input = TextInput(multiline=False)
        self.window.add_widget(self.city_input)

        # Button-Funktion ändern zu "Tagebucheintrag hinzufügen"
        self.entrance_button.unbind(on_press=self.entrance_button_behaviour)
        self.entrance_button.text = 'Tagebucheintrag hinzufügen'
        self.entrance_button.bind(on_press=self.add_diary_entry)

    def add_diary_entry(self, instance):
        # Tagebucheintrag erstellen
        self.diary_label = Label(text='Gib deinen Tagebucheintrag ein:')
        self.window.add_widget(self.diary_label)
        self.diary_input = TextInput(multiline=True)
        self.window.add_widget(self.diary_input)

        # Button-Funktion ändern zu "Eintrag speichern"
        self.entrance_button.unbind(on_press=self.add_diary_entry)
        self.entrance_button.text = 'Eintrag speichern'
        self.entrance_button.bind(on_press=self.save_diary_entry)

    def save_diary_entry(self, instance):
        # Eintrag speichern und anzeigen
        self.diary_entries.append(self.diary_input.text)

        # Zeige gespeicherten Eintrag und biete Option, mehr hinzuzufügen oder zu beenden
        self.greeting.text = f'Eintrag gespeichert!\n\nHerzlich Willkommen {self.user.text}\n' \
                             f'Du bist {self.age_input.text} Jahre alt\nund wohnst in {self.city_input.text}.'
        self.diary_label.text = "Dein Tagebuch:"
        
        self.window.clear_widgets()
        self.window.add_widget(Label(text='Deine Tagebucheinträge:'))

        # Alle Tagebucheinträge anzeigen
        for entry in self.diary_entries:
            self.window.add_widget(Label(text=entry))

        # Button in "Neuen Eintrag hinzufügen" und "Programm Beenden" ändern
        self.add_entry_button = Button(text='Neuen Eintrag hinzufügen')
        self.add_entry_button.bind(on_press=self.add_diary_entry)
        self.window.add_widget(self.add_entry_button)

        self.exit_button = Button(text='Programm Beenden')
        self.exit_button.bind(on_press=self.stop)
        self.window.add_widget(self.exit_button)

    # Methode zum Beenden der App
    def stop(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    MeineApp().run()
