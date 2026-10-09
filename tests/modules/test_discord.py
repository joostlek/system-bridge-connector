"""Test the discord module model."""

from syrupy.assertion import SnapshotAssertion

from systembridgeconnector.models.fixtures.modules.discord import FIXTURE_DISCORD
from systembridgeconnector.models.modules.discord import Discord


def test_discord(snapshot: SnapshotAssertion):
    """Test the discord model."""
    discord = FIXTURE_DISCORD
    assert isinstance(discord, Discord)
    assert discord == snapshot


def test_discord_unexpected_fields():
    """Test the discord model ignores unexpected fields."""
    discord = Discord(connected=True, unexpected="value")  # type: ignore[call-arg]
    assert discord == Discord(connected=True)
