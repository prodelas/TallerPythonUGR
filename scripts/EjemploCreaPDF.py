# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:55:14 2015

@author: aulas
"""

# invoice.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
 
if __name__ == '__main__':
    name = u'Mr. John Doe'
    city = 'Pereira'
    address = 'ELM Street'
    phone = '555-7241'
    c = canvas.Canvas(filename='invoice.pdf', pagesize= (letter[0], letter[1]/2))
    c.setFont('Helvetica', 10)
    # Print Customer Data
    c.drawString(107*mm, 120*mm, name)
    c.drawString(107*mm, 111*mm, city)
    c.drawString(107*mm, 106*mm, address)
    c.drawString(107*mm, 101*mm, phone)
    c.showPage()
    c.save()