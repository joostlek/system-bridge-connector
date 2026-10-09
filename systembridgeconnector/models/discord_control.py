"""Discord Control."""

from dataclasses import dataclass
from enum import StrEnum


class DiscordAction(StrEnum):
    """Discord Action."""

    MUTE = "MUTE"
    UNMUTE = "UNMUTE"
    TOGGLE_MUTE = "TOGGLE_MUTE"
    DEAFEN = "DEAFEN"
    UNDEAFEN = "UNDEAFEN"
    TOGGLE_DEAFEN = "TOGGLE_DEAFEN"
    SET_INPUT_VOLUME = "SET_INPUT_VOLUME"
    SET_OUTPUT_VOLUME = "SET_OUTPUT_VOLUME"


@dataclass(slots=True)
class DiscordControl:
    """Discord Control.

    `value` is required for the volume actions: 0-100 for input volume and
    0-200 for output volume. It is ignored for the other actions.
    """

    action: str
    value: float | None = None
