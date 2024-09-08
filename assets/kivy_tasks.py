from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MeineApp(App):
    def build(self):
        # Hauptlayout erstellen
        self.window = GridLayout()
        self.window.cols = 1

        # Logo hinzufügen
        self.window.add_widget(Image(source='logo_weiss.png'))

        # Abfrage des Namens
        self.greeting = Label(text='Wie ist dein Name?')
        self.window.add_widget(self.greeting)
        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)

        # "Eintreten"-Button hinzufügen
        self.entrance_button = Button(text='Eintreten')
        self.entrance_button.bind(on_press=self.entrance_button_behaviour)
        self.window.add_widget(self.entrance_button)

        return self.window

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

        # Button-Funktion ändern zu "Daten anzeigen"
        self.entrance_button.unbind(on_press=self.entrance_button_behaviour)
        self.entrance_button.text = 'Daten anzeigen'
        self.entrance_button.bind(on_press=self.show_information)

    def show_information(self, instance):
        # Informationen anzeigen
        self.greeting.text = (f'Herzlich Willkommen {self.user.text}\n'
                              f'Du bist {self.age_input.text} Jahre alt\n'
                              f'und wohnst in {self.city_input.text}.')

        # Button in "Programm Beenden" ändern
        self.entrance_button.unbind(on_press=self.show_information)
        self.entrance_button.text = 'Programm Beenden'
        self.entrance_button.bind(on_press=self.stop)

    # Methode zum Beenden der App
    def stop(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    MeineApp().run()
