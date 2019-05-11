from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, URL, Optional


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class UserEditForm(FlaskForm):
    """ Form for editing user pages. """

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image_url = StringField('(Optional) Image URL')
    header_image_url = StringField(
        'Header Image',
        validators=[Optional(), URL()],
        )
    bio = TextAreaField(
        'Bio',
        validators=[Optional(),
                    Length(max=(300),
                    message="""Must be less than 300 characters.""")],
        )
    location = StringField(
        'Location',
        validators=[Optional(),
                    Length(max=(40),
                    message="Must be less than 40 characters.")]
        )
    password = PasswordField('Password', validators=[Length(min=6)])
