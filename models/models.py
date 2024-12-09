from odoo import models, fields


class Empleado(models.Model):
    _name = "recursos.empleado"
    _description = "Datos generales de empleados"

    nombre = fields.Char(string="Nombre", required=True)
    rfc = fields.Char(string="RFC", required=True)
    curp = fields.Char(string="CURP")
    domicilio = fields.Integer(string="Codigo postal")
    departamento = fields.Many2one("recursos.departamento")

    puesto = fields.Many2one("recursos.puesto")
    sindicalizado = fields.Selection([
        ("Si", "si"),
        ("No", "no")
    ])

    salsriodiario = fields.Float(string="Salario diario")
    salarioDiarioBase = fields.Float(string="Salari diario base")

    fechaIngreso = fields.Date(string="Fecha ingreso")
    tipoContrato = fields.Selection([])
    periocidadPago = fields.Selection([])
    tipoRegimen = fields.Selection([])
    numSegSocial = fields.Integer(string="Num. de seguro social")


    def name_get(self):
        result = []
        for record in self:
            name = f"{record.nombre} ({record.rfc})"
            result.append((record.id, name))
        return  result



class Departamento(models.Model):
    _name = "recursos.departamento"

    nomDepartamento = fields.Char(string="Departamento")

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.nomDepartamento}"
            result.append((record.id, name))
        return  result


class Puesto(models.Model):
    _name = "recursos.puesto"

    nomPuesto = fields.Char(string="Puesto")

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.nomPuesto}"
            result.append((record.id, name))
        return  result


