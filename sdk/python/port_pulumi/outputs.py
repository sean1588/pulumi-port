# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'ActionInvocationMethod',
    'ActionUserProperty',
    'BlueprintCalculationProperty',
    'BlueprintChangelogDestination',
    'BlueprintMirrorProperty',
    'BlueprintProperty',
    'BlueprintPropertySpecAuthentication',
    'BlueprintRelation',
    'EntityProperty',
    'EntityRelation',
]

@pulumi.output_type
class ActionInvocationMethod(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "azureOrg":
            suggest = "azure_org"
        elif key == "omitPayload":
            suggest = "omit_payload"
        elif key == "omitUserInputs":
            suggest = "omit_user_inputs"
        elif key == "reportWorkflowStatus":
            suggest = "report_workflow_status"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ActionInvocationMethod. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ActionInvocationMethod.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ActionInvocationMethod.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 agent: Optional[bool] = None,
                 azure_org: Optional[str] = None,
                 omit_payload: Optional[bool] = None,
                 omit_user_inputs: Optional[bool] = None,
                 org: Optional[str] = None,
                 repo: Optional[str] = None,
                 report_workflow_status: Optional[bool] = None,
                 url: Optional[str] = None,
                 webhook: Optional[str] = None,
                 workflow: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if agent is not None:
            pulumi.set(__self__, "agent", agent)
        if azure_org is not None:
            pulumi.set(__self__, "azure_org", azure_org)
        if omit_payload is not None:
            pulumi.set(__self__, "omit_payload", omit_payload)
        if omit_user_inputs is not None:
            pulumi.set(__self__, "omit_user_inputs", omit_user_inputs)
        if org is not None:
            pulumi.set(__self__, "org", org)
        if repo is not None:
            pulumi.set(__self__, "repo", repo)
        if report_workflow_status is not None:
            pulumi.set(__self__, "report_workflow_status", report_workflow_status)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if webhook is not None:
            pulumi.set(__self__, "webhook", webhook)
        if workflow is not None:
            pulumi.set(__self__, "workflow", workflow)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def agent(self) -> Optional[bool]:
        return pulumi.get(self, "agent")

    @property
    @pulumi.getter(name="azureOrg")
    def azure_org(self) -> Optional[str]:
        return pulumi.get(self, "azure_org")

    @property
    @pulumi.getter(name="omitPayload")
    def omit_payload(self) -> Optional[bool]:
        return pulumi.get(self, "omit_payload")

    @property
    @pulumi.getter(name="omitUserInputs")
    def omit_user_inputs(self) -> Optional[bool]:
        return pulumi.get(self, "omit_user_inputs")

    @property
    @pulumi.getter
    def org(self) -> Optional[str]:
        return pulumi.get(self, "org")

    @property
    @pulumi.getter
    def repo(self) -> Optional[str]:
        return pulumi.get(self, "repo")

    @property
    @pulumi.getter(name="reportWorkflowStatus")
    def report_workflow_status(self) -> Optional[bool]:
        return pulumi.get(self, "report_workflow_status")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def webhook(self) -> Optional[str]:
        return pulumi.get(self, "webhook")

    @property
    @pulumi.getter
    def workflow(self) -> Optional[str]:
        return pulumi.get(self, "workflow")


@pulumi.output_type
class ActionUserProperty(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "defaultItems":
            suggest = "default_items"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ActionUserProperty. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ActionUserProperty.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ActionUserProperty.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 identifier: str,
                 title: str,
                 type: str,
                 blueprint: Optional[str] = None,
                 default: Optional[str] = None,
                 default_items: Optional[Sequence[str]] = None,
                 description: Optional[str] = None,
                 enums: Optional[Sequence[str]] = None,
                 format: Optional[str] = None,
                 pattern: Optional[str] = None,
                 required: Optional[bool] = None):
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "type", type)
        if blueprint is not None:
            pulumi.set(__self__, "blueprint", blueprint)
        if default is not None:
            pulumi.set(__self__, "default", default)
        if default_items is not None:
            pulumi.set(__self__, "default_items", default_items)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enums is not None:
            pulumi.set(__self__, "enums", enums)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if pattern is not None:
            pulumi.set(__self__, "pattern", pattern)
        if required is not None:
            pulumi.set(__self__, "required", required)

    @property
    @pulumi.getter
    def identifier(self) -> str:
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def blueprint(self) -> Optional[str]:
        return pulumi.get(self, "blueprint")

    @property
    @pulumi.getter
    def default(self) -> Optional[str]:
        return pulumi.get(self, "default")

    @property
    @pulumi.getter(name="defaultItems")
    def default_items(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "default_items")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enums(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "enums")

    @property
    @pulumi.getter
    def format(self) -> Optional[str]:
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def pattern(self) -> Optional[str]:
        return pulumi.get(self, "pattern")

    @property
    @pulumi.getter
    def required(self) -> Optional[bool]:
        return pulumi.get(self, "required")


@pulumi.output_type
class BlueprintCalculationProperty(dict):
    def __init__(__self__, *,
                 calculation: str,
                 identifier: str,
                 type: str,
                 colorized: Optional[bool] = None,
                 colors: Optional[Mapping[str, str]] = None,
                 description: Optional[str] = None,
                 format: Optional[str] = None,
                 icon: Optional[str] = None,
                 title: Optional[str] = None):
        pulumi.set(__self__, "calculation", calculation)
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "type", type)
        if colorized is not None:
            pulumi.set(__self__, "colorized", colorized)
        if colors is not None:
            pulumi.set(__self__, "colors", colors)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if icon is not None:
            pulumi.set(__self__, "icon", icon)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def calculation(self) -> str:
        return pulumi.get(self, "calculation")

    @property
    @pulumi.getter
    def identifier(self) -> str:
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def colorized(self) -> Optional[bool]:
        return pulumi.get(self, "colorized")

    @property
    @pulumi.getter
    def colors(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "colors")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def format(self) -> Optional[str]:
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def icon(self) -> Optional[str]:
        return pulumi.get(self, "icon")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        return pulumi.get(self, "title")


@pulumi.output_type
class BlueprintChangelogDestination(dict):
    def __init__(__self__, *,
                 type: str,
                 agent: Optional[bool] = None,
                 url: Optional[str] = None):
        pulumi.set(__self__, "type", type)
        if agent is not None:
            pulumi.set(__self__, "agent", agent)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def agent(self) -> Optional[bool]:
        return pulumi.get(self, "agent")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        return pulumi.get(self, "url")


@pulumi.output_type
class BlueprintMirrorProperty(dict):
    def __init__(__self__, *,
                 identifier: str,
                 path: str,
                 title: Optional[str] = None):
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "path", path)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def identifier(self) -> str:
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def path(self) -> str:
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        return pulumi.get(self, "title")


@pulumi.output_type
class BlueprintProperty(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "defaultItems":
            suggest = "default_items"
        elif key == "defaultValue":
            suggest = "default_value"
        elif key == "enumColors":
            suggest = "enum_colors"
        elif key == "maxItems":
            suggest = "max_items"
        elif key == "maxLength":
            suggest = "max_length"
        elif key == "minItems":
            suggest = "min_items"
        elif key == "minLength":
            suggest = "min_length"
        elif key == "specAuthentication":
            suggest = "spec_authentication"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BlueprintProperty. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BlueprintProperty.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BlueprintProperty.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 identifier: str,
                 title: str,
                 type: str,
                 default: Optional[str] = None,
                 default_items: Optional[Sequence[str]] = None,
                 default_value: Optional[Mapping[str, str]] = None,
                 description: Optional[str] = None,
                 enum_colors: Optional[Mapping[str, str]] = None,
                 enums: Optional[Sequence[str]] = None,
                 format: Optional[str] = None,
                 icon: Optional[str] = None,
                 items: Optional[Mapping[str, Any]] = None,
                 max_items: Optional[int] = None,
                 max_length: Optional[int] = None,
                 min_items: Optional[int] = None,
                 min_length: Optional[int] = None,
                 required: Optional[bool] = None,
                 spec: Optional[str] = None,
                 spec_authentication: Optional['outputs.BlueprintPropertySpecAuthentication'] = None):
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "type", type)
        if default is not None:
            pulumi.set(__self__, "default", default)
        if default_items is not None:
            pulumi.set(__self__, "default_items", default_items)
        if default_value is not None:
            pulumi.set(__self__, "default_value", default_value)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enum_colors is not None:
            pulumi.set(__self__, "enum_colors", enum_colors)
        if enums is not None:
            pulumi.set(__self__, "enums", enums)
        if format is not None:
            pulumi.set(__self__, "format", format)
        if icon is not None:
            pulumi.set(__self__, "icon", icon)
        if items is not None:
            pulumi.set(__self__, "items", items)
        if max_items is not None:
            pulumi.set(__self__, "max_items", max_items)
        if max_length is not None:
            pulumi.set(__self__, "max_length", max_length)
        if min_items is not None:
            pulumi.set(__self__, "min_items", min_items)
        if min_length is not None:
            pulumi.set(__self__, "min_length", min_length)
        if required is not None:
            pulumi.set(__self__, "required", required)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)
        if spec_authentication is not None:
            pulumi.set(__self__, "spec_authentication", spec_authentication)

    @property
    @pulumi.getter
    def identifier(self) -> str:
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def default(self) -> Optional[str]:
        warnings.warn("""Use default_value instead""", DeprecationWarning)
        pulumi.log.warn("""default is deprecated: Use default_value instead""")

        return pulumi.get(self, "default")

    @property
    @pulumi.getter(name="defaultItems")
    def default_items(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "default_items")

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enumColors")
    def enum_colors(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "enum_colors")

    @property
    @pulumi.getter
    def enums(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "enums")

    @property
    @pulumi.getter
    def format(self) -> Optional[str]:
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def icon(self) -> Optional[str]:
        return pulumi.get(self, "icon")

    @property
    @pulumi.getter
    def items(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "items")

    @property
    @pulumi.getter(name="maxItems")
    def max_items(self) -> Optional[int]:
        return pulumi.get(self, "max_items")

    @property
    @pulumi.getter(name="maxLength")
    def max_length(self) -> Optional[int]:
        return pulumi.get(self, "max_length")

    @property
    @pulumi.getter(name="minItems")
    def min_items(self) -> Optional[int]:
        return pulumi.get(self, "min_items")

    @property
    @pulumi.getter(name="minLength")
    def min_length(self) -> Optional[int]:
        return pulumi.get(self, "min_length")

    @property
    @pulumi.getter
    def required(self) -> Optional[bool]:
        return pulumi.get(self, "required")

    @property
    @pulumi.getter
    def spec(self) -> Optional[str]:
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter(name="specAuthentication")
    def spec_authentication(self) -> Optional['outputs.BlueprintPropertySpecAuthentication']:
        return pulumi.get(self, "spec_authentication")


@pulumi.output_type
class BlueprintPropertySpecAuthentication(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "authorizationUrl":
            suggest = "authorization_url"
        elif key == "clientId":
            suggest = "client_id"
        elif key == "tokenUrl":
            suggest = "token_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BlueprintPropertySpecAuthentication. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BlueprintPropertySpecAuthentication.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BlueprintPropertySpecAuthentication.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 authorization_url: str,
                 client_id: str,
                 token_url: str):
        pulumi.set(__self__, "authorization_url", authorization_url)
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "token_url", token_url)

    @property
    @pulumi.getter(name="authorizationUrl")
    def authorization_url(self) -> str:
        return pulumi.get(self, "authorization_url")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="tokenUrl")
    def token_url(self) -> str:
        return pulumi.get(self, "token_url")


@pulumi.output_type
class BlueprintRelation(dict):
    def __init__(__self__, *,
                 identifier: str,
                 target: str,
                 many: Optional[bool] = None,
                 required: Optional[bool] = None,
                 title: Optional[str] = None):
        pulumi.set(__self__, "identifier", identifier)
        pulumi.set(__self__, "target", target)
        if many is not None:
            pulumi.set(__self__, "many", many)
        if required is not None:
            pulumi.set(__self__, "required", required)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def identifier(self) -> str:
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def target(self) -> str:
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def many(self) -> Optional[bool]:
        return pulumi.get(self, "many")

    @property
    @pulumi.getter
    def required(self) -> Optional[bool]:
        return pulumi.get(self, "required")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        return pulumi.get(self, "title")


@pulumi.output_type
class EntityProperty(dict):
    def __init__(__self__, *,
                 name: str,
                 items: Optional[Sequence[str]] = None,
                 type: Optional[str] = None,
                 value: Optional[str] = None):
        pulumi.set(__self__, "name", name)
        if items is not None:
            pulumi.set(__self__, "items", items)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def items(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "items")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        warnings.warn("""property type is not required anymore""", DeprecationWarning)
        pulumi.log.warn("""type is deprecated: property type is not required anymore""")

        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class EntityRelation(dict):
    def __init__(__self__, *,
                 name: str,
                 identifier: Optional[str] = None,
                 identifiers: Optional[Sequence[str]] = None):
        pulumi.set(__self__, "name", name)
        if identifier is not None:
            pulumi.set(__self__, "identifier", identifier)
        if identifiers is not None:
            pulumi.set(__self__, "identifiers", identifiers)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def identifier(self) -> Optional[str]:
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def identifiers(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "identifiers")


