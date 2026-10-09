"""Fixture for discord module."""

from systembridgeconnector.models.modules.discord import Discord

FIXTURE_DISCORD = Discord(
    connected=True,
    authenticated=True,
    mute=False,
    deaf=False,
    input_volume=80,
    output_volume=100,
)
