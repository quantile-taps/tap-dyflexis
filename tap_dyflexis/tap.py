"""Dyflexis tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_dyflexis import streams


class TapDyflexis(Tap):
    """Dyflexis tap class."""

    name = "tap-dyflexis"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "system_name",
            th.StringType,
            required=True,
            description="Project IDs to replicate",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.DyflexisStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.RegisteredHoursStream(self),
            streams.EmployeeStream(self),
        ]


if __name__ == "__main__":
    TapDyflexis.cli()
