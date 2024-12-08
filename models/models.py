from odoo import models, fields


class Empleado(models.Model):
    _name = "recursos.empleado"
    _description = "Datos generales de empleados"

    nombre = fields.Char(string="Nombre", required=True)
    rfc = fields.Char(string="RFC", required=True)
    curp = fields.Char(string="CURP")
    domicilio = fields.Integer(string="Codigo postal")
    departamento = fields.Many2one("recursos.departamento", string="nomDepartamento")
    puesto = fields.Many2one("recursos.puesto", string="nomPuesto")


class Departamento(models.Model):
    _name = "recursos.departamento"

    nomDepartamento = fields.Char(string="Departamento")



class Puesto(models.Model):
    _name = "recursos.puesto"

    nomPuesto = fields.Char(string="Puesto")


