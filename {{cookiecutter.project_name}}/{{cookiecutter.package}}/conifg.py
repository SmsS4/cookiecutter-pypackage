import dynaconf

__all_settings = dynaconf.Dynaconf(
    envvar_prefix="{{cookiecutter.package.upper()}}",
    settings_files=[
        "settings.toml",
        ".secrets.toml",
        "tests/settings.toml",
    ],
    environments=True,
    lowercase_read=False,
    load_dotenv=True,
    auto_cast=True,
)
__all_settings.validators.register(
    dynaconf.Validator(
        "BACKEND.LOG",
        is_type_of=bool,
        required=True,
        is_in=("INFO", "DEBUG", "ERROR"),
    )
)
__all_settings.validators.validate_all()


backend = __all_settings.BACKEND
