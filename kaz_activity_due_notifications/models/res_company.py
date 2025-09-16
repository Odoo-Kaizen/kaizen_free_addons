# -*- coding: utf-8 -*-
from odoo import fields, models


class ResCompany(models.Model):
    """Extend company with Activity due-notification policies."""
    _inherit = 'res.company'
    # Master toggle for the feature.
    activity_due_notification = fields.Boolean(
        string="Enable Activity Due Notifications",
        help="If enabled, Odoo can notify users about activities before, on, "
             "and/or after their due date based on the settings below.",
        default=False,
    )
    # On-due date notification.
    ondue_date_notify = fields.Boolean(
        string="Notify On Due Date",
        help="Send a reminder on the exact due date of the activity.",
        default=False,
    )
    # After due date notifications.
    after_first_notify = fields.Boolean(
        string="Notify After Due Date (1st)",
        help="Enable the first reminder after the due date.",
        default=False,
    )
    enter_after_first_notify = fields.Integer(
        string="Days After Due Date (1st)",
        help="Number of days after the due date to send the first reminder.",
        default=0,
    )
    after_second_notify = fields.Boolean(
        string="Notify After Due Date (2nd)",
        help="Enable the second reminder after the due date.",
        default=False,
    )
    enter_after_second_notify = fields.Integer(
        string="Days After Due Date (2nd)",
        help="Number of days after the due date to send the second reminder.",
        default=0,
    )
    # Before due date notifications.
    before_first_notify = fields.Boolean(
        string="Notify Before Due Date (1st)",
        help="Enable the first reminder before the due date.",
        default=False,
    )
    before_second_notify = fields.Boolean(
        string="Notify Before Due Date (2nd)",
        help="Enable the second reminder before the due date.",
        default=False,
    )
    enter_before_first_notify = fields.Integer(
        string="Days Before Due Date (1st)",
        help="Number of days before the due date to send the first reminder.",
        default=0,
    )
    enter_before_second_notify = fields.Integer(
        string="Days Before Due Date (2nd)",
        help="Number of days before the due date to send the second reminder.",
        default=0,
    )

    # Whether to notify the creator of the activity on each event.
    notify_create_user_due = fields.Boolean(
        string="Also Notify Activity Creator (On Due Date)",
        help="If enabled, the activity creator will also receive the on-due reminder.",
        default=False,
    )
    notify_create_user_after_first = fields.Boolean(
        string="Also Notify Activity Creator (After 1st)",
        help="If enabled, the activity creator will also receive the first after-due reminder.",
        default=False,
    )
    notify_create_user_after_second = fields.Boolean(
        string="Also Notify Activity Creator (After 2nd)",
        help="If enabled, the activity creator will also receive the second after-due reminder.",
        default=False,
    )
    notify_create_user_before_first = fields.Boolean(
        string="Also Notify Activity Creator (Before 1st)",
        help="If enabled, the activity creator will also receive the first before-due reminder.",
        default=False,
    )
    notify_create_user_before_second = fields.Boolean(
        string="Also Notify Activity Creator (Before 2nd)",
        help="If enabled, the activity creator will also receive the second before-due reminder.",
        default=False,
    )
