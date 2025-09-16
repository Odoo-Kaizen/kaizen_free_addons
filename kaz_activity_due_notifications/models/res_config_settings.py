# -*- coding: utf-8 -*-


from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """Expose company Activity notification policy in General Settings."""
    _inherit = 'res.config.settings'

    activity_due_notification = fields.Boolean(
        related='company_id.activity_due_notification',
        readonly=False,
    )
    ondue_date_notify = fields.Boolean(
        related='company_id.ondue_date_notify',
        readonly=False,
    )

    # After due
    after_first_notify = fields.Boolean(
        related='company_id.after_first_notify',
        readonly=False,
    )
    after_second_notify = fields.Boolean(
        related='company_id.after_second_notify',
        readonly=False,
    )
    enter_after_first_notify = fields.Integer(
        related='company_id.enter_after_first_notify',
        readonly=False,
    )
    enter_after_second_notify = fields.Integer(
        related='company_id.enter_after_second_notify',
        readonly=False,
    )

    # Before due
    before_first_notify = fields.Boolean(
        related='company_id.before_first_notify',
        readonly=False,
    )
    before_second_notify = fields.Boolean(
        related='company_id.before_second_notify',
        readonly=False,
    )
    enter_before_first_notify = fields.Integer(
        related='company_id.enter_before_first_notify',
        readonly=False,
    )
    enter_before_second_notify = fields.Integer(
        related='company_id.enter_before_second_notify',
        readonly=False,
    )

    # Creator notification toggles
    notify_create_user_due = fields.Boolean(
        related='company_id.notify_create_user_due',
        readonly=False,
    )
    notify_create_user_after_first = fields.Boolean(
        related='company_id.notify_create_user_after_first',
        readonly=False,
    )
    notify_create_user_after_second = fields.Boolean(
        related='company_id.notify_create_user_after_second',
        readonly=False,
    )
    notify_create_user_before_first = fields.Boolean(
        related='company_id.notify_create_user_before_first',
        readonly=False,
    )
    notify_create_user_before_second = fields.Boolean(
        related='company_id.notify_create_user_before_second',
        readonly=False,
    )
