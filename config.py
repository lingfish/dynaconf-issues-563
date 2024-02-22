from dynaconf import Dynaconf, Validator

validators = [
    # Ensure some parameters exists (are required)
    Validator(
        "TMP_ROOT_DIR",
        must_exist=True,
    ),
]

settings = Dynaconf(
    validators=validators,
    envvar_prefix=False,
    settings_files=["settings.toml", ".secrets.toml"],
    environments=True,
    load_dotenv=True,
    env_switcher="MYPKG_ENV",
)
