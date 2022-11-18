# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.ssm import (
    compliance_level,
    notification_event,
    notification_type,
    operating_system,
    task_type,
    validate_document_content,
    validate_json_checker,
    validate_s3_bucket_name,
)


class S3OutputLocation(AWSProperty):
    """
    `S3OutputLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-s3outputlocation.html>`__
    """

    props: PropsDictType = {
        "OutputS3BucketName": (str, False),
        "OutputS3KeyPrefix": (str, False),
        "OutputS3Region": (str, False),
    }


class InstanceAssociationOutputLocation(AWSProperty):
    """
    `InstanceAssociationOutputLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-association-instanceassociationoutputlocation.html>`__
    """

    props: PropsDictType = {
        "S3Location": (S3OutputLocation, False),
    }


class Targets(AWSProperty):
    """
    `Targets <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtarget-targets.html>`__
    """

    props: PropsDictType = {
        "Key": (str, True),
        "Values": ([str], True),
    }


class Association(AWSObject):
    """
    `Association <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html>`__
    """

    resource_type = "AWS::SSM::Association"

    props: PropsDictType = {
        "ApplyOnlyAtCronInterval": (boolean, False),
        "AssociationName": (str, False),
        "AutomationTargetParameterName": (str, False),
        "CalendarNames": ([str], False),
        "ComplianceSeverity": (str, False),
        "DocumentVersion": (str, False),
        "InstanceId": (str, False),
        "MaxConcurrency": (str, False),
        "MaxErrors": (str, False),
        "Name": (str, True),
        "OutputLocation": (InstanceAssociationOutputLocation, False),
        "Parameters": (dict, False),
        "ScheduleExpression": (str, False),
        "ScheduleOffset": (integer, False),
        "SyncCompliance": (str, False),
        "Targets": ([Targets], False),
        "WaitForSuccessTimeoutSeconds": (integer, False),
    }


class AttachmentsSource(AWSProperty):
    """
    `AttachmentsSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-attachmentssource.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Name": (str, False),
        "Values": ([str], False),
    }


class DocumentRequires(AWSProperty):
    """
    `DocumentRequires <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-document-documentrequires.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Version": (str, False),
    }


class Document(AWSObject):
    """
    `Document <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html>`__
    """

    resource_type = "AWS::SSM::Document"

    props: PropsDictType = {
        "Attachments": ([AttachmentsSource], False),
        "Content": (validate_document_content, True),
        "DocumentFormat": (str, False),
        "DocumentType": (str, False),
        "Name": (str, False),
        "Requires": ([DocumentRequires], False),
        "Tags": (Tags, False),
        "TargetType": (str, False),
        "UpdateMethod": (str, False),
        "VersionName": (str, False),
    }


class MaintenanceWindow(AWSObject):
    """
    `MaintenanceWindow <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html>`__
    """

    resource_type = "AWS::SSM::MaintenanceWindow"

    props: PropsDictType = {
        "AllowUnassociatedTargets": (boolean, True),
        "Cutoff": (integer, True),
        "Description": (str, False),
        "Duration": (integer, True),
        "EndDate": (str, False),
        "Name": (str, True),
        "Schedule": (str, True),
        "ScheduleOffset": (integer, False),
        "ScheduleTimezone": (str, False),
        "StartDate": (str, False),
        "Tags": (Tags, False),
    }


class MaintenanceWindowTarget(AWSObject):
    """
    `MaintenanceWindowTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html>`__
    """

    resource_type = "AWS::SSM::MaintenanceWindowTarget"

    props: PropsDictType = {
        "Description": (str, False),
        "Name": (str, False),
        "OwnerInformation": (str, False),
        "ResourceType": (str, True),
        "Targets": ([Targets], True),
        "WindowId": (str, True),
    }


class LoggingInfo(AWSProperty):
    """
    `LoggingInfo <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-logginginfo.html>`__
    """

    props: PropsDictType = {
        "Region": (str, True),
        "S3Bucket": (validate_s3_bucket_name, True),
        "S3Prefix": (str, False),
    }


class MaintenanceWindowAutomationParameters(AWSProperty):
    """
    `MaintenanceWindowAutomationParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowautomationparameters.html>`__
    """

    props: PropsDictType = {
        "DocumentVersion": (str, False),
        "Parameters": (dict, False),
    }


class MaintenanceWindowLambdaParameters(AWSProperty):
    """
    `MaintenanceWindowLambdaParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowlambdaparameters.html>`__
    """

    props: PropsDictType = {
        "ClientContext": (str, False),
        "Payload": (validate_json_checker, False),
        "Qualifier": (str, False),
    }


class CloudWatchOutputConfig(AWSProperty):
    """
    `CloudWatchOutputConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-cloudwatchoutputconfig.html>`__
    """

    props: PropsDictType = {
        "CloudWatchLogGroupName": (str, False),
        "CloudWatchOutputEnabled": (boolean, False),
    }


class NotificationConfig(AWSProperty):
    """
    `NotificationConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-notificationconfig.html>`__
    """

    props: PropsDictType = {
        "NotificationArn": (str, True),
        "NotificationEvents": (notification_event, False),
        "NotificationType": (notification_type, False),
    }


class MaintenanceWindowRunCommandParameters(AWSProperty):
    """
    `MaintenanceWindowRunCommandParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowruncommandparameters.html>`__
    """

    props: PropsDictType = {
        "CloudWatchOutputConfig": (CloudWatchOutputConfig, False),
        "Comment": (str, False),
        "DocumentHash": (str, False),
        "DocumentHashType": (str, False),
        "DocumentVersion": (str, False),
        "NotificationConfig": (NotificationConfig, False),
        "OutputS3BucketName": (validate_s3_bucket_name, False),
        "OutputS3KeyPrefix": (str, False),
        "Parameters": (dict, False),
        "ServiceRoleArn": (str, False),
        "TimeoutSeconds": (integer, False),
    }


class MaintenanceWindowStepFunctionsParameters(AWSProperty):
    """
    `MaintenanceWindowStepFunctionsParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-maintenancewindowstepfunctionsparameters.html>`__
    """

    props: PropsDictType = {
        "Input": (str, False),
        "Name": (str, False),
    }


class TaskInvocationParameters(AWSProperty):
    """
    `TaskInvocationParameters <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-maintenancewindowtask-taskinvocationparameters.html>`__
    """

    props: PropsDictType = {
        "MaintenanceWindowAutomationParameters": (
            MaintenanceWindowAutomationParameters,
            False,
        ),
        "MaintenanceWindowLambdaParameters": (MaintenanceWindowLambdaParameters, False),
        "MaintenanceWindowRunCommandParameters": (
            MaintenanceWindowRunCommandParameters,
            False,
        ),
        "MaintenanceWindowStepFunctionsParameters": (
            MaintenanceWindowStepFunctionsParameters,
            False,
        ),
    }


class MaintenanceWindowTask(AWSObject):
    """
    `MaintenanceWindowTask <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html>`__
    """

    resource_type = "AWS::SSM::MaintenanceWindowTask"

    props: PropsDictType = {
        "CutoffBehavior": (str, False),
        "Description": (str, False),
        "LoggingInfo": (LoggingInfo, False),
        "MaxConcurrency": (str, False),
        "MaxErrors": (str, False),
        "Name": (str, False),
        "Priority": (integer, True),
        "ServiceRoleArn": (str, False),
        "Targets": ([Targets], False),
        "TaskArn": (str, True),
        "TaskInvocationParameters": (TaskInvocationParameters, False),
        "TaskParameters": (dict, False),
        "TaskType": (task_type, True),
        "WindowId": (str, True),
    }


class Parameter(AWSObject):
    """
    `Parameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html>`__
    """

    resource_type = "AWS::SSM::Parameter"

    props: PropsDictType = {
        "AllowedPattern": (str, False),
        "DataType": (str, False),
        "Description": (str, False),
        "Name": (str, False),
        "Policies": (str, False),
        "Tags": (dict, False),
        "Tier": (str, False),
        "Type": (str, True),
        "Value": (str, True),
    }


class PatchFilter(AWSProperty):
    """
    `PatchFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfilter.html>`__
    """

    props: PropsDictType = {
        "Key": (str, False),
        "Values": ([str], False),
    }


class PatchFilterGroup(AWSProperty):
    """
    `PatchFilterGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchfiltergroup.html>`__
    """

    props: PropsDictType = {
        "PatchFilters": ([PatchFilter], False),
    }


class PatchSource(AWSProperty):
    """
    `PatchSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-patchsource.html>`__
    """

    props: PropsDictType = {
        "Configuration": (str, False),
        "Name": (str, False),
        "Products": ([str], False),
    }


class Rule(AWSProperty):
    """
    `Rule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rule.html>`__
    """

    props: PropsDictType = {
        "ApproveAfterDays": (integer, False),
        "ApproveUntilDate": (str, False),
        "ComplianceLevel": (compliance_level, False),
        "EnableNonSecurity": (boolean, False),
        "PatchFilterGroup": (PatchFilterGroup, False),
    }


class RuleGroup(AWSProperty):
    """
    `RuleGroup <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-patchbaseline-rulegroup.html>`__
    """

    props: PropsDictType = {
        "PatchRules": ([Rule], False),
    }


class PatchBaseline(AWSObject):
    """
    `PatchBaseline <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html>`__
    """

    resource_type = "AWS::SSM::PatchBaseline"

    props: PropsDictType = {
        "ApprovalRules": (RuleGroup, False),
        "ApprovedPatches": ([str], False),
        "ApprovedPatchesComplianceLevel": (compliance_level, False),
        "ApprovedPatchesEnableNonSecurity": (boolean, False),
        "Description": (str, False),
        "GlobalFilters": (PatchFilterGroup, False),
        "Name": (str, True),
        "OperatingSystem": (operating_system, False),
        "PatchGroups": ([str], False),
        "RejectedPatches": ([str], False),
        "RejectedPatchesAction": (str, False),
        "Sources": ([PatchSource], False),
        "Tags": (Tags, False),
    }


class S3Destination(AWSProperty):
    """
    `S3Destination <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-s3destination.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "BucketPrefix": (str, False),
        "BucketRegion": (str, True),
        "KMSKeyArn": (str, False),
        "SyncFormat": (str, True),
    }


class AwsOrganizationsSource(AWSProperty):
    """
    `AwsOrganizationsSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-awsorganizationssource.html>`__
    """

    props: PropsDictType = {
        "OrganizationSourceType": (str, True),
        "OrganizationalUnits": ([str], False),
    }


class SyncSource(AWSProperty):
    """
    `SyncSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ssm-resourcedatasync-syncsource.html>`__
    """

    props: PropsDictType = {
        "AwsOrganizationsSource": (AwsOrganizationsSource, False),
        "IncludeFutureRegions": (boolean, False),
        "SourceRegions": ([str], True),
        "SourceType": (str, True),
    }


class ResourceDataSync(AWSObject):
    """
    `ResourceDataSync <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html>`__
    """

    resource_type = "AWS::SSM::ResourceDataSync"

    props: PropsDictType = {
        "BucketName": (str, False),
        "BucketPrefix": (str, False),
        "BucketRegion": (str, False),
        "KMSKeyArn": (str, False),
        "S3Destination": (S3Destination, False),
        "SyncFormat": (str, False),
        "SyncName": (str, True),
        "SyncSource": (SyncSource, False),
        "SyncType": (str, False),
    }


class ResourcePolicy(AWSObject):
    """
    `ResourcePolicy <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcepolicy.html>`__
    """

    resource_type = "AWS::SSM::ResourcePolicy"

    props: PropsDictType = {
        "Policy": (dict, True),
        "ResourceArn": (str, True),
    }
