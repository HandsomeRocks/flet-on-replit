import os
import flet
from flet import (
  Page, 
  Text, 
  Row, 
  TextField, 
  ElevatedButton, 
  FilledButton, 
  TextButton, Checkbox,
  Column as UIColumn, 
  AlertDialog, 
  alignment, 
  colors, 
  border_radius, 
  ListView, 
  FloatingActionButton, 
  icons
)
from time import sleep
from flet.ref import Ref
#from database_helper import *
from numpy.random import seed
from numpy.random import randint
import random
import string

flet_server_port = os.environ['FLET_SERVER_PORT']


def main(page: Page):
    page.add(Text(value="Testing what happens when I push to Git!"))
    page.theme_mode = "light"

    def add_clicked(e):
        page.add(Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    def search_clicked(e):
        page.add(Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    new_task = TextField(hint_text="Whats would you like to drink since you don't have Bombay today?", expand=True)
    tasks_view = UIColumn()
    view = UIColumn(
        controls=[
            Row(
                controls=[
                    new_task,
                    FloatingActionButton(icon=icons.SEARCH, on_click=search_clicked),
                ],
            ),
            tasks_view,
        ],
    )

    page.horizontal_alignment = "center"
    page.add(view)

flet.app(target=main, view=flet.WEB_BROWSER, assets_dir="assets", port=flet_server_port)