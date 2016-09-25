import typing

import flask_wtf
from wtforms import RadioField
from wtforms import StringField
from wtforms.validators import DataRequired

EMPATHY_CHOICES = [
    (2, "very empathic"),
    (1, "somewhat empathic"),
    (0, "neutral"),
    (-1, "somewhat unempathic"),
    (-2, "very unempathic")
]


class BaseHomeForm(flask_wtf.Form):
    name = StringField('name', description="xxxx", validators=[DataRequired()])


def home_form_instance_factory(company_names: typing.List[str]) -> BaseHomeForm:
    new_form_elements = {cn: RadioField(cn, validators=[DataRequired()], choices=EMPATHY_CHOICES) for cn in
                         company_names}
    new_form = type("frm0", (BaseHomeForm,), new_form_elements)
    form_instance = new_form()
    return form_instance
