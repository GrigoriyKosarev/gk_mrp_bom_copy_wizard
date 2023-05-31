from odoo import fields, models, _, api
from odoo.exceptions import UserError, ValidationError

class CopyBOMWizard(models.TransientModel):
    _name = 'gk.copy.bom.wizard'

    # resource_bom_line_id = fields.Many2one(comodel_name='mrp.bom.line', string='BoM Line (resource)')
    bom_id = fields.Many2one(comodel_name='mrp.bom', string='Bill of Material')
    resource_bom_line_ids = fields.Many2many(comodel_name='mrp.bom.line', string='BoM Lines (resources)')

    @api.model
    def default_get(self, fields):
        defaults = super(CopyBOMWizard, self).default_get(fields)
        # bom = self.env['mrp.bom'].browse(1)  # Отримання запису 'mrp.bom' з ID = 1
        # defaults['bom_id'] = bom.id
        active_ids = self.env.context.get('active_ids')
        bom_line_ids = []
        if active_ids != None:
            for bom_line_id in active_ids:
                bom_line_ids.append(bom_line_id)
        defaults['resource_bom_line_ids'] = [(6, 0, bom_line_ids)]
        return defaults

    def action_open_wizard(self):
        return {
            'name': _('Copy BOM Wizard'),
            # 'name': 'Create Partners Wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'gk.copy.bom.wizard',
            'target': 'new',
            'context': self._context,
            # 'context': {'default_country_id': self.env.user.company_id.id},
        }

    def action_copy(self):
        # self.ensure_one()
        if not self.bom_id:
            raise UserError(_("Invalid input: The value cannot be empty"))

        bom = self.bom_id
        for res in self.resource_bom_line_ids:
            self.env['mrp.bom.line'].create({
                    'product_id': res.product_id.id,
                    'product_tmpl_id': res.product_tmpl_id.id,
                    'company_id': res.company_id.id,
                    'product_qty': res.product_qty,
                    'product_uom_id': res.product_uom_id.id,
                    'product_uom_category_id': res.product_uom_category_id.id,
                    # 'sequence': sequence,
                    'bom_id': bom.id,
                    'parent_product_tmpl_id': res.parent_product_tmpl_id.id,
                    # 'possible_bom_product_template_attribute_value_ids': possible_bom_product_template_attribute_value_ids,
                    # 'bom_product_template_attribute_value_ids': bom_product_template_attribute_value_ids,
                    # 'allowed_operation_ids': allowed_operation_ids,
                    'operation_id': res.operation_id.id,
                    # 'child_bom_id': res.child_bom_id.id,
                    # 'child_line_ids': child_line_ids,
                    # 'attachments_count': attachments_count,
                })


