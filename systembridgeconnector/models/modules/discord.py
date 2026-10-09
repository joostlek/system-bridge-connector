"""Discord."""

from dataclasses import dataclass

from systembridgeconnector.models.helpers import filter_unexpected_fields


@filter_unexpected_fields
@dataclass(slots=True)
class Discord:
    """Discord."""

    connected: bool = False
    authenticated: bool = False
    mute: bool | None = None
    deaf: bool | None = None
    input_volume: float | None = None
    output_volume: float | None = None
