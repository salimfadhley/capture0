import typing

import flask_wtf
from capture0.forms import countries
from capture0_data.online_handles import IndexCompany
from wtforms import RadioField
from wtforms import SelectField
from wtforms import StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

EMPATHY_CHOICES = [
    (2, "very empathic"),
    (1, "slightly empathic"),
    (0, "I have no oponion"),
    (-1, "slightly unempathic"),
    (-2, "very unempathic"),
]


class BaseHomeForm(flask_wtf.Form):
    name = StringField('name', description="What's your name?", validators=[DataRequired()])
    country = SelectField('country', description="Where do you live?", choices=countries.COUNTRIES)
    email = EmailField('email', description="Email address?", validators=[DataRequired(), Email()])
    most_empathic = StringField('most_empathic',
                                description="In case we missed your favourite - who is the world's most empathic company?",
                                validators=[DataRequired()])


def home_form_instance_factory(companies: typing.List[IndexCompany]) -> BaseHomeForm:
    new_form_elements = {
    c.company: RadioField(c.company, description=c.display_name, validators=[DataRequired()], choices=EMPATHY_CHOICES)
    for c in
    companies}
    new_form = type("frm0", (BaseHomeForm,), new_form_elements)
    form_instance = new_form()
    return form_instance
