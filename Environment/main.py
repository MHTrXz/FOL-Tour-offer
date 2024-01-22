import sys
import tkinter
import tkinter.messagebox
from tkintermapview import TkinterMapView

import ConnetionCities
import FindCities
import FlatFact  # step 1
import keyFeature  # step 2
import keySearch  # step 3


class App(tkinter.Tk):
    APP_NAME = "map_view_demo.py"
    WIDTH = 800
    HEIGHT = 750  # This is now the initial size, not fixed.

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title(self.APP_NAME)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Configure the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Text area can expand/contract.
        self.grid_rowconfigure(1, weight=0)  # Submit button row; doesn't need to expand.
        self.grid_rowconfigure(2, weight=3)  # Map gets the most space.

        # Upper part: Text Area and Submit Button
        self.text_area = tkinter.Text(self)
        self.text_area.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

        self.submit_button = tkinter.Button(self, text="Submit", command=self.process_text)
        self.submit_button.grid(row=1, column=0, pady=10, sticky="ew")

        # Lower part: Map Widget
        self.map_widget = TkinterMapView(self)
        self.map_widget.grid(row=2, column=0, sticky="nsew")

        self.marker_list = []  # Keeping track of markers

    def check_connections(self, results):
        return ConnetionCities.checkConnection(results)

    def process_text(self):
        """Extract locations from the text area and mark them on the map."""

        text = self.text_area.get("1.0", "end-1c")

        locations, inputText = self.extract_locations(text)

        output = "Flat Fact"
        output += "\nInput text: " + inputText
        output += "\nkey features:" + str(locations)

        results = FindCities.findCities(locations)

        output += "\nfunded locations: " + str(results)

        finalResults = self.check_connections(results)

        if finalResults == -1:
            results = FindCities.findCitiesUnion(locations)
            finalResults = self.check_connections(results)

        output += "\nfinal results: " + str(finalResults)

        output += "\n------------------\n"

        print(output)
        file = open('../Outputs/output.txt', 'a')
        file.write(output + '\n')
        file.close()

        if 6 > len(finalResults) > 1:
            tkinter.messagebox.showinfo(title='Please wait ...',
                                        message='Please wait ... marking the tour route in map.')
            print('start mapping ------')
            self.mark_locations(finalResults)
            tkinter.messagebox.showinfo(title='Successful',
                                        message='Successfully marked. now you can see tour route in map.')
            print('down -------\n\n\n')
        else:
            tkinter.messagebox.showerror(title='Error', message='Information is not enough for specific destinations.')
            print('Information is not enough for specific destinations.')
            self.adderrorinfo('Information is not enough for specific destinations.')

    def mark_locations(self, locations):
        """Mark extracted locations on the map."""
        self.marker_list = []
        for address in locations:
            print(address)
            marker = self.map_widget.set_address(address, marker=True)
            if marker:
                self.marker_list.append(marker)
        self.connect_marker()
        self.map_widget.set_zoom(1)  # Adjust as necessary, 1 is usually the most zoomed out

    def connect_marker(self):
        position_list = []

        for marker in self.marker_list:
            position_list.append(marker.position)

        if hasattr(self, 'marker_path') and self.marker_path is not None:
            self.map_widget.delete(self.marker_path)

        if len(position_list) > 0:
            self.marker_path = self.map_widget.set_path(position_list)

    def extract_locations(self, text):
        text = text.strip().replace("\n", " ")
        while text.find("  ") != -1:
            text = text.replace("  ", " ")
        return keySearch.keySearch(text), text

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
