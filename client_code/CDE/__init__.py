from ._anvil_designer import CDETemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class CDE(CDETemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #Present users with a login form with just one line of code:
    #anvil.users.login_with_form()

    #Set the Plotly plots template to match the theme of the app
    Plot.templates.default = "rally"
    #When the app starts up, the Sales form will be added to the page
    # self.content_panel.add_component(Sales())
    #Change the color of the optimizer_page_link to indicate that the Optimizer page has been selected
    self.CDE_page_link.background = app.theme_colors['Primary Container']

    #Populate plot_1 with dummy data. All three Bar charts will be added to the same figure
    self.plot_1.data = [
      go.Bar(
        x=[2019, 2020, 2021, 2022, 2023],
        y=[510, 620, 687, 745, 881],
        name="Europe"
    ),
      go.Bar(
        x=[2019, 2020, 2021, 2022, 2023],
        y=[733, 880, 964, 980, 1058],
        name="Americas"
    ),
      go.Bar(
        x=[2019, 2020, 2021, 2022, 2023],
        y=[662, 728, 794, 814, 906],
        name="Asia"
    )
    ]

    #Return the figure from the server to populate plot_2
    self.plot_2.figure = anvil.server.call('return_bar_charts')

    self.plot_3.data = [
      go.Pie(
        labels=["Mobile", "Tablet", "Desktop"],
        values=[2650, 755, 9525]
      )
    ]

  def location_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def data_row_panel_1_show(self, **event_args):
    """This method is called when the data row panel is shown on the screen"""
    pass

  def data_grid_1_show(self, **event_args):
    """This method is called when the data grid is shown on the screen"""
    return anvil.server.call('return_test_df')
    

