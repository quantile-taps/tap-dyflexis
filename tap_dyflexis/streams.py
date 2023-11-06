"""Stream type classes for tap-dyflexis."""

from __future__ import annotations

from singer_sdk import typing as th 

from tap_dyflexis.client import DyflexisStream

class RegisteredHoursStream(DyflexisStream):
    """Registered hours from Dyflexis."""

    name = "registered_hours"
    path = "/business/v3/registered-hours"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("employeeId", th.IntegerType),
        th.Property("personnelNumber", th.StringType),
        th.Property("firstName", th.StringType),
        th.Property("infix", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("employeeCostCenter", th.StringType),
        th.Property("contractTypeId", th.IntegerType),
        th.Property("contractType", th.StringType),
        th.Property("officeId", th.IntegerType),
        th.Property("officeName", th.StringType),
        th.Property("departmentId", th.StringType),
        th.Property("departmentName", th.StringType),
        th.Property("costCenterId", th.StringType),
        th.Property("costCenterName", th.StringType),
        th.Property("costCenterCode", th.StringType),
        th.Property("startDateTime", th.DateTimeType),
        th.Property("endDateTime", th.DateTimeType),
        th.Property("hourType", th.StringType),
        th.Property("hours", th.NumberType),
        th.Property("status", th.StringType),
        th.Property("breakMinutes", th.IntegerType),
        th.Property("duration", th.IntegerType),
    ).to_dict()