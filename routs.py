from flask import Flask
from views import Adview

app = Flask("app")

app.add_url_rule("/advertisements/<int:id_ad>/", view_func=Adview.as_view('advertisemements_delete'),
                 methods=['DELETE', 'GET'] )
app.add_url_rule("/advertisements", view_func=Adview.as_view('advertisements_create'), methods=['POST'])