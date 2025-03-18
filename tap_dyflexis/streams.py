"""Stream type classes for tap-dyflexis."""

from __future__ import annotations
from singer_sdk import typing as th 
from tap_dyflexis.client import DyflexisStream
from typing import Any
from urllib.parse import parse_qsl
from datetime import datetime


class RegisteredHoursStream(DyflexisStream):
    """Registered hours from Dyflexis."""

    name = "registered_hours"
    path = "/business/v3/registered-hours"
    primary_keys = ["id"]
    replication_key = "startDateTime"
    records_jsonpath = "$.registeredHours[*]"

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
        th.Property("departmentId", th.IntegerType),
        th.Property("departmentName", th.StringType),
        th.Property("startDateTime", th.DateTimeType),
        th.Property("endDateTime", th.DateTimeType),
        th.Property("hourType", th.StringType),
        th.Property("hours", th.NumberType),
        th.Property("status", th.StringType),
        th.Property("breakMinutes", th.IntegerType),
        th.Property("duration", th.IntegerType),
        # th.Property("costCenterId", th.StringType),
        # th.Property("costCenterName", th.StringType),
        # th.Property("costCenterCode", th.StringType),
        # th.Property("kilometers", th.StringType),
        # th.Property("customExpenses", th.StringType),
    ).to_dict()


class EmployeeStream(DyflexisStream):
    """Employees from Dyflexis."""

    name = "employees"
    path = "/payroll/v3/employees"
    primary_keys = ["employeeId"]
    replication_key = None
    records_jsonpath = "$.employees[*]"

    schema = th.PropertiesList(
        th.Property("employeeId", th.IntegerType),
        th.Property("firstName", th.StringType),
        th.Property("lastNamePrefix", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("nameFormat", th.StringType),
        th.Property("employmentStart", th.StringType),
        th.Property("employmentEnd", th.StringType),
        th.Property("personnelNumber", th.StringType),
        th.Property("costCenter", th.StringType),
        th.Property("probationDate", th.StringType),
        th.Property("employerReferenceId", th.StringType),
        th.Property("jobDescription", th.StringType),
        th.Property("contracts", th.ArrayType(
            th.ObjectType(
                th.Property("contractReference", th.StringType),
                th.Property("officeId", th.IntegerType),
                th.Property("type", th.IntegerType),
                th.Property("start", th.DateType),
                th.Property("end", th.DateType),
                th.Property("hoursPerWeek", th.NumberType),
                th.Property("daysPerWeek", th.IntegerType),
                th.Property("hourlySalary", th.IntegerType),
                th.Property("maxHoursPerWeek", th.IntegerType),
            )
        ))
    ).to_dict()