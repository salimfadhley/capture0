import typing

import flask_wtf
from capture0_data.online_handles import IndexCompany
from wtforms import RadioField
from wtforms import StringField
from wtforms.validators import DataRequired

EMPATHY_CHOICES = [
    (2, "very empathic"),
    (1, "slightly empathic"),
    (0, "I have no oponion"),
    (-1, "slightly unempathic"),
    (-2, "very unempathic"),
]


class BaseHomeForm(flask_wtf.Form):
    name = StringField('name', description="xxxx", validators=[DataRequired()])


def home_form_instance_factory(companies: typing.List[IndexCompany]) -> BaseHomeForm:
    new_form_elements = {
    c.company: RadioField(c.company, description=c.display_name, validators=[DataRequired()], choices=EMPATHY_CHOICES)
    for c in
    companies}
    new_form = type("frm0", (BaseHomeForm,), new_form_elements)
    form_instance = new_form()
    return form_instance
