# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots["test_query_html context"] = {
    "config": {
        "adminUrl": "/admin/data_browser/view/add/",
        "allModelFields": {
            "auth.Group": {
                "fields": {
                    "admin": {"concrete": False, "type": "html"},
                    "id": {"concrete": True, "type": "number"},
                    "name": {"concrete": True, "type": "string"},
                },
                "fks": {},
                "sorted_fields": ["id", "admin", "name"],
                "sorted_fks": [],
            },
            "auth.User": {
                "fields": {
                    "admin": {"concrete": False, "type": "html"},
                    "date_joined": {"concrete": True, "type": "time"},
                    "email": {"concrete": True, "type": "string"},
                    "first_name": {"concrete": True, "type": "string"},
                    "id": {"concrete": True, "type": "number"},
                    "is_active": {"concrete": True, "type": "boolean"},
                    "is_staff": {"concrete": True, "type": "boolean"},
                    "is_superuser": {"concrete": True, "type": "boolean"},
                    "last_login": {"concrete": True, "type": "time"},
                    "last_name": {"concrete": True, "type": "string"},
                    "password": {"concrete": True, "type": "string"},
                    "username": {"concrete": True, "type": "string"},
                },
                "fks": {},
                "sorted_fields": [
                    "id",
                    "admin",
                    "date_joined",
                    "email",
                    "first_name",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "last_login",
                    "last_name",
                    "password",
                    "username",
                ],
                "sorted_fks": [],
            },
            "data_browser.View": {
                "fields": {
                    "admin": {"concrete": False, "type": "html"},
                    "created_time": {"concrete": True, "type": "time"},
                    "description": {"concrete": True, "type": "string"},
                    "fields": {"concrete": True, "type": "string"},
                    "google_sheets_formula": {"concrete": False, "type": "string"},
                    "id": {"concrete": True, "type": "string"},
                    "model_name": {"concrete": True, "type": "string"},
                    "name": {"concrete": True, "type": "string"},
                    "open_view": {"concrete": False, "type": "string"},
                    "public": {"concrete": True, "type": "boolean"},
                    "public_link": {"concrete": False, "type": "string"},
                    "query": {"concrete": True, "type": "string"},
                },
                "fks": {"owner": {"model": "auth.User"}},
                "sorted_fields": [
                    "id",
                    "admin",
                    "created_time",
                    "description",
                    "fields",
                    "google_sheets_formula",
                    "model_name",
                    "name",
                    "open_view",
                    "public",
                    "public_link",
                    "query",
                ],
                "sorted_fks": ["owner"],
            },
            "tests.Address": {
                "fields": {
                    "admin": {"concrete": False, "type": "html"},
                    "city": {"concrete": True, "type": "string"},
                    "id": {"concrete": True, "type": "number"},
                },
                "fks": {},
                "sorted_fields": ["id", "admin", "city"],
                "sorted_fks": [],
            },
            "tests.InAdmin": {
                "fields": {
                    "admin": {"concrete": False, "type": "html"},
                    "id": {"concrete": True, "type": "number"},
                    "name": {"concrete": True, "type": "string"},
                },
                "fks": {},
                "sorted_fields": ["id", "admin", "name"],
                "sorted_fks": [],
            },
            "tests.InlineAdmin": {
                "fields": {
                    "id": {"concrete": True, "type": "number"},
                    "name": {"concrete": True, "type": "string"},
                },
                "fks": {"in_admin": {"model": "tests.InAdmin"}},
                "sorted_fields": ["id", "name"],
                "sorted_fks": ["in_admin"],
            },
            "tests.Normal": {
                "fields": {
                    "admin": {"concrete": False, "type": "html"},
                    "id": {"concrete": True, "type": "number"},
                    "name": {"concrete": True, "type": "string"},
                },
                "fks": {
                    "in_admin": {"model": "tests.InAdmin"},
                    "inline_admin": {"model": "tests.InlineAdmin"},
                },
                "sorted_fields": ["id", "admin", "name"],
                "sorted_fks": ["in_admin", "inline_admin"],
            },
            "tests.Producer": {
                "fields": {
                    "admin": {"concrete": False, "type": "html"},
                    "id": {"concrete": True, "type": "number"},
                    "name": {"concrete": True, "type": "string"},
                },
                "fks": {"address": {"model": "tests.Address"}},
                "sorted_fields": ["id", "admin", "name"],
                "sorted_fks": ["address"],
            },
            "tests.Product": {
                "fields": {
                    "admin": {"concrete": False, "type": "html"},
                    "id": {"concrete": True, "type": "number"},
                    "is_onsale": {"concrete": False, "type": "string"},
                    "name": {"concrete": True, "type": "string"},
                    "onsale": {"concrete": True, "type": "boolean"},
                    "size": {"concrete": True, "type": "number"},
                    "size_unit": {"concrete": True, "type": "string"},
                },
                "fks": {
                    "default_sku": {"model": "tests.SKU"},
                    "producer": {"model": "tests.Producer"},
                },
                "sorted_fields": [
                    "id",
                    "admin",
                    "is_onsale",
                    "name",
                    "onsale",
                    "size",
                    "size_unit",
                ],
                "sorted_fks": ["default_sku", "producer"],
            },
            "tests.SKU": {
                "fields": {
                    "admin": {"concrete": False, "type": "html"},
                    "id": {"concrete": True, "type": "number"},
                    "name": {"concrete": True, "type": "string"},
                },
                "fks": {"product": {"model": "tests.Product"}},
                "sorted_fields": ["id", "admin", "name"],
                "sorted_fks": ["product"],
            },
            "tests.Tag": {
                "fields": {
                    "admin": {"concrete": False, "type": "html"},
                    "id": {"concrete": True, "type": "number"},
                    "name": {"concrete": True, "type": "string"},
                },
                "fks": {},
                "sorted_fields": ["id", "admin", "name"],
                "sorted_fks": [],
            },
        },
        "baseUrl": "/data_browser/",
        "savedViews": [],
        "sortedModels": [
            "auth.Group",
            "auth.User",
            "data_browser.View",
            "tests.Address",
            "tests.InAdmin",
            "tests.InlineAdmin",
            "tests.Normal",
            "tests.Producer",
            "tests.Product",
            "tests.SKU",
            "tests.Tag",
        ],
        "types": {
            "boolean": {
                "aggregates": ["average", "sum"],
                "defaultLookup": "equals",
                "defaultValue": True,
                "lookups": {
                    "equals": {"type": "boolean"},
                    "is_null": {"type": "boolean"},
                    "not_equals": {"type": "boolean"},
                },
                "sortedLookups": ["equals", "not_equals", "is_null"],
            },
            "html": {
                "aggregates": [],
                "defaultLookup": None,
                "defaultValue": None,
                "lookups": {},
                "sortedLookups": [],
            },
            "number": {
                "aggregates": [
                    "average",
                    "count",
                    "max",
                    "min",
                    "std_dev",
                    "sum",
                    "variance",
                ],
                "defaultLookup": "equals",
                "defaultValue": 0,
                "lookups": {
                    "equals": {"type": "number"},
                    "gt": {"type": "number"},
                    "gte": {"type": "number"},
                    "is_null": {"type": "boolean"},
                    "lt": {"type": "number"},
                    "lte": {"type": "number"},
                    "not_equals": {"type": "number"},
                },
                "sortedLookups": [
                    "equals",
                    "not_equals",
                    "gt",
                    "gte",
                    "lt",
                    "lte",
                    "is_null",
                ],
            },
            "string": {
                "aggregates": ["count"],
                "defaultLookup": "equals",
                "defaultValue": "",
                "lookups": {
                    "contains": {"type": "string"},
                    "ends_with": {"type": "string"},
                    "equals": {"type": "string"},
                    "is_null": {"type": "boolean"},
                    "not_contains": {"type": "string"},
                    "not_ends_with": {"type": "string"},
                    "not_equals": {"type": "string"},
                    "not_regex": {"type": "string"},
                    "not_starts_with": {"type": "string"},
                    "regex": {"type": "string"},
                    "starts_with": {"type": "string"},
                },
                "sortedLookups": [
                    "equals",
                    "contains",
                    "starts_with",
                    "ends_with",
                    "regex",
                    "not_equals",
                    "not_contains",
                    "not_starts_with",
                    "not_ends_with",
                    "not_regex",
                    "is_null",
                ],
            },
            "time": {
                "aggregates": ["count"],
                "defaultLookup": "equals",
                "defaultValue": "redacted",
                "lookups": {
                    "equals": {"type": "time"},
                    "gt": {"type": "time"},
                    "gte": {"type": "time"},
                    "is_null": {"type": "boolean"},
                    "lt": {"type": "time"},
                    "lte": {"type": "time"},
                    "not_equals": {"type": "time"},
                },
                "sortedLookups": [
                    "equals",
                    "not_equals",
                    "gt",
                    "gte",
                    "lt",
                    "lte",
                    "is_null",
                ],
            },
        },
        "version": "redacted",
    },
    "initialState": {
        "fields": [
            {"path": "size", "priority": 0, "sort": "dsc"},
            {"path": "name", "priority": 1, "sort": "asc"},
            {"path": "size_unit", "priority": None, "sort": None},
        ],
        "filters": [
            {"errorMessage": None, "lookup": "lt", "path": "size", "value": "2"},
            {"errorMessage": None, "lookup": "gt", "path": "id", "value": "0"},
        ],
        "model": "tests.Product",
        "results": [],
    },
    "sentryDsn": None,
}
