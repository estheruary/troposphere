# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 51.0.0


from . import AWSObject, AWSProperty, PropsDictType, Tags


class ExperimentTemplateAction(AWSProperty):
    """
    `ExperimentTemplateAction <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplateaction.html>`__
    """

    props: PropsDictType = {
        "ActionId": (str, True),
        "Description": (str, False),
        "Parameters": (dict, False),
        "StartAfter": ([str], False),
        "Targets": (dict, False),
    }


class ExperimentTemplateStopCondition(AWSProperty):
    """
    `ExperimentTemplateStopCondition <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatestopcondition.html>`__
    """

    props: PropsDictType = {
        "Source": (str, True),
        "Value": (str, False),
    }


class ExperimentTemplateTargetFilter(AWSProperty):
    """
    `ExperimentTemplateTargetFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetargetfilter.html>`__
    """

    props: PropsDictType = {
        "Path": (str, True),
        "Values": ([str], True),
    }


class ExperimentTemplateTarget(AWSProperty):
    """
    `ExperimentTemplateTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fis-experimenttemplate-experimenttemplatetarget.html>`__
    """

    props: PropsDictType = {
        "Filters": ([ExperimentTemplateTargetFilter], False),
        "ResourceArns": ([str], False),
        "ResourceTags": (dict, False),
        "ResourceType": (str, True),
        "SelectionMode": (str, True),
    }


class ExperimentTemplate(AWSObject):
    """
    `ExperimentTemplate <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fis-experimenttemplate.html>`__
    """

    resource_type = "AWS::FIS::ExperimentTemplate"

    props: PropsDictType = {
        "Actions": (dict, False),
        "Description": (str, True),
        "RoleArn": (str, True),
        "StopConditions": ([ExperimentTemplateStopCondition], True),
        "Tags": (Tags, True),
        "Targets": (dict, True),
    }
