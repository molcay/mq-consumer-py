from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=[
        'configs/default_settings.yaml',
        'configs/consumer.yaml',
    ],
    envvar_prefix=False,  # load all environment variables
)
