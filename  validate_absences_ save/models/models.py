# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from datetime import datetime, date, time

class primermodulo(models.Model):
    _inherit = 'hr.leave'

    fecha_ac = fields.Date(string="Fecha actual",default=fields.Date.today, readonly=True,)


    @api.model
    def create(self, values):
        val= super(primermodulo, self).create(values)
        fecha_actual = val.fecha_ac
        fecha_ex = val.holiday_status_id.validity_stop
        print(fecha_actual)
        print(fecha_ex)
        busque = self.env['hr.leave.allocation'].search([('employee_id','=',val.employee_id.id),('extended_permission','=',True),('holiday_status_id','=',val.holiday_status_id.id)],limit=1)
        em = busque.extended_permission
        if em == False:
            if fecha_actual and fecha_ex:
                if  fecha_actual > fecha_ex:
                    raise ValidationError('Estos días ya vencieron, selecciona otra asignación distinta a esta e intentalo de nuevo.')
        return val