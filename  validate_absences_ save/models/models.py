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
        print(fecha_actual)
        busque = self.env['hr.leave.allocation'].search([('employee_id','=',val.employee_id.id),('holiday_status_id','=',val.holiday_status_id.id)],limit=1)
        em = busque.extended_permission
        fecha_ex = busque.vencimiento
        print(fecha_ex)
        if em == False:
            if fecha_ex:
                if  fecha_actual > fecha_ex:
                    raise ValidationError('Estos días ya vencieron, selecciona otra asignación distinta a esta e intentalo de nuevo.')          
            else:
                  raise ValidationError('el tipo de Asignacion no contine una fecha de vencimiento')
        return val