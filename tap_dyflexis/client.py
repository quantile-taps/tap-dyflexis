"""REST client handling, including DyflexisStream base class."""

from __future__ import annotations

from urllib.parse import parse_qsl
from typing import Any, Iterable

import requests

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from singer_sdk.pagination import BaseHATEOASPaginator, BaseAPIPaginator

class DyflexisPaginator(BaseHATEOASPaginator):
    """Fetches the next url from the response."""
    def get_next_url(self, response):
        data = response.json()
        return data.get("_links").get("next").get("href")

class DyflexisStream(RESTStream):
    """Dyflexis stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return f"https://app.planning.nu/{self.config['system_name']}/api"

    records_jsonpath = "$.registeredHours[*]"  # Or override `parse_response`.

    next_page_token_jsonpath = "$._links.next.href"

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {
            "Accept":"application/json",
            "Content-Type": "application/json",
            "Authorization": f"Token {self.config['api_token']}",
        }
        return headers
    
    def get_new_paginator(self) -> BaseAPIPaginator:
        return DyflexisPaginator()
    
    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,  # noqa: ANN401
    ) -> dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization.

        Args:
            context: The stream context.
            next_page_token: The next page index or value.

        Returns:
            A dictionary of URL query parameters.
        """
        params: dict = {}
        # Next page token is a URL, so we can to parse it to extract the query string
        if next_page_token:
            params.update(parse_qsl(next_page_token.query))

        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result records.

        Args:
            response: The HTTP ``requests.Response`` object.

        Yields:
            Each record from the source.
        """
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(
        self,
        row: dict,
        context: dict | None = None,  # noqa: ARG002
    ) -> dict | None:
        """As needed, append or transform raw data to match expected structure.

        Args:
            row: An individual record from the stream.
            context: The stream context.

        Returns:
            The updated record dictionary, or ``None`` to skip the record.
        """
        return row
    